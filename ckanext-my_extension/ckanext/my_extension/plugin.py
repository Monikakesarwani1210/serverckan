from ckan.plugins.interfaces import IConfigurer, ITemplateHelpers
from ckan.logic import get_action
from ckan.common import CKANConfig
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class TrackingSummaryPlugin(plugins.SingletonPlugin):
    plugins.implements(IConfigurer, inherit=True)
    plugins.implements(ITemplateHelpers, inherit=True)

    # Define a custom helper function to retrieve tracking summary data for a dataset
    def get_dataset_tracking_summary(self, dataset_id):
        context = {'ignore_auth': True, 'use_cache': False}
        result = get_action('package_show')(context, {'id': dataset_id})
        tracking_summary = result.get('tracking_summary', {})
        return tracking_summary

    def update_config(self, config: CKANConfig):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')
    def is_fallback(self):
        return True

    def get_helpers(self):
        # Return the custom helper function in the template context
        return {
            'get_dataset_tracking_summary': self.get_dataset_tracking_summary
        }
