# -*- coding: utf-8 -*-
import types
import ast
import pandas as pd
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual, Layout
from IPython.display import clear_output, display
from refractml.api import register_model


class RegisterModel:
    def __init__(self):
        self.tab = widgets.Tab()
        self.user_config = list()
        self.tab_names = [
            "Meta Information",
            "Model Information",
            "Data",
            "Optional Features",
        ]

        self.layout_ui_on_screen()

    def layout_ui_on_screen(self):
        self.children = [
            self.meta_information(),
            self.model_information(),
            self.data_information(),
            self.optional_batteries(),
        ]
        self.tab.children = self.children

        self.set_titles()

    def meta_information(self):

        self.model_name = widgets.Text(
            placeholder="(string) name of the model  without space ",
            layout=Layout(width="50%", height="80px"),
        )
        self.model_description = widgets.Textarea(
            placeholder="(string): description of the model",
            layout=Layout(width="50%", height="80px"),
        )

        self.input_type = widgets.RadioButtons(
            position="horizontal",
            options=["json", "csv"],
            value="json",
            layout=Layout(width="30%"),
            description="Input Type",
            disabled=False,
        )

        self.flavor = widgets.Dropdown(
            options=[
                "sklearn",
                "pytorch",
                "keras",
                "tensorflow",
                "pyspark",
                "spacy",
                "application",
                "r",
                "pmml",
                "ensemble",
            ],
            layout=Layout(width="30%"),
            value="sklearn",
            description="Flavor*",
            disabled=False,
        )

        self.model_type = widgets.Dropdown(
            options=[None, "classification", "regression"],
            layout=Layout(width="30%"),
            value=None,
            description="Model Type*",
            disabled=False,
        )

        self.tags = widgets.Text(
            layout=Layout(width="100%"),
            placeholder="Variable Name or (array of strings) user tags associated with the model",
            description="Tags",
        )

        self.init_script = widgets.Textarea(
            description="Init Script", layout=Layout(width="100%", height="40px")
        )

        return widgets.VBox(
            [
                widgets.HBox(
                    [
                        widgets.Label("Model Name*", layout=Layout(width="50%")),
                        widgets.Label("Model Description*", layout=Layout(width="50%")),
                    ]
                ),
                widgets.HBox([self.model_name, self.model_description]),
                widgets.HBox([self.input_type, self.flavor, self.model_type]),
                widgets.HBox([self.init_script]),
                widgets.HBox([self.tags]),
            ]
        )

    def model_information(self):

        self.score_function = widgets.Text(
            placeholder="scoring_func (function): function to be used for scoring",
            layout=Layout(width="50%"),
            disabled=False,
        )
        self.model_object = widgets.Text(
            layout=Layout(width="50%"),
            placeholder="model_obj (object): model to be registered",
            disabled=False,
        )
        self.schema = widgets.Text(
            placeholder="(Dict): input and output schema structure for scoring function",
            layout=Layout(width="100%"),
            disabled=False,
        )
        self.metadata_info = widgets.Text(
            placeholder="metadata_info: metadata information about the version",
            layout=Layout(width="100%"),
            disabled=False,
        )
        self.model_display = widgets.Checkbox(
            description="model_display: If true display model on model list",
            layout=Layout(width="100%"),
        )

        return widgets.VBox(
            [
                widgets.HBox(
                    [
                        widgets.Label("Model Object*", layout=Layout(width="50%")),
                        widgets.Label("Score Function*", layout=Layout(width="50%")),
                    ]
                ),
                widgets.HBox([self.model_object, self.score_function]),
                widgets.HBox(
                    [widgets.Label("Scoring Schema", layout=Layout(width="100%"))]
                ),
                widgets.HBox([self.schema]),
                widgets.Label(
                    "Version Metadata Information", layout=Layout(width="100%")
                ),
                self.metadata_info,
                self.model_display,
            ]
        )

    def data_information(self):
        self.y_true = widgets.Text(description="Y True", placeholder="Var Name")
        self.y_pred = widgets.Text(description="Y Pred", placeholder="Var Name")
        self.prob = widgets.Text(description="Prob", placeholder="Var Name")

        self.features = widgets.Text(
            description="Features", placeholder="features : dummy feature names"
        )
        self.labels = widgets.Text(
            description="Labels", placeholder="labels: predicted labels"
        )

        self.feature_names = widgets.Text(
            description="Feature Names", placeholder="feature_names : all features"
        )
        self.datasource_name = widgets.Text(
            description="Data Source Name", placeholder="datasource_name(string):"
        )

        self.x_train = widgets.Text(
            description="X Train",
            placeholder="x_train (numpy array) : training data of model with feature column",
        )
        self.x_test = widgets.Text(
            description="X Test",
            placeholder="x_test (numpy array) :  test data of model with feature column",
        )

        self.y_train = widgets.Text(
            description="Y Train",
            placeholder="y_train (numpy array) : training data of model with feature column",
        )
        self.y_test = widgets.Text(
            description="Y Test",
            placeholder="y_test (numpy array) :  test data of model with feature column",
        )

        return widgets.VBox(
            [
                widgets.HBox([self.y_true, self.y_pred, self.prob]),
                widgets.HBox([self.labels, self.feature_names, self.datasource_name]),
                widgets.HBox([self.x_train, self.x_test]),
                widgets.HBox([self.y_train, self.y_test]),
            ]
        )

    def optional_batteries(self):
        self.explain_ai = widgets.Checkbox(
            value=False, description="Explain AI", disabled=False
        )

        self.kyd = widgets.Checkbox(
            value=False, description="Know Your Data", disabled=False
        )

        self.kyd_score = widgets.Checkbox(
            value=False, description="Drift Score", disabled=False
        )

        return widgets.VBox([self.explain_ai, self.kyd, self.kyd_score])

    def set_titles(self):
        for i in range(len(self.tab_names)):
            self.tab.set_title(i, self.tab_names[i])

    def variable_inference(self, value):
        if value == "":
            return None, None
        try:
            return_value = eval(value)
        except Exception as e:
            try:
                return_value = ast.literal_eval(value)
            except Exception as e:
                return_value = value

        return type(return_value), return_value

    def build_config(self):

        self.user_config.append(
            dict(parameter_name="name", data_type=str, value=str(self.model_name.value))
        )
        self.user_config.append(
            dict(
                parameter_name="description",
                data_type=str,
                value=str(self.model_description.value),
            )
        )
        self.user_config.append(
            dict(parameter_name="flavour", data_type=str, value=str(self.flavor.value))
        )
        self.user_config.append(
            dict(
                parameter_name="init_script",
                data_type=str,
                value=str(self.init_script.value),
            )
        )

        _list_of_var = [
            (self.tags, "tags"),
            (self.model_type, "model_type"),
            (self.model_object, "model_object"),
            (self.score_function, "score_function"),
            (self.schema, "schema"),
            (self.metadata_info, "metadata_info"),
            (self.model_display, "model_display"),
            (self.y_true, "y_true"),
            (self.y_pred, "y_pred"),
            (self.prob, "prob"),
            (self.labels, "labels"),
            (self.feature_names, "feature_names"),
            (self.datasource_name, "datasource_name"),
            (self.x_train, "x_train"),
            (self.y_train, "y_train"),
            (self.x_test, "x_test"),
            (self.y_test, "y_test"),
            (self.explain_ai, "explain_ai"),
            (self.kyd, "kyd"),
            (self.kyd_score, "kyd_score"),
        ]
        for field, name in _list_of_var:
            data_type, value = self.variable_inference(field.value)
            self.user_config.append(
                dict(parameter_name=name, data_type=data_type, value=value)
            )

        self.user_config_frame = pd.DataFrame(self.user_config)

    def register_model_callback(self, *args, **kwargs):
        self.build_config()
        user_config = dict(
            zip(self.user_config_frame.parameter_name, self.user_config_frame.value)
        )
        clear_output(wait=True)
        display(
            register_model(
                model_obj=user_config.get("model_object"),
                scoring_func=user_config.get("score_function"),
                name=user_config.get("name"),
                description=user_config.get("description"),
                flavour=user_config.get("flavour"),
                tags=user_config.get("tags", None),
                init_script=user_config.get("init_script", None),
                schema=user_config.get("schema", None),
                y_true=user_config.get("y_true", None),
                y_pred=user_config.get("y_pred", None),
                prob=user_config.get("prob", None),
                features=user_config.get("feature_names", None),
                labels=user_config.get("labels", None),
                model_type=user_config.get("model_type", None),
                datasource_name=user_config.get("datasource_name", None),
                metadata_info=user_config.get("metadata_info", None),
                input_type=user_config.get("input_type", None),
                x_train=user_config.get("x_train", None),
                y_train=user_config.get("y_train", None),
                feature_names=user_config.get("feature_names", None),
                explain_ai=user_config.get("explain_ai", False),
                x_test=user_config.get("x_test", None),
                y_test=user_config.get("y_test", None),
                kyd=user_config.get("kyd", False),
                kyd_score=user_config.get("kyd_score", False),
                **kwargs
            )
        )

    def print_all(self, *args, **kwargs):
        self.build_config()

        display(self.user_config_frame)

    def run(self):
        self.css = widgets.HTML(
            "<style >.grad_1{background: #2468a4;} .grad_2{ color:white; background: #2468a4;}</style>"
        )

        self.buttons = widgets.Button(description="Display")
        self.buttons.on_click(self.print_all)
        self.register_button = widgets.Button(description="Register")
        self.register_button.on_click(self.register_model_callback)

        self.logo = widgets.HTML(value="<h3>Model Registeration</h3>")
        self.logo.add_class("grad_2")
        self.dashboard = widgets.VBox(
            [
                self.css,
                self.logo,
                self.tab,
                widgets.HBox([self.buttons, self.register_button]),
            ]
        )
        self.dashboard.add_class("grad_1")
        display(self.dashboard)
