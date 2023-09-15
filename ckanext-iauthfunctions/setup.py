from setuptools import setup

setup(
    # ... other setup options ...

    # Define entry points for CKAN plugins as a dictionary
    entry_points={
        'ckan.plugins': [
            'tracking_summary=ckanext.iauthfunctions.plugin:ExampleThemeTrackingSummaryPlugin',
        ],
    },

    # ... other setup options ...
)

