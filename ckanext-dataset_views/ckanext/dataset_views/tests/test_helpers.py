"""Tests for helpers.py."""

import ckanext.dataset_views.helpers as helpers


def test_dataset_views_hello():
    assert helpers.dataset_views_hello() == "Hello, dataset_views!"
