import shutil
from tests.utils.tests_utils import test_function
from geoformat.driver.csv_driver import (
    csv_to_geolayer,
    geoformat_feature_to_csv_feature,
    feature_attributes_to_csv_attributes,
    geolayer_to_csv,
)
from pathlib import Path

from tests.data.geolayers import (
    geolayer_attributes_only,
    geolayer_attributes_only_without_none_value,
    geolayer_attributes_to_force_only_forced,
    geolayer_fr_dept_data_only,
    geolayer_fr_dept_geometry_only,
    geolayer_fr_dept_data_and_geometry,
    geolayer_paris_velib,
    geolayer_paris_velib_str,
    geolayer_paris_velib_str_no_header,
)
from tests.data.features import (
    feature_attributes_only,
    feature_dpt_geometry_only_a,
    feature_dpt_data_and_geometry_a,
)


# declare path
file_path_base = Path(__file__).parent.parent.parent.parent.joinpath

geolayer_attributes_only_path = file_path_base(
    "tests/geoformat/driver/test/attributes_only.csv"
)

geolayer_attributes_to_force_only_forced_path = file_path_base(
    "tests/geoformat/driver/test/attributes_to_force_only_forced.csv"
)
geolayer_fr_dept_data_only_path = file_path_base(
    "tests/geoformat/driver/test/fr_dept_data_only.csv"
)
geolayer_fr_dept_geometry_only_path = file_path_base(
    "tests/geoformat/driver/test/fr_dept_geometry_only.csv"
)
geolayer_fr_dept_data_and_geometry_path = file_path_base(
    "tests/geoformat/driver/test/fr_dept_data_and_geometry.csv"
)
geolayer_paris_velib_path = file_path_base(
    "tests/geoformat/driver/test/paris_velib.csv"
)
geolayer_paris_velib_str_path = file_path_base(
    "tests/geoformat/driver/test/paris_velib_str.csv"
)
paris_velib_str_no_header_path = file_path_base(
    "tests/geoformat/driver/test/paris_velib_str_no_header.csv"
)

