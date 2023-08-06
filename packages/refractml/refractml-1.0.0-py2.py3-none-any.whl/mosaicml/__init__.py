# -*- coding: utf-8 -*-

from .api import (
    add_version,
    apply_model_strategy,
    build_time_metrics,
    delete_model,
    deploy_model,
    describe_model,
    describe_model_using_model_name,
    ensemble_model_list,
    fetch_model_resources,
    generate_schema,
    get_model_info,
    get_model_profiling,
    list_models,
    load_model,
    load_train_and_test_data,
    promote_model,
    register_ensemble_model,
    register_model,
    stop_model,
    update_existing_model,
    update_metadata_info,
    update_model_details,
    update_version_details,
    fetch_feedback_accuracy,
    delete_model_version,
    add_artifacts,
    download_artifacts
)

from refractml.widgets.register_model import RegisterModel

from .decorators import scoring_func


__all__ = [
    "scoring_func",
    "add_version",
    "delete_model",
    "deploy_model",
    "apply_model_strategy",
    "promote_model",
    "describe_model",
    "list_models",
    "load_model",
    "register_model",
    "stop_model",
    "get_model_profiling",
    "generate_schema",
    "update_metadata_info",
    "update_existing_model",
    "update_model_details",
    "update_version_details",
    "register_ensemble_model",
    "ensemble_model_list",
    "build_time_metrics",
    "load_train_and_test_data",
    "fetch_model_resources",
    "describe_model_using_model_name",
    "get_model_info",
    "fetch_feedback_accuracy",
    "delete_model_version",
    "RegisterModel",
    "add_artifacts",
    "download_artifacts"
]
