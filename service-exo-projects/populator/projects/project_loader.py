import yaml


from populate.populator.common.errors import ConfigurationError

from .projects_manager import ProjectsManager


def project_constructor(loader, node):
    if isinstance(node, yaml.ScalarNode):
        item = loader.construct_scalar(node)
        if not isinstance(item, str) or not item:
            raise ConfigurationError(
                'value {} cannot be interpreted as project'.format(item))
    elif isinstance(node, yaml.MappingNode):
        item = loader.construct_mapping(node)
        if not isinstance(item, dict) or not item:
            raise ConfigurationError(
                'value {} cannot be interpreted as project'.format(item))
    return ProjectsManager().get_object(item)
