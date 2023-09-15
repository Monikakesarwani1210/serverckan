
import ckan.plugins as plugins
from ckan.plugins.interfaces import IConfigurer, ITemplateHelpers
from ckan.common import c
from ckan.logic import get_action

class ExampleThemeTrackingSummaryPlugin(plugins.SingletonPlugin):
    plugins.implements(IConfigurer, inherit=True)
    plugins.implements(ITemplateHelpers, inherit=True)

    def update_config(self, config):
        # Add the template directory to the search path
        plugins.toolkit.add_template_directory(config, 'templates')

    def is_fallback(self):
        return True

    def get_helpers(self):
        # Define a custom helper function to retrieve page view count
        def get_page_view_count(dataset_id):
            context = {'ignore_auth': True, 'use_cache': False}
            result = get_action('package_show')(context, {'id': dataset_id})
            tracking_summary = result.get('tracking_summary', {})
            return tracking_summary.get('total', 0)

        # Return the helper function
        return {
            'get_page_view_count': get_page_view_count
        }

