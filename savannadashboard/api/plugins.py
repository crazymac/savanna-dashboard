from savannadashboard.api import base


class Plugin(base.Resource):
    resource_name = 'Plugin'

    def __init__(self, manager, info):
        base.Resource.__init__(self, manager, info)

        # Horizon requires each object in table to have an id
        self.id = self.name


class PluginManager(base.ResourceManager):
    resource_class = Plugin

    def list(self):
        return self._list('/plugins', 'plugins')

    def get(self, plugin_name):
        return self._get('/plugins/%s' % plugin_name, 'plugin')

    def get_version_details(self, plugin_name, hadoop_version):
        return self._get('/plugins/%s/%s' % (plugin_name, hadoop_version),
                         'plugin')