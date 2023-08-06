# -*- coding: utf-8 -*-
import os
import unittest
from unittest.mock import patch


class TestSparkDistributedSession(unittest.TestCase):
    """
    This class is used for implement test method of spark distributed session creation.
    """

    def setUp(self):
        # Add setup data for Test cases
        os.environ['executor_pod_image'] = "sample_docker_image:tag"
        os.environ['executor_request_cpu'] = "500m"
        os.environ['executor_request_memory'] = "500m"
        os.environ['executor_limit_cpu'] = "1"
        os.environ['executor_limit_memory'] = "1Gi"
        os.environ['number_of_executors'] = "2"
        os.environ['pod_name'] = "jy-service"
        os.environ['pvc_name'] = "test_pvc"
        os.environ['PROJECT_ID'] = "sample_project_id"
        os.environ['userId'] = "test_user"
        os.environ['MINIO_DATA_BUCKET'] = "spark_testing"
        os.environ['NAMESPACE'] = "spark_test"
        os.environ['PYTHONPATH'] = ':/mosaic_data/Python/a5534e37-bc4e-4439-bf2d-c9a27163112f/3.6:/tmp/pip_packages'
        os.environ['is_job_run'] = "false"

    @patch("pyspark.sql.SparkSession")
    @patch("pyspark.SparkConf")
    def test_get_memory(self, mock_config, mock_spark):
        from refractml.spark_distributed_session import get_memory
        output = get_memory("500Mi")
        self.assertEqual(output, "500m")

    @patch("pyspark.sql.SparkSession")
    @patch("pyspark.SparkConf")
    def test_get_memory2(self, mock_config, mock_spark):
        from refractml.spark_distributed_session import get_memory
        output = get_memory("400Mi")
        self.assertEqual(output, "500m")

    @patch("pyspark.sql.SparkSession")
    @patch("pyspark.SparkConf")
    def test_get_memory3(self, mock_config, mock_spark):
        from refractml.spark_distributed_session import get_memory
        output = get_memory("1Gi")
        self.assertEqual(output, "1g")

    @patch("pyspark.sql.SparkSession")
    @patch("pyspark.SparkConf")
    @patch("mosaic_utils.ai.k8.pod_metrics_summary.volume_mount_count")
    @patch("mosaic_utils.ai.k8.pod_metrics_summary.volume_custom_mount")
    def test_add_volume_mounts(self, mock_vm, mock_vc, mock_config, mock_spark):
        from refractml.spark_distributed_session import add_volume_mounts
        mock_vm.return_value = [{"name": "test_mount", "mountPath": "samplePath", "subPath": "sub_path"}]
        mock_vc.return_value = [{"name": "test_mount", "mountPath": "samplePath"}]
        output = add_volume_mounts({})
        self.assertEqual(
            output["spark.kubernetes.executor.volumes.persistentVolumeClaim.test_mount.mount.readOnly"], "false")

    @patch("pyspark.sql.SparkSession")
    @patch("pyspark.SparkConf")
    def test_get_spark_session(self, mock_config, mock_spark):
        from refractml.spark_distributed_session import get_spark_session
        output = get_spark_session("app-name", mock_config)
        self.assertEqual(output.side_effect, None)

    @patch("pyspark.SparkConf")
    def test_get_spark_session(self, mock_config):
        from refractml.spark_distributed_session import add_executor_env_variables
        output = add_executor_env_variables(mock_config)
        self.assertEqual(output.side_effect, None)
