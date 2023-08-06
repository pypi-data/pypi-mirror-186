# -*- coding: utf-8 -*-
import json
import os
import subprocess

from mosaic_utils.ai.flavours import (
    keras,
    pyspark,
    pytorch,
    sklearn,
    spacy,
    tensorflow,
    xgboost,
)
from pip._internal.operations.freeze import freeze

from .constants import (
    CRANPackageList,
    Client,
    Headers,
    MLModelFlavours,
    MosaicPipPackages,
    RPYPackage,
)
from .exceptions import ConfigError


def read_jwt():
    config_file = os.path.expanduser(Client.config_file)
    if os.path.exists(config_file):
        with open(config_file) as f:
            jwt = f.read().strip("\n")
        return jwt
    elif os.getenv("TOKEN"):
        jwt = os.getenv("TOKEN")
        return jwt
    raise ConfigError


def get_headers():
    jwt = read_jwt()
    return {
        Headers.authorization: f"Token {jwt}",
        Headers.x_project_id: os.environ.get("PROJECT_ID"),
    }


def get_flavour_handler(flavour):
    if flavour == MLModelFlavours.sklearn:
        return sklearn
    if flavour == MLModelFlavours.pytorch:
        return pytorch
    if flavour == MLModelFlavours.keras:
        return keras
    if flavour == MLModelFlavours.tensorflow:
        return tensorflow
    if flavour == MLModelFlavours.pyspark:
        return pyspark
    if flavour == MLModelFlavours.spacy:
        return spacy
    if flavour == MLModelFlavours.xgboost:
        return xgboost


def create_r_installation(pip_installation):
    from mosaic_utils.ai.flavours.r import get_r_packages, check_pre_installed_packages

    package_list, version_list = get_r_packages()
    revised_package_list = check_pre_installed_packages(
        package_list, version_list, CRANPackageList.pre_installed_packages
    )
    package_names = []
    package_versions = []
    for i in range(0, len(revised_package_list)):
        package_names.append(revised_package_list[i]["name"])
        package_versions.append(revised_package_list[i]["version"])
    package_names = tuple(package_names)
    package_versions = tuple(package_versions)
    create_command = (
        f'\\n echo \\" package_name<-c{package_names}; package_version<-c{package_versions};'
        "pkgname<- rownames(installed.packages());"
        "df <- data.frame(installed.packages());pkgversion <- sapply(df$Version, as.character);"
        f"pkgversion<-pkgversion[,'Version'];df1<-data.frame(p=package_name, v=package_version);"
        "df2<-data.frame(p=pkgname, v=pkgversion);"
        "library(dplyr);final_df<- setdiff(df1,df2);"
        "final_df= data.frame(final_df,stringsAsFactors = F);"
        "for (row in 1:nrow(final_df)){tryCatch({remotes::install_version"
        f"(final_df[row,'p'],final_df[row,'v'],"
        f"repos='{RPYPackage.r_url}',"
        "dependencies=TRUE, silent = TRUE, upgrade='never')},"
        'error = function(e){{print(e)}})};\\" | R --no-save \\n'
    )
    pip_installation += create_command
    return pip_installation


def get_pip_packages():
    packages = []
    data = subprocess.check_output(["pip", "list", "--format", "json"])
    parsed_results = json.loads(data)
    for element in parsed_results:
        package = element["name"] + "==" + element["version"]
        packages.append(package)
    return packages


def generate_conda_packages():
    try:
        packages = []
        data = subprocess.check_output(["conda", "list", "--json"])
        parsed_results = json.loads(data)
        if parsed_results:
            for element in parsed_results:
                package = element["name"] + "==" + element["version"]
                packages.append(package)
            return packages
    except:
        return []


def generate_init_script():
    packages = get_pip_packages()
    conda_packages = generate_conda_packages()
    # find difference between pip and conda packages, remove common between two
    # few packages have difference only in case & _, hence taking those in consideration
    # p = ["zipp", "pandas", "Flask"]
    # c = ["zipp", "flask", "numpy"]
    # final packages getting installed by conda would be
    # c = ["numpy"]
    conda_packages_not_in_pip_freeze = [
        p.replace("-", "_")
        for p in packages
        if p.lower() not in (c.lower() for c in conda_packages)
    ]
    packages = remove_mosaic_packages(packages)
    init = f"pip install -i {RPYPackage.py_url} "
    init_script = '"'
    for package in packages:
        if package.startswith("-e"):
            pass
        if package.startswith("pip"):
            pass
        else:
            init_script += (
                init
                + package
                + " || conda install -c {0} {1} --yes {2};\\n ".format(
                    RPYPackage.conda_url, package, RPYPackage.override_channel_value
                )
            )
    for each_package in conda_packages_not_in_pip_freeze:
        # try installing using pip first, if it fails then only try with conda,
        # as pip installation are faster than conda
        init_script = (
            init_script
            + "pip install -i {2} {1} || conda install -c {0} {1} --yes {3};\\n ".format(
                RPYPackage.conda_url,
                each_package,
                RPYPackage.py_url,
                RPYPackage.override_channel_value,
            )
        )
    return init_script


def remove_mosaic_packages(packages):
    package = [
        x
        for x in packages
        if not (
            x.startswith(MosaicPipPackages.client)
            or x.startswith(MosaicPipPackages.common_utils)
            or x.startswith(MosaicPipPackages.automl)
            or x.startswith(MosaicPipPackages.connector)
            or x.startswith(MosaicPipPackages.visual_client)
        )
    ]
    return package


def get_model_structure(model_obj, flavour):
    try:
        model_structure = get_flavour_handler(flavour).get_model_structure(model_obj)
    except:
        model_structure = json.dumps({"class": str(model_obj.__class__)[8:-2:]})
    return model_structure


def get_deployment_data(deployments):
    deployment_data = dict()
    for item in deployments:
        if item.get("deployment_type") == "Default":
            deployment_data.update({"deployment_id": item.get("deployment_id")})
        if item.get("deployment_type") != "Default":
            deployment_data.update(
                {
                    "deployment_type": item.get("deployment_type"),
                    "cpu_utilization": item.get("cpu_utilization"),
                    "resource_id": item.get("resource_id"),
                }
            )
    return deployment_data


def get_version_deployment_status(deployment=None):
    """
    This function is used to return the status of version deployment
    :param deployment:
    :return:
    """
    if deployment:
        return deployment[0].get("deployment_info").get("deployment_type")
    return "Not deployed"
