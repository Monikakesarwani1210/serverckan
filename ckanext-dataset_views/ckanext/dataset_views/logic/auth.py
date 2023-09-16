import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def dataset_views_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "dataset_views_get_sum": dataset_views_get_sum,
    }
