import copy
import datetime

from geoformat.conf.error_messages import (
    field_exists,
    field_missing,
    field_name_still_indexing,
    field_name_not_indexing,
    geometry_not_in_variable
)
from geoformat.manipulation.geolayer_manipulation import (
    delete_feature,
    drop_field,
    rename_field,
    create_field,
    add_attributes_index,
    check_attributes_index,
    delete_attributes_index,
    check_if_field_exists,
    split_geolayer_by_geometry_type,
)
from tests.data.coordinates import point_coordinates, linestring_coordinates, polygon_coordinates, \
    multipoint_coordinates, multilinestring_coordinates, multipolygon_coordinates
from tests.utils.tests_utils import test_function
from tests.data.geolayers import (
    geolayer_attributes_to_force_in_str,
    feature_list_data_and_geometry_geolayer,
    geolayer_attributes_only,
    geolayer_attributes_only_rename,
    geolayer_fr_dept_population,
    geolayer_geometry_only_all_geometries_type,
    geolayer_paris_velib,
    geolayer_paris_tokyo,
    geolayer_idf_reseau_ferre,
    feature_list_data_and_geometry_serialized_geolayer, geolayer_fields_with_bytes_values,
    geolayer_fields_with_bytes_values_forced,
)

from tests.data.features import (
    feature_geometry_only_collection,
    feature_geometry_only_collection_with_empty_geometries,
    feature_geometry_only_collection_empty, feature_list_structure_alpha, feature_list_attribute_only, date_value,
    time_value, date_time_value, feature_list_geometry_only, feature_list_geometry_only_with_all_geometries,
    feature_geometry_only_point, feature_geometry_only_point_empty, feature_geometry_only_linestring,
    feature_geometry_only_linestring_empty, feature_geometry_only_polygon, feature_geometry_only_polygon_empty,
    feature_geometry_only_multipoint, feature_geometry_only_multipoint_empty, feature_geometry_only_multilinestring,
    feature_geometry_only_multilinestring_empty, feature_geometry_only_multipolygon,
    feature_geometry_only_multipolygon_empty, feature_list_data_and_geometry, feature_list_bytes_attributes,
)
from tests.data.index import geolayer_fr_dept_population_CODE_DEPT_hash_index

from geoformat.manipulation.geolayer_manipulation import feature_list_to_geolayer

delete_feature_parameters = {
    0: {
        "geolayer": copy.deepcopy(geolayer_attributes_to_force_in_str),
        "i_feat_to_delete": 0,
        "return_value": {
            "metadata": {
                "name": "attributes_to_force_only_forced",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                1: {
                    "attributes": {
                        "field_integer": "1466",
                        "field_integer_list": "[987, 2345]",
                        "field_real": "8789.0",
                        "field_real_list": "[2.0, 5.0]",
                        "field_string": "salut",
                        "field_date": "",
                        "field_time": "11:22:10.000999",
                        "field_binary": "000000000140eff36b0a3d70a440bde68b020c49ba",
                        "field_boolean": "False",
                        "field_string_list": "['hi', 'mister']",
                        "field_datetime": "2020-03-31 11:22:10.000999",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": "149",
                        "field_integer_list": "[987, 2345]",
                        "field_real": "8789.0",
                        "field_real_list": "[2.0, 5.0]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_date": "",
                        "field_time": "11:22:10.000999",
                        "field_binary": "000000000140eff36b0a3d70a440bde68b020c49ba",
                        "field_boolean": "True",
                        "field_string_list": "['hi', 'mister']",
                        "field_datetime": "2020-03-31 11:22:10.000999",
                    }
                },
            },
        },
    },
    1: {
        "geolayer": copy.deepcopy(geolayer_attributes_to_force_in_str),
        "i_feat_to_delete": [0, 1, 2],
        "return_value": {
            "metadata": {"name": "attributes_to_force_only_forced"},
            "features": {},
        },
    },
    2: {
        "geolayer": copy.deepcopy(feature_list_data_and_geometry_geolayer),
        "i_feat_to_delete": [0, 1, 2, 3],
        "return_value": {
            "metadata": {"name": "data_and_geometries"},
            "features": {},
        },
    },
}

drop_field_parameters = {
    0: {
        "geolayer": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
        "field_name_to_drop": "field_integer",
        "return_value": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer_list": {"type": "String", "width": 13, "index": 0},
                    "field_real": {"type": "String", "width": 7, "index": 1},
                    "field_real_list": {"type": "String", "width": 19, "index": 2},
                    "field_string": {"type": "String", "width": 26, "index": 3},
                    "field_date": {"type": "Date", "index": 4},
                    "field_time": {"type": "String", "width": 15, "index": 5},
                    "field_binary": {"type": "String", "width": 201, "index": 6},
                    "field_boolean": {"type": "String", "width": 5, "index": 7},
                    "field_string_list": {"type": "String", "width": 16, "index": 8},
                    "field_datetime": {"type": "DateTime", "index": 9},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
    },
    1: {
        "geolayer": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
        "field_name_to_drop": "field_datetime",
        "return_value": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
    },
    2: {
        "geolayer": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
        "field_name_to_drop": "field_string",
        "return_value": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_date": {"type": "Date", "index": 4},
                    "field_time": {"type": "String", "width": 15, "index": 5},
                    "field_binary": {"type": "String", "width": 201, "index": 6},
                    "field_boolean": {"type": "String", "width": 5, "index": 7},
                    "field_string_list": {"type": "String", "width": 16, "index": 8},
                    "field_datetime": {"type": "DateTime", "index": 9},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
    },
    3: {
        "geolayer": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
        "field_name_to_drop": ["field_string", "field_integer", "field_datetime"],
        "return_value": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer_list": {"type": "String", "width": 13, "index": 0},
                    "field_real": {"type": "String", "width": 7, "index": 1},
                    "field_real_list": {"type": "String", "width": 19, "index": 2},
                    "field_date": {"type": "Date", "index": 3},
                    "field_time": {"type": "String", "width": 15, "index": 4},
                    "field_binary": {"type": "String", "width": 201, "index": 5},
                    "field_boolean": {"type": "String", "width": 5, "index": 6},
                    "field_string_list": {"type": "String", "width": 16, "index": 7},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
    },
    4: {
        "geolayer": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
        "field_name_to_drop": [
            "field_string_list",
            "field_binary",
            "field_time",
            "field_boolean",
            "field_integer_list",
            "field_datetime",
            "field_real",
            "field_string",
            "field_integer",
            "field_real_list",
            "field_date",
        ],
        "return_value": {"metadata": {"name": "new_geolayer"}, "features": {}},
    },
}

rename_field_parameters = {
    0: {
        "geolayer": geolayer_attributes_only,
        "old_field_name": "field_integer",
        "new_field_name": "field_integer_rename",
        "return_value": geolayer_attributes_only_rename,
    },
    1: {
        "geolayer": geolayer_attributes_only,
        "old_field_name": "foo",
        "new_field_name": "field_integer_rename",
        "return_value": field_missing.format(field_name="foo"),
    },
    2: {
        "geolayer": geolayer_attributes_only,
        "old_field_name": "field_string_list",
        "new_field_name": "field_string",
        "return_value": field_exists.format(field_name="field_string"),
    },
}

create_field_parameters = {
    0: {
        "geolayer": copy.deepcopy(geolayer_attributes_only),
        "field_name": "foo",
        "field_type": "Date",
        "field_width": None,
        "field_precision": None,
        "field_index": None,
        "return_value": {
            "metadata": {
                "name": "attributes_only",
                "fields": {
                    "field_integer": {"type": "Integer", "index": 0},
                    "field_integer_list": {"type": "IntegerList", "index": 1},
                    "field_real": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 2,
                    },
                    "field_real_list": {
                        "type": "RealList",
                        "width": 10,
                        "precision": 5,
                        "index": 3,
                    },
                    "field_string": {"type": "String", "width": 5, "index": 4},
                    "field_string_list": {"type": "StringList", "width": 8, "index": 5},
                    "field_date": {"type": "Date", "index": 6},
                    "field_time": {"type": "Time", "index": 7},
                    "field_datetime": {"type": "DateTime", "index": 8},
                    "field_binary": {"type": "Binary", "index": 9},
                    "field_boolean": {"type": "Boolean", "index": 10},
                    "foo": {"type": "Date", "index": 11},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586,
                        "field_integer_list": [5879, 8557],
                        "field_real": 8789.97568,
                        "field_real_list": [89798.3654, 8757.97568],
                        "field_string": "salut",
                        "field_string_list": ["bonjour", "monsieur"],
                        "field_none": None,
                        "field_date": datetime.date(2020, 3, 31),
                        "field_time": datetime.time(11, 22, 10, 999),
                        "field_datetime": datetime.datetime(
                            2020, 3, 31, 11, 22, 10, 999
                        ),
                        "field_binary": b"\x00\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01?\xf0\x00\x00\x00\x00\x00\x00?\xf0\x00\x00\x00\x00\x00\x00",
                        "field_boolean": True,
                    }
                }
            },
        },
    },
    1: {
        "geolayer": copy.deepcopy(geolayer_attributes_only),
        "field_name": "foo",
        "field_type": "Binary",
        "field_width": None,
        "field_precision": None,
        "field_index": 0,
        "return_value": {
            "metadata": {
                "name": "attributes_only",
                "fields": {
                    "field_integer": {"type": "Integer", "index": 1},
                    "field_integer_list": {"type": "IntegerList", "index": 2},
                    "field_real": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 3,
                    },
                    "field_real_list": {
                        "type": "RealList",
                        "width": 10,
                        "precision": 5,
                        "index": 4,
                    },
                    "field_string": {"type": "String", "width": 5, "index": 5},
                    "field_string_list": {"type": "StringList", "width": 8, "index": 6},
                    "field_date": {"type": "Date", "index": 7},
                    "field_time": {"type": "Time", "index": 8},
                    "field_datetime": {"type": "DateTime", "index": 9},
                    "field_binary": {"type": "Binary", "index": 10},
                    "field_boolean": {"type": "Boolean", "index": 11},
                    "foo": {"type": "Binary", "index": 0},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586,
                        "field_integer_list": [5879, 8557],
                        "field_real": 8789.97568,
                        "field_real_list": [89798.3654, 8757.97568],
                        "field_string": "salut",
                        "field_string_list": ["bonjour", "monsieur"],
                        "field_none": None,
                        "field_date": datetime.date(2020, 3, 31),
                        "field_time": datetime.time(11, 22, 10, 999),
                        "field_datetime": datetime.datetime(
                            2020, 3, 31, 11, 22, 10, 999
                        ),
                        "field_binary": b"\x00\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01?\xf0\x00\x00\x00\x00\x00\x00?\xf0\x00\x00\x00\x00\x00\x00",
                        "field_boolean": True,
                    }
                }
            },
        },
    },
}

