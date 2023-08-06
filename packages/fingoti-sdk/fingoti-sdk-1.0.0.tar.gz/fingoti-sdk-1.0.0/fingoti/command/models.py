from fingoti.model_utils import (  # noqa: F401
    ModelSimple,
    cached_property
)

class Command(ModelSimple):
    _composed_schemas = {}
    attribute_map = {
        'property': 'property',
        'operation': 'operation',
        'payload': 'payload'
    }
    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])
    @cached_property
    def discriminator():
        return None


class CommandOperation():
    READ = 0
    WRITE = 1