geoformat_feature_to_csv_feature_parameters = {
    0: {
        "feature": feature_attributes_only,
        "recast_field_mapping": {
            "field_integer": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_integer_list": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_real": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_real_list": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_string_list": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_date": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_time": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_datetime": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_binary": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_boolean": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
        },
        "string_field_name": ["field_string"],
        "null_string": None,
        "quote_character": "",
        "write_geometry": False,
        "geometry_format": None,
        "return_value": {
            "attributes": {
                "field_integer": "586",
                "field_integer_list": "[5879, 8557]",
                "field_real": "8789.97568",
                "field_real_list": "[89798.3654, 8757.97568]",
                "field_string": "salut",
                "field_string_list": "['bonjour', 'monsieur']",
                "field_none": None,
                "field_date": "2020-03-31",
                "field_time": "11:22:10.000999",
                "field_datetime": "2020-03-31 11:22:10.000999",
                "field_binary": "00000000040000000200000000010000000000000000000000000000000000000000013ff00000000000003ff0000000000000",
                "field_boolean": "True",
            },
            "geometry": {},
        },
    },
    1: {
        "feature": feature_attributes_only,
        "recast_field_mapping": {
            "field_integer": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_integer_list": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_real": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_real_list": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_string_list": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_date": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_time": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_datetime": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_binary": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_boolean": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
        },
        "string_field_name": ["field_string"],
        "null_string": "",
        "quote_character": "",
        "write_geometry": False,
        "geometry_format": None,
        "return_value": {
            "attributes": {
                "field_integer": "586",
                "field_integer_list": "[5879, 8557]",
                "field_real": "8789.97568",
                "field_real_list": "[89798.3654, 8757.97568]",
                "field_string": "salut",
                "field_string_list": "['bonjour', 'monsieur']",
                "field_none": "",
                "field_date": "2020-03-31",
                "field_time": "11:22:10.000999",
                "field_datetime": "2020-03-31 11:22:10.000999",
                "field_binary": "00000000040000000200000000010000000000000000000000000000000000000000013ff00000000000003ff0000000000000",
                "field_boolean": "True",
            },
            "geometry": {},
        },
    },
    2: {
        "feature": feature_attributes_only,
        "recast_field_mapping": {
            "field_integer": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_integer_list": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_real": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_real_list": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_string_list": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_date": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_time": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_datetime": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_binary": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_boolean": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
        },
        "string_field_name": ["field_string"],
        "null_string": "",
        "quote_character": '"',
        "write_geometry": False,
        "geometry_format": None,
        "return_value": {
            "attributes": {
                "field_integer": "586",
                "field_integer_list": "[5879, 8557]",
                "field_real": "8789.97568",
                "field_real_list": "[89798.3654, 8757.97568]",
                "field_string": '"salut"',
                "field_string_list": "['bonjour', 'monsieur']",
                "field_none": "",
                "field_date": "2020-03-31",
                "field_time": "11:22:10.000999",
                "field_datetime": "2020-03-31 11:22:10.000999",
                "field_binary": "00000000040000000200000000010000000000000000000000000000000000000000013ff00000000000003ff0000000000000",
                "field_boolean": "True",
            },
            "geometry": {},
        },
    },
    3: {
        "feature": feature_dpt_geometry_only_a,
        "recast_field_mapping": {},
        "string_field_name": [],
        "null_string": "",
        "quote_character": '"',
        "write_geometry": True,
        "geometry_format": "WKT",
        "return_value": {
            "attributes": {},
            "geometry": "POLYGON ((399495.0 6830885.0,398130.0 6822559.0,400321.0 6810723.0,395852.0 6803336.0,398626.0 6784333.0,400465.0 6781914.0,400197.0 6773697.0,394099.0 6773357.0,390140.0 6770978.0,386941.0 6760260.0,382932.0 6754022.0,389872.0 6749698.0,393110.0 6750366.0,402067.0 6747685.0,404251.0 6751414.0,412442.0 6746090.0,419671.0 6744167.0,429458.0 6743442.0,440863.0 6746201.0,446732.0 6745443.0,446459.0 6750432.0,442128.0 6753611.0,448124.0 6758669.0,447308.0 6764356.0,455060.0 6767070.0,451057.0 6776681.0,459373.0 6778102.0,460615.0 6783387.0,458409.0 6789055.0,466280.0 6794064.0,465298.0 6799724.0,467628.0 6811401.0,473893.0 6813452.0,474394.0 6821359.0,467262.0 6822174.0,466087.0 6830999.0,463434.0 6833996.0,457920.0 6827997.0,451256.0 6826715.0,446687.0 6829012.0,441174.0 6828584.0,437568.0 6825109.0,429868.0 6822252.0,422197.0 6821752.0,414934.0 6829326.0,407934.0 6831360.0,404267.0 6828490.0,399495.0 6830885.0))",
        },
    },
    4: {
        "feature": feature_dpt_geometry_only_a,
        "recast_field_mapping": {},
        "string_field_name": [],
        "null_string": "",
        "quote_character": '"',
        "write_geometry": True,
        "geometry_format": "WKB",
        "return_value": {
            "attributes": {},
            "geometry": "000000000300000001000000304118621c00000000415a0ec94000000041184cc800000000415a06a7c000000041186f04000000004159fb18c000000041182930000000004159f3e20000000041185488000000004159e1534000000041187144000000004159def68000000041186d14000000004159d6f04000000041180dcc000000004159d69b400000004117cff0000000004159d4488000000041179df4000000004159c9d10000000041175f50000000004159c3b9800000004117cbc0000000004159bf80800000004117fe58000000004159c0278000000041188a4c000000004159bd89400000004118ac6c000000004159c12d8000000041192c68000000004159bbfa8000000041199d5c000000004159ba19c0000000411a3648000000004159b96480000000411ae87c000000004159bc1640000000411b4430000000004159bb58c0000000411b3fec000000004159c03800000000411afc40000000004159c352c0000000411b59f0000000004159c84340000000411b4d30000000004159cdd100000000411bc650000000004159d07780000000411b87c4000000004159d9da40000000411c09b4000000004159db3d80000000411c1d1c000000004159e066c0000000411bfaa4000000004159e5efc0000000411c75a0000000004159ead400000000411c6648000000004159f05b00000000411c8ab0000000004159fbc240000000411cec94000000004159fdc300000000411cf46800000000415a057bc0000000411c84f800000000415a064780000000411c729c00000000415a0ee5c0000000411c492800000000415a11d300000000411bf30000000000415a0bf740000000411b8ae000000000415a0ab6c0000000411b437c00000000415a0cf500000000411aed5800000000415a0c8a00000000411ab50000000000415a092540000000411a3cb000000000415a065b000000004119c4d400000000415a05de000000004119535800000000415a0d43800000004118e5f800000000415a0f40000000004118acac00000000415a0c72800000004118621c00000000415a0ec940000000",
        },
    },
    5: {
        "feature": feature_dpt_geometry_only_a,
        "recast_field_mapping": {},
        "string_field_name": [],
        "null_string": "",
        "quote_character": '"',
        "write_geometry": True,
        "geometry_format": "GEOJSON",
        "return_value": {
            "attributes": {},
            "geometry": '{"type": "Polygon", "coordinates": [[[399495.0, 6830885.0], [398130.0, 6822559.0], [400321.0, 6810723.0], [395852.0, 6803336.0], [398626.0, 6784333.0], [400465.0, 6781914.0], [400197.0, 6773697.0], [394099.0, 6773357.0], [390140.0, 6770978.0], [386941.0, 6760260.0], [382932.0, 6754022.0], [389872.0, 6749698.0], [393110.0, 6750366.0], [402067.0, 6747685.0], [404251.0, 6751414.0], [412442.0, 6746090.0], [419671.0, 6744167.0], [429458.0, 6743442.0], [440863.0, 6746201.0], [446732.0, 6745443.0], [446459.0, 6750432.0], [442128.0, 6753611.0], [448124.0, 6758669.0], [447308.0, 6764356.0], [455060.0, 6767070.0], [451057.0, 6776681.0], [459373.0, 6778102.0], [460615.0, 6783387.0], [458409.0, 6789055.0], [466280.0, 6794064.0], [465298.0, 6799724.0], [467628.0, 6811401.0], [473893.0, 6813452.0], [474394.0, 6821359.0], [467262.0, 6822174.0], [466087.0, 6830999.0], [463434.0, 6833996.0], [457920.0, 6827997.0], [451256.0, 6826715.0], [446687.0, 6829012.0], [441174.0, 6828584.0], [437568.0, 6825109.0], [429868.0, 6822252.0], [422197.0, 6821752.0], [414934.0, 6829326.0], [407934.0, 6831360.0], [404267.0, 6828490.0], [399495.0, 6830885.0]]]}',
        },
    },
    6: {
        "feature": feature_dpt_data_and_geometry_a,
        "recast_field_mapping": {},
        "string_field_name": ["CODE_DEPT", "NOM_DEPT"],
        "null_string": "",
        "quote_character": '"',
        "write_geometry": True,
        "geometry_format": "GEOJSON",
        "return_value": {
            "attributes": {"CODE_DEPT": '"53"', "NOM_DEPT": '"MAYENNE"'},
            "geometry": '{"type": "Polygon", "coordinates": [[[399495.0, 6830885.0], [398130.0, 6822559.0], [400321.0, 6810723.0], [395852.0, 6803336.0], [398626.0, 6784333.0], [400465.0, 6781914.0], [400197.0, 6773697.0], [394099.0, 6773357.0], [390140.0, 6770978.0], [386941.0, 6760260.0], [382932.0, 6754022.0], [389872.0, 6749698.0], [393110.0, 6750366.0], [402067.0, 6747685.0], [404251.0, 6751414.0], [412442.0, 6746090.0], [419671.0, 6744167.0], [429458.0, 6743442.0], [440863.0, 6746201.0], [446732.0, 6745443.0], [446459.0, 6750432.0], [442128.0, 6753611.0], [448124.0, 6758669.0], [447308.0, 6764356.0], [455060.0, 6767070.0], [451057.0, 6776681.0], [459373.0, 6778102.0], [460615.0, 6783387.0], [458409.0, 6789055.0], [466280.0, 6794064.0], [465298.0, 6799724.0], [467628.0, 6811401.0], [473893.0, 6813452.0], [474394.0, 6821359.0], [467262.0, 6822174.0], [466087.0, 6830999.0], [463434.0, 6833996.0], [457920.0, 6827997.0], [451256.0, 6826715.0], [446687.0, 6829012.0], [441174.0, 6828584.0], [437568.0, 6825109.0], [429868.0, 6822252.0], [422197.0, 6821752.0], [414934.0, 6829326.0], [407934.0, 6831360.0], [404267.0, 6828490.0], [399495.0, 6830885.0]]]}',
        },
    },
}