add_attributes_index_parameters = {
    0: {
        "geolayer": copy.deepcopy(geolayer_fr_dept_population),
        "field_name": "CODE_DEPT",
        "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
        "return_value": {
            "metadata": {
                "name": "dept_population",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "INSEE_REG": {"type": "String", "width": 2, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "AREA": {"type": "Real", "width": 7, "precision": 2, "index": 3},
                    "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 4},
                },
                "index": {
                    "attributes": {
                        "CODE_DEPT": {
                            "type": "hashtable",
                            "index": {
                                "32": [0],
                                "47": [1],
                                "38": [2],
                                "62": [3],
                                "08": [4],
                                "10": [5],
                                "42": [6],
                                "06": [7],
                                "31": [8],
                                "71": [9],
                                "53": [10],
                                "78": [11],
                                "50": [12],
                                "16": [13],
                                "25": [14],
                                "55": [15],
                                "33": [16],
                                "14": [17],
                                "88": [18],
                                "18": [19],
                                "07": [20],
                                "02": [21],
                                "64": [22],
                                "41": [23],
                                "57": [24],
                                "86": [25],
                                "24": [26],
                                "39": [27],
                                "82": [28],
                                "49": [29],
                                "69": [30],
                                "12": [31],
                                "23": [32],
                                "45": [33],
                                "70": [34],
                                "63": [35],
                                "81": [36],
                                "27": [37],
                                "76": [38],
                                "52": [39],
                                "30": [40],
                                "67": [41],
                                "11": [42],
                                "77": [43],
                                "43": [44],
                                "51": [45],
                                "80": [46],
                                "46": [47],
                                "65": [48],
                                "04": [49],
                                "72": [50],
                                "56": [51],
                                "2A": [52],
                                "28": [53],
                                "54": [54],
                                "01": [55],
                                "19": [56],
                                "09": [57],
                                "68": [58],
                                "59": [59],
                                "90": [60],
                                "44": [61],
                                "89": [62],
                                "35": [63],
                                "40": [64],
                                "29": [65],
                                "74": [66],
                                "60": [67],
                                "95": [68],
                                "58": [69],
                                "61": [70],
                                "91": [71],
                                "21": [72],
                                "22": [73],
                                "03": [74],
                                "17": [75],
                                "15": [76],
                                "34": [77],
                                "26": [78],
                                "66": [79],
                                "73": [80],
                                "37": [81],
                                "05": [82],
                                "79": [83],
                                "84": [84],
                                "36": [85],
                                "2B": [86],
                                "87": [87],
                                "85": [88],
                                "83": [89],
                                "94": [90],
                                "92": [91],
                                "48": [92],
                                "13": [93],
                                "93": [94],
                                "75": [95],
                            },
                        }
                    }
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "INSEE_REG": "76",
                        "POPULATION": 191091,
                        "AREA": 6304.33,
                        "DENSITY": 30.31,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "INSEE_REG": "75",
                        "POPULATION": 332842,
                        "AREA": 5382.87,
                        "DENSITY": 61.83,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "INSEE_REG": "84",
                        "POPULATION": 1258722,
                        "AREA": 7868.79,
                        "DENSITY": 159.96,
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "INSEE_REG": "32",
                        "POPULATION": 1468018,
                        "AREA": 6714.14,
                        "DENSITY": 218.65,
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "INSEE_REG": "44",
                        "POPULATION": 273579,
                        "AREA": 5253.13,
                        "DENSITY": 52.08,
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "INSEE_REG": "44",
                        "POPULATION": 310020,
                        "AREA": 6021.83,
                        "DENSITY": 51.48,
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "INSEE_REG": "84",
                        "POPULATION": 762941,
                        "AREA": 4795.85,
                        "DENSITY": 159.08,
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "INSEE_REG": "93",
                        "POPULATION": 1083310,
                        "AREA": 4291.62,
                        "DENSITY": 252.42,
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "INSEE_REG": "76",
                        "POPULATION": 1362672,
                        "AREA": 6364.82,
                        "DENSITY": 214.09,
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "INSEE_REG": "27",
                        "POPULATION": 553595,
                        "AREA": 8598.33,
                        "DENSITY": 64.38,
                    }
                },
                10: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "INSEE_REG": "52",
                        "POPULATION": 307445,
                        "AREA": 5208.37,
                        "DENSITY": 59.03,
                    }
                },
                11: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "INSEE_REG": "11",
                        "POPULATION": 1438266,
                        "AREA": 2305.64,
                        "DENSITY": 623.8,
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "INSEE_REG": "28",
                        "POPULATION": 496883,
                        "AREA": 6015.07,
                        "DENSITY": 82.61,
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "INSEE_REG": "75",
                        "POPULATION": 352335,
                        "AREA": 5963.54,
                        "DENSITY": 59.08,
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "INSEE_REG": "27",
                        "POPULATION": 539067,
                        "AREA": 5248.31,
                        "DENSITY": 102.71,
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "INSEE_REG": "44",
                        "POPULATION": 187187,
                        "AREA": 6233.18,
                        "DENSITY": 30.03,
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "INSEE_REG": "75",
                        "POPULATION": 1583384,
                        "AREA": 10068.74,
                        "DENSITY": 157.26,
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "INSEE_REG": "28",
                        "POPULATION": 694002,
                        "AREA": 5588.48,
                        "DENSITY": 124.18,
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "INSEE_REG": "44",
                        "POPULATION": 367673,
                        "AREA": 5891.56,
                        "DENSITY": 62.41,
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "INSEE_REG": "24",
                        "POPULATION": 304256,
                        "AREA": 7292.67,
                        "DENSITY": 41.72,
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "INSEE_REG": "84",
                        "POPULATION": 325712,
                        "AREA": 5562.05,
                        "DENSITY": 58.56,
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "INSEE_REG": "32",
                        "POPULATION": 534490,
                        "AREA": 7418.97,
                        "DENSITY": 72.04,
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "INSEE_REG": "75",
                        "POPULATION": 677309,
                        "AREA": 7691.6,
                        "DENSITY": 88.06,
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "INSEE_REG": "24",
                        "POPULATION": 331915,
                        "AREA": 6412.3,
                        "DENSITY": 51.76,
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "INSEE_REG": "44",
                        "POPULATION": 1043522,
                        "AREA": 6252.63,
                        "DENSITY": 166.89,
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "INSEE_REG": "75",
                        "POPULATION": 436876,
                        "AREA": 7025.24,
                        "DENSITY": 62.19,
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "INSEE_REG": "75",
                        "POPULATION": 413606,
                        "AREA": 9209.9,
                        "DENSITY": 44.91,
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "INSEE_REG": "27",
                        "POPULATION": 260188,
                        "AREA": 5040.63,
                        "DENSITY": 51.62,
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "INSEE_REG": "76",
                        "POPULATION": 258349,
                        "AREA": 3731.0,
                        "DENSITY": 69.24,
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "INSEE_REG": "52",
                        "POPULATION": 813493,
                        "AREA": 7161.34,
                        "DENSITY": 113.6,
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "INSEE_REG": "84",
                        "POPULATION": 1843319,
                        "AREA": 3253.11,
                        "DENSITY": 566.63,
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "INSEE_REG": "76",
                        "POPULATION": 279206,
                        "AREA": 8770.69,
                        "DENSITY": 31.83,
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "INSEE_REG": "75",
                        "POPULATION": 118638,
                        "AREA": 5589.16,
                        "DENSITY": 21.23,
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "INSEE_REG": "24",
                        "POPULATION": 678008,
                        "AREA": 6804.01,
                        "DENSITY": 99.65,
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "INSEE_REG": "27",
                        "POPULATION": 236659,
                        "AREA": 5382.37,
                        "DENSITY": 43.97,
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "INSEE_REG": "84",
                        "POPULATION": 653742,
                        "AREA": 8003.1,
                        "DENSITY": 81.69,
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "INSEE_REG": "76",
                        "POPULATION": 387890,
                        "AREA": 5785.79,
                        "DENSITY": 67.04,
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "INSEE_REG": "28",
                        "POPULATION": 601843,
                        "AREA": 6035.85,
                        "DENSITY": 99.71,
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "INSEE_REG": "28",
                        "POPULATION": 1254378,
                        "AREA": 6318.26,
                        "DENSITY": 198.53,
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "INSEE_REG": "44",
                        "POPULATION": 175640,
                        "AREA": 6249.91,
                        "DENSITY": 28.1,
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "INSEE_REG": "76",
                        "POPULATION": 744178,
                        "AREA": 5874.71,
                        "DENSITY": 126.67,
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "INSEE_REG": "44",
                        "POPULATION": 1125559,
                        "AREA": 4796.37,
                        "DENSITY": 234.67,
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "INSEE_REG": "76",
                        "POPULATION": 370260,
                        "AREA": 6351.35,
                        "DENSITY": 58.3,
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "INSEE_REG": "11",
                        "POPULATION": 1403997,
                        "AREA": 5924.64,
                        "DENSITY": 236.98,
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "INSEE_REG": "84",
                        "POPULATION": 227283,
                        "AREA": 4996.58,
                        "DENSITY": 45.49,
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "INSEE_REG": "44",
                        "POPULATION": 568895,
                        "AREA": 8195.78,
                        "DENSITY": 69.41,
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "INSEE_REG": "32",
                        "POPULATION": 572443,
                        "AREA": 6206.58,
                        "DENSITY": 92.23,
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "INSEE_REG": "76",
                        "POPULATION": 173828,
                        "AREA": 5221.64,
                        "DENSITY": 33.29,
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "INSEE_REG": "76",
                        "POPULATION": 228530,
                        "AREA": 4527.89,
                        "DENSITY": 50.47,
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "INSEE_REG": "93",
                        "POPULATION": 163915,
                        "AREA": 6993.79,
                        "DENSITY": 23.44,
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "INSEE_REG": "52",
                        "POPULATION": 566506,
                        "AREA": 6236.75,
                        "DENSITY": 90.83,
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "INSEE_REG": "53",
                        "POPULATION": 750863,
                        "AREA": 6864.07,
                        "DENSITY": 109.39,
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "INSEE_REG": "94",
                        "POPULATION": 157249,
                        "AREA": 4028.53,
                        "DENSITY": 39.03,
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "INSEE_REG": "24",
                        "POPULATION": 433233,
                        "AREA": 5927.23,
                        "DENSITY": 73.09,
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "INSEE_REG": "44",
                        "POPULATION": 733481,
                        "AREA": 5283.29,
                        "DENSITY": 138.83,
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "INSEE_REG": "84",
                        "POPULATION": 643350,
                        "AREA": 5773.77,
                        "DENSITY": 111.43,
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "INSEE_REG": "75",
                        "POPULATION": 241464,
                        "AREA": 5888.93,
                        "DENSITY": 41.0,
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "INSEE_REG": "76",
                        "POPULATION": 153153,
                        "AREA": 4921.75,
                        "DENSITY": 31.12,
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "INSEE_REG": "44",
                        "POPULATION": 764030,
                        "AREA": 3526.37,
                        "DENSITY": 216.66,
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "INSEE_REG": "32",
                        "POPULATION": 2604361,
                        "AREA": 5774.99,
                        "DENSITY": 450.97,
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "INSEE_REG": "27",
                        "POPULATION": 142622,
                        "AREA": 609.64,
                        "DENSITY": 233.94,
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "INSEE_REG": "52",
                        "POPULATION": 1394909,
                        "AREA": 6992.78,
                        "DENSITY": 199.48,
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "INSEE_REG": "27",
                        "POPULATION": 338291,
                        "AREA": 7450.97,
                        "DENSITY": 45.4,
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "INSEE_REG": "53",
                        "POPULATION": 1060199,
                        "AREA": 6830.2,
                        "DENSITY": 155.22,
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "INSEE_REG": "75",
                        "POPULATION": 407444,
                        "AREA": 9353.03,
                        "DENSITY": 43.56,
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "INSEE_REG": "53",
                        "POPULATION": 909028,
                        "AREA": 6756.76,
                        "DENSITY": 134.54,
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "INSEE_REG": "84",
                        "POPULATION": 807360,
                        "AREA": 4596.53,
                        "DENSITY": 175.65,
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "INSEE_REG": "32",
                        "POPULATION": 824503,
                        "AREA": 5893.6,
                        "DENSITY": 139.9,
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "INSEE_REG": "11",
                        "POPULATION": 1228618,
                        "AREA": 1254.18,
                        "DENSITY": 979.62,
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "INSEE_REG": "27",
                        "POPULATION": 207182,
                        "AREA": 6862.87,
                        "DENSITY": 30.19,
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "INSEE_REG": "28",
                        "POPULATION": 283372,
                        "AREA": 6142.73,
                        "DENSITY": 46.13,
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "INSEE_REG": "11",
                        "POPULATION": 1296130,
                        "AREA": 1818.35,
                        "DENSITY": 712.81,
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "INSEE_REG": "27",
                        "POPULATION": 532871,
                        "AREA": 8787.51,
                        "DENSITY": 60.64,
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "INSEE_REG": "53",
                        "POPULATION": 598814,
                        "AREA": 6963.26,
                        "DENSITY": 86.0,
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "INSEE_REG": "84",
                        "POPULATION": 337988,
                        "AREA": 7365.26,
                        "DENSITY": 45.89,
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "INSEE_REG": "75",
                        "POPULATION": 644303,
                        "AREA": 6913.03,
                        "DENSITY": 93.2,
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "INSEE_REG": "84",
                        "POPULATION": 145143,
                        "AREA": 5767.47,
                        "DENSITY": 25.17,
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "INSEE_REG": "76",
                        "POPULATION": 1144892,
                        "AREA": 6231.05,
                        "DENSITY": 183.74,
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "INSEE_REG": "84",
                        "POPULATION": 511553,
                        "AREA": 6553.53,
                        "DENSITY": 78.06,
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "INSEE_REG": "76",
                        "POPULATION": 474452,
                        "AREA": 4147.76,
                        "DENSITY": 114.39,
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "INSEE_REG": "84",
                        "POPULATION": 431174,
                        "AREA": 6260.4,
                        "DENSITY": 68.87,
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "INSEE_REG": "24",
                        "POPULATION": 606511,
                        "AREA": 6147.6,
                        "DENSITY": 98.66,
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "INSEE_REG": "93",
                        "POPULATION": 141284,
                        "AREA": 5685.31,
                        "DENSITY": 24.85,
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "INSEE_REG": "75",
                        "POPULATION": 374351,
                        "AREA": 6029.06,
                        "DENSITY": 62.09,
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "INSEE_REG": "93",
                        "POPULATION": 559479,
                        "AREA": 3577.19,
                        "DENSITY": 156.4,
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "INSEE_REG": "24",
                        "POPULATION": 222232,
                        "AREA": 6887.38,
                        "DENSITY": 32.27,
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "INSEE_REG": "94",
                        "POPULATION": 177689,
                        "AREA": 4719.71,
                        "DENSITY": 37.65,
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "INSEE_REG": "75",
                        "POPULATION": 374426,
                        "AREA": 5549.31,
                        "DENSITY": 67.47,
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "INSEE_REG": "52",
                        "POPULATION": 675247,
                        "AREA": 6758.23,
                        "DENSITY": 99.91,
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "INSEE_REG": "93",
                        "POPULATION": 1058740,
                        "AREA": 6002.84,
                        "DENSITY": 176.37,
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "INSEE_REG": "11",
                        "POPULATION": 1387926,
                        "AREA": 244.7,
                        "DENSITY": 5671.95,
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "INSEE_REG": "11",
                        "POPULATION": 1609306,
                        "AREA": 175.63,
                        "DENSITY": 9163.05,
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "INSEE_REG": "76",
                        "POPULATION": 76601,
                        "AREA": 5172.02,
                        "DENSITY": 14.81,
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "INSEE_REG": "93",
                        "POPULATION": 2024162,
                        "AREA": 5082.57,
                        "DENSITY": 398.26,
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "INSEE_REG": "11",
                        "POPULATION": 1623111,
                        "AREA": 236.96,
                        "DENSITY": 6849.73,
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "INSEE_REG": "11",
                        "POPULATION": 2187526,
                        "AREA": 105.44,
                        "DENSITY": 20746.64,
                    }
                },
            },
        },
    },
    1: {
        "geolayer": {
            "metadata": {
                "name": "dept_population",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "INSEE_REG": {"type": "String", "width": 2, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "AREA": {"type": "Real", "width": 7, "precision": 2, "index": 3},
                    "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 4},
                },
                "index": {
                    "attributes": {
                        "CODE_DEPT": {
                            "type": "hashtable",
                            "index": {
                                "32": [0],
                                "47": [1],
                                "38": [2],
                                "62": [3],
                                "08": [4],
                                "10": [5],
                                "42": [6],
                                "06": [7],
                                "31": [8],
                                "71": [9],
                                "53": [10],
                                "78": [11],
                                "50": [12],
                                "16": [13],
                                "25": [14],
                                "55": [15],
                                "33": [16],
                                "14": [17],
                                "88": [18],
                                "18": [19],
                                "07": [20],
                                "02": [21],
                                "64": [22],
                                "41": [23],
                                "57": [24],
                                "86": [25],
                                "24": [26],
                                "39": [27],
                                "82": [28],
                                "49": [29],
                                "69": [30],
                                "12": [31],
                                "23": [32],
                                "45": [33],
                                "70": [34],
                                "63": [35],
                                "81": [36],
                                "27": [37],
                                "76": [38],
                                "52": [39],
                                "30": [40],
                                "67": [41],
                                "11": [42],
                                "77": [43],
                                "43": [44],
                                "51": [45],
                                "80": [46],
                                "46": [47],
                                "65": [48],
                                "04": [49],
                                "72": [50],
                                "56": [51],
                                "2A": [52],
                                "28": [53],
                                "54": [54],
                                "01": [55],
                                "19": [56],
                                "09": [57],
                                "68": [58],
                                "59": [59],
                                "90": [60],
                                "44": [61],
                                "89": [62],
                                "35": [63],
                                "40": [64],
                                "29": [65],
                                "74": [66],
                                "60": [67],
                                "95": [68],
                                "58": [69],
                                "61": [70],
                                "91": [71],
                                "21": [72],
                                "22": [73],
                                "03": [74],
                                "17": [75],
                                "15": [76],
                                "34": [77],
                                "26": [78],
                                "66": [79],
                                "73": [80],
                                "37": [81],
                                "05": [82],
                                "79": [83],
                                "84": [84],
                                "36": [85],
                                "2B": [86],
                                "87": [87],
                                "85": [88],
                                "83": [89],
                                "94": [90],
                                "92": [91],
                                "48": [92],
                                "13": [93],
                                "93": [94],
                                "75": [95],
                            },
                        }
                    }
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "INSEE_REG": "76",
                        "POPULATION": 191091,
                        "AREA": 6304.33,
                        "DENSITY": 30.31,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "INSEE_REG": "75",
                        "POPULATION": 332842,
                        "AREA": 5382.87,
                        "DENSITY": 61.83,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "INSEE_REG": "84",
                        "POPULATION": 1258722,
                        "AREA": 7868.79,
                        "DENSITY": 159.96,
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "INSEE_REG": "32",
                        "POPULATION": 1468018,
                        "AREA": 6714.14,
                        "DENSITY": 218.65,
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "INSEE_REG": "44",
                        "POPULATION": 273579,
                        "AREA": 5253.13,
                        "DENSITY": 52.08,
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "INSEE_REG": "44",
                        "POPULATION": 310020,
                        "AREA": 6021.83,
                        "DENSITY": 51.48,
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "INSEE_REG": "84",
                        "POPULATION": 762941,
                        "AREA": 4795.85,
                        "DENSITY": 159.08,
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "INSEE_REG": "93",
                        "POPULATION": 1083310,
                        "AREA": 4291.62,
                        "DENSITY": 252.42,
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "INSEE_REG": "76",
                        "POPULATION": 1362672,
                        "AREA": 6364.82,
                        "DENSITY": 214.09,
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "INSEE_REG": "27",
                        "POPULATION": 553595,
                        "AREA": 8598.33,
                        "DENSITY": 64.38,
                    }
                },
                10: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "INSEE_REG": "52",
                        "POPULATION": 307445,
                        "AREA": 5208.37,
                        "DENSITY": 59.03,
                    }
                },
                11: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "INSEE_REG": "11",
                        "POPULATION": 1438266,
                        "AREA": 2305.64,
                        "DENSITY": 623.8,
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "INSEE_REG": "28",
                        "POPULATION": 496883,
                        "AREA": 6015.07,
                        "DENSITY": 82.61,
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "INSEE_REG": "75",
                        "POPULATION": 352335,
                        "AREA": 5963.54,
                        "DENSITY": 59.08,
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "INSEE_REG": "27",
                        "POPULATION": 539067,
                        "AREA": 5248.31,
                        "DENSITY": 102.71,
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "INSEE_REG": "44",
                        "POPULATION": 187187,
                        "AREA": 6233.18,
                        "DENSITY": 30.03,
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "INSEE_REG": "75",
                        "POPULATION": 1583384,
                        "AREA": 10068.74,
                        "DENSITY": 157.26,
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "INSEE_REG": "28",
                        "POPULATION": 694002,
                        "AREA": 5588.48,
                        "DENSITY": 124.18,
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "INSEE_REG": "44",
                        "POPULATION": 367673,
                        "AREA": 5891.56,
                        "DENSITY": 62.41,
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "INSEE_REG": "24",
                        "POPULATION": 304256,
                        "AREA": 7292.67,
                        "DENSITY": 41.72,
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "INSEE_REG": "84",
                        "POPULATION": 325712,
                        "AREA": 5562.05,
                        "DENSITY": 58.56,
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "INSEE_REG": "32",
                        "POPULATION": 534490,
                        "AREA": 7418.97,
                        "DENSITY": 72.04,
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "INSEE_REG": "75",
                        "POPULATION": 677309,
                        "AREA": 7691.6,
                        "DENSITY": 88.06,
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "INSEE_REG": "24",
                        "POPULATION": 331915,
                        "AREA": 6412.3,
                        "DENSITY": 51.76,
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "INSEE_REG": "44",
                        "POPULATION": 1043522,
                        "AREA": 6252.63,
                        "DENSITY": 166.89,
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "INSEE_REG": "75",
                        "POPULATION": 436876,
                        "AREA": 7025.24,
                        "DENSITY": 62.19,
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "INSEE_REG": "75",
                        "POPULATION": 413606,
                        "AREA": 9209.9,
                        "DENSITY": 44.91,
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "INSEE_REG": "27",
                        "POPULATION": 260188,
                        "AREA": 5040.63,
                        "DENSITY": 51.62,
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "INSEE_REG": "76",
                        "POPULATION": 258349,
                        "AREA": 3731.0,
                        "DENSITY": 69.24,
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "INSEE_REG": "52",
                        "POPULATION": 813493,
                        "AREA": 7161.34,
                        "DENSITY": 113.6,
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "INSEE_REG": "84",
                        "POPULATION": 1843319,
                        "AREA": 3253.11,
                        "DENSITY": 566.63,
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "INSEE_REG": "76",
                        "POPULATION": 279206,
                        "AREA": 8770.69,
                        "DENSITY": 31.83,
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "INSEE_REG": "75",
                        "POPULATION": 118638,
                        "AREA": 5589.16,
                        "DENSITY": 21.23,
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "INSEE_REG": "24",
                        "POPULATION": 678008,
                        "AREA": 6804.01,
                        "DENSITY": 99.65,
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "INSEE_REG": "27",
                        "POPULATION": 236659,
                        "AREA": 5382.37,
                        "DENSITY": 43.97,
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "INSEE_REG": "84",
                        "POPULATION": 653742,
                        "AREA": 8003.1,
                        "DENSITY": 81.69,
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "INSEE_REG": "76",
                        "POPULATION": 387890,
                        "AREA": 5785.79,
                        "DENSITY": 67.04,
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "INSEE_REG": "28",
                        "POPULATION": 601843,
                        "AREA": 6035.85,
                        "DENSITY": 99.71,
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "INSEE_REG": "28",
                        "POPULATION": 1254378,
                        "AREA": 6318.26,
                        "DENSITY": 198.53,
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "INSEE_REG": "44",
                        "POPULATION": 175640,
                        "AREA": 6249.91,
                        "DENSITY": 28.1,
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "INSEE_REG": "76",
                        "POPULATION": 744178,
                        "AREA": 5874.71,
                        "DENSITY": 126.67,
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "INSEE_REG": "44",
                        "POPULATION": 1125559,
                        "AREA": 4796.37,
                        "DENSITY": 234.67,
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "INSEE_REG": "76",
                        "POPULATION": 370260,
                        "AREA": 6351.35,
                        "DENSITY": 58.3,
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "INSEE_REG": "11",
                        "POPULATION": 1403997,
                        "AREA": 5924.64,
                        "DENSITY": 236.98,
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "INSEE_REG": "84",
                        "POPULATION": 227283,
                        "AREA": 4996.58,
                        "DENSITY": 45.49,
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "INSEE_REG": "44",
                        "POPULATION": 568895,
                        "AREA": 8195.78,
                        "DENSITY": 69.41,
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "INSEE_REG": "32",
                        "POPULATION": 572443,
                        "AREA": 6206.58,
                        "DENSITY": 92.23,
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "INSEE_REG": "76",
                        "POPULATION": 173828,
                        "AREA": 5221.64,
                        "DENSITY": 33.29,
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "INSEE_REG": "76",
                        "POPULATION": 228530,
                        "AREA": 4527.89,
                        "DENSITY": 50.47,
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "INSEE_REG": "93",
                        "POPULATION": 163915,
                        "AREA": 6993.79,
                        "DENSITY": 23.44,
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "INSEE_REG": "52",
                        "POPULATION": 566506,
                        "AREA": 6236.75,
                        "DENSITY": 90.83,
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "INSEE_REG": "53",
                        "POPULATION": 750863,
                        "AREA": 6864.07,
                        "DENSITY": 109.39,
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "INSEE_REG": "94",
                        "POPULATION": 157249,
                        "AREA": 4028.53,
                        "DENSITY": 39.03,
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "INSEE_REG": "24",
                        "POPULATION": 433233,
                        "AREA": 5927.23,
                        "DENSITY": 73.09,
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "INSEE_REG": "44",
                        "POPULATION": 733481,
                        "AREA": 5283.29,
                        "DENSITY": 138.83,
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "INSEE_REG": "84",
                        "POPULATION": 643350,
                        "AREA": 5773.77,
                        "DENSITY": 111.43,
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "INSEE_REG": "75",
                        "POPULATION": 241464,
                        "AREA": 5888.93,
                        "DENSITY": 41.0,
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "INSEE_REG": "76",
                        "POPULATION": 153153,
                        "AREA": 4921.75,
                        "DENSITY": 31.12,
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "INSEE_REG": "44",
                        "POPULATION": 764030,
                        "AREA": 3526.37,
                        "DENSITY": 216.66,
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "INSEE_REG": "32",
                        "POPULATION": 2604361,
                        "AREA": 5774.99,
                        "DENSITY": 450.97,
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "INSEE_REG": "27",
                        "POPULATION": 142622,
                        "AREA": 609.64,
                        "DENSITY": 233.94,
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "INSEE_REG": "52",
                        "POPULATION": 1394909,
                        "AREA": 6992.78,
                        "DENSITY": 199.48,
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "INSEE_REG": "27",
                        "POPULATION": 338291,
                        "AREA": 7450.97,
                        "DENSITY": 45.4,
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "INSEE_REG": "53",
                        "POPULATION": 1060199,
                        "AREA": 6830.2,
                        "DENSITY": 155.22,
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "INSEE_REG": "75",
                        "POPULATION": 407444,
                        "AREA": 9353.03,
                        "DENSITY": 43.56,
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "INSEE_REG": "53",
                        "POPULATION": 909028,
                        "AREA": 6756.76,
                        "DENSITY": 134.54,
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "INSEE_REG": "84",
                        "POPULATION": 807360,
                        "AREA": 4596.53,
                        "DENSITY": 175.65,
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "INSEE_REG": "32",
                        "POPULATION": 824503,
                        "AREA": 5893.6,
                        "DENSITY": 139.9,
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "INSEE_REG": "11",
                        "POPULATION": 1228618,
                        "AREA": 1254.18,
                        "DENSITY": 979.62,
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "INSEE_REG": "27",
                        "POPULATION": 207182,
                        "AREA": 6862.87,
                        "DENSITY": 30.19,
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "INSEE_REG": "28",
                        "POPULATION": 283372,
                        "AREA": 6142.73,
                        "DENSITY": 46.13,
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "INSEE_REG": "11",
                        "POPULATION": 1296130,
                        "AREA": 1818.35,
                        "DENSITY": 712.81,
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "INSEE_REG": "27",
                        "POPULATION": 532871,
                        "AREA": 8787.51,
                        "DENSITY": 60.64,
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "INSEE_REG": "53",
                        "POPULATION": 598814,
                        "AREA": 6963.26,
                        "DENSITY": 86.0,
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "INSEE_REG": "84",
                        "POPULATION": 337988,
                        "AREA": 7365.26,
                        "DENSITY": 45.89,
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "INSEE_REG": "75",
                        "POPULATION": 644303,
                        "AREA": 6913.03,
                        "DENSITY": 93.2,
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "INSEE_REG": "84",
                        "POPULATION": 145143,
                        "AREA": 5767.47,
                        "DENSITY": 25.17,
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "INSEE_REG": "76",
                        "POPULATION": 1144892,
                        "AREA": 6231.05,
                        "DENSITY": 183.74,
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "INSEE_REG": "84",
                        "POPULATION": 511553,
                        "AREA": 6553.53,
                        "DENSITY": 78.06,
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "INSEE_REG": "76",
                        "POPULATION": 474452,
                        "AREA": 4147.76,
                        "DENSITY": 114.39,
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "INSEE_REG": "84",
                        "POPULATION": 431174,
                        "AREA": 6260.4,
                        "DENSITY": 68.87,
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "INSEE_REG": "24",
                        "POPULATION": 606511,
                        "AREA": 6147.6,
                        "DENSITY": 98.66,
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "INSEE_REG": "93",
                        "POPULATION": 141284,
                        "AREA": 5685.31,
                        "DENSITY": 24.85,
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "INSEE_REG": "75",
                        "POPULATION": 374351,
                        "AREA": 6029.06,
                        "DENSITY": 62.09,
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "INSEE_REG": "93",
                        "POPULATION": 559479,
                        "AREA": 3577.19,
                        "DENSITY": 156.4,
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "INSEE_REG": "24",
                        "POPULATION": 222232,
                        "AREA": 6887.38,
                        "DENSITY": 32.27,
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "INSEE_REG": "94",
                        "POPULATION": 177689,
                        "AREA": 4719.71,
                        "DENSITY": 37.65,
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "INSEE_REG": "75",
                        "POPULATION": 374426,
                        "AREA": 5549.31,
                        "DENSITY": 67.47,
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "INSEE_REG": "52",
                        "POPULATION": 675247,
                        "AREA": 6758.23,
                        "DENSITY": 99.91,
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "INSEE_REG": "93",
                        "POPULATION": 1058740,
                        "AREA": 6002.84,
                        "DENSITY": 176.37,
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "INSEE_REG": "11",
                        "POPULATION": 1387926,
                        "AREA": 244.7,
                        "DENSITY": 5671.95,
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "INSEE_REG": "11",
                        "POPULATION": 1609306,
                        "AREA": 175.63,
                        "DENSITY": 9163.05,
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "INSEE_REG": "76",
                        "POPULATION": 76601,
                        "AREA": 5172.02,
                        "DENSITY": 14.81,
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "INSEE_REG": "93",
                        "POPULATION": 2024162,
                        "AREA": 5082.57,
                        "DENSITY": 398.26,
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "INSEE_REG": "11",
                        "POPULATION": 1623111,
                        "AREA": 236.96,
                        "DENSITY": 6849.73,
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "INSEE_REG": "11",
                        "POPULATION": 2187526,
                        "AREA": 105.44,
                        "DENSITY": 20746.64,
                    }
                },
            },
        },
        "field_name": "CODE_DEPT",
        "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
        "return_value": field_name_still_indexing.format(field_name="CODE_DEPT"),
    },
    2: {
        "geolayer": geolayer_fr_dept_population,
        "field_name": "CODE",
        "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
        "return_value": field_missing.format(field_name="CODE"),
    },
    3: {
        "geolayer": geolayer_geometry_only_all_geometries_type,
        "field_name": "CODE_DEPT",
        "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
        "return_value": field_missing.format(field_name="CODE_DEPT"),
    },
}

