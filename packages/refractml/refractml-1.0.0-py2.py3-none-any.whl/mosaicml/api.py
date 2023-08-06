# -*- coding: utf-8 -*-
import base64
import json
import os
import shutil
import tempfile
import uuid
import time
from json import JSONDecodeError
import platform
import PIL
import requests
from datetime import datetime
from mosaic_utils.ai.build_time_metrics.metrics import metrics_stats
from mosaic_utils.ai.encoding_utils import base64_encode
from mosaic_utils.ai.file_utils import (
    create_model_tar,
    extract_tar,
    pickle_dumps,
    pickle_loads,
)
from requests_toolbelt.multipart.encoder import MultipartEncoder

from .constants import (
    MLModelArtifactsV1,
    MLModelDeployV1,
    MLModelFlavours,
    MLModelProfiling,
    MLModelResource,
    MLModelV1,
    MLModelVersionListing,
    MLModelVersionMetadataInfo,
    MLModelVersionV1,
    MosaicAI,
    MLModelVersionFeedback,
    MLKYDDataStoreV1,
)
from .decorators import scoring_func
from .schema import generate_service_schema
from .utils import (
    create_r_installation,
    generate_init_script,
    get_flavour_handler,
    get_headers,
    get_model_structure,
    get_version_deployment_status,
)
from .validators import *
from mosaic_utils.ai.validate.validators import ValidationHandler
from refractml.widgets.registered_output import ModelDescribe
import logging as log

kyd_executor = "<< KYDExecutor >>"


def register_model(
    model_obj,
    scoring_func,
    name,
    description,
    flavour,
    tags=None,
    init_script=None,
    schema=None,
    y_true=None,
    y_pred=None,
    prob=None,
    features=None,
    labels=None,
    model_type=None,
    datasource_name=None,
    metadata_info=None,
    input_type="json",
    target_names=None,
    target_names_mapping=None,
    x_train=None,
    y_train=None,
    feature_names=None,
    feature_ids=None,
    explain_ai=False,
    x_test=None,
    y_test=None,
    kyd=False,
    kyd_score=False,
    pretty_output=True,
    custom_score=None,
    **kwargs
):
    """
    Register model to the mosaic ai server

    Args:
        model_obj (object): model to be registered
        scoring_func (function): function to be used for scoring
        name (string): name of the model
        description (string): description of the model
        flavour (string): flavour of the model eg: keras, pytorch, tensorflow etc
        tags (array of strings): user tags associated with the model
        schema (Dict): input and output schema structure for scoring function
        y_true: array, shape = [n_samples]
        y_pred : array, shape = [n_samples]
        prob : array-like of shape (n_samples,)
        features : dummy feature names
        labels: predicted labels
        feature_names : all features
        model_type(string): type of the model eg: classification, regression etc
        datasource_name(string):
        metadata_info: metadata information about the version
        x_train (numpy array) : training data of model with feature column
        x_test (numpy array) :  test data of model with feature column
        y_train (numpy array) : training data of model with target column
        y_test (numpy array) : test data of model with target column
        kyd (bool)  :
            If True will generate Know your data Data Drift for the model.

            Once model registered import global variable for viewing InNotebook result.
            from refractml.api import kyd_executor
            kyd_executor.kyd_client.fallback_display()
        kyd_score (bool) :
            if True will generate drift score for the model.
        pretty_output (bool):
            if True returns widget after registeration else dictionary
    Optional:
        explicit_x_train:
            :pd.DataFrame or np.ndarray
            Explicit x_train clean raw data.
            if Provided the following algorithm will automatically pickup for its executions:
                - Know Your Data : explicit_x_train is used for extraction of knowledge. x_train is still used internally.
        explicit_x_test:
            :pd.DataFrame or np.ndarray
            Explicit x_test clean raw data.
            if Provided the following algorithm will automatically pickup for its executions:
                - Know Your Data : explicit_x_test is used for extraction of knowledge. x_test is still used internally.
        explicit_feature_names:
            :list
            Feature Names for The Explicit Provided Data.
        source:
            :string
            Value will be automl if model registered from automl else None
        model_display
            :bool
            If true display model on model list

    Returns:

    """
    validation_handler = ValidationHandler(
        mandatory_fields={"name": name,
                          "description": description,
                          "flavour": flavour,
                          "scoring_func": scoring_func,
                          },
        alphanum_uscore_excl={"name": name
                              },
        if_present_validate_type={'schema': (schema, (dict, )),
                                  'metadata_info': (metadata_info, (dict, )),
                                  'tags': (tags, (list, ))
                                  },
        if_present_sub_field_must_exist={'kyd': (kyd, {"x_train": x_train,
                                                       "y_train": y_train,
                                                       "x_test": x_test,
                                                       "y_test": y_test,
                                                       "feature_names": feature_names,
                                                       "model_type": model_type,
                                                       "kyd_score": kyd_score}),
                                         },
    )
    validation_status_, message_ = validation_handler.validate()
    if validation_status_ is False:
        return message_



    global kyd_executor
    # create model and version
    if init_script is None:
        init_script = ""
    if model_type:
        metrics_parameter_validation(model_type, y_true, y_pred, prob)
    if tags is not None:
        tags = list(set(tags))
        tags = {"user_tags": tags}
        tags = json.dumps(tags)

    # generate model artifacts
    artifacts_dir, artifacts_tar = create_artifacts(
        flavour,
        model_obj,
        scoring_func,
        x_train=x_train,
        y_train=y_train,
        x_test=x_test,
        y_test=y_test,
        custom_score=custom_score,
    )

    type_inference = {}
    model_info = {
        "mode": model_type,
        "targets_mapping": dict(
            target_names=target_names, mapping_value=target_names_mapping
        ),
        "features_name": kwargs.get("explicit_feature_names")
        if kwargs.get("explicit_feature_names", None)
        else feature_names,
        "features_type": type_inference,
        "feature_type_inferenced": bool(type_inference),
        "number_of_features": len(feature_names) if feature_names else 0,
        "number_of_targets": len(target_names) if target_names else 0,
        "deep_learning_model": False,
        "temp_dir": "",
        "expai": explain_ai,
        "kyd": kyd,
    }
    source = kwargs.get("source") if kwargs.get("source") else None
    model_display = kwargs.get("model_display")
    if model_display is None:
        model_display = True

    # register model
    ml_model = register(
        name,
        description,
        flavour,
        schema,
        metadata_info,
        model_display=model_display,
        source=source,
        init_script=create_init_script(init_script, flavour),
        input_type=input_type,
        target_names={"target": target_names},
        datasource_name=datasource_name,
        model_class=get_model_structure(model_obj, flavour),
        tar_file=artifacts_tar,
        tags=tags,
        model_info=model_info,
        score_file=dump_score_func(scoring_func)
    ) 
    _ml_model_id = ml_model["id"]
    ml_model["versions"].sort(key=lambda x: x["created_on"])
    _ml_version_id = ml_model["versions"][-1]["id"]
    model_summary = describe_model(_ml_model_id)
    detailed_matrix = {}
    # calculate model metrics
    if model_type:
        metrics = metrics_stats(
            None,
            _ml_model_id,
            _ml_version_id,
            y_true,
            y_pred,
            prob,
            model_type,
            model_summary,
            model_obj,
            labels,
            features,
            feature_names,
            None,
        )
        detailed_matrix = metrics.detailed_matrix()
    project_id = ml_model["project_id"]
    store_model_profiling(datasource_name, _ml_version_id, _ml_model_id, project_id)

    if pretty_output:
        described_model = ModelDescribe(_ml_model_id)
        described_model.view()
    else:
        described_model = describe_model(_ml_model_id)
        described_model["versions"][-1]["detailed_matrix"] = detailed_matrix
        return described_model


