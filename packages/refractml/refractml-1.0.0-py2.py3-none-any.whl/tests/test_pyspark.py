# -*- coding: utf-8 -*-
"""Test cases for pyspark model flavor."""

import os
import shutil
import unittest

from mosaic_utils.ai.flavours.pyspark import (
    dump_model,
    get_model_type,
    load_model,
)
from pyspark.sql import SparkSession


class TestPySpark(unittest.TestCase):
    """Class cases for pyspark model flavor."""

    spark = SparkSession.builder.appName(__name__).getOrCreate()

    def setUp(self):
        """Setup test environment."""
        self._base_dir = os.path.dirname(os.path.abspath(__file__))
        self._saved_models_dir = os.path.join(self._base_dir, "saved_models")
        self._temp_model_dir = os.path.join(self._base_dir, "temp_models")
        self._dummy_model_path = os.path.join(self._temp_model_dir, "dummy_model")

        if os.path.exists(self._temp_model_dir):
            shutil.rmtree(self._temp_model_dir)

        os.makedirs(self._temp_model_dir)

    def tearDown(self):
        """Teardown test environment."""
        if os.path.exists(self._temp_model_dir):
            shutil.rmtree(self._temp_model_dir)

    def test_get_model_type(self):
        """Test get model type."""
        model_type = get_model_type(
            os.path.join(self._saved_models_dir, "SurvivalRegressionModel")
        )
        self.assertEqual(model_type, "pyspark.ml.regression.AFTSurvivalRegressionModel")

    def test_load_model(self):
        """Test load_model function."""
        for path in os.listdir(self._saved_models_dir):
            model_path = os.path.join(self._saved_models_dir, path)
            load_model(model_path)
        self.assertEqual(1, 1)

    def test_dump_model(self):
        """Test for dump_model."""
        model_path = os.path.join(
            self._saved_models_dir, os.listdir(self._saved_models_dir)[0]
        )
        model_object = load_model(model_path)
        self.assertFalse(os.path.exists(self._dummy_model_path))
        dump_model(model_object, self._dummy_model_path)
        self.assertTrue(os.path.exists(self._dummy_model_path))


if __name__ == "__main__":
    unittest.main()
