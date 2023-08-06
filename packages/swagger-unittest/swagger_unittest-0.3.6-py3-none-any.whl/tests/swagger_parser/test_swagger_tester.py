# -*- coding:utf-8 -*-
import pytest

from swagger_unittest.swagger_tester import swagger_tester


def test_validate_definition(swagger_parser, pet_definition_example):
    valid_response = swagger_parser.definitions_example['Pet']

    # Valid Pet is valid definition
    swagger_tester.validate_definition(swagger_parser, valid_response, valid_response)

    # Changing list with emtpy list is valid definition of Pet
    response = valid_response.copy()
    assert len(response['tags']) > 0
    response['tags'] = []
    swagger_tester.validate_definition(swagger_parser, valid_response, response)

    # Changing list with string is not valid definition of Pet
    with pytest.raises(AssertionError):
        response = valid_response.copy()
        response['tags'] = 'foo'
        swagger_tester.validate_definition(swagger_parser, valid_response, response)

    # Empty dict is not valid Pet
    with pytest.raises(AssertionError, match=r".*Responses are not compatible\. Definition of valid response is.*"):
        swagger_tester.validate_definition(swagger_parser, valid_response, {})
