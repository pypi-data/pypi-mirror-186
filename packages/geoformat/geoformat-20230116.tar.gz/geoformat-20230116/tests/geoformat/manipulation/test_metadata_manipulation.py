import copy

from geoformat.conf.error_messages import (
    field_missing,
    field_exists,
    field_type_not_valid,
    field_width_not_valid,
    field_precision_not_valid,
    variable_must_be_int,
    field_name_still_indexing,
    field_name_not_indexing,
)
from tests.data.index import geolayer_fr_dept_population_CODE_DEPT_hash_index
from geoformat.conf.fields_variable import field_type_set
from geoformat.manipulation.metadata_manipulation import (
    drop_field_in_metadata,
    drop_field_that_not_exists_in_metadata,
    reorder_metadata_field_index_after_field_drop,
    rename_field_in_metadata,
    create_field_in_metadata,
    check_if_field_exists_in_metadata,
    add_attributes_index_in_metadata,
    check_attributes_index_in_metadata,
    delete_attributes_index_in_metadata,
)
from tests.utils.tests_utils import test_function

from tests.data.metadata import (
    metadata_attributes_to_force_in_str,
    metadata_attributes_only,
    metadata_fr_dept_geometry_only,
    metadata_fr_dept_population,
    metadata_geometry_only_all_geometries_type,
)

reorder_metadata_field_index_after_field_drop_parameters = {
    0: {
        "fields_metadata": {"NOM_DEPT": {"type": "String", "width": 10, "index": 1}},
        "reorder_field_index": 0,
        "return_value": {"NOM_DEPT": {"type": "String", "width": 10, "index": 0}},
    },
    1: {
        "fields_metadata": {"CODE_DEPT": {"type": "String", "width": 2, "index": 0}},
        "reorder_field_index": 1,
        "return_value": {"CODE_DEPT": {"type": "String", "width": 2, "index": 0}},
    },
    2: {
        "fields_metadata": {
            "field_integer": {"type": "Integer", "index": 0},
            "field_integer_list": {"type": "IntegerList", "index": 1},
            "field_real": {"type": "Real", "width": 6, "precision": 0, "index": 2},
            "field_real_list": {
                "type": "RealList",
                "width": 10,
                "precision": 5,
                "index": 3,
            },
            "field_date": {"type": "Date", "index": 6},
            "field_time": {"type": "Time", "index": 7},
            "field_datetime": {"type": "DateTime", "index": 8},
            "field_binary": {"type": "Binary", "index": 9},
            "field_boolean": {"type": "Boolean", "index": 10},
        },
        "reorder_field_index": [4, 5],
        "return_value": {
            "field_integer": {"type": "Integer", "index": 0},
            "field_integer_list": {"type": "IntegerList", "index": 1},
            "field_real": {"type": "Real", "width": 6, "precision": 0, "index": 2},
            "field_real_list": {
                "type": "RealList",
                "width": 10,
                "precision": 5,
                "index": 3,
            },
            "field_date": {"type": "Date", "index": 4},
            "field_time": {"type": "Time", "index": 5},
            "field_datetime": {"type": "DateTime", "index": 6},
            "field_binary": {"type": "Binary", "index": 7},
            "field_boolean": {"type": "Boolean", "index": 8},
        },
    },
    3: {
        "fields_metadata": {
            "field_real": {"type": "Real", "width": 6, "precision": 0, "index": 2},
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
        },
        "reorder_field_index": [0, 1],
        "return_value": {
            "field_real": {"type": "Real", "width": 6, "precision": 0, "index": 0},
            "field_real_list": {
                "type": "RealList",
                "width": 10,
                "precision": 5,
                "index": 1,
            },
            "field_string": {"type": "String", "width": 5, "index": 2},
            "field_string_list": {"type": "StringList", "width": 8, "index": 3},
            "field_date": {"type": "Date", "index": 4},
            "field_time": {"type": "Time", "index": 5},
            "field_datetime": {"type": "DateTime", "index": 6},
            "field_binary": {"type": "Binary", "index": 7},
            "field_boolean": {"type": "Boolean", "index": 8},
        },
    },
    4: {
        "fields_metadata": {
            "field_integer": {"type": "Integer", "index": 0},
            "field_integer_list": {"type": "IntegerList", "index": 1},
            "field_real": {"type": "Real", "width": 6, "precision": 0, "index": 2},
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
        },
        "reorder_field_index": [8, 9, 10],
        "return_value": {
            "field_integer": {"type": "Integer", "index": 0},
            "field_integer_list": {"type": "IntegerList", "index": 1},
            "field_real": {"type": "Real", "width": 6, "precision": 0, "index": 2},
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
        },
    },
}

