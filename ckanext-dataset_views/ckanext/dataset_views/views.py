
from flask import Blueprint


dataset_views = Blueprint(
    "dataset_views", __name__)


def page():
    return "Hello, dataset_views!"


dataset_views.add_url_rule(
    "/dataset_views/page", view_func=page)


def get_blueprints():
    return [dataset_views]