feature_attributes_to_csv_attributes_parameters = {
    0: {
        "attributes": feature_attributes_only["attributes"],
        "recast_field_mapping": {
            "field_integer": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_integer_list": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_real": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_real_list": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_string_list": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_date": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_time": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_datetime": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_binary": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
            "field_boolean": {
                "recast_value_to_python_type": str,
                "resize_value_width": None,
                "resize_value_precision": None,
            },
        },
        "return_value": {
            "field_integer": "586",
            "field_integer_list": "[5879, 8557]",
            "field_real": "8789.97568",
            "field_real_list": "[89798.3654, 8757.97568]",
            "field_string": "salut",
            "field_string_list": "['bonjour', 'monsieur']",
            "field_none": None,
            "field_date": "2020-03-31",
            "field_time": "11:22:10.000999",
            "field_datetime": "2020-03-31 11:22:10.000999",
            "field_binary": "00000000040000000200000000010000000000000000000000000000000000000000013ff00000000000003ff0000000000000",
            "field_boolean": "True",
        },
    },
    1: {"attributes": {}, "recast_field_mapping": {}, "return_value": {}},
}

geolayer_to_csv_parameters = {
    0: {
        "geolayer": geolayer_attributes_only,
        "path": geolayer_attributes_only_path,
        "overwrite": True,
        "add_extension": False,
        "delimiter": ";",  # we prefer semicolon because StringList, IntegerList and FloatList
        "header": True,
        "null_string": "",
        "quote_character": "",
        "write_geometry": True,
        "geometry_format": "WKT",
        "geometry_field_name": "geom",
        "encoding": "utf8",
        "return_value": geolayer_attributes_only_path,
    },
    1: {
        "geolayer": geolayer_attributes_to_force_only_forced,
        "path": geolayer_attributes_to_force_only_forced_path,
        "overwrite": True,
        "add_extension": False,
        "delimiter": ";",  # we prefer semicolon because StringList, IntegerList and FloatList
        "header": True,
        "null_string": "",
        "quote_character": "",
        "write_geometry": True,
        "geometry_format": "WKT",
        "geometry_field_name": "geom",
        "encoding": "utf8",
        "return_value": geolayer_attributes_to_force_only_forced_path,
    },
    2: {
        "geolayer": geolayer_fr_dept_data_only,
        "path": geolayer_fr_dept_data_only_path,
        "overwrite": True,
        "add_extension": False,
        "delimiter": ";",  # we prefer semicolon because StringList, IntegerList and FloatList
        "header": True,
        "null_string": "",
        "quote_character": "",
        "write_geometry": True,
        "geometry_format": "WKT",
        "geometry_field_name": "geom",
        "encoding": "utf8",
        "return_value": geolayer_fr_dept_data_only_path,
    },
    3: {
        "geolayer": geolayer_fr_dept_geometry_only,
        "path": geolayer_fr_dept_geometry_only_path,
        "overwrite": True,
        "add_extension": False,
        "delimiter": ";",  # we prefer semicolon because StringList, IntegerList and FloatList
        "header": True,
        "null_string": "",
        "quote_character": "",
        "write_geometry": True,
        "geometry_format": "WKT",
        "geometry_field_name": "geom",
        "encoding": "utf8",
        "return_value": geolayer_fr_dept_geometry_only_path,
    },
    4: {
        "geolayer": geolayer_fr_dept_data_and_geometry,
        "path": geolayer_fr_dept_data_and_geometry_path,
        "overwrite": True,
        "add_extension": False,
        "delimiter": ";",  # we prefer semicolon because StringList, IntegerList and FloatList
        "header": True,
        "null_string": "",
        "quote_character": "",
        "write_geometry": True,
        "geometry_format": "WKT",
        "geometry_field_name": "geom",
        "encoding": "utf8",
        "return_value": geolayer_fr_dept_data_and_geometry_path,
    },
    5: {
        "geolayer": geolayer_paris_velib,
        "path": geolayer_paris_velib_path,
        "overwrite": True,
        "add_extension": False,
        "delimiter": ";",  # we prefer semicolon because StringList, IntegerList and FloatList
        "header": True,
        "null_string": "",
        "quote_character": "",
        "write_geometry": True,
        "geometry_format": "WKT",
        "geometry_field_name": "geom",
        "encoding": "utf8",
        "return_value": geolayer_paris_velib_path,
    },
    6: {
        "geolayer": geolayer_paris_velib_str,
        "path": geolayer_paris_velib_str_path,
        "overwrite": True,
        "add_extension": False,
        "delimiter": ";",  # we prefer semicolon because StringList, IntegerList and FloatList
        "header": True,
        "null_string": "",
        "quote_character": '"',
        "write_geometry": True,
        "geometry_format": "WKT",
        "geometry_field_name": "geom",
        "encoding": "utf8",
        "return_value": geolayer_paris_velib_str_path,
    },
    7: {
        "geolayer": geolayer_paris_velib_str,
        "path": paris_velib_str_no_header_path,
        "overwrite": True,
        "add_extension": False,
        "delimiter": ";",  # we prefer semicolon because StringList, IntegerList and FloatList
        "header": False,
        "null_string": "",
        "quote_character": "",
        "write_geometry": True,
        "geometry_format": "WKT",
        "geometry_field_name": "geom",
        "encoding": "utf8",
        "return_value": paris_velib_str_no_header_path,
    },
}

