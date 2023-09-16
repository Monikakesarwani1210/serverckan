import ckan.plugins.toolkit as tk
import ckanext.dataset_views.logic.schema as schema


@tk.side_effect_free
def dataset_views_get_sum(context, data_dict):
    tk.check_access(
        "dataset_views_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.dataset_views_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'dataset_views_get_sum': dataset_views_get_sum,
    }