def register(
    name,
    description,
    flavour,
    schema,
    metadata_info,
    init_script,
    input_type,
    target_names,
    datasource_name,
    model_class,
    tar_file,
    model_display=None,
    source=None,
    tags=None,
    model_info=None,
    model_list=None,
    score_file=None
):
    if model_list:
        model_list = [
            {
                k: v
                for k, v in list_meta.items()
                if k
                not in [
                    "flavour",
                    "init_script",
                    "description",
                    "previous_model_id",
                    "previous_version_id",
                ]
            }
            for list_meta in model_list
        ]
    if type(score_file) == str:
        score_file_data = ("score_func.pkl", open(score_file, "rb"))
    else:
        score_file_data = None

    multipart_data = MultipartEncoder(
        fields={
            "tar_file": ("ml_model.tar.gz", open(tar_file, "rb")),
            "score_file": score_file_data,
            "name": name,
            "description": description,
            "flavour": flavour,
            "tags": tags,
            "init_script": base64_encode('"'+init_script+'"'),
            "input_type": input_type,
            "target_names": json.dumps(target_names),
            "datasource_name": datasource_name,
            "model_class": model_class,
            "schema": json.dumps(schema),
            "metadata_info": json.dumps(metadata_info),
            "model_info": json.dumps(model_info),
            "model_display": json.dumps(model_display),
            "source": source,
            "model_list": json.dumps(model_list),
            "base_id": platform.python_version(),
            "template_id":os.getenv('template_id') if os.getenv('template_id') else ""
        }
    )
    url = MosaicAI.server + MLModelV1.c
    headers = get_headers()
    headers["Content-Type"] = multipart_data.content_type
    response = requests.post(url, data=multipart_data, headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def dump_score_func(score_func):
    temp_dir = tempfile.mkdtemp()
    scoring_func_path = os.path.join(temp_dir, "score_func.pkl")
    pickle_dumps(score_func, scoring_func_path)
    return scoring_func_path

def create_artifacts(
    flavour,
    model_obj,
    scoring_func_from_user,
    x_train=None,
    model_list=None,
    x_test=None,
    y_train=None,
    y_test=None,
    custom_score=None,
):
    # create temporary directory
    temp_dir = tempfile.mkdtemp(dir=os.getenv("SPARK_MODEL_PVC"))
    # serialize model
    model_file = _pickle_model(flavour, model_obj, temp_dir)
    # serialize scoring function
    scoring_func_file = _pickle_scoring_func(scoring_func_from_user, temp_dir)
    if model_list:
        model_list_file = _pickle_model_list(model_list, temp_dir)
        return (
            temp_dir,
            create_model_tar(
                temp_dir, None, model_file, scoring_func_file, model_list_file
            ),
        )
    # generate tar file
    tar_file = create_model_tar(
            temp_dir,
            None,
            model_file,
            scoring_func_file,
            _pickle_training_test_data(x_train, temp_dir, "x_train"),
            _pickle_training_test_data(x_test, temp_dir, "x_test"),
            _pickle_training_test_data(y_train, temp_dir, "y_train"),
            _pickle_training_test_data(y_test, temp_dir, "y_test"),
            _pickle_training_test_data(custom_score, temp_dir, "custom_score"),
        )
    # delete from location once tar is created 
    if flavour=="pyspark" and os.path.exists(model_file):
        shutil.rmtree(model_file)
    return (
        temp_dir,
        tar_file,
    )


def metrics_parameter_validation(model_type, y_true, y_pred, prob):
    missing_param({"y_true": y_true, "y_pred": y_pred})
    if model_type == "classification":
        missing_param({"prob": prob})


def missing_param(parameter):
    for param in parameter:
        if parameter[param] is None:
            raise ValueError(param + " is/are missing")


def _pickle_model(flavour, model_obj, base_dir):
    model_path = os.path.join(base_dir, "ml_model")
    if flavour == MLModelFlavours.ensemble:
        pickle_dumps(model_obj, model_path)
    else:
        model_handler = get_flavour_handler(flavour)
        model_handler.dump_model(model_obj, model_path)
    return model_path


def _pickle_scoring_func(scoring_func_from_user, base_dir):
    scoring_func_path = os.path.join(base_dir, "scoring_func")
    pickle_dumps(scoring_func_from_user, scoring_func_path)
    return scoring_func_path


def _pickle_x_train(x_train, base_dir):
    x_train_path = os.path.join(base_dir, "x_train")
    pickle_dumps(x_train, x_train_path)
    return x_train_path


def _pickle_training_test_data(data, base_dir, data_type):
    """
    This function is used to pickle our training and test data set
    :param data:
    :param base_dir:
    :param data_type:
    :return:
    """
    data_path = os.path.join(base_dir, data_type)
    pickle_dumps(data, data_path)
    return data_path


def create_init_script(user_init_script, flavour):
    if flavour == MLModelFlavours.r:
        print("inside init script")
        # fetched_pip_packages = generate_init_script()
        fetched_pip_packages = ""
        r_installation = create_r_installation(fetched_pip_packages)
        init_script = r_installation + "\\n" + user_init_script + '"'
        return init_script
    
    init_script = user_init_script
    return init_script


def upload_model(ml_model, ml_model_version, tar_file, score_func=None):
    ml_model_id = ml_model["id"]
    ml_model_version_id = ml_model_version["id"]
    url = MosaicAI.server + MLModelVersionV1.upload.format(
        ml_model_id=ml_model_id, version_id=ml_model_version_id
    )
    files = {"ml_model.tar.gz": open(tar_file, "rb")}

    if score_func:
        score_func_file_path = dump_score_func(score_func)
        score_func_file_data = open(score_func_file_path, "rb")
        files.update({"score_func.pkl": score_func_file_data})

    response = requests.post(url, files=files, headers=get_headers())
    response.raise_for_status()


def add_model_version(
    ml_model,
    schema,
    metadata_info,
    init_script,
    flavour,
    input_type,
    target_names,
    datasource_name,
    model_class,
    tar_file,
):
    if init_script is None:
        init_script = ""
    multipart_data = MultipartEncoder(
        fields={
            "tar_file": ("ml_model.tar.gz", open(tar_file, "rb")),
            "ml_model": json.dumps(ml_model),
            "flavour": flavour,
            "init_script": base64_encode('"'+init_script+'"'),
            "input_type": input_type,
            "target_names": json.dumps(target_names),
            "datasource_name": datasource_name,
            "model_class": model_class,
            "schema": json.dumps(schema),
            "metadata_info": json.dumps(metadata_info),
        }
    )
    url = MosaicAI.server + MLModelV1.u
    headers = get_headers()
    headers["Content-Type"] = multipart_data.content_type
    response = requests.put(url, data=multipart_data, headers=headers)
    if response.status_code != 200:
        raise Exception(response.json())
    return response.json()


def add_version(
    ml_model,
    ml_model_obj,
    scoring_func,
    flavour,
    init_script,
    schema=None,
    y_true=None,
    y_pred=None,
    prob=None,
    features=None,
    original_features=None,
    labels=None,
    model_type=None,
    datasource_name=None,
    metadata_info=None,
    input_type="json",
    target_names=None,
    x_train=None,
    y_train=None,
    x_test=None,
    y_test=None,
    feature_names=None,
    feature_ids=None,
    explain_ai=False,
    custom_score=None,
):
    """
    Method to add new version to the registered model

    Args:
        ml_model (dict): ml_model retrieved using describe_model or list_models
        ml_model_obj (object): new version of the model to be registered
        scoring_func (function): function to be used for scoring
        schema (Dict): input and output schema structure for scoring function
        y_true: array, shape = [n_samples]
        y_pred : array, shape = [n_samples]
        prob : array-like of shape (n_samples,)
        features : dummy feature names
        labels: predicted labels
        original_features : all features
        model_type(string): type of the model eg: classification, regression etc
        datasource_name(string):
        metadata_info: metadata information about the version
        x_train (numpy array) : training data of model with feature column
        x_test (numpy array) :  test data of model with feature column
        y_train (numpy array) : training data of model with target column
        y_test (numpy array) : test data of model with target column
    Returns:
        dict
    """
    if model_type:
        metrics_parameter_validation(
            model_type, y_true, y_pred, prob, features, original_features
        )
    # generate model artifacts
    artifacts_dir, artifacts_tar = create_artifacts(
        flavour,
        ml_model_obj,
        scoring_func,
        x_train=x_train,
        y_train=y_train,
        x_test=x_test,
        y_test=y_test,
    )
    # add version
    ml_model_version = add_model_version(
        ml_model,
        schema,
        metadata_info,
        init_script,
        flavour,
        input_type,
        target_names={"target": target_names},
        datasource_name=datasource_name,
        model_class=get_model_structure(ml_model_obj, flavour),
        tar_file=artifacts_tar,
    )
    # get model id
    _ml_model_id = ml_model["id"]
    # get version id
    ml_model_version["versions"].sort(key=lambda x: x["created_on"])
    _ml_version_id = ml_model_version["versions"][-1]["id"]
    # metrics call
    model_summary = describe_model(_ml_model_id)
    if model_type:
        metrics_stats(
            None,
            _ml_model_id,
            _ml_version_id,
            y_true,
            y_pred,
            prob,
            model_type,
            model_summary,
            ml_model_obj,
            labels,
            features,
            original_features,
            None,
        )
    return describe_model(_ml_model_id)


def create_model(name, description, flavour, tags=None):
    payload = {
        "name": name,
        "description": description,
        "flavour": flavour,
        "tags": tags,
    }
    url = MosaicAI.server + MLModelV1.lc
    response = requests.post(url, json=payload, headers=get_headers())
    if response.status_code != 201:
        raise Exception(response.json())
    return response.json()


def create_version(
    ml_model,
    schema,
    metadata_info,
    user_init_script,
    flavour,
    input_type="json",
    target_names=None,
    datasource_name=None,
    model_class=None,
    base_id=None
):
    """

    Args:
        ml_model:
        schema (Dict): input and output schema structure for scoring function

    Returns:

    """
    #init_script = create_init_script(user_init_script, flavour) # removed r init
    init_script = user_init_script
    ml_model_id = ml_model["id"]
    payload = {
        "ml_model_id": ml_model_id,
        "init_script": base64_encode('"'+init_script+'"'),
        "input_type": input_type,
        "flavour": flavour,
        "target_names": {"target": target_names},
        "datasource_name": datasource_name,
        "base_id": base_id,
        "template_id":os.getenv('template_id') if os.getenv('template_id') else ""
    }
    if model_class:
        model_class_dict = {"model_class": json.loads(model_class)}
        payload.update(model_class_dict)
    if schema:
        schema_dict = {"schema": schema}
        payload.update(schema_dict)
    if metadata_info:
        metadata_info = {"metadata_info": metadata_info}
        payload.update(metadata_info)

    url = MosaicAI.server + MLModelVersionV1.lc.format(ml_model_id=ml_model_id)
    response = requests.post(url, json=payload, headers=get_headers())
    response.raise_for_status()
    return response.json()


def add_artifacts(
    tag, image_object, ml_model_id=None, version_id=None, pipeline_id=None, artifacts_path=None
):
    """
    Method to upload artifacts for a model
       Args:
           ml_model_id (string): ml_model id
           version_id (string): version id
           tag (string): name of the graph
           image_object (Onject): Object of image function
           artifacts_path : A directory containing the artifacts
       Returns:
           data
       """
    try:
        tempdir = None
        object_type = "file"
        if artifacts_path:
            object_type = "path"
            if not os.path.isdir(artifacts_path):
                tempdir = tempfile.mkdtemp()
                shutil.copy(artifacts_path, tempdir)
                artifacts_path = tempdir
            file_path = shutil.make_archive("/tmp/sample", 'zip', artifacts_path)
            multipart_form_data = {"image": (os.path.basename(file_path), open(file_path, "rb"))}
        elif image_object:
            image_name = uuid.uuid1()
            file_path = "/tmp/{}.{}".format(image_name, image_object.format)
            image_object.save(file_path)
            image_filename = os.path.basename(file_path)
            multipart_form_data = {"image": (image_filename, open(file_path, "rb"))}
        else:
            raise Exception("Invalid Input")
        response = _upload_artifacts(file_path, ml_model_id, multipart_form_data,
                                     tag, version_id, pipeline_id, object_type)
        return response
    except Exception as ex:
        log.error(ex)
    finally:
        if tempdir:
            shutil.rmtree(tempdir)


def _upload_artifacts(file_path, ml_model_id, multipart_form_data, tag, version_id, pipeline_id,
                      object_type):
    payload = {
        "ml_model_id": ml_model_id,
        "version_id": version_id,
        "pipeline_id": pipeline_id,
        "tag": tag,
        "object_type": object_type
    }
    url = MosaicAI.server + MLModelArtifactsV1.add_artifacts_url
    response = requests.post(
        url, data=payload, files=multipart_form_data, headers=get_headers()
    )
    response.raise_for_status()
    os.unlink(file_path)
    return response.json()


def download_artifacts(
        ml_model_id=None, version_id=None, tag=None
):
    """
    Method to download the artifacts from minio
       Args:
           ml_model_id (string): ml_model id
           version_id (string): version id
           tag (string): name of the graph
       Returns:
           Directory path, File list
       """
    try:
        tempdir = None
        file_path = None
        files_list = []
        url = MosaicAI.server + MLModelArtifactsV1.download_artifacts_url
        payload = {
            "ml_model_id": ml_model_id,
            "request_id": tag,
            "version_id": version_id
        }
        response = requests.post(url, headers=get_headers(), json=payload, stream=True)
        if response.status_code == 200:
            tempdir = tempfile.mkdtemp()
            file_path = tempdir + "/" + tag + ".tar.gz"
            with open(file_path, 'wb') as fd:
                for chunk in response.iter_content(chunk_size=128):
                    fd.write(chunk)
                fd.close()
            shutil.unpack_archive(file_path, tempdir, format="gztar")
            files_list = os.listdir(tempdir)
            files_list.remove(tag + ".tar.gz")
        return tempdir, files_list
    except Exception as ex:
        log.error(ex)
    finally:
        if file_path:
            os.remove(file_path)


def list_models(type='model'):
    """
    Method to retrieve the models and versions registered

    Returns:
        dict
    """
    url = MosaicAI.server + MLModelV1.lc + f"?type={type}"
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()


def describe_model(ml_model_id):
    """
    Method to retrieve the model using id

    Returns:
        dict
    """
    url = MosaicAI.server + MLModelV1.rud.format(ml_model_id=ml_model_id)
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()


def delete_model(ml_model_id):
    """
    Method to delete the model using id
    """
    url = MosaicAI.server + MLModelV1.rud.format(ml_model_id=ml_model_id)
    response = requests.delete(url, headers=get_headers())
    response.raise_for_status()


def load_model(ml_model_id, version_id):
    """
    Method to construct the model object from the model and version id

    Args:
        ml_model_id (string): identifier for ml_model
        version_id (string): identifier for version_id

    Returns:
        tuple
    """
    # fetch model metadata
    model_info = describe_model(ml_model_id)
    # download model artifacts
    url = MosaicAI.server + MLModelVersionV1.download.format(
        ml_model_id=ml_model_id, version_id=version_id
    )
    response = requests.get(url, headers=get_headers())
    # create temperory directory
    base_dir = tempfile.mkdtemp()
    # write downloaded artifacts to tar file
    tar_path = os.path.join(base_dir, "ml_model.tar.gz")
    tar_file = open(tar_path, "wb")
    tar_file.write(response.content)
    tar_file.close()
    # extract tar file
    extract_tar(tar_path, base_dir)
    # build model object
    flavour = model_info["flavour"]
    # build scoring function
    scoring_func_path = os.path.join(base_dir, "scoring_func")
    scoring_func = pickle_loads(scoring_func_path)
    if flavour == MLModelFlavours.ensemble:
        return scoring_func, model_info["versions"][0]["dependent_model"]

    model_handler = get_flavour_handler(flavour)
    model_path = os.path.join(base_dir, "ml_model")
    model = model_handler.load_model(model_path)
    # delete temperory directory
    shutil.rmtree(base_dir)
    return model, scoring_func


def load_train_and_test_data(ml_model_id, version_id):
    """
    This function is used to fetch train and test data of model using model and version id
    :param ml_model_id:
    :param version_id:
    :return:
    """

    # download model artifacts
    url = MosaicAI.server + MLModelVersionV1.download.format(
        ml_model_id=ml_model_id, version_id=version_id
    )
    response = requests.get(url, headers=get_headers())

    x_train = y_train = x_test = y_test = None

    if response.status_code == 200:
        # create temperory directory
        base_dir = tempfile.mkdtemp()
        # write downloaded artifacts to tar file
        tar_path = os.path.join(base_dir, "ml_model.tar.gz")
        tar_file = open(tar_path, "wb")
        tar_file.write(response.content)
        tar_file.close()
        # extract tar file
        extract_tar(tar_path, base_dir)

        # loading training and test data
        x_train = pickle_loads(os.path.join(base_dir, "x_train"))
        x_test = pickle_loads(os.path.join(base_dir, "x_test"))
        y_train = pickle_loads(os.path.join(base_dir, "y_train"))
        y_test = pickle_loads(os.path.join(base_dir, "y_test"))

    return x_train, y_train, x_test, y_test


def get_build_time_metrics(ml_model_id, ml_version_id):
    """
    This function is used to return performance or build time metrics of model
    :param ml_model_id:
    :param ml_version_id:
    :return:
    """


def deploy_model(ml_model_id, version_id, resource_id=None, cpu_utilization=None):
    """
    This will deploy the model version in k8
    Args:
        ml_model_id (str):
        version_id (str):
        resource_id (str):
        cpu_utilization (str):

    Returns:
        deployment_info (dict)
    """
    try:
        value = validate_details_for_deployment(
            describe_model(ml_model_id), version_id, strategy="default"
        )
        payload = {"ml_model_id": ml_model_id, "version_id": version_id}

        if resource_id:
            payload.update({"resource_id": resource_id})
        if cpu_utilization:
            payload.update({"cpu_utilization": cpu_utilization})
        url = MosaicAI.server + MLModelDeployV1.c.format(ml_model_id=ml_model_id)
        response = requests.post(url, json=payload, headers=get_headers())
        if response.status_code != 201:
            return response.text
        return response.json()
    except Exception as ex:
        return ex.args[0]


def apply_model_strategy(
    ml_model_id,
    version_id,
    deployment_type=None,
    resource_id=None,
    cpu_utilization=None,
):
    """
    This will apply the strategy to the deployed model
    Args:
        ml_model_id (str):
        version_id (str):
        deployment_type (str)
        resource_id (str):
        cpu_utilization (str):
    Returns:
        Deployment Response (str)

    Note:
        Value of Deployment type should always be one of the following:
            Ramped - Will perform a ramped update of the deployment to the new version
            AB-Testing - Will deploy the given version in parallel, this can be accessed by setting request header "ab-access": "always"
            Canary - Will deploy the given version in parallel and will randomly distribut 10% traffic to the newly deployed version
            PreProd - Will deploy the given version in parallel and all requests to the already deployed model (Production Model) will be mirrored.

            If deployment_type is not passed, then default strategy applied will be "Ramped"

    Examples:
        AB-Testing:
            apply_model_strategy(
                ml_model_id="707e3667-3ce1-4c21-a3ef-77570c8c44fe",
                version_id="c0ef08a6-55a2-4b69-97d3-75fd0ffec423",
                deployment_type="AB-Testing",
                resource_id="51b9f415-1c8d-4b96-ae48-c0dad16be2a9",
                cpu_utilization="90"
                )
        Canary:
            apply_model_strategy(
                ml_model_id="707e3667-3ce1-4c21-a3ef-77570c8c44fe",
                version_id="c0ef08a6-55a2-4b69-97d3-75fd0ffec423",
                deployment_type="Canary",
                resource_id="51b9f415-1c8d-4b96-ae48-c0dad16be2a9",
                cpu_utilization="90"
                )
        Ramped:
            apply_model_strategy(
                 ml_model_id="707e3667-3ce1-4c21-a3ef-77570c8c44fe",
                version_id="c0ef08a6-55a2-4b69-97d3-75fd0ffec423",
                deployment_type="Ramped",
                resource_id="51b9f415-1c8d-4b96-ae48-c0dad16be2a9",
                cpu_utilization="90"
                )
        PreProd:
            apply_model_strategy(
                ml_model_id="707e3667-3ce1-4c21-a3ef-77570c8c44fe",
                version_id="c0ef08a6-55a2-4b69-97d3-75fd0ffec423",
                deployment_type="PreProd",
                resource_id="51b9f415-1c8d-4b96-ae48-c0dad16be2a9",
                cpu_utilization="90"
                )



    """
    try:
        deployment_data = validate_details_for_deployment(
            describe_model(ml_model_id), version_id, strategy="apply_strategy"
        )
        payload = {
            "ml_model_id": ml_model_id,
            "version_id": version_id,
            "deployment_type": deployment_type
            if deployment_type is not None
            else "Ramped",
        }
        if resource_id:
            payload.update({"resource_id": resource_id})
        if cpu_utilization:
            payload.update({"cpu_utilization": cpu_utilization})
        url = MosaicAI.server + MLModelDeployV1.ud.format(
            ml_model_id=ml_model_id, deployment_id=deployment_data.get("deployment_id")
        )
        response = requests.put(url, json=payload, headers=get_headers())
        if response.status_code == 201:
            return "Strategy successfully applied!"
        return response.text
    except Exception as ex:
        return ex.args[0]


def promote_model(ml_model_id, version_id):
    """
    This method will promote the Model Version to production
    :param ml_model_id:
    :param version_id:
    :return:
    """
    try:
        model_data = describe_model(ml_model_id)
        deployment_data = validate_details_for_deployment(
            model_data, version_id, strategy="promote"
        )
        payload = {
            "ml_model_id": ml_model_id,
            "version_id": version_id,
            "deployment_type": deployment_data.get("promotion_key"),
            "cou_utilization": deployment_data.get("cou_utilization"),
            "resource_id": deployment_data.get("resource_id"),
        }
        url = MosaicAI.server + MLModelDeployV1.ud.format(
            ml_model_id=ml_model_id, deployment_id=deployment_data.get("deployment_id")
        )
        response = requests.put(url, json=payload, headers=get_headers())
        if response.status_code == 201:
            return "Model successfully promoted"
        return response.text
    except Exception as ex:
        return ex.args[0]


def stop_model(ml_model_id, version_id):
    """
    This method will delete the deployed model from k8
    Args:
        ml_model_id:
        version_id:

    Returns:
    """
    try:
        deployment_id = stop_model_validations(describe_model(ml_model_id), version_id)
        url = MosaicAI.server + MLModelDeployV1.ud.format(
            ml_model_id=ml_model_id, deployment_id=deployment_id
        )
        response = requests.delete(url, headers=get_headers())
        if response.status_code == 204:
            return "Version Deployment stopped successfully !"
        return response.text
    except Exception as ex:
        return ex.args[0]


def store_model_profiling(datasource_name, ml_version_id, ml_model_id, project_id):
    if datasource_name:
        url = MosaicAI.server + MLModelProfiling.c
        payload = {
            "datasource_name": datasource_name,
            "version_id": ml_version_id,
            "ml_model_id": ml_model_id,
            "project_id": project_id,
        }
        response = requests.post(url, json=payload, headers=get_headers())
        return response.status_code


def get_model_profiling(datasource_name, column_name, ml_model_id, version_id):
    if datasource_name and column_name and ml_model_id and version_id:
        url = MosaicAI.server + MLModelProfiling.l.format(
            datasource_name=datasource_name,
            column_name=column_name,
            version_id=version_id,
            ml_model_id=ml_model_id,
        )
        response = requests.get(url, headers=get_headers())
        return response.json()
    else:
        return "please enter valid data"


def generate_schema(func, func_args, model_input):
    """Test and generates schema for a scoring function.

    Ensures convention of a scoring function definition, and runs a test using
    the test input. As a side effect, it also generates schema for the service
    definition.
    """
    if not isinstance(func, scoring_func):
        raise TypeError(
            "Scoring function must be defined using the scoring_func decorator"
        )
    try:
        model = func_args[0]
        result = func(*func_args)
        schema = generate_service_schema(model_input, result)
        func._schema = schema
        return schema
    except Exception as e:
        print("Error while generating schema:")
        print(str(e))


def update_metadata_info(ml_model_id=None, version_id=None, metadata_info=None):
    """ Method to update metadata info"""
    payload = {"ml_model_id": ml_model_id, "version_id": version_id}
    if metadata_info:
        metadata_info = {"metadata_info": metadata_info}
        payload.update(metadata_info)
    url = MosaicAI.server + MLModelVersionMetadataInfo.u.format(
        ml_model_id=ml_model_id, version_id=version_id
    )
    response = requests.put(url, json=payload, headers=get_headers())
    response.raise_for_status()
    return response


def update_model_details(ml_model_id, flavour):
    payload = {"flavour": flavour}
    url = MosaicAI.server + MLModelV1.rud.format(ml_model_id=ml_model_id)
    response = requests.put(url, json=payload, headers=get_headers())
    response.raise_for_status()
    return response.status_code


def update_version_details(
    ml_model_id,
    version_id,
    flavour,
    user_init_script=None,
    schema=None,
    metadata_info=None,
    input_type="json",
    target_names=None,
    datasource_name=None,
):
    payload = {"ml_model_id": ml_model_id, "input_type": input_type, "flavour": flavour}
    if schema:
        schema_dict = {"schema": schema}
        payload.update(schema_dict)
    if metadata_info:
        metadata_info = {"metadata_info": metadata_info}
        payload.update(metadata_info)
    if user_init_script:
        init_script = create_init_script(user_init_script, flavour)
        init_script = {"init_script": base64_encode('"'+init_script+'"')}
        payload.update(init_script)
    if target_names:
        target_names = {"target_names": {"target": target_names}}
        payload.update(target_names)
    if datasource_name:
        datasource_name = {"datasource_name": datasource_name}
        payload.update(datasource_name)
    url = MosaicAI.server + MLModelVersionV1.rud.format(
        ml_model_id=ml_model_id, version_id=version_id
    )
    response = requests.put(url, json=payload, headers=get_headers())
    response.raise_for_status()
    return response.status_code


def update_existing_model(
    ml_model_id,
    version_id,
    model_obj,
    scoring_func,
    flavour,
    init_script=None,
    schema=None,
    metadata_info=None,
    input_type="json",
    target_names=None,
    datasource_name=None,
    x_train=None,
    x_test=None,
    y_train=None,
    y_test=None,
):
    """
    Api to update an existing model

    Args:
        ml_model_id(UUID): unique id for the model
        version_id(UUID): unique id for version
        model_obj (object): model to be registered
        scoring_func (function): function to be used for scoring
        flavour (string): flavour of the model eg: keras, pytorch, tensorflow etc
        init_script(string):script provided by user
        schema (Dict): input and output schema structure for scoring function
        metadata_info: metadata information about the version
        input_type(String):input  type passed in scoring function
        target_names(list): Unique column names in case of classification or target column in regression
        datasource_name(string): name of the datasource
        x_train (numpy array) : training data of model with feature column
        x_test (numpy array) :  test data of model with feature column
        y_train (numpy array) : training data of model with target column
        y_test (numpy array) : test data of model with target column
    Returns:
        dict
    """
    if schema is not None and not isinstance(schema, dict):
        raise TypeError("Invalid schema definition - must be a dictionary")
    if metadata_info and not (isinstance(metadata_info, dict)):
        raise TypeError("invalid metadata_info definition : Must be a dictionary")
    # update model details
    update_model_details(ml_model_id, flavour)
    # update version details
    update_version_details(
        ml_model_id,
        version_id,
        flavour,
        init_script,
        schema,
        metadata_info,
        input_type,
        target_names,
        datasource_name,
    )
    # generate model artifacts
    ml_model = describe_model(ml_model_id)
    model_version = ml_model["versions"]
    ml_model_version = None
    # check if the model has more then 1 version pass the correct version for upload
    for version in model_version:
        if version["id"] == version_id:
            ml_model_version = version
    artifacts_dir, artifacts_tar = create_artifacts(
        ml_model["flavour"],
        model_obj,
        scoring_func,
        x_train=x_train,
        y_train=y_train,
        x_test=x_test,
        y_test=y_test,
    )
    # upload artifacts to object storage
    upload_model(ml_model, ml_model_version, artifacts_tar, scoring_func)
    # remove artifacts directory
    shutil.rmtree(artifacts_dir)
    return describe_model(ml_model_id)


def _pickle_model_list(model_list, base_dir):
    model_list_path = os.path.join(base_dir, "model_list")
    pickle_dumps(model_list, model_list_path)
    return model_list_path


def ensemble_model_list(version_list):
    url = (
        MosaicAI.server
        + MLModelVersionListing.l
        + "?version_list={}".format(version_list)
    )
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    model_list = []
    if response.status_code == 200:
        for version in response.json():
            model_list.append(
                {
                    "model_id": version["ml_model_id"],
                    "version_id": version["id"],
                    "version_no": version["version_no"],
                    "name": version["name"],
                    "flavour": version["flavour"],
                    "init_script": version["init_script"],
                    "description": version["description"],
                    "previous_model_id": version["ml_model_id"],
                    "previous_version_id": version["id"],
                }
            )
    return model_list


def register_ensemble_model(
    name, description, version_list, scoring_func, init_script=None
):
    """
    Register ensemble model to the mosaic ai server

    Args:
        name (string): name of the model
        description (string): description of the model
        version_list (list): list of versions of dependent models required for final prediction
        E.g [ "v1", "v2"]
        scoring_func (function): function to be used for scoring
        init_script(string):script provided by user
    Returns:
        dict
    """
    try:
        if init_script is None:
            init_script = ""
        flavour = MLModelFlavours.ensemble
        model_obj = None
        # fetching dependent ensemble model details
        model_list = ensemble_model_list(version_list)
        # generate model artifacts
        artifacts_dir, artifacts_tar = create_artifacts(
            flavour, model_obj, scoring_func, model_list=model_list
        )
        # register model
        ml_model = register(
            name,
            description,
            flavour,
            schema=None,
            metadata_info=None,
            init_script=create_init_script(init_script, flavour),
            input_type="json",
            target_names={"target": None},
            datasource_name=None,
            model_class=get_model_structure(model_obj, flavour),
            tar_file=artifacts_tar,
            model_list=model_list,
            model_display=True,
            source=None,
            score_file=scoring_func
        )
        _ml_model_id = ml_model["id"]
        return describe_model(_ml_model_id)
    except Exception as e:
        print("Error while registering ensemble model")
        print(str(e))


def build_time_metrics(ml_version_id, tag=None):
    """
     This function is used to return performance or build time metrics of model
    :param ml_version_id:
    :param tag:
    :return:
    """
    try:
        if tag is None:
            tag = "detailed_matrix"
        url = MosaicAI.server + MLModelVersionV1.build_time_metrics.format(
            version_id=ml_version_id, tag=tag
        )
        response = requests.get(url, headers=get_headers())
        return response.json()[0]["metric_value"]
    except Exception as ex:
        print("no performance metrics avaiable")
        return {}


def fetch_model_resources():
    """
    Function to fetch ML Model Resources details

    Example:

    resources_data = fetch_model_resource()
    print(resources_data)

    :return:
    """
    url = MosaicAI.server + MLModelResource.r
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return response.text


def describe_model_using_model_name(model_name=None, model_type="model"):
    """
    Method to retrieve the model using name
    Returns:
        dict
    """
    url = MosaicAI.server + MLModelV1.rud_model_name1.format(
        ml_model_id="undefined", ml_model_name=model_name, model_type=model_type
    )
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()


def get_model_info(model_name=None, model_type="model"):
    """
    This function is used to return model information like its
     version and their deployment along with model Id
    :param model_name:
    :return:
    {"model_id" : "<model_id>", "versions" : {"version_id" :
     "<version_id>" : "deployment_status"}}
    """
    model_info = describe_model_using_model_name(model_name=model_name,model_type=model_type)
    model_details = {}
    if model_info:
        model_details = {"model_id": model_info.get("id"), "versions": []}
        for version in model_info["versions"]:
            model_details["versions"].append(
                {
                    "id": version["id"],
                    "deployment_status": get_version_deployment_status(
                        version["deployments"]
                    ),
                }
            )
    return model_details


def fetch_feedback_accuracy(version_id):
    """
    This function is used to fetch the feedback accuracy of the specified version
    :param version_id:
    :return:
    """
    url = MosaicAI.server + MLModelVersionFeedback.r.format(version_id=version_id)
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()


def delete_model_version(model_id, version_id):
    """
    This function is used to delete specified version of model
    :param model_id:
    :param version_id:
    :return:
    """
    try:
        url = MosaicAI.server + MLModelVersionV1.delete.format(
            ml_model_id=model_id, version_id=version_id
        )
        model_data = describe_model(model_id)
        validate_model_id_version_id(model_data, version_id)
        response = requests.delete(url, headers=get_headers())
        if response.status_code == 204:
            response.raise_for_status()
            return "Version deleted successfully !"
        return "Failed to delete Version ! Kindly try again !"
    except Exception as ex:
        return ex.args[0] 