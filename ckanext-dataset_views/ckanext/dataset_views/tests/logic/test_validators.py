"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.dataset_views.logic import validators


def test_dataset_views_reauired_with_valid_value():
    assert validators.dataset_views_required("value") == "value"


def test_dataset_views_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.dataset_views_required(None)
