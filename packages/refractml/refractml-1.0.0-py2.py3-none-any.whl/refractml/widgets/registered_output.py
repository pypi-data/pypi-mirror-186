# -*- coding: utf-8 -*-
# Pretty Prints Model Describe
import pprint

import ipywidgets as widgets
from IPython.display import clear_output, display
from dateutil import parser
from refractml.widgets.fields import Fields


class ModelDescribe(Fields):
    def __init__(self, ml_model_id=None):
        self.pp = pprint.PrettyPrinter(indent=2)
        self.ml_model_id = ml_model_id
        self._data = {}

        self.datetime_format = '%Y-%m-%dT%H:%M:%S%z'

        self.tab = widgets.Tab()
        self.tab_names = [
            "Model Metadata",
            "Version Metadata",
        ]

    def set_titles(self):
        for i in range(len(self.tab_names)):
            self.tab.set_title(i, self.tab_names[i])

    def model_meta_information(self):
        self.modelid_widget_ = self.text("Model id", value=self._data.get("id", ""), disabled=False)

        return widgets.VBox(
            [
                widgets.HBox(
                    [
                        self.modelid_widget_,
                        self.text("Name", value=self._data.get("name", "")),
                        self.text("Flavour", value=self._data.get("flavour", "")),
                    ]
                ),
                widgets.HBox(
                    [
                        self.textarea("Description", value=self._data.get("description", False)),
                        self.text("Project", value=self._data.get("project_id", "")),
                    ]
                ),
                widgets.HBox(
                    [
                        self.checkbox("Deployment Status", value=self._data.get("deploymentstatus", False)),
                        self.checkbox("Model Display", value=self._data.get("model_display", False))
                    ]
                ),
                widgets.HBox(
                    [
                        self.text("Source", value=self._data.get("source", "")),
                        self.text("Tag", value=self._data.get("tags", "")),
                        self.text("Type", value=self._data.get("type", "")),
                    ]
                ),
                widgets.HBox(
                    [
                        self.text("Created By", "25%", value=self._data.get("created_by", "")),
                        self.datetime("On",
                                      value=parser.parse(self._data.get("created_on"))),
                    ]
                ),
                widgets.HBox(
                    [
                        self.text("Modified By", "25%", value=self._data.get("last_modified_by", "")),
                        self.datetime("On", value=parser.parse(self._data.get("last_modified_on"))),
                    ]
                ),

            ]
        )

    def init_script_dashboard(self, init_script):
        script_ = str(init_script).replace('\\n', '\n').replace('\\t', '\t').replace('\"', "")
        init_script_dashboard = widgets.VBox([
            widgets.HBox([self.textarea("Init Script", value=script_, width="100%", rows=20)]),
        ])
        return init_script_dashboard

    def model_info_dashboard(self, model_info):
        if not model_info:
            return widgets.HBox([widgets.Label("Model Info Is Not Present")])

        features_name = model_info.get("features_name", "")
        if isinstance(features_name, str) or not features_name:
            features_name = ["Empty"]

        model_info_dashboard = widgets.VBox([
            widgets.HBox([self.checkbox("Deeplearning Model", value=model_info.get("deep_learning_model", False)),
                          self.checkbox("Know Your Data", value=model_info.get("kyd", False)),
                          self.checkbox("Explain AI", value=model_info.get("expai", False)),
                          self.checkbox("Infer Feature DType", value=model_info.get("feature_type_inferenced", False)),
                          ]),
            widgets.HBox([self.select_multiple("Features",
                                               features_name,
                                               value=features_name),
                          self.textarea("Feature Type", value=self.pp.pformat(model_info.get("features_type", "")),
                                        rows=8)
                          ]),
            widgets.HBox(
                [self.radio("Mode", options=["classification", "regression"], value=model_info.get("mode", "")),
                 self.text("No. Features", value=str(model_info.get("number_of_features", ""))),
                 self.text("No. Targets", value=str(model_info.get("number_of_targets", "")))
                 ]),
            widgets.HBox(
                [self.textarea("Target Mapping", value=self.pp.pformat(model_info.get("targets_mapping", "")), rows=8),
                 self.textarea("Temp Dir", value=str(model_info.get("temp_dir", "")), rows=8)
                 ]),

        ])

        return model_info_dashboard

    def model_class_dashboard(self, model_class):
        model_class_ = str(model_class).replace('\\n', '\n').replace('\\t', '\t').replace('\"', "")
        model_class_dashboard = widgets.VBox([
            widgets.HBox([self.textarea("Model Class", value=model_class_, width="100%", rows=20)]),
        ])
        return model_class_dashboard

    def deploy_info_dashboard(self, deploy_info):
        deploy_info_dashboard = widgets.VBox([
            widgets.HBox(
                [self.textarea("Deploy Info", value=str(deploy_info.get("deploy_info", "")), width="100%", rows=5)]),
            widgets.HBox(
                [self.textarea("Deployment", value=str(deploy_info.get("deployments", "")), width="100%", rows=5)]),
        ])
        return deploy_info_dashboard

    def others_dashboard(self, version_info):

        others_info_dashboard = widgets.VBox([
            widgets.HBox(
                [self.textarea("Profiling", value=str(version_info.get("profiling", "")), width="100%", rows=5)]),
            widgets.HBox([self.textarea("Schema", value=str(version_info.get("schema", "")), width="100%", rows=5)]),
        ])
        return others_info_dashboard

    def version_meta_information(self):
        children_ = []
        titles_ = []
        for each_version in self._data["versions"]:
            detail_tab = widgets.Tab()
            detail_tab_children = []
            detail_titles_ = ["Image", "Model Information", "Init Script", "Model Class", "Deploy Info", "Others"]

            image_dashboard = widgets.VBox([
                self.text("CPU", value=str(each_version.get("docker_image_url", "")), width="80%"),
                self.text("GPU", value=str(each_version.get("gpu_docker_image_url", "")), width="80%"),

            ])

            detail_tab_children.append(image_dashboard)

            model_info_dashboard = self.model_info_dashboard(each_version.get("model_info", ""))
            detail_tab_children.append(model_info_dashboard)

            init_script_dashboard = self.init_script_dashboard(each_version.get("init_script", ""))
            detail_tab_children.append(init_script_dashboard)

            model_class_dashboard = self.model_class_dashboard(each_version.get("model_class", ""))
            detail_tab_children.append(model_class_dashboard)

            deploy_info_dashboard = self.deploy_info_dashboard(each_version)
            detail_tab_children.append(deploy_info_dashboard)

            others_dashboard = self.others_dashboard(each_version)
            detail_tab_children.append(others_dashboard)

            detail_tab.children = detail_tab_children
            for i in range(len(detail_tab_children)):
                detail_tab.set_title(i, detail_titles_[i])

            dashboard = widgets.VBox([
                widgets.HBox([self.text("No", value=str(each_version.get("version_no", ""))),
                              self.text("Id", value=str(each_version.get("id", ""))),
                              self.text("Status", value=str(each_version.get("description", ""))),
                              ]),
                widgets.HBox([self.text("Datasource", value=str(each_version.get("datasource_name", ""))),
                              self.text("Deployment Model", value=str(each_version.get("dependent_model", ""))),
                              self.textarea("Description", value=str(each_version.get("description", ""))),
                              ]),
                detail_tab,
                widgets.HBox([self.text("Input Type", value=str(each_version.get("input_type", ""))),
                              self.text("Model Id", value=str(each_version.get("ml_model_id", ""))),

                              ]),
                widgets.HBox([self.text("Object URL", value=str(each_version.get("object_url", "")), width="100%"),
                              ]),
                widgets.HBox(
                    [
                        self.text("Created By", "25%", value=each_version.get("created_by", "")),
                        self.datetime("On",
                                      value=parser.parse(each_version.get("created_on", ""))),
                    ]
                ),
                widgets.HBox(
                    [
                        self.text("Modified By", "25%", value=each_version.get("last_modified_by", "")),
                        self.datetime("On", value=parser.parse(each_version.get("last_modified_on", ""))),
                    ]
                ),
            ])

            children_.append(dashboard)
            titles_.append(str(each_version.get("version_no", "")) + ") " + each_version.get("id", ""))
        accordion = widgets.Accordion(children=children_, titles=titles_)
        for i in range(len(children_)):
            accordion.set_title(i, titles_[i])
        return accordion

    def print_raw(self, *args, **kwargs):
        return display(self._data)

    def clear_raw(self, *args, **kwargs):
        clear_output(wait=True)

    def describe_button_callback(self, *args, **kwargs):
        from refractml.api import describe_model
        self._data = describe_model(self.modelid_widget_.value)
        self.clear_raw()
        self.view(load_data=False)

    def view(self, use_data=None, load_data=True):
        try:
            if load_data:
                from refractml.api import describe_model
                self._data = describe_model(self.ml_model_id)

            if use_data:
                self._data = use_data

            self.children = [
                self.model_meta_information(),
                self.version_meta_information()
            ]
            self.tab.children = self.children

            self.set_titles()

            self.css = widgets.HTML(
                "<style>.grad_1{background: #2468a4;} .grad_2{ color:white; background: #2468a4;}</style>"
            )

            self.buttons = self.button("Print Raw", 'eye')
            self.buttons.on_click(self.print_raw)
            self.clear_button = self.button("Close", 'close')
            self.clear_button.on_click(self.clear_raw)
            self.describe_button = self.button("Describe", 'binoculars')
            self.describe_button.on_click(self.describe_button_callback)

            self.logo = widgets.HTML(value="<h3>Model Describe</h3>")
            self.logo.add_class("grad_2")
            self.dashboard = widgets.VBox(
                [
                    self.css,
                    self.logo,
                    self.tab,
                    widgets.HBox([self.buttons, self.clear_button, self.describe_button]),
                ]
            )
            self.dashboard.add_class("grad_1")
            display(self.dashboard)
        except Exception as e:
            print(self._data)