check_attributes_index_parameters = {
    0: {
        "geolayer": geolayer_fr_dept_population,
        "field_name": "CODE_DEPT",
        "type": "hashtable",
        "return_value": False,
    },
    1: {
        "geolayer": add_attributes_index(
            **{
                "geolayer": copy.deepcopy(geolayer_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "CODE_DEPT",
        "type": "hashtable",
        "return_value": True,
    },
    2: {
        "geolayer": add_attributes_index(
            **{
                "geolayer": copy.deepcopy(geolayer_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "CODE_DEPT",
        "type": "btree",
        "return_value": False,
    },
    3: {
        "geolayer": add_attributes_index(
            **{
                "geolayer": copy.deepcopy(geolayer_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "FOO",
        "type": "hashtable",
        "return_value": field_missing.format(field_name="FOO"),
    },
    4: {
        "geolayer": geolayer_geometry_only_all_geometries_type,
        "field_name": "FOO",
        "type": "hashtable",
        "return_value": field_missing.format(field_name="FOO"),
    },
}

delete_attributes_index_parameters = {
    0: {
        "geolayer": geolayer_fr_dept_population,
        "field_name": "CODE_DEPT",
        "type": None,
        "return_value": field_name_not_indexing.format(field_name="CODE_DEPT"),
    },
    1: {
        "geolayer": add_attributes_index(
            **{
                "geolayer": copy.deepcopy(geolayer_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "CODE_DEPT",
        "type": None,
        "return_value": geolayer_fr_dept_population,
    },
    2: {
        "geolayer": add_attributes_index(
            **{
                "geolayer": copy.deepcopy(geolayer_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "CODE_DEPT",
        "type": "btree",
        "return_value": field_name_not_indexing.format(field_name="CODE_DEPT"),
    },
}

check_if_field_exists_parameters = {
    0: {
        "geolayer": geolayer_attributes_only,
        "field_name": "field_integer",
        "return_value": True,
    },
    1: {
        "geolayer": geolayer_attributes_only,
        "field_name": "foo",
        "return_value": False,
    },
    2: {
        "geolayer": geolayer_geometry_only_all_geometries_type,
        "field_name": "bar",
        "return_value": False,
    },
}

feature_list_to_geolayer_parameters = {
    0: {
        "feature_list": copy.deepcopy(feature_list_structure_alpha),
        "geolayer_name": "new_geolayer",
        "field_name_filter": None,
        "force_field_conversion": False,
        "bbox_extent": False,
        "crs": None,
        "return_value": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 4,
                        "precision": 0,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_none": {"type": "String", "width": 4, "index": 9},
                    "field_string_list": {"type": "String", "width": 16, "index": 10},
                    "field_datetime": {"type": "DateTime", "index": 11},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                        "field_none": None,
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  #  good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba".hex(),
                        "field_boolean": "False",
                        "field_none": None,
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=0,
                            minute=0,
                            second=0,
                            microsecond=0,
                        ),
                        "field_binary": "000000000140eff36b0a3d70a440bde68b020c49ba",
                        "field_boolean": "1",
                        "field_none": "NULL",
                    }
                },
            },
        },
    },
    1: {
        "feature_list": copy.deepcopy(feature_list_structure_alpha),
        "geolayer_name": "new_geolayer",
        "field_name_filter": None,
        "force_field_conversion": True,
        "bbox_extent": False,
        "crs": None,
        "none_value_pattern": {None, "NULL"},
        "return_value": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {"type": "Integer", "index": 0},
                    "field_integer_list": {"type": "IntegerList", "index": 1},
                    "field_real": {
                        "type": "Real",
                        "width": 6,
                        "precision": 2,
                        "index": 2,
                    },
                    "field_real_list": {
                        "type": "RealList",
                        "width": 9,
                        "precision": 4,
                        "index": 3,
                    },
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "Time", "index": 6},
                    "field_binary": {"type": "Binary", "index": 7},
                    "field_boolean": {"type": "Boolean", "index": 8},
                    "field_string_list": {"type": "StringList", "width": 6, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586,
                        "field_integer_list": [5879, 8557],
                        "field_real": 8789.98,
                        "field_real_list": [89798.3654, 8757.0],
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": datetime.time.fromisoformat("18:41:04"),
                        "field_binary": b"\x00\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01?\xf0\x00\x00\x00\x00\x00\x00?\xf0\x00\x00\x00\x00\x00\x00",
                        "field_boolean": True,
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466,
                        "field_integer_list": [987, 2345],
                        "field_real": 8789.0,
                        "field_real_list": [2.0, 5.0],
                        "field_string": "salut",
                        "field_string_list": ["hi", "mister"],
                        "field_time": datetime.time.fromisoformat("11:22:10.000999"),
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba",
                        "field_boolean": False,
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149,
                        "field_integer_list": [987, 2345],
                        "field_real": 8789.0,
                        "field_real_list": [2.0, 5.0],
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": ["hi", "mister"],
                        "field_time": datetime.time.fromisoformat("11:22:10.000999"),
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=0,
                            minute=0,
                            second=0,
                            microsecond=0,
                        ),
                        "field_binary": b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba",
                        "field_boolean": True,
                    }
                },
            },
        },
    },
    2: {
        "feature_list": copy.deepcopy(feature_list_attribute_only),
        "geolayer_name": "attributes_only",
        "field_name_filter": None,
        "force_field_conversion": False,
        "bbox_extent": False,
        "crs": None,
        "return_value": {
            "metadata": {
                "name": "attributes_only",
                "fields": {
                    "field_binary": {"index": 9, "type": "Binary"},
                    "field_boolean": {"index": 10, "type": "Boolean"},
                    "field_date": {"index": 6, "type": "Date"},
                    "field_datetime": {"index": 8, "type": "DateTime"},
                    "field_integer": {"index": 0, "type": "Integer"},
                    "field_integer_list": {"index": 1, "type": "IntegerList"},
                    "field_real": {
                        "index": 2,
                        "precision": 5,
                        "type": "Real",
                        "width": 9,
                    },
                    "field_real_list": {
                        "index": 3,
                        "precision": 5,
                        "type": "RealList",
                        "width": 10,
                    },
                    "field_string": {"index": 4, "type": "String", "width": 5},
                    "field_string_list": {"index": 5, "type": "StringList", "width": 8},
                    "field_time": {"index": 7, "type": "Time"},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586,
                        "field_integer_list": [5879, 8557],
                        "field_real": 8789.97568,
                        "field_real_list": [89798.3654, 8757.97568],
                        "field_string": "salut",
                        "field_string_list": ["bonjour", "monsieur"],
                        "field_date": date_value,
                        "field_time": time_value,
                        "field_datetime": date_time_value,
                        "field_binary": b"\x00\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01?\xf0\x00\x00\x00\x00\x00\x00?\xf0\x00\x00\x00\x00\x00\x00",
                        "field_boolean": True,
                    }
                }
            },
        },
    },
    3: {
        "feature_list": copy.deepcopy(feature_list_attribute_only),
        "geolayer_name": "attributes_only",
        "field_name_filter": None,
        "force_field_conversion": True,
        "bbox_extent": False,
        "crs": None,
        "return_value": {
            "metadata": {
                "name": "attributes_only",
                "fields": {
                    "field_binary": {"index": 9, "type": "Binary"},
                    "field_boolean": {"index": 10, "type": "Boolean"},
                    "field_date": {"index": 6, "type": "Date"},
                    "field_datetime": {"index": 8, "type": "DateTime"},
                    "field_integer": {"index": 0, "type": "Integer"},
                    "field_integer_list": {"index": 1, "type": "IntegerList"},
                    "field_real": {
                        "index": 2,
                        "type": "Real",
                        "precision": 5,
                        "width": 9,
                    },
                    "field_real_list": {
                        "index": 3,
                        "precision": 5,
                        "type": "RealList",
                        "width": 10,
                    },
                    "field_string": {"index": 4, "type": "String", "width": 5},
                    "field_string_list": {"index": 5, "type": "StringList", "width": 8},
                    "field_time": {"index": 7, "type": "Time"},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586,
                        "field_integer_list": [5879, 8557],
                        "field_real": 8789.97568,
                        "field_real_list": [89798.3654, 8757.97568],
                        "field_string": "salut",
                        "field_string_list": ["bonjour", "monsieur"],
                        "field_date": date_value,
                        "field_time": time_value,
                        "field_datetime": date_time_value,
                        "field_binary": b"\x00\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01?\xf0\x00\x00\x00\x00\x00\x00?\xf0\x00\x00\x00\x00\x00\x00",
                        "field_boolean": True,
                    }
                }
            },
        },
    },
    4: {
        "feature_list": copy.deepcopy(feature_list_geometry_only),
        "geolayer_name": "geometry_only",
        "field_name_filter": None,
        "force_field_conversion": False,
        "bbox_extent": False,
        "crs": None,
        "return_value": {
            "metadata": {
                "name": "geometry_only",
                "geometry_ref": {"type": {"Polygon", "MultiPolygon"}},
            },
            "features": {
                0: copy.deepcopy(feature_list_geometry_only[0]),
                1: copy.deepcopy(feature_list_geometry_only[1]),
                2: copy.deepcopy(feature_list_geometry_only[2]),
                3: copy.deepcopy(feature_list_geometry_only[3]),
            },
        },
    },
    5: {
        "feature_list": copy.deepcopy(feature_list_geometry_only),
        "geolayer_name": "geometry_only",
        "field_name_filter": None,
        "force_field_conversion": False,
        "bbox_extent": True,
        "crs": 2154,
        "return_value": {
            "metadata": {
                "name": "geometry_only",
                "geometry_ref": {
                    "type": {"Polygon", "MultiPolygon"},
                    "crs": 2154,
                    "extent": (202166.0, 6704696.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: copy.deepcopy(feature_list_geometry_only[0]),
                1: copy.deepcopy(feature_list_geometry_only[1]),
                2: copy.deepcopy(feature_list_geometry_only[2]),
                3: copy.deepcopy(feature_list_geometry_only[3]),
            },
        },
    },
    6: {
        "feature_list": copy.deepcopy(feature_list_geometry_only_with_all_geometries),
        "geolayer_name": "all_geometries",
        "field_name_filter": None,
        "force_field_conversion": False,
        "bbox_extent": False,
        "crs": 4326,
        "return_value": {
            "metadata": {
                "name": "all_geometries",
                "geometry_ref": {
                    "type": {
                        "Point",
                        "LineString",
                        "Polygon",
                        "MultiPoint",
                        "MultiLineString",
                        "MultiPolygon",
                        "GeometryCollection",
                    },
                    "crs": 4326,
                },
            },
            "features": {
                0: feature_geometry_only_point,
                1: feature_geometry_only_point_empty,
                2: feature_geometry_only_linestring,
                3: feature_geometry_only_linestring_empty,
                4: feature_geometry_only_polygon,
                5: feature_geometry_only_polygon_empty,
                6: feature_geometry_only_multipoint,
                7: feature_geometry_only_multipoint_empty,
                8: feature_geometry_only_multilinestring,
                9: feature_geometry_only_multilinestring_empty,
                10: feature_geometry_only_multipolygon,
                11: feature_geometry_only_multipolygon_empty,
                12: feature_geometry_only_collection,
                13: feature_geometry_only_collection_empty,
                14: feature_geometry_only_collection_with_empty_geometries,
            },
        },
    },
    7: {
        "feature_list": copy.deepcopy(feature_list_geometry_only_with_all_geometries),
        "geolayer_name": "all_geometries",
        "field_name_filter": "foo",
        "force_field_conversion": True,
        "bbox_extent": True,
        "geometry_type_filter": None,
        "bbox_filter": None,
        "crs": 4326,
        "return_value": {
            "metadata": {
                "name": "all_geometries",
                "geometry_ref": {
                    "type": {
                        "Point",
                        "LineString",
                        "Polygon",
                        "MultiPoint",
                        "MultiLineString",
                        "MultiPolygon",
                        "GeometryCollection",
                    },
                    "extent": (-157.97, -34.29, 35.12, 77.95),
                    "crs": 4326,
                },
            },
            "features": {
                0: {
                    "geometry": {
                        "type": "Point",
                        "coordinates": point_coordinates,
                        "bbox": (-115.81, 37.24, -115.81, 37.24),
                    }
                },
                1: feature_geometry_only_point_empty,
                2: {
                    "geometry": {
                        "type": "LineString",
                        "coordinates": linestring_coordinates,
                        "bbox": (8.919, 44.4074, 8.923, 44.4075),
                    }
                },
                3: feature_geometry_only_linestring_empty,
                4: {
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": polygon_coordinates,
                        "bbox": (-120.43, -20.28, 23.194, 57.322),
                    }
                },
                5: feature_geometry_only_polygon_empty,
                6: {
                    "geometry": {
                        "type": "MultiPoint",
                        "coordinates": multipoint_coordinates,
                        "bbox": (-157.97, 19.61, -155.52, 21.46),
                    }
                },
                7: feature_geometry_only_multipoint_empty,
                8: {
                    "geometry": {
                        "type": "MultiLineString",
                        "coordinates": multilinestring_coordinates,
                        "bbox": (-130.95, -34.25, 23.15, 77.95),
                    }
                },
                9: feature_geometry_only_multilinestring_empty,
                10: {
                    "geometry": {
                        "type": "MultiPolygon",
                        "coordinates": multipolygon_coordinates,
                        "bbox": (-130.91, -34.29, 35.12, 77.91),
                    }
                },
                11: feature_geometry_only_multipolygon_empty,
                12: {
                    "geometry": {
                        "type": "GeometryCollection",
                        "geometries": [
                            {
                                "type": "Point",
                                "coordinates": [-115.81, 37.24],
                                "bbox": (-115.81, 37.24, -115.81, 37.24),
                            },
                            {
                                "type": "LineString",
                                "coordinates": [[8.919, 44.4074], [8.923, 44.4075]],
                                "bbox": (8.919, 44.4074, 8.923, 44.4075),
                            },
                            {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [2.38, 57.322],
                                        [23.194, -20.28],
                                        [-120.43, 19.15],
                                        [2.38, 57.322],
                                    ],
                                    [
                                        [-5.21, 23.51],
                                        [15.21, -10.81],
                                        [-20.51, 1.51],
                                        [-5.21, 23.51],
                                    ],
                                ],
                                "bbox": (-120.43, -20.28, 23.194, 57.322),
                            },
                            {
                                "type": "MultiPoint",
                                "coordinates": [
                                    [-155.52, 19.61],
                                    [-156.22, 20.74],
                                    [-157.97, 21.46],
                                ],
                                "bbox": (-157.97, 19.61, -155.52, 21.46),
                            },
                            {
                                "type": "MultiLineString",
                                "coordinates": [
                                    [[3.75, 9.25], [-130.95, 1.52]],
                                    [[23.15, -34.25], [-1.35, -4.65], [3.45, 77.95]],
                                ],
                                "bbox": (-130.95, -34.25, 23.15, 77.95),
                            },
                            {
                                "type": "MultiPolygon",
                                "coordinates": [
                                    [
                                        [
                                            [3.78, 9.28],
                                            [-130.91, 1.52],
                                            [35.12, 72.234],
                                            [3.78, 9.28],
                                        ]
                                    ],
                                    [
                                        [
                                            [23.18, -34.29],
                                            [-1.31, -4.61],
                                            [3.41, 77.91],
                                            [23.18, -34.29],
                                        ]
                                    ],
                                ],
                                "bbox": (-130.91, -34.29, 35.12, 77.91),
                            },
                        ],
                        "bbox": (-157.97, -34.29, 35.12, 77.95),
                    }
                },
                13: feature_geometry_only_collection_empty,
                14: {
                    "geometry": {
                        "type": "GeometryCollection",
                        "geometries": [
                            {"type": "Point", "coordinates": []},
                            {
                                "type": "LineString",
                                "coordinates": [[8.919, 44.4074], [8.923, 44.4075]],
                                "bbox": (8.919, 44.4074, 8.923, 44.4075),
                            },
                            {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [2.38, 57.322],
                                        [23.194, -20.28],
                                        [-120.43, 19.15],
                                        [2.38, 57.322],
                                    ],
                                    [
                                        [-5.21, 23.51],
                                        [15.21, -10.81],
                                        [-20.51, 1.51],
                                        [-5.21, 23.51],
                                    ],
                                ],
                                "bbox": (-120.43, -20.28, 23.194, 57.322),
                            },
                            {"type": "MultiPoint", "coordinates": []},
                            {
                                "type": "MultiLineString",
                                "coordinates": [
                                    [[3.75, 9.25], [-130.95, 1.52]],
                                    [[23.15, -34.25], [-1.35, -4.65], [3.45, 77.95]],
                                ],
                                "bbox": (-130.95, -34.25, 23.15, 77.95),
                            },
                            {"type": "MultiPolygon", "coordinates": []},
                        ],
                        "bbox": (-130.95, -34.25, 23.194, 77.95),
                    }
                },
            },
        },
    },
    8: {
        "feature_list": copy.deepcopy(feature_list_geometry_only_with_all_geometries),
        "geolayer_name": "all_geometries",
        "field_name_filter": "foo",
        "force_field_conversion": True,
        "bbox_extent": False,
        "crs": 4326,
        "return_value": {
            "metadata": {
                "name": "all_geometries",
                "geometry_ref": {
                    "type": {
                        "Point",
                        "LineString",
                        "Polygon",
                        "MultiPoint",
                        "MultiLineString",
                        "MultiPolygon",
                        "GeometryCollection",
                    },
                    "crs": 4326,
                },
            },
            "features": {
                0: feature_geometry_only_point,
                1: feature_geometry_only_point_empty,
                2: feature_geometry_only_linestring,
                3: feature_geometry_only_linestring_empty,
                4: feature_geometry_only_polygon,
                5: feature_geometry_only_polygon_empty,
                6: feature_geometry_only_multipoint,
                7: feature_geometry_only_multipoint_empty,
                8: feature_geometry_only_multilinestring,
                9: feature_geometry_only_multilinestring_empty,
                10: feature_geometry_only_multipolygon,
                11: feature_geometry_only_multipolygon_empty,
                12: feature_geometry_only_collection,
                13: feature_geometry_only_collection_empty,
                14: feature_geometry_only_collection_with_empty_geometries,
            },
        },
    },
    9: {
        "feature_list": copy.deepcopy(feature_list_data_and_geometry),
        "geolayer_name": "data_and_geometries",
        "field_name_filter": None,
        "force_field_conversion": False,
        "bbox_extent": False,
        "crs": 2154,
        "return_value": feature_list_data_and_geometry_geolayer,
    },
    10: {
        "feature_list": copy.deepcopy(feature_list_data_and_geometry),
        "geolayer_name": "data_and_geometries",
        "field_name_filter": None,
        "force_field_conversion": True,
        "bbox_extent": True,
        "crs": None,
        "return_value": {
            "metadata": {
                "name": "data_and_geometries",
                "fields": {
                    "CODE_DEPT": {"type": "Integer", "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                },
                "geometry_ref": {
                    "type": {"Polygon", "MultiPolygon"},
                    "extent": (202166.0, 6704696.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (382932.0, 6743442.0, 474394.0, 6833996.0),
                        "coordinates": [
                            [
                                [399495.0, 6830885.0],
                                [398130.0, 6822559.0],
                                [400321.0, 6810723.0],
                                [395852.0, 6803336.0],
                                [398626.0, 6784333.0],
                                [400465.0, 6781914.0],
                                [400197.0, 6773697.0],
                                [394099.0, 6773357.0],
                                [390140.0, 6770978.0],
                                [386941.0, 6760260.0],
                                [382932.0, 6754022.0],
                                [389872.0, 6749698.0],
                                [393110.0, 6750366.0],
                                [402067.0, 6747685.0],
                                [404251.0, 6751414.0],
                                [412442.0, 6746090.0],
                                [419671.0, 6744167.0],
                                [429458.0, 6743442.0],
                                [440863.0, 6746201.0],
                                [446732.0, 6745443.0],
                                [446459.0, 6750432.0],
                                [442128.0, 6753611.0],
                                [448124.0, 6758669.0],
                                [447308.0, 6764356.0],
                                [455060.0, 6767070.0],
                                [451057.0, 6776681.0],
                                [459373.0, 6778102.0],
                                [460615.0, 6783387.0],
                                [458409.0, 6789055.0],
                                [466280.0, 6794064.0],
                                [465298.0, 6799724.0],
                                [467628.0, 6811401.0],
                                [473893.0, 6813452.0],
                                [474394.0, 6821359.0],
                                [467262.0, 6822174.0],
                                [466087.0, 6830999.0],
                                [463434.0, 6833996.0],
                                [457920.0, 6827997.0],
                                [451256.0, 6826715.0],
                                [446687.0, 6829012.0],
                                [441174.0, 6828584.0],
                                [437568.0, 6825109.0],
                                [429868.0, 6822252.0],
                                [422197.0, 6821752.0],
                                [414934.0, 6829326.0],
                                [407934.0, 6831360.0],
                                [404267.0, 6828490.0],
                                [399495.0, 6830885.0],
                            ]
                        ],
                    },
                    "attributes": {"CODE_DEPT": 53, "NOM_DEPT": "MAYENNE"},
                },
                1: {
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                        "coordinates": [
                            [
                                [776081.0, 6923412.0],
                                [775403.0, 6934852.0],
                                [777906.0, 6941851.0],
                                [774574.0, 6946610.0],
                                [779463.0, 6948255.0],
                                [781387.0, 6953785.0],
                                [790134.0, 6962730.0],
                                [787172.0, 6965431.0],
                                [789845.0, 6973793.0],
                                [788558.0, 6985051.0],
                                [781905.0, 6987282.0],
                                [778060.0, 6986162.0],
                                [770359.0, 6988977.0],
                                [766237.0, 6992385.0],
                                [753505.0, 6995276.0],
                                [751253.0, 6997000.0],
                                [744014.0, 6992056.0],
                                [739058.0, 6995179.0],
                                [735248.0, 6991264.0],
                                [725313.0, 6993104.0],
                                [720100.0, 6990781.0],
                                [716534.0, 6992565.0],
                                [712391.0, 6990404.0],
                                [713833.0, 6986563.0],
                                [708480.0, 6979518.0],
                                [705667.0, 6969289.0],
                                [708546.0, 6956332.0],
                                [707064.0, 6950845.0],
                                [709520.0, 6938240.0],
                                [706939.0, 6934901.0],
                                [711648.0, 6928031.0],
                                [706805.0, 6926038.0],
                                [706929.0, 6919738.0],
                                [698137.0, 6911415.0],
                                [701957.0, 6908433.0],
                                [704672.0, 6899225.0],
                                [710189.0, 6894765.0],
                                [705248.0, 6890863.0],
                                [712067.0, 6888882.0],
                                [712559.0, 6879371.0],
                                [722321.0, 6872132.0],
                                [724211.0, 6867685.0],
                                [729581.0, 6862815.0],
                                [735603.0, 6861428.0],
                                [738742.0, 6868146.0],
                                [744067.0, 6871735.0],
                                [747254.0, 6882494.0],
                                [743801.0, 6891376.0],
                                [745398.0, 6894771.0],
                                [751361.0, 6898188.0],
                                [747051.0, 6913033.0],
                                [761575.0, 6918670.0],
                                [767112.0, 6923360.0],
                                [775242.0, 6918312.0],
                                [776081.0, 6923412.0],
                            ]
                        ],
                    },
                    "attributes": {"CODE_DEPT": 2, "NOM_DEPT": "AISNE"},
                },
                2: {
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                        "coordinates": [
                            [
                                [598361.0, 6887345.0],
                                [603102.0, 6887292.0],
                                [606678.0, 6883543.0],
                                [614076.0, 6886919.0],
                                [622312.0, 6880731.0],
                                [628641.0, 6878089.0],
                                [633062.0, 6879807.0],
                                [641836.0, 6872490.0],
                                [641404.0, 6867928.0],
                                [648071.0, 6872567.0],
                                [653619.0, 6875101.0],
                                [660416.0, 6872923.0],
                                [667303.0, 6878971.0],
                                [670084.0, 6886723.0],
                                [659205.0, 6894147.0],
                                [652314.0, 6895981.0],
                                [649761.0, 6898738.0],
                                [645465.0, 6895048.0],
                                [633020.0, 6901508.0],
                                [626847.0, 6897876.0],
                                [618689.0, 6896449.0],
                                [612180.0, 6899061.0],
                                [608283.0, 6898554.0],
                                [605624.0, 6904387.0],
                                [603501.0, 6902160.0],
                                [601892.0, 6893098.0],
                                [598361.0, 6887345.0],
                            ]
                        ],
                    },
                    "attributes": {"CODE_DEPT": 95, "NOM_DEPT": "VAL-D'OISE"},
                },
                3: {
                    "geometry": {
                        "type": "MultiPolygon",
                        "bbox": (202166.0, 6704696.0, 322365.0, 6807535.0),
                        "coordinates": [
                            [
                                [
                                    [229520.0, 6710085.0],
                                    [240383.0, 6704696.0],
                                    [240163.0, 6708285.0],
                                    [235835.0, 6713741.0],
                                    [229006.0, 6716339.0],
                                    [229520.0, 6710085.0],
                                ]
                            ],
                            [
                                [
                                    [212687.0, 6770001.0],
                                    [211559.0, 6762660.0],
                                    [216528.0, 6752538.0],
                                    [224759.0, 6753321.0],
                                    [234540.0, 6747533.0],
                                    [234220.0, 6745025.0],
                                    [240082.0, 6736634.0],
                                    [251238.0, 6736509.0],
                                    [260889.0, 6740570.0],
                                    [266327.0, 6740184.0],
                                    [271833.0, 6736526.0],
                                    [269308.0, 6731426.0],
                                    [263161.0, 6733044.0],
                                    [258643.0, 6731063.0],
                                    [263631.0, 6725691.0],
                                    [274085.0, 6728424.0],
                                    [283689.0, 6728526.0],
                                    [290663.0, 6724762.0],
                                    [288997.0, 6719519.0],
                                    [300067.0, 6720583.0],
                                    [315995.0, 6726944.0],
                                    [317487.0, 6738014.0],
                                    [315562.0, 6748257.0],
                                    [318803.0, 6749864.0],
                                    [322365.0, 6758359.0],
                                    [317839.0, 6765781.0],
                                    [320890.0, 6769878.0],
                                    [317014.0, 6776765.0],
                                    [309516.0, 6779524.0],
                                    [306739.0, 6782705.0],
                                    [310549.0, 6787938.0],
                                    [306966.0, 6794650.0],
                                    [300637.0, 6793781.0],
                                    [298204.0, 6799128.0],
                                    [291749.0, 6798375.0],
                                    [285132.0, 6789099.0],
                                    [280665.0, 6785525.0],
                                    [277875.0, 6787107.0],
                                    [279762.0, 6794931.0],
                                    [270150.0, 6795768.0],
                                    [252150.0, 6805897.0],
                                    [246074.0, 6807146.0],
                                    [242780.0, 6802066.0],
                                    [233945.0, 6800703.0],
                                    [229439.0, 6804532.0],
                                    [212675.0, 6807535.0],
                                    [202658.0, 6804638.0],
                                    [202166.0, 6798131.0],
                                    [205220.0, 6785800.0],
                                    [211608.0, 6786141.0],
                                    [216607.0, 6782805.0],
                                    [223352.0, 6780867.0],
                                    [221788.0, 6771592.0],
                                    [212687.0, 6770001.0],
                                ]
                            ],
                        ],
                    },
                    "attributes": {"CODE_DEPT": 56, "NOM_DEPT": "MORBIHAN"},
                },
            },
        },
    },
    11: {
        "feature_list": copy.deepcopy(feature_list_data_and_geometry),
        "geolayer_name": "data_and_geometries",
        "field_name_filter": ["NOM_DEPT", "CODE_DEPT"],
        "force_field_conversion": True,
        "bbox_extent": True,
        "crs": None,
        "return_value": {
            "metadata": {
                "name": "data_and_geometries",
                "fields": {
                    "CODE_DEPT": {"type": "Integer", "index": 1},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 0},
                },
                "geometry_ref": {
                    "type": {"Polygon", "MultiPolygon"},
                    "extent": (202166.0, 6704696.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (382932.0, 6743442.0, 474394.0, 6833996.0),
                        "coordinates": [
                            [
                                [399495.0, 6830885.0],
                                [398130.0, 6822559.0],
                                [400321.0, 6810723.0],
                                [395852.0, 6803336.0],
                                [398626.0, 6784333.0],
                                [400465.0, 6781914.0],
                                [400197.0, 6773697.0],
                                [394099.0, 6773357.0],
                                [390140.0, 6770978.0],
                                [386941.0, 6760260.0],
                                [382932.0, 6754022.0],
                                [389872.0, 6749698.0],
                                [393110.0, 6750366.0],
                                [402067.0, 6747685.0],
                                [404251.0, 6751414.0],
                                [412442.0, 6746090.0],
                                [419671.0, 6744167.0],
                                [429458.0, 6743442.0],
                                [440863.0, 6746201.0],
                                [446732.0, 6745443.0],
                                [446459.0, 6750432.0],
                                [442128.0, 6753611.0],
                                [448124.0, 6758669.0],
                                [447308.0, 6764356.0],
                                [455060.0, 6767070.0],
                                [451057.0, 6776681.0],
                                [459373.0, 6778102.0],
                                [460615.0, 6783387.0],
                                [458409.0, 6789055.0],
                                [466280.0, 6794064.0],
                                [465298.0, 6799724.0],
                                [467628.0, 6811401.0],
                                [473893.0, 6813452.0],
                                [474394.0, 6821359.0],
                                [467262.0, 6822174.0],
                                [466087.0, 6830999.0],
                                [463434.0, 6833996.0],
                                [457920.0, 6827997.0],
                                [451256.0, 6826715.0],
                                [446687.0, 6829012.0],
                                [441174.0, 6828584.0],
                                [437568.0, 6825109.0],
                                [429868.0, 6822252.0],
                                [422197.0, 6821752.0],
                                [414934.0, 6829326.0],
                                [407934.0, 6831360.0],
                                [404267.0, 6828490.0],
                                [399495.0, 6830885.0],
                            ]
                        ],
                    },
                    "attributes": {"CODE_DEPT": 53, "NOM_DEPT": "MAYENNE"},
                },
                1: {
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                        "coordinates": [
                            [
                                [776081.0, 6923412.0],
                                [775403.0, 6934852.0],
                                [777906.0, 6941851.0],
                                [774574.0, 6946610.0],
                                [779463.0, 6948255.0],
                                [781387.0, 6953785.0],
                                [790134.0, 6962730.0],
                                [787172.0, 6965431.0],
                                [789845.0, 6973793.0],
                                [788558.0, 6985051.0],
                                [781905.0, 6987282.0],
                                [778060.0, 6986162.0],
                                [770359.0, 6988977.0],
                                [766237.0, 6992385.0],
                                [753505.0, 6995276.0],
                                [751253.0, 6997000.0],
                                [744014.0, 6992056.0],
                                [739058.0, 6995179.0],
                                [735248.0, 6991264.0],
                                [725313.0, 6993104.0],
                                [720100.0, 6990781.0],
                                [716534.0, 6992565.0],
                                [712391.0, 6990404.0],
                                [713833.0, 6986563.0],
                                [708480.0, 6979518.0],
                                [705667.0, 6969289.0],
                                [708546.0, 6956332.0],
                                [707064.0, 6950845.0],
                                [709520.0, 6938240.0],
                                [706939.0, 6934901.0],
                                [711648.0, 6928031.0],
                                [706805.0, 6926038.0],
                                [706929.0, 6919738.0],
                                [698137.0, 6911415.0],
                                [701957.0, 6908433.0],
                                [704672.0, 6899225.0],
                                [710189.0, 6894765.0],
                                [705248.0, 6890863.0],
                                [712067.0, 6888882.0],
                                [712559.0, 6879371.0],
                                [722321.0, 6872132.0],
                                [724211.0, 6867685.0],
                                [729581.0, 6862815.0],
                                [735603.0, 6861428.0],
                                [738742.0, 6868146.0],
                                [744067.0, 6871735.0],
                                [747254.0, 6882494.0],
                                [743801.0, 6891376.0],
                                [745398.0, 6894771.0],
                                [751361.0, 6898188.0],
                                [747051.0, 6913033.0],
                                [761575.0, 6918670.0],
                                [767112.0, 6923360.0],
                                [775242.0, 6918312.0],
                                [776081.0, 6923412.0],
                            ]
                        ],
                    },
                    "attributes": {"CODE_DEPT": 2, "NOM_DEPT": "AISNE"},
                },
                2: {
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                        "coordinates": [
                            [
                                [598361.0, 6887345.0],
                                [603102.0, 6887292.0],
                                [606678.0, 6883543.0],
                                [614076.0, 6886919.0],
                                [622312.0, 6880731.0],
                                [628641.0, 6878089.0],
                                [633062.0, 6879807.0],
                                [641836.0, 6872490.0],
                                [641404.0, 6867928.0],
                                [648071.0, 6872567.0],
                                [653619.0, 6875101.0],
                                [660416.0, 6872923.0],
                                [667303.0, 6878971.0],
                                [670084.0, 6886723.0],
                                [659205.0, 6894147.0],
                                [652314.0, 6895981.0],
                                [649761.0, 6898738.0],
                                [645465.0, 6895048.0],
                                [633020.0, 6901508.0],
                                [626847.0, 6897876.0],
                                [618689.0, 6896449.0],
                                [612180.0, 6899061.0],
                                [608283.0, 6898554.0],
                                [605624.0, 6904387.0],
                                [603501.0, 6902160.0],
                                [601892.0, 6893098.0],
                                [598361.0, 6887345.0],
                            ]
                        ],
                    },
                    "attributes": {"CODE_DEPT": 95, "NOM_DEPT": "VAL-D'OISE"},
                },
                3: {
                    "geometry": {
                        "type": "MultiPolygon",
                        "bbox": (202166.0, 6704696.0, 322365.0, 6807535.0),
                        "coordinates": [
                            [
                                [
                                    [229520.0, 6710085.0],
                                    [240383.0, 6704696.0],
                                    [240163.0, 6708285.0],
                                    [235835.0, 6713741.0],
                                    [229006.0, 6716339.0],
                                    [229520.0, 6710085.0],
                                ]
                            ],
                            [
                                [
                                    [212687.0, 6770001.0],
                                    [211559.0, 6762660.0],
                                    [216528.0, 6752538.0],
                                    [224759.0, 6753321.0],
                                    [234540.0, 6747533.0],
                                    [234220.0, 6745025.0],
                                    [240082.0, 6736634.0],
                                    [251238.0, 6736509.0],
                                    [260889.0, 6740570.0],
                                    [266327.0, 6740184.0],
                                    [271833.0, 6736526.0],
                                    [269308.0, 6731426.0],
                                    [263161.0, 6733044.0],
                                    [258643.0, 6731063.0],
                                    [263631.0, 6725691.0],
                                    [274085.0, 6728424.0],
                                    [283689.0, 6728526.0],
                                    [290663.0, 6724762.0],
                                    [288997.0, 6719519.0],
                                    [300067.0, 6720583.0],
                                    [315995.0, 6726944.0],
                                    [317487.0, 6738014.0],
                                    [315562.0, 6748257.0],
                                    [318803.0, 6749864.0],
                                    [322365.0, 6758359.0],
                                    [317839.0, 6765781.0],
                                    [320890.0, 6769878.0],
                                    [317014.0, 6776765.0],
                                    [309516.0, 6779524.0],
                                    [306739.0, 6782705.0],
                                    [310549.0, 6787938.0],
                                    [306966.0, 6794650.0],
                                    [300637.0, 6793781.0],
                                    [298204.0, 6799128.0],
                                    [291749.0, 6798375.0],
                                    [285132.0, 6789099.0],
                                    [280665.0, 6785525.0],
                                    [277875.0, 6787107.0],
                                    [279762.0, 6794931.0],
                                    [270150.0, 6795768.0],
                                    [252150.0, 6805897.0],
                                    [246074.0, 6807146.0],
                                    [242780.0, 6802066.0],
                                    [233945.0, 6800703.0],
                                    [229439.0, 6804532.0],
                                    [212675.0, 6807535.0],
                                    [202658.0, 6804638.0],
                                    [202166.0, 6798131.0],
                                    [205220.0, 6785800.0],
                                    [211608.0, 6786141.0],
                                    [216607.0, 6782805.0],
                                    [223352.0, 6780867.0],
                                    [221788.0, 6771592.0],
                                    [212687.0, 6770001.0],
                                ]
                            ],
                        ],
                    },
                    "attributes": {"CODE_DEPT": 56, "NOM_DEPT": "MORBIHAN"},
                },
            },
        },
    },
    12: {
        "feature_list": copy.deepcopy(feature_list_data_and_geometry),
        "geolayer_name": "data_and_geometries",
        "field_name_filter": ["NOM_DEPT"],
        "force_field_conversion": True,
        "bbox_extent": True,
        "crs": None,
        "return_value": {
            "metadata": {
                "name": "data_and_geometries",
                "fields": {"NOM_DEPT": {"type": "String", "width": 10, "index": 0}},
                "geometry_ref": {
                    "type": {"Polygon", "MultiPolygon"},
                    "extent": (202166.0, 6704696.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (382932.0, 6743442.0, 474394.0, 6833996.0),
                        "coordinates": [
                            [
                                [399495.0, 6830885.0],
                                [398130.0, 6822559.0],
                                [400321.0, 6810723.0],
                                [395852.0, 6803336.0],
                                [398626.0, 6784333.0],
                                [400465.0, 6781914.0],
                                [400197.0, 6773697.0],
                                [394099.0, 6773357.0],
                                [390140.0, 6770978.0],
                                [386941.0, 6760260.0],
                                [382932.0, 6754022.0],
                                [389872.0, 6749698.0],
                                [393110.0, 6750366.0],
                                [402067.0, 6747685.0],
                                [404251.0, 6751414.0],
                                [412442.0, 6746090.0],
                                [419671.0, 6744167.0],
                                [429458.0, 6743442.0],
                                [440863.0, 6746201.0],
                                [446732.0, 6745443.0],
                                [446459.0, 6750432.0],
                                [442128.0, 6753611.0],
                                [448124.0, 6758669.0],
                                [447308.0, 6764356.0],
                                [455060.0, 6767070.0],
                                [451057.0, 6776681.0],
                                [459373.0, 6778102.0],
                                [460615.0, 6783387.0],
                                [458409.0, 6789055.0],
                                [466280.0, 6794064.0],
                                [465298.0, 6799724.0],
                                [467628.0, 6811401.0],
                                [473893.0, 6813452.0],
                                [474394.0, 6821359.0],
                                [467262.0, 6822174.0],
                                [466087.0, 6830999.0],
                                [463434.0, 6833996.0],
                                [457920.0, 6827997.0],
                                [451256.0, 6826715.0],
                                [446687.0, 6829012.0],
                                [441174.0, 6828584.0],
                                [437568.0, 6825109.0],
                                [429868.0, 6822252.0],
                                [422197.0, 6821752.0],
                                [414934.0, 6829326.0],
                                [407934.0, 6831360.0],
                                [404267.0, 6828490.0],
                                [399495.0, 6830885.0],
                            ]
                        ],
                    },
                    "attributes": {"NOM_DEPT": "MAYENNE"},
                },
                1: {
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                        "coordinates": [
                            [
                                [776081.0, 6923412.0],
                                [775403.0, 6934852.0],
                                [777906.0, 6941851.0],
                                [774574.0, 6946610.0],
                                [779463.0, 6948255.0],
                                [781387.0, 6953785.0],
                                [790134.0, 6962730.0],
                                [787172.0, 6965431.0],
                                [789845.0, 6973793.0],
                                [788558.0, 6985051.0],
                                [781905.0, 6987282.0],
                                [778060.0, 6986162.0],
                                [770359.0, 6988977.0],
                                [766237.0, 6992385.0],
                                [753505.0, 6995276.0],
                                [751253.0, 6997000.0],
                                [744014.0, 6992056.0],
                                [739058.0, 6995179.0],
                                [735248.0, 6991264.0],
                                [725313.0, 6993104.0],
                                [720100.0, 6990781.0],
                                [716534.0, 6992565.0],
                                [712391.0, 6990404.0],
                                [713833.0, 6986563.0],
                                [708480.0, 6979518.0],
                                [705667.0, 6969289.0],
                                [708546.0, 6956332.0],
                                [707064.0, 6950845.0],
                                [709520.0, 6938240.0],
                                [706939.0, 6934901.0],
                                [711648.0, 6928031.0],
                                [706805.0, 6926038.0],
                                [706929.0, 6919738.0],
                                [698137.0, 6911415.0],
                                [701957.0, 6908433.0],
                                [704672.0, 6899225.0],
                                [710189.0, 6894765.0],
                                [705248.0, 6890863.0],
                                [712067.0, 6888882.0],
                                [712559.0, 6879371.0],
                                [722321.0, 6872132.0],
                                [724211.0, 6867685.0],
                                [729581.0, 6862815.0],
                                [735603.0, 6861428.0],
                                [738742.0, 6868146.0],
                                [744067.0, 6871735.0],
                                [747254.0, 6882494.0],
                                [743801.0, 6891376.0],
                                [745398.0, 6894771.0],
                                [751361.0, 6898188.0],
                                [747051.0, 6913033.0],
                                [761575.0, 6918670.0],
                                [767112.0, 6923360.0],
                                [775242.0, 6918312.0],
                                [776081.0, 6923412.0],
                            ]
                        ],
                    },
                    "attributes": {"NOM_DEPT": "AISNE"},
                },
                2: {
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                        "coordinates": [
                            [
                                [598361.0, 6887345.0],
                                [603102.0, 6887292.0],
                                [606678.0, 6883543.0],
                                [614076.0, 6886919.0],
                                [622312.0, 6880731.0],
                                [628641.0, 6878089.0],
                                [633062.0, 6879807.0],
                                [641836.0, 6872490.0],
                                [641404.0, 6867928.0],
                                [648071.0, 6872567.0],
                                [653619.0, 6875101.0],
                                [660416.0, 6872923.0],
                                [667303.0, 6878971.0],
                                [670084.0, 6886723.0],
                                [659205.0, 6894147.0],
                                [652314.0, 6895981.0],
                                [649761.0, 6898738.0],
                                [645465.0, 6895048.0],
                                [633020.0, 6901508.0],
                                [626847.0, 6897876.0],
                                [618689.0, 6896449.0],
                                [612180.0, 6899061.0],
                                [608283.0, 6898554.0],
                                [605624.0, 6904387.0],
                                [603501.0, 6902160.0],
                                [601892.0, 6893098.0],
                                [598361.0, 6887345.0],
                            ]
                        ],
                    },
                    "attributes": {"NOM_DEPT": "VAL-D'OISE"},
                },
                3: {
                    "geometry": {
                        "type": "MultiPolygon",
                        "bbox": (202166.0, 6704696.0, 322365.0, 6807535.0),
                        "coordinates": [
                            [
                                [
                                    [229520.0, 6710085.0],
                                    [240383.0, 6704696.0],
                                    [240163.0, 6708285.0],
                                    [235835.0, 6713741.0],
                                    [229006.0, 6716339.0],
                                    [229520.0, 6710085.0],
                                ]
                            ],
                            [
                                [
                                    [212687.0, 6770001.0],
                                    [211559.0, 6762660.0],
                                    [216528.0, 6752538.0],
                                    [224759.0, 6753321.0],
                                    [234540.0, 6747533.0],
                                    [234220.0, 6745025.0],
                                    [240082.0, 6736634.0],
                                    [251238.0, 6736509.0],
                                    [260889.0, 6740570.0],
                                    [266327.0, 6740184.0],
                                    [271833.0, 6736526.0],
                                    [269308.0, 6731426.0],
                                    [263161.0, 6733044.0],
                                    [258643.0, 6731063.0],
                                    [263631.0, 6725691.0],
                                    [274085.0, 6728424.0],
                                    [283689.0, 6728526.0],
                                    [290663.0, 6724762.0],
                                    [288997.0, 6719519.0],
                                    [300067.0, 6720583.0],
                                    [315995.0, 6726944.0],
                                    [317487.0, 6738014.0],
                                    [315562.0, 6748257.0],
                                    [318803.0, 6749864.0],
                                    [322365.0, 6758359.0],
                                    [317839.0, 6765781.0],
                                    [320890.0, 6769878.0],
                                    [317014.0, 6776765.0],
                                    [309516.0, 6779524.0],
                                    [306739.0, 6782705.0],
                                    [310549.0, 6787938.0],
                                    [306966.0, 6794650.0],
                                    [300637.0, 6793781.0],
                                    [298204.0, 6799128.0],
                                    [291749.0, 6798375.0],
                                    [285132.0, 6789099.0],
                                    [280665.0, 6785525.0],
                                    [277875.0, 6787107.0],
                                    [279762.0, 6794931.0],
                                    [270150.0, 6795768.0],
                                    [252150.0, 6805897.0],
                                    [246074.0, 6807146.0],
                                    [242780.0, 6802066.0],
                                    [233945.0, 6800703.0],
                                    [229439.0, 6804532.0],
                                    [212675.0, 6807535.0],
                                    [202658.0, 6804638.0],
                                    [202166.0, 6798131.0],
                                    [205220.0, 6785800.0],
                                    [211608.0, 6786141.0],
                                    [216607.0, 6782805.0],
                                    [223352.0, 6780867.0],
                                    [221788.0, 6771592.0],
                                    [212687.0, 6770001.0],
                                ]
                            ],
                        ],
                    },
                    "attributes": {"NOM_DEPT": "MORBIHAN"},
                },
            },
        },
    },
    13: {
        "feature_list": copy.deepcopy(feature_list_data_and_geometry),
        "geolayer_name": "data_and_geometries",
        "field_name_filter": "NOM_DEPT",
        "force_field_conversion": True,
        "geometry_type_filter": None,
        "bbox_filter": None,
        "bbox_extent": True,
        "crs": None,
        "return_value": {
            "metadata": {
                "name": "data_and_geometries",
                "fields": {"NOM_DEPT": {"type": "String", "width": 10, "index": 0}},
                "geometry_ref": {
                    "type": {"Polygon", "MultiPolygon"},
                    "extent": (202166.0, 6704696.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {
                    "attributes": {"NOM_DEPT": "MAYENNE"},
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (382932.0, 6743442.0, 474394.0, 6833996.0),
                        "coordinates": [
                            [
                                [399495.0, 6830885.0],
                                [398130.0, 6822559.0],
                                [400321.0, 6810723.0],
                                [395852.0, 6803336.0],
                                [398626.0, 6784333.0],
                                [400465.0, 6781914.0],
                                [400197.0, 6773697.0],
                                [394099.0, 6773357.0],
                                [390140.0, 6770978.0],
                                [386941.0, 6760260.0],
                                [382932.0, 6754022.0],
                                [389872.0, 6749698.0],
                                [393110.0, 6750366.0],
                                [402067.0, 6747685.0],
                                [404251.0, 6751414.0],
                                [412442.0, 6746090.0],
                                [419671.0, 6744167.0],
                                [429458.0, 6743442.0],
                                [440863.0, 6746201.0],
                                [446732.0, 6745443.0],
                                [446459.0, 6750432.0],
                                [442128.0, 6753611.0],
                                [448124.0, 6758669.0],
                                [447308.0, 6764356.0],
                                [455060.0, 6767070.0],
                                [451057.0, 6776681.0],
                                [459373.0, 6778102.0],
                                [460615.0, 6783387.0],
                                [458409.0, 6789055.0],
                                [466280.0, 6794064.0],
                                [465298.0, 6799724.0],
                                [467628.0, 6811401.0],
                                [473893.0, 6813452.0],
                                [474394.0, 6821359.0],
                                [467262.0, 6822174.0],
                                [466087.0, 6830999.0],
                                [463434.0, 6833996.0],
                                [457920.0, 6827997.0],
                                [451256.0, 6826715.0],
                                [446687.0, 6829012.0],
                                [441174.0, 6828584.0],
                                [437568.0, 6825109.0],
                                [429868.0, 6822252.0],
                                [422197.0, 6821752.0],
                                [414934.0, 6829326.0],
                                [407934.0, 6831360.0],
                                [404267.0, 6828490.0],
                                [399495.0, 6830885.0],
                            ]
                        ],
                    },
                },
                1: {
                    "attributes": {"NOM_DEPT": "AISNE"},
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                        "coordinates": [
                            [
                                [776081.0, 6923412.0],
                                [775403.0, 6934852.0],
                                [777906.0, 6941851.0],
                                [774574.0, 6946610.0],
                                [779463.0, 6948255.0],
                                [781387.0, 6953785.0],
                                [790134.0, 6962730.0],
                                [787172.0, 6965431.0],
                                [789845.0, 6973793.0],
                                [788558.0, 6985051.0],
                                [781905.0, 6987282.0],
                                [778060.0, 6986162.0],
                                [770359.0, 6988977.0],
                                [766237.0, 6992385.0],
                                [753505.0, 6995276.0],
                                [751253.0, 6997000.0],
                                [744014.0, 6992056.0],
                                [739058.0, 6995179.0],
                                [735248.0, 6991264.0],
                                [725313.0, 6993104.0],
                                [720100.0, 6990781.0],
                                [716534.0, 6992565.0],
                                [712391.0, 6990404.0],
                                [713833.0, 6986563.0],
                                [708480.0, 6979518.0],
                                [705667.0, 6969289.0],
                                [708546.0, 6956332.0],
                                [707064.0, 6950845.0],
                                [709520.0, 6938240.0],
                                [706939.0, 6934901.0],
                                [711648.0, 6928031.0],
                                [706805.0, 6926038.0],
                                [706929.0, 6919738.0],
                                [698137.0, 6911415.0],
                                [701957.0, 6908433.0],
                                [704672.0, 6899225.0],
                                [710189.0, 6894765.0],
                                [705248.0, 6890863.0],
                                [712067.0, 6888882.0],
                                [712559.0, 6879371.0],
                                [722321.0, 6872132.0],
                                [724211.0, 6867685.0],
                                [729581.0, 6862815.0],
                                [735603.0, 6861428.0],
                                [738742.0, 6868146.0],
                                [744067.0, 6871735.0],
                                [747254.0, 6882494.0],
                                [743801.0, 6891376.0],
                                [745398.0, 6894771.0],
                                [751361.0, 6898188.0],
                                [747051.0, 6913033.0],
                                [761575.0, 6918670.0],
                                [767112.0, 6923360.0],
                                [775242.0, 6918312.0],
                                [776081.0, 6923412.0],
                            ]
                        ],
                    },
                },
                2: {
                    "attributes": {"NOM_DEPT": "VAL-D'OISE"},
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                        "coordinates": [
                            [
                                [598361.0, 6887345.0],
                                [603102.0, 6887292.0],
                                [606678.0, 6883543.0],
                                [614076.0, 6886919.0],
                                [622312.0, 6880731.0],
                                [628641.0, 6878089.0],
                                [633062.0, 6879807.0],
                                [641836.0, 6872490.0],
                                [641404.0, 6867928.0],
                                [648071.0, 6872567.0],
                                [653619.0, 6875101.0],
                                [660416.0, 6872923.0],
                                [667303.0, 6878971.0],
                                [670084.0, 6886723.0],
                                [659205.0, 6894147.0],
                                [652314.0, 6895981.0],
                                [649761.0, 6898738.0],
                                [645465.0, 6895048.0],
                                [633020.0, 6901508.0],
                                [626847.0, 6897876.0],
                                [618689.0, 6896449.0],
                                [612180.0, 6899061.0],
                                [608283.0, 6898554.0],
                                [605624.0, 6904387.0],
                                [603501.0, 6902160.0],
                                [601892.0, 6893098.0],
                                [598361.0, 6887345.0],
                            ]
                        ],
                    },
                },
                3: {
                    "attributes": {"NOM_DEPT": "MORBIHAN"},
                    "geometry": {
                        "type": "MultiPolygon",
                        "bbox": (202166.0, 6704696.0, 322365.0, 6807535.0),
                        "coordinates": [
                            [
                                [
                                    [229520.0, 6710085.0],
                                    [240383.0, 6704696.0],
                                    [240163.0, 6708285.0],
                                    [235835.0, 6713741.0],
                                    [229006.0, 6716339.0],
                                    [229520.0, 6710085.0],
                                ]
                            ],
                            [
                                [
                                    [212687.0, 6770001.0],
                                    [211559.0, 6762660.0],
                                    [216528.0, 6752538.0],
                                    [224759.0, 6753321.0],
                                    [234540.0, 6747533.0],
                                    [234220.0, 6745025.0],
                                    [240082.0, 6736634.0],
                                    [251238.0, 6736509.0],
                                    [260889.0, 6740570.0],
                                    [266327.0, 6740184.0],
                                    [271833.0, 6736526.0],
                                    [269308.0, 6731426.0],
                                    [263161.0, 6733044.0],
                                    [258643.0, 6731063.0],
                                    [263631.0, 6725691.0],
                                    [274085.0, 6728424.0],
                                    [283689.0, 6728526.0],
                                    [290663.0, 6724762.0],
                                    [288997.0, 6719519.0],
                                    [300067.0, 6720583.0],
                                    [315995.0, 6726944.0],
                                    [317487.0, 6738014.0],
                                    [315562.0, 6748257.0],
                                    [318803.0, 6749864.0],
                                    [322365.0, 6758359.0],
                                    [317839.0, 6765781.0],
                                    [320890.0, 6769878.0],
                                    [317014.0, 6776765.0],
                                    [309516.0, 6779524.0],
                                    [306739.0, 6782705.0],
                                    [310549.0, 6787938.0],
                                    [306966.0, 6794650.0],
                                    [300637.0, 6793781.0],
                                    [298204.0, 6799128.0],
                                    [291749.0, 6798375.0],
                                    [285132.0, 6789099.0],
                                    [280665.0, 6785525.0],
                                    [277875.0, 6787107.0],
                                    [279762.0, 6794931.0],
                                    [270150.0, 6795768.0],
                                    [252150.0, 6805897.0],
                                    [246074.0, 6807146.0],
                                    [242780.0, 6802066.0],
                                    [233945.0, 6800703.0],
                                    [229439.0, 6804532.0],
                                    [212675.0, 6807535.0],
                                    [202658.0, 6804638.0],
                                    [202166.0, 6798131.0],
                                    [205220.0, 6785800.0],
                                    [211608.0, 6786141.0],
                                    [216607.0, 6782805.0],
                                    [223352.0, 6780867.0],
                                    [221788.0, 6771592.0],
                                    [212687.0, 6770001.0],
                                ]
                            ],
                        ],
                    },
                },
            },
        },
    },
    14: {
        "feature_list": copy.deepcopy(feature_list_data_and_geometry),
        "geolayer_name": "data_and_geometries",
        "field_name_filter": "NOM_DEPT",
        "force_field_conversion": True,
        "geometry_type_filter": "MultiPolygon",
        "bbox_filter": None,
        "bbox_extent": True,
        "crs": None,
        "return_value": {
            "metadata": {
                "name": "data_and_geometries",
                "fields": {"NOM_DEPT": {"type": "String", "width": 10, "index": 0}},
                "geometry_ref": {
                    "type": {"MultiPolygon"},
                    "extent": (202166.0, 6704696.0, 322365.0, 6807535.0),
                },
            },
            "features": {
                0: {
                    "attributes": {"NOM_DEPT": "MORBIHAN"},
                    "geometry": {
                        "type": "MultiPolygon",
                        "bbox": (202166.0, 6704696.0, 322365.0, 6807535.0),
                        "coordinates": [
                            [
                                [
                                    [229520.0, 6710085.0],
                                    [240383.0, 6704696.0],
                                    [240163.0, 6708285.0],
                                    [235835.0, 6713741.0],
                                    [229006.0, 6716339.0],
                                    [229520.0, 6710085.0],
                                ]
                            ],
                            [
                                [
                                    [212687.0, 6770001.0],
                                    [211559.0, 6762660.0],
                                    [216528.0, 6752538.0],
                                    [224759.0, 6753321.0],
                                    [234540.0, 6747533.0],
                                    [234220.0, 6745025.0],
                                    [240082.0, 6736634.0],
                                    [251238.0, 6736509.0],
                                    [260889.0, 6740570.0],
                                    [266327.0, 6740184.0],
                                    [271833.0, 6736526.0],
                                    [269308.0, 6731426.0],
                                    [263161.0, 6733044.0],
                                    [258643.0, 6731063.0],
                                    [263631.0, 6725691.0],
                                    [274085.0, 6728424.0],
                                    [283689.0, 6728526.0],
                                    [290663.0, 6724762.0],
                                    [288997.0, 6719519.0],
                                    [300067.0, 6720583.0],
                                    [315995.0, 6726944.0],
                                    [317487.0, 6738014.0],
                                    [315562.0, 6748257.0],
                                    [318803.0, 6749864.0],
                                    [322365.0, 6758359.0],
                                    [317839.0, 6765781.0],
                                    [320890.0, 6769878.0],
                                    [317014.0, 6776765.0],
                                    [309516.0, 6779524.0],
                                    [306739.0, 6782705.0],
                                    [310549.0, 6787938.0],
                                    [306966.0, 6794650.0],
                                    [300637.0, 6793781.0],
                                    [298204.0, 6799128.0],
                                    [291749.0, 6798375.0],
                                    [285132.0, 6789099.0],
                                    [280665.0, 6785525.0],
                                    [277875.0, 6787107.0],
                                    [279762.0, 6794931.0],
                                    [270150.0, 6795768.0],
                                    [252150.0, 6805897.0],
                                    [246074.0, 6807146.0],
                                    [242780.0, 6802066.0],
                                    [233945.0, 6800703.0],
                                    [229439.0, 6804532.0],
                                    [212675.0, 6807535.0],
                                    [202658.0, 6804638.0],
                                    [202166.0, 6798131.0],
                                    [205220.0, 6785800.0],
                                    [211608.0, 6786141.0],
                                    [216607.0, 6782805.0],
                                    [223352.0, 6780867.0],
                                    [221788.0, 6771592.0],
                                    [212687.0, 6770001.0],
                                ]
                            ],
                        ],
                    },
                }
            },
        },
    },
    15: {
        "feature_list": copy.deepcopy(feature_list_data_and_geometry),
        "geolayer_name": "data_and_geometries",
        "field_name_filter": "NOM_DEPT",
        "force_field_conversion": True,
        "geometry_type_filter": "Polygon",
        "bbox_filter": (599361, 6868928, 669084, 6903387),
        "bbox_extent": True,
        "crs": None,
        "return_value": {
            "metadata": {
                "name": "data_and_geometries",
                "fields": {"NOM_DEPT": {"type": "String", "width": 10, "index": 0}},
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6867928.0, 670084.0, 6904387.0),
                },
            },
            "features": {
                0: {
                    "attributes": {"NOM_DEPT": "VAL-D'OISE"},
                    "geometry": {
                        "type": "Polygon",
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                        "coordinates": [
                            [
                                [598361.0, 6887345.0],
                                [603102.0, 6887292.0],
                                [606678.0, 6883543.0],
                                [614076.0, 6886919.0],
                                [622312.0, 6880731.0],
                                [628641.0, 6878089.0],
                                [633062.0, 6879807.0],
                                [641836.0, 6872490.0],
                                [641404.0, 6867928.0],
                                [648071.0, 6872567.0],
                                [653619.0, 6875101.0],
                                [660416.0, 6872923.0],
                                [667303.0, 6878971.0],
                                [670084.0, 6886723.0],
                                [659205.0, 6894147.0],
                                [652314.0, 6895981.0],
                                [649761.0, 6898738.0],
                                [645465.0, 6895048.0],
                                [633020.0, 6901508.0],
                                [626847.0, 6897876.0],
                                [618689.0, 6896449.0],
                                [612180.0, 6899061.0],
                                [608283.0, 6898554.0],
                                [605624.0, 6904387.0],
                                [603501.0, 6902160.0],
                                [601892.0, 6893098.0],
                                [598361.0, 6887345.0],
                            ]
                        ],
                    },
                }
            },
        },
    },
    16: {
        "feature_list": copy.deepcopy(feature_list_data_and_geometry),
        "geolayer_name": "data_and_geometries",
        "field_name_filter": None,
        "force_field_conversion": False,
        "geometry_type_filter": None,
        "bbox_filter": None,
        "bbox_extent": False,
        "crs": 2154,
        "serialize": True,
        "return_value": feature_list_data_and_geometry_serialized_geolayer,
    },
    17: {
        "feature_list": copy.deepcopy(feature_list_bytes_attributes),
        "geolayer_name": "bytes_values",
        "field_name_filter": None,
        "force_field_conversion": False,
        "geometry_type_filter": None,
        "bbox_filter": None,
        "bbox_extent": False,
        "crs": None,
        "serialize": False,
        "return_value": geolayer_fields_with_bytes_values,
    },
    18: {
        "feature_list": copy.deepcopy(feature_list_bytes_attributes),
        "geolayer_name": "bytes_values",
        "field_name_filter": None,
        "force_field_conversion": True,
        "geometry_type_filter": None,
        "bbox_filter": None,
        "bbox_extent": False,
        "crs": None,
        "serialize": False,
        "return_value": geolayer_fields_with_bytes_values_forced,
    },
}


