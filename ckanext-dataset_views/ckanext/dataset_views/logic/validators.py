import ckan.plugins.toolkit as tk


def dataset_views_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "dataset_views_required": dataset_views_required,
    }
