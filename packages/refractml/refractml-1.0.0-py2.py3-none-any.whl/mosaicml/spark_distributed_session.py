from pyspark import SparkConf
from pyspark.sql import SparkSession
import re

from .constants import SparkDistributed
from mosaic_utils.ai.k8.pod_metrics_summary import volume_custom_mount, volume_mount_count


def get_memory(memory):
    try:
        temp = re.compile("([0-9\.]+)([a-zA-Z]+)")
        res = temp.match(memory).groups()
        if 'M' in res[1]:
            if float(res[0]) >= 500:
                return str(res[0]) + "m"
            else:
                return "500m"
        elif 'G' in res[1]:
            return str(res[0]) + "g"
    except Exception as ex:
        print(f"Memory issue: {ex}")
        return None


def get_configs():
    return {
        "spark.kubernetes.namespace": SparkDistributed.namespace,
        "spark.kubernetes.container.image": SparkDistributed.executor_pod_image,
        "spark.kubernetes.container.image.pullSecrets": "gitlab",
        "spark.kubernetes.container.image.pullPolicy": "IfNotPresent",
        "spark.executor.instances": SparkDistributed.number_of_executors,
        "spark.kubernetes.executor.request.cores": SparkDistributed.executor_request_cpu,
        "spark.kubernetes.executor.limit.cores": SparkDistributed.executor_limit_cpu,
        # "spark.executor.cores": SparkDistributed.executor_request_cpu,
        "spark.executor.memory": get_memory(SparkDistributed.executor_limit_memory),
        # At least 500m memory is required.
        "spark.driver.blockManager.port": "7777",
        "spark.driver.port": "2222",
        "spark.driver.host": str(SparkDistributed.executor_service_name) + "." + str(SparkDistributed.namespace)
                             + ".svc.cluster.local",  # service-name.namespace.svc.cluster.local
        "spark.driver.bindAddress": "0.0.0.0",
        "spark.jars": "/opt/conda/lib/python3.7/site-packages/pyspark/jars"
        # https://spark.apache.org/docs/2.4.3/running-on-kubernetes.html -> Configuration
    }


def add_volume_mounts(config):
    vm = volume_custom_mount(SparkDistributed.project_id, SparkDistributed.minio_data_bucket)[0]
    # spark.kubernetes.driver.volumes.[VolumeType].[VolumeName].mount.path -> for adding multiple volumes
    conf = "spark.kubernetes.executor.volumes.persistentVolumeClaim."
    config[conf + str(vm.get('name')) + ".options.claimName"] = SparkDistributed.pvc_name
    config[conf + str(vm.get('name')) + ".mount.path"] = vm.get("mountPath")
    config[conf + str(vm.get('name')) + ".mount.subPath"] = vm.get("subPath")
    config[conf + str(vm.get('name')) + ".mount.readOnly"] = vm.get("readOnly", "false")
    # For adding any custom volumes to executor.
    for i in volume_mount_count(SparkDistributed.project_id, SparkDistributed.user_id):
        config[conf + str(i.get('name')) + ".options.claimName"] = str(i.get('name'))
        config[conf + str(i.get('name')) + ".mount.path"] = str(i.get('mountPath'))
        config[conf + str(i.get('name')) + ".mount.readOnly"] = "false"
    return config


def add_executor_env_variables(config):
    try:
        config["spark.executorEnv.PYTHONPATH"] = SparkDistributed.PYTHONPATH
        f = list(open("/notebooks/.bashrc", "r"))
        for i in f:
            x = " ".join(i.split(" ")[1:]).rstrip().split("=")
            # Removing single quotes used in file
            # export userId = 'data_user'
            # export custom_spark_jars_path = '/data/*'
            x[1] = x[1].strip("\'")
            config[f"spark.executorEnv.{x[0]}"] = x[1]
            if x[0] == "custom_spark_jars_path":
                config[f"spark.driver.extraClassPath"] = x[1] if x[1] else "/data/*"
                config[f"spark.executor.extraClassPath"] = x[1] if x[1] else "/data/*"
        return config
    except Exception as ex:
        print(f"EXCEPTION occurred while reading custom env variables: {ex}")
        return config


def get_spark_session(app_name: str, conf: SparkConf):
    print("Launching Spark Session! ...\n")
    conf.setMaster("k8s://https://kubernetes.default.svc.cluster.local")
    for key, value in config.items():
        conf.set(key, value)
    session = SparkSession.builder.appName(app_name).config(conf=conf).getOrCreate()
    return session


if SparkDistributed.is_job_run:
    print("Launching Spark Session for JOB RUN!\n")
    config = {}
    spark = SparkSession.builder.appName("spark-operator-run").getOrCreate()
else:
    config = add_volume_mounts(get_configs())
    config = add_executor_env_variables(config)
    spark = get_spark_session("jy-spark-executor", SparkConf(config))