drop_field_in_metadata_parameters = {
    0: {
        "metadata": metadata_attributes_to_force_in_str,
        "field_name_or_field_name_list": "field_integer",
        "return_value": {
            "name": "attributes_to_force_only_forced",
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
    },
    1: {
        "metadata": metadata_attributes_to_force_in_str,
        "field_name_or_field_name_list": "field_datetime",
        "return_value": {
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
            },
        },
    },
    2: {
        "metadata": metadata_attributes_to_force_in_str,
        "field_name_or_field_name_list": "field_string",
        "return_value": {
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
                "field_date": {"type": "Date", "index": 4},
                "field_time": {"type": "String", "width": 15, "index": 5},
                "field_binary": {"type": "String", "width": 201, "index": 6},
                "field_boolean": {"type": "String", "width": 5, "index": 7},
                "field_string_list": {"type": "String", "width": 16, "index": 8},
                "field_datetime": {"type": "DateTime", "index": 9},
            },
        },
    },
    3: {
        "metadata": metadata_attributes_to_force_in_str,
        "field_name_or_field_name_list": [
            "field_datetime",
            "field_string",
            "field_integer",
        ],
        "return_value": {
            "name": "attributes_to_force_only_forced",
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
    },
    4: {
        "metadata": metadata_attributes_to_force_in_str,
        "field_name_or_field_name_list": [
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
        "return_value": {"name": "attributes_to_force_only_forced"},
    },
}

drop_field_that_not_exists_in_metadata_parameters = {
    0: {
        "metadata": copy.deepcopy(metadata_attributes_to_force_in_str),
        "not_deleting_field_name_or_field_name_list": [
            "field_integer_list",
            "field_real",
            "field_real_list",
            "field_string",
            "field_date",
            "field_time",
            "field_binary",
            "field_boolean",
            "field_string_list",
            "field_datetime",
        ],
        "return_value": {
            "name": "attributes_to_force_only_forced",
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
    },
    1: {
        "metadata": copy.deepcopy(metadata_attributes_to_force_in_str),
        "not_deleting_field_name_or_field_name_list": [
            "field_integer",
            "field_integer_list",
            "field_real",
            "field_real_list",
            "field_string",
            "field_date",
            "field_time",
            "field_binary",
            "field_boolean",
            "field_string_list",
        ],
        "return_value": {
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
            },
        },
    },
    2: {
        "metadata": copy.deepcopy(metadata_attributes_to_force_in_str),
        "not_deleting_field_name_or_field_name_list": [
            "field_integer",
            "field_integer_list",
            "field_real",
            "field_real_list",
            "field_date",
            "field_time",
            "field_binary",
            "field_boolean",
            "field_string_list",
            "field_datetime",
        ],
        "return_value": {
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
                "field_date": {"type": "Date", "index": 4},
                "field_time": {"type": "String", "width": 15, "index": 5},
                "field_binary": {"type": "String", "width": 201, "index": 6},
                "field_boolean": {"type": "String", "width": 5, "index": 7},
                "field_string_list": {"type": "String", "width": 16, "index": 8},
                "field_datetime": {"type": "DateTime", "index": 9},
            },
        },
    },
    3: {
        "metadata": metadata_attributes_to_force_in_str,
        "not_deleting_field_name_or_field_name_list": [
            "field_integer_list",
            "field_real",
            "field_real_list",
            "field_date",
            "field_time",
            "field_binary",
            "field_boolean",
            "field_string_list",
        ],
        "return_value": {
            "name": "attributes_to_force_only_forced",
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
    },
    4: {
        "metadata": copy.deepcopy(metadata_attributes_to_force_in_str),
        "not_deleting_field_name_or_field_name_list": [],
        "return_value": {"name": "attributes_to_force_only_forced"},
    },
    5: {
        "metadata": {'name': 'geolayer_dpt_2_with_geom', 'fields': {'CODE_DEPT': {'type': 'String', 'width': 2, 'index': 0}, 'NOM_DEPT': {'type': 'String', 'width': 10, 'index': 1}}, 'geometry_ref': {'type': {'Polygon'}, 'extent': (598361.0, 6861428.0, 790134.0, 6997000.0)}},
        "not_deleting_field_name_or_field_name_list": ['CODE_DEPT', 'NOM_DEPT'],
        "return_value": {'name': 'geolayer_dpt_2_with_geom', 'fields': {'CODE_DEPT': {'type': 'String', 'width': 2, 'index': 0}, 'NOM_DEPT': {'type': 'String', 'width': 10, 'index': 1}}, 'geometry_ref': {'type': {'Polygon'}, 'extent': (598361.0, 6861428.0, 790134.0, 6997000.0)}},
    },

}

rename_field_in_metadata_parameters = {
    0: {
        "metadata": metadata_attributes_only,
        "old_field_name": "field_string",
        "new_field_name": "string",
        "return_value": {
            "name": "attributes_only",
            "fields": {
                "field_integer": {"type": "Integer", "index": 0},
                "field_integer_list": {"type": "IntegerList", "index": 1},
                "field_real": {"type": "Real", "width": 9, "precision": 5, "index": 2},
                "field_real_list": {
                    "type": "RealList",
                    "width": 10,
                    "precision": 5,
                    "index": 3,
                },
                "field_string_list": {"type": "StringList", "width": 8, "index": 5},
                "field_date": {"type": "Date", "index": 6},
                "field_time": {"type": "Time", "index": 7},
                "field_datetime": {"type": "DateTime", "index": 8},
                "field_binary": {"type": "Binary", "index": 9},
                "field_boolean": {"type": "Boolean", "index": 10},
                "string": {"type": "String", "width": 5, "index": 4},
            },
        },
    },
    1: {
        "metadata": metadata_attributes_only,
        "old_field_name": "field_foo",
        "new_field_name": "string",
        "return_value": field_missing.format(field_name="field_foo"),
    },
    2: {
        "metadata": metadata_attributes_only,
        "old_field_name": "field_binary",
        "new_field_name": "field_string",
        "return_value": field_exists.format(field_name="field_string"),
    },
}

create_field_in_metadata_parameters = {
    0: {
        "metadata": metadata_attributes_to_force_in_str,
        "field_name": "field_string",
        "field_type": "int",
        "field_width": None,
        "field_precision": None,
        "return_value": field_exists.format(field_name="field_string"),
    },
    1: {
        "metadata": metadata_attributes_to_force_in_str,
        "field_name": "foo",
        "field_type": "int",
        "field_width": None,
        "field_precision": None,
        "return_value": field_type_not_valid.format(
            field_type="int", field_type_list=str(sorted(list(field_type_set)))
        ),
    },
    2: {
        "metadata": metadata_attributes_to_force_in_str,
        "field_name": "foo",
        "field_type": "Real",
        "field_width": None,
        "field_precision": None,
        "return_value": field_width_not_valid.format(field_name="foo"),
    },
    3: {
        "metadata": metadata_attributes_to_force_in_str,
        "field_name": "foo",
        "field_type": "Real",
        "field_width": "bar",
        "field_precision": None,
        "return_value": variable_must_be_int.format(variable_name="field_width"),
    },
    4: {
        "metadata": metadata_attributes_to_force_in_str,
        "field_name": "foo",
        "field_type": "Real",
        "field_width": 5,
        "field_precision": None,
        "return_value": field_precision_not_valid.format(field_name="foo"),
    },
    5: {
        "metadata": metadata_attributes_to_force_in_str,
        "field_name": "foo",
        "field_type": "Real",
        "field_width": 5,
        "field_precision": "deux",
        "return_value": variable_must_be_int.format(variable_name="field_precision"),
    },
    6: {
        "metadata": copy.deepcopy(metadata_attributes_to_force_in_str),
        "field_name": "foo",
        "field_type": "Integer",
        "field_width": None,
        "field_precision": None,
        "return_value": {
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
                "foo": {"type": "Integer", "index": 11},
            },
        },
    },
    7: {
        "metadata": copy.deepcopy(metadata_attributes_to_force_in_str),
        "field_name": "foo",
        "field_type": "Integer",
        "field_width": 10,
        "field_precision": 2,
        "return_value": {
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
                "foo": {"type": "Integer", "index": 11},
            },
        },
    },
    8: {
        "metadata": copy.deepcopy(metadata_fr_dept_geometry_only),
        "field_name": "foo",
        "field_type": "Integer",
        "field_width": 10,
        "field_precision": 2,
        "return_value": {
            "name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_GEOMETRY_ONLY",
            "geometry_ref": {
                "type": {"Polygon", "MultiPolygon"},
                "extent": (124277.0, 6050136.0, 1242213.0, 7110430.0),
                "crs": 2154,
            },
            "fields": {"foo": {"type": "Integer", "index": 0}},
        },
    },
}

