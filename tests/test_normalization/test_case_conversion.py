from ngohub.normalization.processors import camel_to_snake_case_dictionary, camel_to_snake_case_dictionary_list


def test_camel_to_snake_case_dictionary():
    test_dictionary = {
        "camelCase": "value",
        "anotherCamelCase": "value",
        "anIntegerCamelCase": 22,
        "aCamelCaseIsoDate": "2021-01-01T00:00:00Z",
        "a_snake_case_key": "value",
    }

    expected_result = {
        "camel_case": "value",
        "another_camel_case": "value",
        "an_integer_camel_case": 22,
        "a_camel_case_iso_date": "2021-01-01T00:00:00Z",
        "a_snake_case_key": "value",
    }

    actual_result = camel_to_snake_case_dictionary(test_dictionary)

    assert actual_result == expected_result


def test_camel_to_snake_case_dictionary_list():
    test_list = [
        {
            "camelCase": "value",
            "anotherCamelCase": "value",
            "anIntegerCamelCase": 22,
            "aCamelCaseIsoDate": "2021-01-01T00:00:00Z",
            "a_snake_case_key": "value",
        },
        {
            "camelCase": "value",
            "anotherCamelCase": "value",
            "anIntegerCamelCase": 22,
            "aCamelCaseIsoDate": "2021-01-01T00:00:00Z",
            "a_snake_case_key": "value",
        },
    ]

    expected_result = [
        {
            "camel_case": "value",
            "another_camel_case": "value",
            "an_integer_camel_case": 22,
            "a_camel_case_iso_date": "2021-01-01T00:00:00Z",
            "a_snake_case_key": "value",
        },
        {
            "camel_case": "value",
            "another_camel_case": "value",
            "an_integer_camel_case": 22,
            "a_camel_case_iso_date": "2021-01-01T00:00:00Z",
            "a_snake_case_key": "value",
        },
    ]

    actual_result = camel_to_snake_case_dictionary_list(test_list)

    assert actual_result == expected_result
