"""Tests for views.py."""

import pytest

import ckanext.dataset_views.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "dataset_views")
@pytest.mark.usefixtures("with_plugins")
def test_dataset_views_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("dataset_views.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, dataset_views!"