add_attributes_index_in_metadata_parameters = {
    0: {
        "metadata": copy.deepcopy(metadata_fr_dept_population),
        "field_name": "CODE_DEPT",
        "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
        "return_value": {
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
    },
    1: {
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
        "field_name": "CODE_DEPT",
        "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
        "return_value": field_name_still_indexing.format(field_name="CODE_DEPT"),
    },
    2: {
        "metadata": metadata_fr_dept_population,
        "field_name": "CODE",
        "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
        "return_value": field_missing.format(field_name="CODE"),
    },
    3: {
        "metadata": metadata_geometry_only_all_geometries_type,
        "field_name": "CODE_DEPT",
        "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
        "return_value": field_missing.format(field_name="CODE_DEPT"),
    },
}

check_if_field_exists_in_metadata_parameters = {
    0: {
        "metadata": metadata_attributes_only,
        "field_name": "field_integer",
        "return_value": True,
    },
    1: {
        "metadata": metadata_attributes_only,
        "field_name": "foo",
        "return_value": False,
    },
    2: {
        "metadata": metadata_fr_dept_geometry_only,
        "field_name": "bar",
        "return_value": False,
    },
}

check_attributes_index_in_metadata_parameters = {
    0: {
        "metadata": metadata_fr_dept_population,
        "field_name": "CODE_DEPT",
        "type": "hashtable",
        "return_value": False,
    },
    1: {
        "metadata": add_attributes_index_in_metadata(
            **{
                "metadata": copy.deepcopy(metadata_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "CODE_DEPT",
        "type": "hashtable",
        "return_value": True,
    },
    2: {
        "metadata": add_attributes_index_in_metadata(
            **{
                "metadata": copy.deepcopy(metadata_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "CODE_DEPT",
        "type": "btree",
        "return_value": False,
    },
    3: {
        "metadata": add_attributes_index_in_metadata(
            **{
                "metadata": copy.deepcopy(metadata_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "FOO",
        "type": "hashtable",
        "return_value": field_missing.format(field_name="FOO"),
    },
    4: {
        "metadata": metadata_geometry_only_all_geometries_type,
        "field_name": "FOO",
        "type": "hashtable",
        "return_value": field_missing.format(field_name="FOO"),
    },
}

delete_attributes_index_in_metadata_parameters = {
    0: {
        "metadata": metadata_fr_dept_population,
        "field_name": "CODE_DEPT",
        "type": None,
        "return_value": field_name_not_indexing.format(field_name="CODE_DEPT"),
    },
    1: {
        "metadata": add_attributes_index_in_metadata(
            **{
                "metadata": copy.deepcopy(metadata_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "CODE_DEPT",
        "type": None,
        "return_value": metadata_fr_dept_population,
    },
    2: {
        "metadata": add_attributes_index_in_metadata(
            **{
                "metadata": copy.deepcopy(metadata_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "CODE_DEPT",
        "type": "btree",
        "return_value": field_name_not_indexing.format(field_name="CODE_DEPT"),
    },
}


def test_all():
    # drop_field_in_metadata
    print(test_function(drop_field_in_metadata, drop_field_in_metadata_parameters))

    # drop_field_that_not_exists_in_metadata
    print(
        test_function(
            drop_field_that_not_exists_in_metadata,
            drop_field_that_not_exists_in_metadata_parameters,
        )
    )

    # reorder_metadata_field_index_after_field_drop
    print(
        test_function(
            reorder_metadata_field_index_after_field_drop,
            reorder_metadata_field_index_after_field_drop_parameters,
        )
    )

    # rename_field_in_metadata_parameters
    print(test_function(rename_field_in_metadata, rename_field_in_metadata_parameters))

    # create_field_in_metadata
    print(test_function(create_field_in_metadata, create_field_in_metadata_parameters))

    # check_if_field_exists
    print(
        test_function(
            check_if_field_exists_in_metadata,
            check_if_field_exists_in_metadata_parameters,
        )
    )

    # add_attributes_index_in_metadata
    print(
        test_function(
            add_attributes_index_in_metadata,
            add_attributes_index_in_metadata_parameters,
        )
    )

    # check_attributes_index_in_metadata
    print(
        test_function(
            check_attributes_index_in_metadata,
            check_attributes_index_in_metadata_parameters,
        )
    )

    # delete_attributes_index_in_metadata
    print(
        test_function(
            delete_attributes_index_in_metadata,
            delete_attributes_index_in_metadata_parameters,
        )
    )


if __name__ == "__main__":
    test_all()
