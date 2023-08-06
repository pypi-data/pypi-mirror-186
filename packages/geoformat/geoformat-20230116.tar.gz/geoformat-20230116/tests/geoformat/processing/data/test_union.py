from tests.utils.tests_utils import test_function

from geoformat.processing.data.union import (
    union_metadata,
    union_geolayer
)

from geoformat.conf.error_messages import (
    metadata_fields_not_same,
    metadata_geometry_crs
)
from tests.data.fields_metadata import geolayer_data_fields_metadata_complete

from tests.data.metadata import metadata_fr_dept_data_and_geometry, metadata_paris_velib

from tests.data.geolayers import (
    geolayer_btc_price_sample,
    geolayer_btc_price_sample_a,
    geolayer_btc_price_sample_b,
    geolayer_btc_price_sample_c,
)

union_metadata_parameters = {
    0: {
        "metadata_a": metadata_fr_dept_data_and_geometry,
        "metadata_b": metadata_fr_dept_data_and_geometry,
        "metadata_name": metadata_fr_dept_data_and_geometry["name"],
        "feature_serialize": None,
        "return_value": metadata_fr_dept_data_and_geometry,
    },
    1: {
        "metadata_a": metadata_fr_dept_data_and_geometry,
        "metadata_b": metadata_fr_dept_data_and_geometry,
        "metadata_name": "test_metadata",
        "feature_serialize": None,
        "return_value": {
            "name": "test_metadata",
            "fields": {
                "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
            },
            "geometry_ref": {"type": {"Polygon", "MultiPolygon"}, "crs": 2154},
        },
    },
    2: {
        "metadata_a": metadata_fr_dept_data_and_geometry,
        "metadata_b": metadata_paris_velib,
        "metadata_name": "test_metadata",
        "feature_serialize": None,
        "return_value": metadata_fields_not_same,
    },
    3: {
        "metadata_a": {
            "name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
            "fields": geolayer_data_fields_metadata_complete,
            "geometry_ref": {"type": {"MultiPolygon"}, "crs": 2154},
        },
        "metadata_b": {
            "name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
            "fields": geolayer_data_fields_metadata_complete,
            "geometry_ref": {"type": {"Polygon"}, "crs": 2154},
        },
        "metadata_name": "test_metadata",
        "feature_serialize": None,
        "return_value": {
            "name": "test_metadata",
            "fields": geolayer_data_fields_metadata_complete,
            "geometry_ref": {"type": {"MultiPolygon", "Polygon"}, "crs": 2154},
        }
    },
    4: {
        "metadata_a": {
            "name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
            "fields": geolayer_data_fields_metadata_complete,
            "geometry_ref": {"type": {"MultiPolygon"}, "crs": 2154},
        },
        "metadata_b": {
            "name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
            "fields": geolayer_data_fields_metadata_complete,
            "geometry_ref": {"type": {"Polygon"}, "crs": 4326},
        },
        "metadata_name": "test_metadata",
        "feature_serialize": None,
        "return_value": metadata_geometry_crs
    },
    5: {
        "metadata_a": {'name': 'BTC_DAILY_PRICE', 'fields': {'DATE': {'type': 'Date', 'index': 0}, 'DAYS': {'type': 'Integer', 'index': 1}, 'TIMESTAMP': {'type': 'Integer', 'index': 2}, 'USD_PRICE_CLOSE': {'type': 'Real', 'width': 7, 'precision': 2, 'index': 3}, 'PRICE_ESTIMATE_MINUS_1STD': {'type': 'Real', 'width': 22, 'precision': 20, 'index': 4}, 'PRICE_ESTIMATE_MINUS_2STD': {'type': 'Real', 'width': 21, 'precision': 20, 'index': 5}, 'PRICE_ESTIMATE_2019': {'type': 'Real', 'width': 22, 'precision': 20, 'index': 6}, 'PRICE_ESTIMATE': {'type': 'Real', 'width': 22, 'precision': 20, 'index': 7}, 'PRICE_ESTIMATE_PLUS_1STD': {'type': 'Real', 'width': 22, 'precision': 20, 'index': 8}, 'PRICE_ESTIMATE_PLUS_2STD': {'type': 'Real', 'width': 22, 'precision': 20, 'index': 9}}},
        "metadata_b": {'name': 'BTC_DAILY_PRICE', 'fields': {'DATE': {'type': 'Date', 'index': 0}, 'DAYS': {'type': 'Integer', 'index': 1}, 'TIMESTAMP': {'type': 'Integer', 'index': 2}, 'USD_PRICE_CLOSE': {'type': 'Real', 'width': 7, 'precision': 2, 'index': 3}, 'PRICE_ESTIMATE_MINUS_1STD': {'type': 'Real', 'width': 18, 'precision': 15, 'index': 4}, 'PRICE_ESTIMATE_MINUS_2STD': {'type': 'Real', 'width': 18, 'precision': 15, 'index': 5}, 'PRICE_ESTIMATE_2019': {'type': 'Real', 'width': 19, 'precision': 15, 'index': 6}, 'PRICE_ESTIMATE': {'type': 'Real', 'width': 17, 'precision': 14, 'index': 7}, 'PRICE_ESTIMATE_PLUS_1STD': {'type': 'Real', 'width': 17, 'precision': 14, 'index': 8}, 'PRICE_ESTIMATE_PLUS_2STD': {'type': 'Real', 'width': 18, 'precision': 14, 'index': 9}}},
        "metadata_name": "BTC_DAILY_PRICE",
        "feature_serialize": None,
        "return_value": {'name': 'BTC_DAILY_PRICE', 'fields': {'DATE': {'type': 'Date', 'index': 0}, 'DAYS': {'type': 'Integer', 'index': 1}, 'TIMESTAMP': {'type': 'Integer', 'index': 2}, 'USD_PRICE_CLOSE': {'type': 'Real', 'width': 7, 'precision': 2, 'index': 3}, 'PRICE_ESTIMATE_MINUS_1STD': {'type': 'Real', 'width': 22, 'precision': 20, 'index': 4}, 'PRICE_ESTIMATE_MINUS_2STD': {'type': 'Real', 'width': 21, 'precision': 20, 'index': 5}, 'PRICE_ESTIMATE_2019': {'type': 'Real', 'width': 22, 'precision': 20, 'index': 6}, 'PRICE_ESTIMATE': {'type': 'Real', 'width': 22, 'precision': 20, 'index': 7}, 'PRICE_ESTIMATE_PLUS_1STD': {'type': 'Real', 'width': 22, 'precision': 20, 'index': 8}, 'PRICE_ESTIMATE_PLUS_2STD': {'type': 'Real', 'width': 22, 'precision': 20, 'index': 9}}}
    },
}

union_geolayer_parameters = {
    0: {
        "geolayer_list": [geolayer_btc_price_sample_a, geolayer_btc_price_sample_b, geolayer_btc_price_sample_c],
        "geolayer_name": 'BTC_DAILY_PRICE',
        "serialize": False,
        "return_value": geolayer_btc_price_sample
    }
}


def test_all():
    # union_metadata
    print(test_function(union_metadata, union_metadata_parameters))

    # union geolayer
    print(test_function(union_geolayer, union_geolayer_parameters))


if __name__ == "__main__":
    test_all()
