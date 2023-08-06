# -*- coding: utf-8 -*-

import pytest

from swagger_unittest.swagger_parser.swagger_parser import SwaggerParser


@pytest.fixture
def swagger_parser():
    return SwaggerParser('data/swagger.yaml')


@pytest.fixture
def swagger_allof_parser():
    return SwaggerParser('data/allof.yaml')


@pytest.fixture
def swagger_test2_parser():
    return SwaggerParser('data/test.yaml')


@pytest.fixture
def inline_parser():
    return SwaggerParser('data/inline.yaml')


@pytest.fixture
def swagger_enum_parser():
    return SwaggerParser('data/enum.yaml')


@pytest.fixture(scope='module',
                params=['data/no_properties.yaml',
                        'data/object_no_schema.yaml',
                        'data/allof.yaml',
                        'data/array_ref_simple.yaml',
                        'data/null_type.yaml',
                        'data/array_items_list.yaml',
                        'data/type_list.yaml',
                        ])
def swagger_file_parser(request):
    return SwaggerParser(request.param)


@pytest.fixture
def pet_definition_example():
    return {
        'category': {
            'id': 1,
            'name': 'string'
        },
        'status': 'string',
        'name': 'doggie',
        'tags': [
            {
                'id': 1,
                'name': 'string'
            }
        ],
        'photoUrls': [
        ],
        'id': 1
    }


@pytest.fixture
def inline_example():
    return {
        '4a57805895c24bb72e81eb6a6df32b7ddf3c1bea42a8f2173bb5c1f6a1c9a8ef': ('test', 'post', None)
    }


@pytest.fixture
def get_path_data():
    pet_get = {
        'description': "Pet's Unique identifier",
        'name': 'petId',
        'in': 'path',
        'pattern': '^[a-zA-Z0-9-]+$',
        'required': True,
        'type': 'string',
    }
    get_responses = {
        '200': {
            'description': u'successful \xb5-\xf8per\xe4tio\xf1',
            'schema': {
                '$ref': '#/definitions/Pet',
            }
        },
        '400': {'description': 'Invalid ID supplied'},
        '404': {'description': 'Pet not found'}
    }
    expected_get_pet_path = {
        'parameters': {'petId': pet_get},
        'responses': get_responses
    }
    return expected_get_pet_path


@pytest.fixture
def post_put_path_data():
    pet_post = {
        'description': u'Pet object that needs to be added to the store (it may be a \xb5Pig or a Sm\xf8rebr\xf6d)',
        'in': 'body',
        'name': 'body',
        'required': False,
        'schema': {
            '$ref': '#/definitions/Pet',
        }
    }
    pet_put = pet_post.copy()
    pet_put['description'] = 'Pet object that needs to be added to the store'
    schema_created = {
        'description': 'Created',
        'schema': {
            '$ref': '#/definitions/Pet',
        }
    }
    expected_post_put_paths = {
        'post': {
            'consumes': ['application/json'],
            'parameters': {'body': pet_post},
            'responses': {
                '201': schema_created,
                '405': {'description': 'Invalid input'}
            }
        },
        'put': {
            'consumes': ['application/json'],
            'parameters': {'body': pet_put},
            'responses': {
                '200': schema_created,
                '400': {'description': 'Invalid ID supplied'},
                '404': {'description': 'Pet not found'},
                '405': {'description': 'Validation exception'}
            }
        }
    }
    return expected_post_put_paths


@pytest.fixture
def swagger_array_parser():
    return SwaggerParser('data/swagger_arrays.yaml')