csv_to_geolayer_parameters = {
    0: {
        "path": geolayer_attributes_only_path,
        "geolayer_name": None,
        "delimiter": ";",
        "header": True,
        "null_string": "",
        "field_name_filter": None,
        "force_field_conversion": True,
        "serialize": False,
        "geometry_field": False,
        "geometry_field_name": None,
        "geometry_format": "WKT",
        "encoding": "utf8",
        "http_headers": None,
        "return_value": geolayer_attributes_only_without_none_value,
    },
    1: {
        "path": geolayer_attributes_to_force_only_forced_path,
        "geolayer_name": "geolayer_attributes_to_force_only",
        "delimiter": ";",
        "header": True,
        "null_string": "",
        "field_name_filter": None,
        "force_field_conversion": True,
        "serialize": False,
        "geometry_field": False,
        "geometry_field_name": None,
        "geometry_format": "WKT",
        "encoding": "utf8",
        "http_headers": None,
        "return_value": geolayer_attributes_to_force_only_forced,
    },
    2: {
        "path": geolayer_fr_dept_data_only_path,
        "geolayer_name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_ONLY",
        "delimiter": ";",
        "header": True,
        "field_name_filter": None,
        "force_field_conversion": True,
        "serialize": False,
        "geometry_field": False,
        "geometry_field_name": None,
        "geometry_format": "WKT",
        "encoding": "utf8",
        "http_headers": None,
        "return_value": geolayer_fr_dept_data_only,
    },
    3: {
        "path": geolayer_fr_dept_geometry_only_path,
        "geolayer_name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_GEOMETRY_ONLY",
        "delimiter": ";",
        "header": True,
        "field_name_filter": None,
        "force_field_conversion": True,
        "serialize": False,
        "geometry_field": True,
        "geometry_field_name": "geom",
        "geometry_format": "WKT",
        "crs": 2154,
        "bbox_extent": True,
        "encoding": "utf8",
        "http_headers": None,
        "return_value": geolayer_fr_dept_geometry_only,
    },
    4: {
        "path": geolayer_fr_dept_data_and_geometry_path,
        "geolayer_name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
        "delimiter": ";",
        "header": True,
        "field_name_filter": None,
        "force_field_conversion": True,
        "serialize": False,
        "geometry_field": True,
        "geometry_field_name": "geom",
        "geometry_format": "WKT",
        "crs": 2154,
        "bbox_extent": False,
        "encoding": "utf8",
        "http_headers": None,
        "return_value": geolayer_fr_dept_data_and_geometry,
    },
    5: {
        "path": geolayer_paris_velib_path,
        "geolayer_name": "geolayer_paris_velib",
        "delimiter": ";",
        "header": True,
        "field_name_filter": None,
        "force_field_conversion": True,
        "serialize": False,
        "geometry_field": False,
        "geometry_field_name": None,
        "geometry_format": "WKT",
        "encoding": "utf8",
        "http_headers": None,
        "return_value": geolayer_paris_velib,
    },
    6: {
        "path": geolayer_paris_velib_str_path,
        "delimiter": ";",
        "header": True,
        "field_name_filter": None,
        "force_field_conversion": False,
        "serialize": False,
        "geometry_field": False,
        "geometry_field_name": None,
        "geometry_format": "WKT",
        "encoding": "utf8",
        "http_headers": None,
        "return_value": geolayer_paris_velib_str,
    },
    7: {
        "path": paris_velib_str_no_header_path,
        "geolayer_name": "paris_velib_str",
        "delimiter": ";",
        "header": False,
        "field_name_filter": None,
        "force_field_conversion": False,
        "serialize": False,
        "geometry_field": False,
        "geometry_field_name": None,
        "geometry_format": "WKT",
        "encoding": "utf8",
        "http_headers": None,
        "return_value": geolayer_paris_velib_str_no_header,
    },
    8: {
        "path": "https://framagit.org/Guilhain/Geoformat/-/raw/master/data/csv/velib-disponibilite-en-temps-reel.csv?inline=false",
        "geolayer_name": "geolayer_paris_velib",
        "delimiter": ";",
        "header": True,
        "field_name_filter": None,
        "force_field_conversion": True,
        "serialize": False,
        "geometry_field": False,
        "geometry_field_name": None,
        "geometry_format": "WKT",
        "encoding": "utf8",
        "http_headers": None,
        "return_value": geolayer_paris_velib,
    },
}


def test_all():
    # create test dir
    dir_test_path = file_path_base("tests/geoformat/driver/test/")
    if not dir_test_path.exists():
        dir_test_path.mkdir()

    # geoformat_feature_to_csv_feature
    print(
        test_function(
            geoformat_feature_to_csv_feature,
            geoformat_feature_to_csv_feature_parameters,
        )
    )

    # feature_attributes_to_csv_attributes
    print(
        test_function(
            feature_attributes_to_csv_attributes,
            feature_attributes_to_csv_attributes_parameters,
        )
    )

    # geolayer_to_csv
    print(test_function(geolayer_to_csv, geolayer_to_csv_parameters))

    # csv_to_geolayer
    print(test_function(csv_to_geolayer, csv_to_geolayer_parameters))

    shutil.rmtree(path=dir_test_path)


if __name__ == "__main__":
    test_all()