split_geolayer_by_geometry_type_parameters = {
    0: {
        "geolayer": geolayer_attributes_only,
        "geometry_type_mapping": {
            "Point": "Point",
            "LineString": "LineString",
            "Polygon": "Polygon",
            "MultiPoint": "MultiPoint",
            "MultiLineString": "MultiLineString",
            "MultiPolygon": "MultiPolygon",
            "GeometryCollection": "GeometryCollection",
        },
        "return_value": (),
    },
    1: {
        "geolayer": geolayer_paris_tokyo,
        "geometry_type_mapping": {
            "Point": "Point",
            "LineString": "LineString",
            "Polygon": "Polygon",
            "MultiPoint": "MultiPoint",
            "MultiLineString": "MultiLineString",
            "MultiPolygon": "MultiPolygon",
            "GeometryCollection": "GeometryCollection",
        },
        "return_value": (geolayer_paris_tokyo,),
    },
    2: {
        "geolayer": feature_list_to_geolayer(
            feature_list=feature_geometry_only_collection,
            geolayer_name="test_geometry_collection",
            bbox_extent=False,
        ),
        "geometry_type_mapping": {
            "Point": "Point",
            "LineString": "LineString",
            "Polygon": "Polygon",
            "MultiPoint": "MultiPoint",
            "MultiLineString": "MultiLineString",
            "MultiPolygon": "MultiPolygon",
            "GeometryCollection": "SPLIT_BY_GEOMETRY_TYPE",
        },
        "return_value": (
            {
                "metadata": {
                    "name": "test_geometry_collection_Point",
                    "geometry_ref": {"type": {"Point"}},
                },
                "features": {
                    0: {"geometry": {"type": "Point", "coordinates": [-115.81, 37.24]}}
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_LineString",
                    "geometry_ref": {"type": {"LineString"}},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "LineString",
                            "coordinates": [[8.919, 44.4074], [8.923, 44.4075]],
                        }
                    }
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_Polygon",
                    "geometry_ref": {"type": {"Polygon"}},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [2.38, 57.322],
                                    [23.194, -20.28],
                                    [-120.43, 19.15],
                                    [2.38, 57.322],
                                ],
                                [
                                    [-5.21, 23.51],
                                    [15.21, -10.81],
                                    [-20.51, 1.51],
                                    [-5.21, 23.51],
                                ],
                            ],
                        }
                    }
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_MultiPoint",
                    "geometry_ref": {"type": {"MultiPoint"}},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "MultiPoint",
                            "coordinates": [
                                [-155.52, 19.61],
                                [-156.22, 20.74],
                                [-157.97, 21.46],
                            ],
                        }
                    }
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_MultiLineString",
                    "geometry_ref": {"type": {"MultiLineString"}},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [[3.75, 9.25], [-130.95, 1.52]],
                                [[23.15, -34.25], [-1.35, -4.65], [3.45, 77.95]],
                            ],
                        }
                    }
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_MultiPolygon",
                    "geometry_ref": {"type": {"MultiPolygon"}},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "MultiPolygon",
                            "coordinates": [
                                [
                                    [
                                        [3.78, 9.28],
                                        [-130.91, 1.52],
                                        [35.12, 72.234],
                                        [3.78, 9.28],
                                    ]
                                ],
                                [
                                    [
                                        [23.18, -34.29],
                                        [-1.31, -4.61],
                                        [3.41, 77.91],
                                        [23.18, -34.29],
                                    ]
                                ],
                            ],
                        }
                    }
                },
            },
        ),
    },
    3: {
        "geolayer": feature_list_to_geolayer(
            feature_list=feature_geometry_only_collection,
            geolayer_name="test_geometry_collection",
            bbox_extent=False,
        ),
        "geometry_type_mapping": {
            "Point": "Point",
            "LineString": "LineString",
            "Polygon": "Polygon",
            "MultiPoint": "MultiPoint",
            "MultiLineString": "MultiLineString",
            "MultiPolygon": "MultiPolygon",
            "GeometryCollection": "SPLIT_BY_GEOMETRY_TYPE",
        },
        "return_value": (
            {
                "metadata": {
                    "name": "test_geometry_collection_Point",
                    "geometry_ref": {"type": {"Point"}},
                },
                "features": {
                    0: {"geometry": {"type": "Point", "coordinates": [-115.81, 37.24]}}
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_LineString",
                    "geometry_ref": {"type": {"LineString"}},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "LineString",
                            "coordinates": [[8.919, 44.4074], [8.923, 44.4075]],
                        }
                    }
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_Polygon",
                    "geometry_ref": {"type": {"Polygon"}},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [2.38, 57.322],
                                    [23.194, -20.28],
                                    [-120.43, 19.15],
                                    [2.38, 57.322],
                                ],
                                [
                                    [-5.21, 23.51],
                                    [15.21, -10.81],
                                    [-20.51, 1.51],
                                    [-5.21, 23.51],
                                ],
                            ],
                        }
                    }
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_MultiPoint",
                    "geometry_ref": {"type": {"MultiPoint"}},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "MultiPoint",
                            "coordinates": [
                                [-155.52, 19.61],
                                [-156.22, 20.74],
                                [-157.97, 21.46],
                            ],
                        }
                    }
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_MultiLineString",
                    "geometry_ref": {"type": {"MultiLineString"}},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [[3.75, 9.25], [-130.95, 1.52]],
                                [[23.15, -34.25], [-1.35, -4.65], [3.45, 77.95]],
                            ],
                        }
                    }
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_MultiPolygon",
                    "geometry_ref": {"type": {"MultiPolygon"}},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "MultiPolygon",
                            "coordinates": [
                                [
                                    [
                                        [3.78, 9.28],
                                        [-130.91, 1.52],
                                        [35.12, 72.234],
                                        [3.78, 9.28],
                                    ]
                                ],
                                [
                                    [
                                        [23.18, -34.29],
                                        [-1.31, -4.61],
                                        [3.41, 77.91],
                                        [23.18, -34.29],
                                    ]
                                ],
                            ],
                        }
                    }
                },
            },
        ),
    },
    4: {
        "geolayer": feature_list_to_geolayer(
            feature_list=feature_geometry_only_collection_empty,
            geolayer_name="test_geometry_collection",
            bbox_extent=False,
        ),
        "geometry_type_mapping": {
            "Point": "Point",
            "LineString": "LineString",
            "Polygon": "Polygon",
            "MultiPoint": "MultiPoint",
            "MultiLineString": "MultiLineString",
            "MultiPolygon": "MultiPolygon",
            "GeometryCollection": "SPLIT_BY_GEOMETRY_TYPE",
        },
        "return_value": (
            {
                "metadata": {
                    "name": "test_geometry_collection_Point",
                    "geometry_ref": {"type": {"Point"}},
                },
                "features": {0: {"geometry": {"type": "Point", "coordinates": []}}},
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_LineString",
                    "geometry_ref": {"type": {"LineString"}},
                },
                "features": {
                    0: {"geometry": {"type": "LineString", "coordinates": []}}
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_Polygon",
                    "geometry_ref": {"type": {"Polygon"}},
                },
                "features": {0: {"geometry": {"type": "Polygon", "coordinates": []}}},
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_MultiPoint",
                    "geometry_ref": {"type": {"MultiPoint"}},
                },
                "features": {
                    0: {"geometry": {"type": "MultiPoint", "coordinates": []}}
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_MultiLineString",
                    "geometry_ref": {"type": {"MultiLineString"}},
                },
                "features": {
                    0: {"geometry": {"type": "MultiLineString", "coordinates": []}}
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_MultiPolygon",
                    "geometry_ref": {"type": {"MultiPolygon"}},
                },
                "features": {
                    0: {"geometry": {"type": "MultiPolygon", "coordinates": []}}
                },
            },
        ),
    },
    5: {
        "geolayer": feature_list_to_geolayer(
            feature_list=feature_geometry_only_collection_empty,
            geolayer_name="test_geometry_collection",
            bbox_extent=False,
        ),
        "geometry_type_mapping": {
            "Point": "Point",
            "LineString": "LineString",
            "Polygon": "Polygon",
            "MultiPoint": "Point",
            "MultiLineString": "LineString",
            "MultiPolygon": "Polygon",
            "GeometryCollection": "SPLIT_BY_GEOMETRY_TYPE",
        },
        "return_value": (
            {
                "metadata": {
                    "name": "test_geometry_collection_Point",
                    "geometry_ref": {"type": {"Point"}},
                },
                "features": {0: {"geometry": {"type": "Point", "coordinates": []}}},
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_LineString",
                    "geometry_ref": {"type": {"LineString"}},
                },
                "features": {
                    0: {"geometry": {"type": "LineString", "coordinates": []}}
                },
            },
            {
                "metadata": {
                    "name": "test_geometry_collection_Polygon",
                    "geometry_ref": {"type": {"Polygon"}},
                },
                "features": {0: {"geometry": {"type": "Polygon", "coordinates": []}}},
            },
        ),
    },
    6: {
        "geolayer": geolayer_geometry_only_all_geometries_type,
        "geometry_type_mapping": {
            "Point": "Point",
            "LineString": "LineString",
            "Polygon": "Polygon",
            "MultiPoint": "MultiPoint",
            "MultiLineString": "LineString",
            "MultiPolygon": "Polygon",
            "GeometryCollection": "SPLIT_BY_GEOMETRY_TYPE",
        },
        "return_value": (
            {
                "metadata": {
                    "name": "all_geometry_type_only_Point",
                    "geometry_ref": {"type": {"Point"}, "crs": 4326},
                },
                "features": {
                    0: {"geometry": {"type": "Point", "coordinates": [-115.81, 37.24]}},
                    1: {"geometry": {"type": "Point", "coordinates": []}},
                    2: {"geometry": {"type": "Point", "coordinates": [-115.81, 37.24]}},
                    3: {"geometry": {"type": "Point", "coordinates": []}},
                    4: {"geometry": {"type": "Point", "coordinates": []}},
                },
            },
            {
                "metadata": {
                    "name": "all_geometry_type_only_LineString",
                    "geometry_ref": {"type": {"LineString"}, "crs": 4326},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "LineString",
                            "coordinates": [[8.919, 44.4074], [8.923, 44.4075]],
                        }
                    },
                    1: {"geometry": {"type": "LineString", "coordinates": []}},
                    2: {
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [[3.75, 9.25], [-130.95, 1.52]],
                                [[23.15, -34.25], [-1.35, -4.65], [3.45, 77.95]],
                            ],
                        }
                    },
                    3: {"geometry": {"type": "MultiLineString", "coordinates": []}},
                    4: {
                        "geometry": {
                            "type": "LineString",
                            "coordinates": [[8.919, 44.4074], [8.923, 44.4075]],
                        }
                    },
                    5: {
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [[3.75, 9.25], [-130.95, 1.52]],
                                [[23.15, -34.25], [-1.35, -4.65], [3.45, 77.95]],
                            ],
                        }
                    },
                    6: {"geometry": {"type": "LineString", "coordinates": []}},
                    7: {
                        "geometry": {
                            "type": "LineString",
                            "coordinates": [[8.919, 44.4074], [8.923, 44.4075]],
                        }
                    },
                    8: {
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [[3.75, 9.25], [-130.95, 1.52]],
                                [[23.15, -34.25], [-1.35, -4.65], [3.45, 77.95]],
                            ],
                        }
                    },
                },
            },
            {
                "metadata": {
                    "name": "all_geometry_type_only_Polygon",
                    "geometry_ref": {"type": {"Polygon"}, "crs": 4326},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [2.38, 57.322],
                                    [23.194, -20.28],
                                    [-120.43, 19.15],
                                    [2.38, 57.322],
                                ],
                                [
                                    [-5.21, 23.51],
                                    [15.21, -10.81],
                                    [-20.51, 1.51],
                                    [-5.21, 23.51],
                                ],
                            ],
                        }
                    },
                    1: {"geometry": {"type": "Polygon", "coordinates": []}},
                    2: {
                        "geometry": {
                            "type": "MultiPolygon",
                            "coordinates": [
                                [
                                    [
                                        [3.78, 9.28],
                                        [-130.91, 1.52],
                                        [35.12, 72.234],
                                        [3.78, 9.28],
                                    ]
                                ],
                                [
                                    [
                                        [23.18, -34.29],
                                        [-1.31, -4.61],
                                        [3.41, 77.91],
                                        [23.18, -34.29],
                                    ]
                                ],
                            ],
                        }
                    },
                    3: {"geometry": {"type": "MultiPolygon", "coordinates": []}},
                    4: {
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [2.38, 57.322],
                                    [23.194, -20.28],
                                    [-120.43, 19.15],
                                    [2.38, 57.322],
                                ],
                                [
                                    [-5.21, 23.51],
                                    [15.21, -10.81],
                                    [-20.51, 1.51],
                                    [-5.21, 23.51],
                                ],
                            ],
                        }
                    },
                    5: {
                        "geometry": {
                            "type": "MultiPolygon",
                            "coordinates": [
                                [
                                    [
                                        [3.78, 9.28],
                                        [-130.91, 1.52],
                                        [35.12, 72.234],
                                        [3.78, 9.28],
                                    ]
                                ],
                                [
                                    [
                                        [23.18, -34.29],
                                        [-1.31, -4.61],
                                        [3.41, 77.91],
                                        [23.18, -34.29],
                                    ]
                                ],
                            ],
                        }
                    },
                    6: {"geometry": {"type": "Polygon", "coordinates": []}},
                    7: {
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [2.38, 57.322],
                                    [23.194, -20.28],
                                    [-120.43, 19.15],
                                    [2.38, 57.322],
                                ],
                                [
                                    [-5.21, 23.51],
                                    [15.21, -10.81],
                                    [-20.51, 1.51],
                                    [-5.21, 23.51],
                                ],
                            ],
                        }
                    },
                    8: {"geometry": {"type": "MultiPolygon", "coordinates": []}},
                },
            },
            {
                "metadata": {
                    "name": "all_geometry_type_only_MultiPoint",
                    "geometry_ref": {"type": {"MultiPoint"}, "crs": 4326},
                },
                "features": {
                    0: {
                        "geometry": {
                            "type": "MultiPoint",
                            "coordinates": [
                                [-155.52, 19.61],
                                [-156.22, 20.74],
                                [-157.97, 21.46],
                            ],
                        }
                    },
                    1: {"geometry": {"type": "MultiPoint", "coordinates": []}},
                    2: {
                        "geometry": {
                            "type": "MultiPoint",
                            "coordinates": [
                                [-155.52, 19.61],
                                [-156.22, 20.74],
                                [-157.97, 21.46],
                            ],
                        }
                    },
                    3: {"geometry": {"type": "MultiPoint", "coordinates": []}},
                    4: {"geometry": {"type": "MultiPoint", "coordinates": []}},
                },
            },
        ),
    },
    7: {
        "geolayer": geolayer_idf_reseau_ferre,
        "geometry_type_mapping": {
            "Point": "Point",
        },
        "return_value": "LineString must be include in geometry_type_mapping"  # geometry_not_in_variable.format(geometry_type="LineString", variable_name="geometry_type_mapping")
    },
    8: {
        "geolayer": feature_list_to_geolayer(
            feature_list=[feature for i_feat, feature in geolayer_geometry_only_all_geometries_type['features'].items()],
            geolayer_name="test_geometry_collection_bbox_extent",
            bbox_extent=True,
        ),
        "geometry_type_mapping": {
            "Point": "Point",
            "LineString": "LineString",
            "Polygon": "Polygon",
            "MultiPoint": "MultiPoint",
            "MultiLineString": "LineString",
            "MultiPolygon": "Polygon",
            "GeometryCollection": "SPLIT_BY_GEOMETRY_TYPE",
        },
        "return_value": ({'metadata': {'name': 'test_geometry_collection_bbox_extent_Point', 'geometry_ref': {'type': {'Point'}}, 'extent': (-115.81, 37.24, -115.81, 37.24)}, 'features': {0: {'geometry': {'type': 'Point', 'coordinates': [-115.81, 37.24], 'bbox': (-115.81, 37.24, -115.81, 37.24)}}, 1: {'geometry': {'type': 'Point', 'coordinates': []}}, 2: {'geometry': {'type': 'Point', 'coordinates': [-115.81, 37.24], 'bbox': (-115.81, 37.24, -115.81, 37.24)}}, 3: {'geometry': {'type': 'Point', 'coordinates': []}}, 4: {'geometry': {'type': 'Point', 'coordinates': []}}}}, {'metadata': {'name': 'test_geometry_collection_bbox_extent_LineString', 'geometry_ref': {'type': {'LineString'}}, 'extent': (-130.95, -34.25, 23.15, 77.95)}, 'features': {0: {'geometry': {'type': 'LineString', 'coordinates': [[8.919, 44.4074], [8.923, 44.4075]], 'bbox': (8.919, 44.4074, 8.923, 44.4075)}}, 1: {'geometry': {'type': 'LineString', 'coordinates': []}}, 2: {'geometry': {'type': 'MultiLineString', 'coordinates': [[[3.75, 9.25], [-130.95, 1.52]], [[23.15, -34.25], [-1.35, -4.65], [3.45, 77.95]]], 'bbox': (-130.95, -34.25, 23.15, 77.95)}}, 3: {'geometry': {'type': 'MultiLineString', 'coordinates': []}}, 4: {'geometry': {'type': 'LineString', 'coordinates': [[8.919, 44.4074], [8.923, 44.4075]], 'bbox': (8.919, 44.4074, 8.923, 44.4075)}}, 5: {'geometry': {'type': 'MultiLineString', 'coordinates': [[[3.75, 9.25], [-130.95, 1.52]], [[23.15, -34.25], [-1.35, -4.65], [3.45, 77.95]]], 'bbox': (-130.95, -34.25, 23.15, 77.95)}}, 6: {'geometry': {'type': 'LineString', 'coordinates': []}}, 7: {'geometry': {'type': 'LineString', 'coordinates': [[8.919, 44.4074], [8.923, 44.4075]], 'bbox': (8.919, 44.4074, 8.923, 44.4075)}}, 8: {'geometry': {'type': 'MultiLineString', 'coordinates': [[[3.75, 9.25], [-130.95, 1.52]], [[23.15, -34.25], [-1.35, -4.65], [3.45, 77.95]]], 'bbox': (-130.95, -34.25, 23.15, 77.95)}}}}, {'metadata': {'name': 'test_geometry_collection_bbox_extent_Polygon', 'geometry_ref': {'type': {'Polygon'}}, 'extent': (-130.91, -34.29, 35.12, 77.91)}, 'features': {0: {'geometry': {'type': 'Polygon', 'coordinates': [[[2.38, 57.322], [23.194, -20.28], [-120.43, 19.15], [2.38, 57.322]], [[-5.21, 23.51], [15.21, -10.81], [-20.51, 1.51], [-5.21, 23.51]]], 'bbox': (-120.43, -20.28, 23.194, 57.322)}}, 1: {'geometry': {'type': 'Polygon', 'coordinates': []}}, 2: {'geometry': {'type': 'MultiPolygon', 'coordinates': [[[[3.78, 9.28], [-130.91, 1.52], [35.12, 72.234], [3.78, 9.28]]], [[[23.18, -34.29], [-1.31, -4.61], [3.41, 77.91], [23.18, -34.29]]]], 'bbox': (-130.91, -34.29, 35.12, 77.91)}}, 3: {'geometry': {'type': 'MultiPolygon', 'coordinates': []}}, 4: {'geometry': {'type': 'Polygon', 'coordinates': [[[2.38, 57.322], [23.194, -20.28], [-120.43, 19.15], [2.38, 57.322]], [[-5.21, 23.51], [15.21, -10.81], [-20.51, 1.51], [-5.21, 23.51]]], 'bbox': (-120.43, -20.28, 23.194, 57.322)}}, 5: {'geometry': {'type': 'MultiPolygon', 'coordinates': [[[[3.78, 9.28], [-130.91, 1.52], [35.12, 72.234], [3.78, 9.28]]], [[[23.18, -34.29], [-1.31, -4.61], [3.41, 77.91], [23.18, -34.29]]]], 'bbox': (-130.91, -34.29, 35.12, 77.91)}}, 6: {'geometry': {'type': 'Polygon', 'coordinates': []}}, 7: {'geometry': {'type': 'Polygon', 'coordinates': [[[2.38, 57.322], [23.194, -20.28], [-120.43, 19.15], [2.38, 57.322]], [[-5.21, 23.51], [15.21, -10.81], [-20.51, 1.51], [-5.21, 23.51]]], 'bbox': (-120.43, -20.28, 23.194, 57.322)}}, 8: {'geometry': {'type': 'MultiPolygon', 'coordinates': []}}}}, {'metadata': {'name': 'test_geometry_collection_bbox_extent_MultiPoint', 'geometry_ref': {'type': {'MultiPoint'}}, 'extent': (-157.97, 19.61, -155.52, 21.46)}, 'features': {0: {'geometry': {'type': 'MultiPoint', 'coordinates': [[-155.52, 19.61], [-156.22, 20.74], [-157.97, 21.46]], 'bbox': (-157.97, 19.61, -155.52, 21.46)}}, 1: {'geometry': {'type': 'MultiPoint', 'coordinates': []}}, 2: {'geometry': {'type': 'MultiPoint', 'coordinates': [[-155.52, 19.61], [-156.22, 20.74], [-157.97, 21.46]], 'bbox': (-157.97, 19.61, -155.52, 21.46)}}, 3: {'geometry': {'type': 'MultiPoint', 'coordinates': []}}, 4: {'geometry': {'type': 'MultiPoint', 'coordinates': []}}}}),
    },
    9: {
        "geolayer": feature_list_data_and_geometry_serialized_geolayer,
        "geometry_type_mapping": {
            "Polygon": "Polygon",
            "MultiPolygon": "MultiPolygon",
        },
        "return_value":({'metadata': {'name': 'data_and_geometries_Polygon', 'fields': {'CODE_DEPT': {'type': 'String', 'width': 2, 'index': 0}, 'NOM_DEPT': {'type': 'String', 'width': 10, 'index': 1}}, 'geometry_ref': {'type': {'Polygon'}, 'crs': 2154}, 'feature_serialize': True}, 'features': {0: {'attributes': "{'CODE_DEPT': '53', 'NOM_DEPT': 'MAYENNE'}", 'geometry': b"\x00\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x000A\x18b\x1c\x00\x00\x00\x00AZ\x0e\xc9@\x00\x00\x00A\x18L\xc8\x00\x00\x00\x00AZ\x06\xa7\xc0\x00\x00\x00A\x18o\x04\x00\x00\x00\x00AY\xfb\x18\xc0\x00\x00\x00A\x18)0\x00\x00\x00\x00AY\xf3\xe2\x00\x00\x00\x00A\x18T\x88\x00\x00\x00\x00AY\xe1S@\x00\x00\x00A\x18qD\x00\x00\x00\x00AY\xde\xf6\x80\x00\x00\x00A\x18m\x14\x00\x00\x00\x00AY\xd6\xf0@\x00\x00\x00A\x18\r\xcc\x00\x00\x00\x00AY\xd6\x9b@\x00\x00\x00A\x17\xcf\xf0\x00\x00\x00\x00AY\xd4H\x80\x00\x00\x00A\x17\x9d\xf4\x00\x00\x00\x00AY\xc9\xd1\x00\x00\x00\x00A\x17_P\x00\x00\x00\x00AY\xc3\xb9\x80\x00\x00\x00A\x17\xcb\xc0\x00\x00\x00\x00AY\xbf\x80\x80\x00\x00\x00A\x17\xfeX\x00\x00\x00\x00AY\xc0'\x80\x00\x00\x00A\x18\x8aL\x00\x00\x00\x00AY\xbd\x89@\x00\x00\x00A\x18\xacl\x00\x00\x00\x00AY\xc1-\x80\x00\x00\x00A\x19,h\x00\x00\x00\x00AY\xbb\xfa\x80\x00\x00\x00A\x19\x9d\\\x00\x00\x00\x00AY\xba\x19\xc0\x00\x00\x00A\x1a6H\x00\x00\x00\x00AY\xb9d\x80\x00\x00\x00A\x1a\xe8|\x00\x00\x00\x00AY\xbc\x16@\x00\x00\x00A\x1bD0\x00\x00\x00\x00AY\xbbX\xc0\x00\x00\x00A\x1b?\xec\x00\x00\x00\x00AY\xc08\x00\x00\x00\x00A\x1a\xfc@\x00\x00\x00\x00AY\xc3R\xc0\x00\x00\x00A\x1bY\xf0\x00\x00\x00\x00AY\xc8C@\x00\x00\x00A\x1bM0\x00\x00\x00\x00AY\xcd\xd1\x00\x00\x00\x00A\x1b\xc6P\x00\x00\x00\x00AY\xd0w\x80\x00\x00\x00A\x1b\x87\xc4\x00\x00\x00\x00AY\xd9\xda@\x00\x00\x00A\x1c\t\xb4\x00\x00\x00\x00AY\xdb=\x80\x00\x00\x00A\x1c\x1d\x1c\x00\x00\x00\x00AY\xe0f\xc0\x00\x00\x00A\x1b\xfa\xa4\x00\x00\x00\x00AY\xe5\xef\xc0\x00\x00\x00A\x1cu\xa0\x00\x00\x00\x00AY\xea\xd4\x00\x00\x00\x00A\x1cfH\x00\x00\x00\x00AY\xf0[\x00\x00\x00\x00A\x1c\x8a\xb0\x00\x00\x00\x00AY\xfb\xc2@\x00\x00\x00A\x1c\xec\x94\x00\x00\x00\x00AY\xfd\xc3\x00\x00\x00\x00A\x1c\xf4h\x00\x00\x00\x00AZ\x05{\xc0\x00\x00\x00A\x1c\x84\xf8\x00\x00\x00\x00AZ\x06G\x80\x00\x00\x00A\x1cr\x9c\x00\x00\x00\x00AZ\x0e\xe5\xc0\x00\x00\x00A\x1cI(\x00\x00\x00\x00AZ\x11\xd3\x00\x00\x00\x00A\x1b\xf3\x00\x00\x00\x00\x00AZ\x0b\xf7@\x00\x00\x00A\x1b\x8a\xe0\x00\x00\x00\x00AZ\n\xb6\xc0\x00\x00\x00A\x1bC|\x00\x00\x00\x00AZ\x0c\xf5\x00\x00\x00\x00A\x1a\xedX\x00\x00\x00\x00AZ\x0c\x8a\x00\x00\x00\x00A\x1a\xb5\x00\x00\x00\x00\x00AZ\t%@\x00\x00\x00A\x1a<\xb0\x00\x00\x00\x00AZ\x06[\x00\x00\x00\x00A\x19\xc4\xd4\x00\x00\x00\x00AZ\x05\xde\x00\x00\x00\x00A\x19SX\x00\x00\x00\x00AZ\rC\x80\x00\x00\x00A\x18\xe5\xf8\x00\x00\x00\x00AZ\x0f@\x00\x00\x00\x00A\x18\xac\xac\x00\x00\x00\x00AZ\x0cr\x80\x00\x00\x00A\x18b\x1c\x00\x00\x00\x00AZ\x0e\xc9@\x00\x00\x00"}, 1: {'attributes': "{'CODE_DEPT': '02', 'NOM_DEPT': 'AISNE'}", 'geometry': b'\x00\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x007A\'\xaf"\x00\x00\x00\x00AZi%\x00\x00\x00\x00A\'\xa9\xd6\x00\x00\x00\x00AZtQ\x00\x00\x00\x00A\'\xbdd\x00\x00\x00\x00AZ{&\xc0\x00\x00\x00A\'\xa3\\\x00\x00\x00\x00AZ\x7f\xcc\x80\x00\x00\x00A\'\xc9\x8e\x00\x00\x00\x00AZ\x81g\xc0\x00\x00\x00A\'\xd8\x96\x00\x00\x00\x00AZ\x86\xce@\x00\x00\x00A(\x1c\xec\x00\x00\x00\x00AZ\x8f\x8a\x80\x00\x00\x00A(\x05\xc8\x00\x00\x00\x00AZ\x92-\xc0\x00\x00\x00A(\x1a\xaa\x00\x00\x00\x00AZ\x9aX@\x00\x00\x00A(\x10\x9c\x00\x00\x00\x00AZ\xa5V\xc0\x00\x00\x00A\'\xdc\xa2\x00\x00\x00\x00AZ\xa7\x84\x80\x00\x00\x00A\'\xbe\x98\x00\x00\x00\x00AZ\xa6l\x80\x00\x00\x00A\'\x82n\x00\x00\x00\x00AZ\xa9,@\x00\x00\x00A\'b:\x00\x00\x00\x00AZ\xac\x80@\x00\x00\x00A&\xfe\xc2\x00\x00\x00\x00AZ\xafS\x00\x00\x00\x00A&\xed*\x00\x00\x00\x00AZ\xb1\x02\x00\x00\x00\x00A&\xb4\x9c\x00\x00\x00\x00AZ\xac.\x00\x00\x00\x00A&\x8d\xe4\x00\x00\x00\x00AZ\xaf:\xc0\x00\x00\x00A&p \x00\x00\x00\x00AZ\xabh\x00\x00\x00\x00A&"\x82\x00\x00\x00\x00AZ\xad4\x00\x00\x00\x00A%\xf9\xc8\x00\x00\x00\x00AZ\xaa\xef@\x00\x00\x00A%\xdd\xec\x00\x00\x00\x00AZ\xac\xad@\x00\x00\x00A%\xbd\x8e\x00\x00\x00\x00AZ\xaa\x91\x00\x00\x00\x00A%\xc8\xd2\x00\x00\x00\x00AZ\xa6\xd0\xc0\x00\x00\x00A%\x9f\x00\x00\x00\x00\x00AZ\x9f\xef\x80\x00\x00\x00A%\x89\x06\x00\x00\x00\x00AZ\x95\xf2@\x00\x00\x00A%\x9f\x84\x00\x00\x00\x00AZ\x89K\x00\x00\x00\x00A%\x93\xf0\x00\x00\x00\x00AZ\x83\xef@\x00\x00\x00A%\xa7 \x00\x00\x00\x00AZw\xa0\x00\x00\x00\x00A%\x92\xf6\x00\x00\x00\x00AZt]@\x00\x00\x00A%\xb7\xc0\x00\x00\x00\x00AZm\xa7\xc0\x00\x00\x00A%\x91\xea\x00\x00\x00\x00AZk\xb5\x80\x00\x00\x00A%\x92\xe2\x00\x00\x00\x00AZe\x8e\x80\x00\x00\x00A%N2\x00\x00\x00\x00AZ]m\xc0\x00\x00\x00A%l\n\x00\x00\x00\x00AZZ\x84@\x00\x00\x00A%\x81@\x00\x00\x00\x00AZQ\x86@\x00\x00\x00A%\xacZ\x00\x00\x00\x00AZM+@\x00\x00\x00A%\x85\xc0\x00\x00\x00\x00AZI[\xc0\x00\x00\x00A%\xbb\x06\x00\x00\x00\x00AZGl\x80\x00\x00\x00A%\xbe\xde\x00\x00\x00\x00AZ>"\xc0\x00\x00\x00A&\x0b"\x00\x00\x00\x00AZ7\x11\x00\x00\x00\x00A&\x19\xe6\x00\x00\x00\x00AZ2\xb9@\x00\x00\x00A&C\xda\x00\x00\x00\x00AZ-\xf7\xc0\x00\x00\x00A&r\xe6\x00\x00\x00\x00AZ,\x9d\x00\x00\x00\x00A&\x8bl\x00\x00\x00\x00AZ3,\x80\x00\x00\x00A&\xb5\x06\x00\x00\x00\x00AZ6\xad\xc0\x00\x00\x00A&\xcd\xec\x00\x00\x00\x00AZA/\x80\x00\x00\x00A&\xb2\xf2\x00\x00\x00\x00AZI\xdc\x00\x00\x00\x00A&\xbfl\x00\x00\x00\x00AZM,\xc0\x00\x00\x00A&\xee\x02\x00\x00\x00\x00AZP\x83\x00\x00\x00\x00A&\xccV\x00\x00\x00\x00AZ_\x02@\x00\x00\x00A\'=\xce\x00\x00\x00\x00AZd\x83\x80\x00\x00\x00A\'i\x10\x00\x00\x00\x00AZi\x18\x00\x00\x00\x00A\'\xa8\x94\x00\x00\x00\x00AZd*\x00\x00\x00\x00A\'\xaf"\x00\x00\x00\x00AZi%\x00\x00\x00\x00'}, 2: {'attributes': '{\'CODE_DEPT\': \'95\', \'NOM_DEPT\': "VAL-D\'OISE"}', 'geometry': b'\x00\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x1bA"B\xb2\x00\x00\x00\x00AZE\xec@\x00\x00\x00A"g\xbc\x00\x00\x00\x00AZE\xdf\x00\x00\x00\x00A"\x83\xac\x00\x00\x00\x00AZB5\xc0\x00\x00\x00A"\xbdx\x00\x00\x00\x00AZE\x81\xc0\x00\x00\x00A"\xfd\xd0\x00\x00\x00\x00AZ?v\xc0\x00\x00\x00A#/B\x00\x00\x00\x00AZ<\xe2@\x00\x00\x00A#Q\xcc\x00\x00\x00\x00AZ>\x8f\xc0\x00\x00\x00A#\x96X\x00\x00\x00\x00AZ7j\x80\x00\x00\x00A#\x92\xf8\x00\x00\x00\x00AZ2\xf6\x00\x00\x00\x00A#\xc7\x0e\x00\x00\x00\x00AZ7}\xc0\x00\x00\x00A#\xf2f\x00\x00\x00\x00AZ9\xf7@\x00\x00\x00A$\'\x80\x00\x00\x00\x00AZ7\xd6\xc0\x00\x00\x00A$]N\x00\x00\x00\x00AZ=\xbe\xc0\x00\x00\x00A$s\x08\x00\x00\x00\x00AZEP\xc0\x00\x00\x00A$\x1e\n\x00\x00\x00\x00AZL\x90\xc0\x00\x00\x00A#\xe84\x00\x00\x00\x00AZN[@\x00\x00\x00A#\xd4B\x00\x00\x00\x00AZQ\x0c\x80\x00\x00\x00A#\xb2\xb2\x00\x00\x00\x00AZMr\x00\x00\x00\x00A#Qx\x00\x00\x00\x00AZS\xc1\x00\x00\x00\x00A#!>\x00\x00\x00\x00AZP5\x00\x00\x00\x00A"\xe1\x82\x00\x00\x00\x00AZN\xd0@\x00\x00\x00A"\xae\xa8\x00\x00\x00\x00AZQ]@\x00\x00\x00A"\x906\x00\x00\x00\x00AZP\xde\x80\x00\x00\x00A"{p\x00\x00\x00\x00AZV\x90\xc0\x00\x00\x00A"j\xda\x00\x00\x00\x00AZTd\x00\x00\x00\x00A"^H\x00\x00\x00\x00AZK\x8a\x80\x00\x00\x00A"B\xb2\x00\x00\x00\x00AZE\xec@\x00\x00\x00'}}}, {'metadata': {'name': 'data_and_geometries_MultiPolygon', 'fields': {'CODE_DEPT': {'type': 'String', 'width': 2, 'index': 0}, 'NOM_DEPT': {'type': 'String', 'width': 10, 'index': 1}}, 'geometry_ref': {'type': {'MultiPolygon'}, 'crs': 2154}, 'feature_serialize': True}, 'features': {0: {'attributes': "{'CODE_DEPT': '56', 'NOM_DEPT': 'MORBIHAN'}", 'geometry': b"\x00\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x06A\x0c\x04\x80\x00\x00\x00\x00AY\x98\xd1@\x00\x00\x00A\rW\xf8\x00\x00\x00\x00AY\x93\x8e\x00\x00\x00\x00A\rQ\x18\x00\x00\x00\x00AY\x97\x0f@\x00\x00\x00A\x0c\xc9\xd8\x00\x00\x00\x00AY\x9cc@\x00\x00\x00A\x0b\xf4p\x00\x00\x00\x00AY\x9e\xec\xc0\x00\x00\x00A\x0c\x04\x80\x00\x00\x00\x00AY\x98\xd1@\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x006A\t\xf6x\x00\x00\x00\x00AY\xd3T@\x00\x00\x00A\t\xd38\x00\x00\x00\x00AY\xcc)\x00\x00\x00\x00A\nn\x80\x00\x00\x00\x00AY\xc2F\x80\x00\x00\x00A\x0bo\xb8\x00\x00\x00\x00AY\xc3\n@\x00\x00\x00A\x0c\xa1`\x00\x00\x00\x00AY\xbdc@\x00\x00\x00A\x0c\x97`\x00\x00\x00\x00AY\xba\xf0@\x00\x00\x00A\rN\x90\x00\x00\x00\x00AY\xb2\xbe\x80\x00\x00\x00A\x0e\xab0\x00\x00\x00\x00AY\xb2\x9f@\x00\x00\x00A\x0f\xd8\xc8\x00\x00\x00\x00AY\xb6\x96\x80\x00\x00\x00A\x10A\\\x00\x00\x00\x00AY\xb66\x00\x00\x00\x00A\x10\x97d\x00\x00\x00\x00AY\xb2\xa3\x80\x00\x00\x00A\x10o\xf0\x00\x00\x00\x00AY\xad\xa8\x80\x00\x00\x00A\x10\x0f\xe4\x00\x00\x00\x00AY\xaf=\x00\x00\x00\x00A\x0f\x92\x98\x00\x00\x00\x00AY\xadM\xc0\x00\x00\x00A\x10\x17<\x00\x00\x00\x00AY\xa8\x0e\xc0\x00\x00\x00A\x10\xba\x94\x00\x00\x00\x00AY\xaa\xba\x00\x00\x00\x00A\x11P\xa4\x00\x00\x00\x00AY\xaa\xd3\x80\x00\x00\x00A\x11\xbd\x9c\x00\x00\x00\x00AY\xa7&\x80\x00\x00\x00A\x11\xa3\x94\x00\x00\x00\x00AY\xa2\x07\xc0\x00\x00\x00A\x12P\x8c\x00\x00\x00\x00AY\xa3\x11\xc0\x00\x00\x00A\x13Il\x00\x00\x00\x00AY\xa9H\x00\x00\x00\x00A\x13`\xbc\x00\x00\x00\x00AY\xb4\x17\x80\x00\x00\x00A\x13B\xa8\x00\x00\x00\x00AY\xbe\x18@\x00\x00\x00A\x13uL\x00\x00\x00\x00AY\xbf\xaa\x00\x00\x00\x00A\x13\xac\xf4\x00\x00\x00\x00AY\xc7\xf5\xc0\x00\x00\x00A\x13f<\x00\x00\x00\x00AY\xcf5@\x00\x00\x00A\x13\x95\xe8\x00\x00\x00\x00AY\xd35\x80\x00\x00\x00A\x13YX\x00\x00\x00\x00AY\xd9\xef@\x00\x00\x00A\x12\xe40\x00\x00\x00\x00AY\xdc\xa1\x00\x00\x00\x00A\x12\xb8\xcc\x00\x00\x00\x00AY\xdf\xbc@\x00\x00\x00A\x12\xf4T\x00\x00\x00\x00AY\xe4\xd8\x80\x00\x00\x00A\x12\xbcX\x00\x00\x00\x00AY\xebf\x80\x00\x00\x00A\x12Yt\x00\x00\x00\x00AY\xea\x8d@\x00\x00\x00A\x123p\x00\x00\x00\x00AY\xef\xc6\x00\x00\x00\x00A\x11\xce\x94\x00\x00\x00\x00AY\xef\t\xc0\x00\x00\x00A\x11g0\x00\x00\x00\x00AY\xe5\xfa\xc0\x00\x00\x00A\x11!d\x00\x00\x00\x00AY\xe2}@\x00\x00\x00A\x10\xf5\xcc\x00\x00\x00\x00AY\xe4\x08\xc0\x00\x00\x00A\x11\x13H\x00\x00\x00\x00AY\xeb\xac\xc0\x00\x00\x00A\x10}\x18\x00\x00\x00\x00AY\xec~\x00\x00\x00\x00A\x0e\xc7\xb0\x00\x00\x00\x00AY\xf6b@\x00\x00\x00A\x0e\t\xd0\x00\x00\x00\x00AY\xf7\x9a\x80\x00\x00\x00A\r\xa2\xe0\x00\x00\x00\x00AY\xf2\xa4\x80\x00\x00\x00A\x0c\x8e\xc8\x00\x00\x00\x00AY\xf1O\xc0\x00\x00\x00A\x0c\x01\xf8\x00\x00\x00\x00AY\xf5\r\x00\x00\x00\x00A\t\xf6\x18\x00\x00\x00\x00AY\xf7\xfb\xc0\x00\x00\x00A\x08\xbd\x10\x00\x00\x00\x00AY\xf5'\x80\x00\x00\x00A\x08\xad\xb0\x00\x00\x00\x00AY\xee\xcc\xc0\x00\x00\x00A\t\r \x00\x00\x00\x00AY\xe2\xc2\x00\x00\x00\x00A\t\xd4\xc0\x00\x00\x00\x00AY\xe3\x17@\x00\x00\x00A\np\xf8\x00\x00\x00\x00AY\xdf\xd5@\x00\x00\x00A\x0bC\xc0\x00\x00\x00\x00AY\xdd\xf0\xc0\x00\x00\x00A\x0b\x12\xe0\x00\x00\x00\x00AY\xd4\xe2\x00\x00\x00\x00A\t\xf6x\x00\x00\x00\x00AY\xd3T@\x00\x00\x00"}}})
    },
}


def test_all():

    # delete feature
    print(test_function(delete_feature, delete_feature_parameters))

    # drop_field
    print(test_function(drop_field, drop_field_parameters))

    # rename_field
    print(test_function(rename_field, rename_field_parameters))

    # create field
    print(test_function(create_field, create_field_parameters))

    # add_attributes_index
    print(test_function(add_attributes_index, add_attributes_index_parameters))

    # check_attributes_index
    print(test_function(check_attributes_index, check_attributes_index_parameters))

    # delete_attributes_index
    print(test_function(delete_attributes_index, delete_attributes_index_parameters))

    # check_if_field_exists
    print(test_function(check_if_field_exists, check_if_field_exists_parameters))

    # feature_list_to_geolayer
    print(test_function(feature_list_to_geolayer, feature_list_to_geolayer_parameters))

    # split_geolayer_by_geometry_type
    print(
        test_function(
            split_geolayer_by_geometry_type, split_geolayer_by_geometry_type_parameters
        )
    )


if __name__ == "__main__":
    test_all()