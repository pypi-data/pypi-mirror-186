import datetime

from tests.utils.tests_utils import test_function

from geoformat.conversion.datetime_conversion import format_datetime_object_to_str_value


format_datetime_object_to_str_value_parameters = {
    0: {
        "datetime_value": datetime.datetime(year=2022, month=12, day=12),
        "format": ["year", "month", "day"],
        "return_value": "20221212",
    },
    1: {
        "datetime_value": datetime.datetime(year=2022, month=12, day=12),
        "format": ["year", "month"],
        "return_value": "202212",
    },
    2: {
        "datetime_value": datetime.datetime(year=2022, month=12, day=12, hour=11),
        "format": ["year", "month", "hour"],
        "return_value": "20221211",
    },
}


def test_all():
    # format_datetime_object_to_str_value
    print(
        test_function(
            format_datetime_object_to_str_value,
            format_datetime_object_to_str_value_parameters,
        )
    )


if __name__ == "__main__":
    test_all()
