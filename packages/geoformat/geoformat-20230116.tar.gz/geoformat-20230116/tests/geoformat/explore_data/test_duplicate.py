from tests.utils.tests_utils import test_function

from tests.data.geometries import POINT, POINT_EMPTY, LINESTRING, LINESTRING_EMPTY, POLYGON, POLYGON_EMPTY, MULTIPOINT, MULTIPOINT_EMPTY, MULTILINESTRING, MULTILINESTRING_EMPTY, MULTIPOLYGON, MULTIPOLYGON_EMPTY, GEOMETRYCOLLECTION, GEOMETRYCOLLECTION_EMPTY

from geoformat.explore_data.duplicate import (
    get_feature_attributes_hash,
    get_feature_geometry_hash,
    get_feature_hash,
    get_duplicate_features
)

from geoformat.manipulation.geolayer_manipulation import feature_list_to_geolayer

from tests.data.features import (
    feature_dpt_data_only_a,
    feature_dpt_data_only_b,
    feature_dpt_data_only_c,
    feature_dpt_data_only_d,
    feature_dpt_geometry_only_a,
    feature_dpt_geometry_only_b,
    feature_dpt_geometry_only_c,
    feature_dpt_geometry_only_d,
    feature_dpt_data_and_geometry_a,
    feature_dpt_data_and_geometry_b,
    feature_dpt_data_and_geometry_c,
    feature_dpt_data_and_geometry_d,
)

get_feature_attributes_hash_parameters = {
    0: {
        "feature_attributes": {"CODE_DEPT": "53", "NOM_DEPT": "MAYENNE"},
        "field_attributes_field_name_order": ['CODE_DEPT', "NOM_DEPT"],
        "return_value": "51c7470e93695db9d24dea51653ee9a1249864a1a09c84fd9736e87080f75d0f",
    },
    1: {
        "feature_attributes": {"CODE_DEPT": "53", "NOM_DEPT": "MAYENNE"},
        "field_attributes_field_name_order": ['NOM_DEPT', "CODE_DEPT"],
        "return_value": "129cd2a582cd17950c10376e6242eebe6b817e163091b6cd17547017180cd9d6",
    },
    2: {
        "feature_attributes": {"NOM_DEPT": "MAYENNE", "CODE_DEPT": "53",},
        "field_attributes_field_name_order": ['CODE_DEPT', "NOM_DEPT"],
        "return_value": "51c7470e93695db9d24dea51653ee9a1249864a1a09c84fd9736e87080f75d0f",
    },
    3: {
        "feature_attributes": {"NOM_DEPT": "MAYENNE", "CODE_DEPT": "53", },
        "field_attributes_field_name_order": ['NOM_DEPT', "CODE_DEPT"],
        "return_value": "129cd2a582cd17950c10376e6242eebe6b817e163091b6cd17547017180cd9d6",
    },
    4: {
        "feature_attributes": {"NOM_DEPT": "MAYENNE", "CODE_DEPT": "53", },
        "field_attributes_field_name_order": [],
        "return_value": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    },
    5: {
        "feature_attributes": {},
        "field_attributes_field_name_order": [],
        "return_value": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    },
    6: {
        "feature_attributes": {},
        "field_attributes_field_name_order": ['NOM_DEPT', "CODE_DEPT"],
        "return_value": "b554fb2635a2b08395e00bee3abb78acdc3ca105b7844665ed1f6000b4ade489",
    },
    7: {
        "feature_attributes": None,
        "field_attributes_field_name_order": ['NOM_DEPT', "CODE_DEPT"],
        "return_value": "b554fb2635a2b08395e00bee3abb78acdc3ca105b7844665ed1f6000b4ade489",
    },
}

get_feature_geometry_hash_parameters = {
    0: {
        "feature_geometry": POINT,
        "return_value": "8fa3638269b284ff81154796e64c3622d766449fc711b21ae532a6d30dc674f7",
    },
    1: {
        "feature_geometry": POINT_EMPTY,
        "return_value": "95af905f4db3b819abc809b159456929f0e6b71cc7dba8eaa23992adcfe0f6c3",
    },
    2: {
        "feature_geometry": LINESTRING,
        "return_value": "b4cd3ad1b61a78511ef26d19aca752bba385b9a3abbe86d515e745ef0b104378",
    },
    3: {
        "feature_geometry": LINESTRING_EMPTY,
        "return_value": "3a40f051d7860323de7dc25da2f7c03f7727837c16e9c7a208c217e6c11ba57d",
    },
    4: {
        "feature_geometry": POLYGON,
        "return_value": "bfe28dbb4b9952b0a3ebb87f4e581197cab2f643e30e6912cbb8881247d33b8f",
    },
    5: {
        "feature_geometry": POLYGON_EMPTY,
        "return_value": "a10cdee8d37cc737efda4f4ecb273a62ef6281eb059831723a7f05db6ca91203",
    },
    6: {
        "feature_geometry": MULTIPOINT,
        "return_value": "5c79decd6b19e2f0ecd200f4459c0df3b40dd636258b571e42be398e48803c1d",
    },
    7: {
        "feature_geometry": MULTIPOINT_EMPTY,
        "return_value": "d04df4541745df552bf656601bd0ba5a803ff47be8c8d06e4f7e833f5fd72727",
    },

    8: {
        "feature_geometry": MULTILINESTRING,
        "return_value": "d59e25a3cf6c253494f13721088677bbe5077f5060d817a60cc71e9b837eeb97",
    },
    9: {
        "feature_geometry": MULTILINESTRING_EMPTY,
        "return_value": "b8db8e1a212398c530e340e0c8fb2b7bcfdc33639c64ee290a92acf9d52f4f27",
    },
    10: {
        "feature_geometry": MULTIPOLYGON,
        "return_value": "94594e71f626c43f8d871d64e10c88e86d32e4ec0b89fa3a5c0118f5ee1bc007",
    },
    11: {
        "feature_geometry": MULTIPOLYGON_EMPTY,
        "return_value": "9503e533b097397f5118a748890cd09caacfd4c95c4d13f1fd106a5b5e39e78a",
    },
    12: {
        "feature_geometry": GEOMETRYCOLLECTION,
        "return_value": "b6c9d62bdfcd0c440ff0a952b255957c6869b96fb532ad6e76f2dbac05af611d",
    },
    13: {
        "feature_geometry": GEOMETRYCOLLECTION_EMPTY,
        "return_value": "fde666df544418c9cc1c2d036f1e0677658e66d56a2c40241290404e61567404",
    },
    14: {
        "feature_geometry": {},
        "return_value": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    },
    15: {
        "feature_geometry": {},
        "return_value": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    },

}

get_feature_hash_parameters = {
    0: {
        "feature": {"attributes": {"id": 0, "name": "Alice"}},
        "field_attributes_field_name_order": ["id", "name"],
        "attribute_hash": True,
        "geometry_hash": True,
        "return_value": "1abfc0b0962e2f8f0bc269edc68b7bdee90b0ccae602d811ee2e5c84d82e6bcc"
    },
    1: {
        "feature": {"attributes": {"id": 0, "name": "Alice"}},
        "field_attributes_field_name_order": None,
        "attribute_hash": True,
        "geometry_hash": True,
        "return_value": "variable field_attributes_field_name_order must be fill"
    },
    2: {
        "feature": {"attributes": {"id": 0, "name": "Alice"}},
        "field_attributes_field_name_order": ["name", "id"],
        "attribute_hash": True,
        "geometry_hash": True,
        "return_value": "1abee36b192e37746120c85c1abc88a22af548aa37bf82f6639b31e29f8b6614"
    },
    3: {
        "feature": {"attributes": {"id": 0, "name": "Alice"}},
        "field_attributes_field_name_order": ["id", "name"],
        "attribute_hash": True,
        "geometry_hash": False,
        "return_value": "1abfc0b0962e2f8f0bc269edc68b7bdee90b0ccae602d811ee2e5c84d82e6bcc"
    },
    4: {
        "feature": {"attributes": {"id": 0, "name": "Alice"}},
        "field_attributes_field_name_order": ["id", "name"],
        "attribute_hash": False,
        "geometry_hash": True,
        "return_value": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    5: {
        "feature": {"attributes": {"id": 0, "name": "Alice"}},
        "field_attributes_field_name_order": ["id", "name"],
        "attribute_hash": False,
        "geometry_hash": False,
        "return_value": "At least one of this variables (attribute_hash or geometry_hash) must be True"
    },
    6: {
        "feature": {"attributes": {"id": 0, "name": "Alice"}, "geometry": POINT},
        "field_attributes_field_name_order": ["id", "name"],
        "attribute_hash": True,
        "geometry_hash": True,
        "return_value": "4fd3977f22544bc2127918097464827828a7c856052fddba6647c61b7fa0328c"
    },
    7: {
        "feature": {"attributes": {"id": 0, "name": "Alice"}, "geometry": POINT},
        "field_attributes_field_name_order": ["id", "name"],
        "attribute_hash": True,
        "geometry_hash": False,
        "return_value": "1abfc0b0962e2f8f0bc269edc68b7bdee90b0ccae602d811ee2e5c84d82e6bcc"
    },
    8: {
        "feature": {"attributes": {"id": 0, "name": "Alice"}, "geometry": POINT},
        "field_attributes_field_name_order": ["id", "name"],
        "attribute_hash": False,
        "geometry_hash": True,
        "return_value": "f1d248b203635aece53e123298ee6779a2d06df0ab68078c02bd6ef6f72af70c"
    },
    9: {
        "feature": {"geometry": POINT},
        "field_attributes_field_name_order": None,
        "attribute_hash": True,
        "geometry_hash": True,
        "return_value": "f1d248b203635aece53e123298ee6779a2d06df0ab68078c02bd6ef6f72af70c"
    },
    10: {
        "feature": {"geometry": POINT},
        "field_attributes_field_name_order": None,
        "attribute_hash": True,
        "geometry_hash": False,
        "return_value": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
}

get_duplicate_features_parameters = {
    0: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_data_only_a,
            feature_dpt_data_only_b,
            feature_dpt_data_only_c,
            feature_dpt_data_only_d,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": True,
        "return_value": ()
    },
    1: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_data_only_a,
            feature_dpt_data_only_c,
            feature_dpt_data_only_c,
            feature_dpt_data_only_d,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": True,
        "return_value": (2,)
    },
    2: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_data_only_a,
            feature_dpt_data_only_c,
            feature_dpt_data_only_c,
            feature_dpt_data_only_c,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": True,
        "return_value": (2, 3)
    },
    3: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_data_only_a,
            feature_dpt_data_only_c,
            feature_dpt_data_only_c,
            feature_dpt_data_only_c,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": False,
        "check_geometry_duplicate": True,
        "return_value": (1, 2, 3)
    },
    4: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_data_only_a,
            feature_dpt_data_only_c,
            feature_dpt_data_only_c,
            feature_dpt_data_only_c,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": False,
        "return_value": (2, 3)
    },
    5: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_geometry_only_a,
            feature_dpt_geometry_only_b,
            feature_dpt_geometry_only_c,
            feature_dpt_geometry_only_d,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": True,
        "return_value": ()
    },
    6: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_geometry_only_a,
            feature_dpt_geometry_only_c,
            feature_dpt_geometry_only_c,
            feature_dpt_geometry_only_d,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": True,
        "return_value": (2,)
    },
    7: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_geometry_only_a,
            feature_dpt_geometry_only_c,
            feature_dpt_geometry_only_c,
            feature_dpt_geometry_only_c,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": True,
        "return_value": (2, 3)
    },
    8: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_geometry_only_a,
            feature_dpt_geometry_only_c,
            feature_dpt_geometry_only_c,
            feature_dpt_geometry_only_c,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": False,
        "check_geometry_duplicate": True,
        "return_value": (2, 3)
    },
    9: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_geometry_only_a,
            feature_dpt_geometry_only_c,
            feature_dpt_geometry_only_c,
            feature_dpt_geometry_only_c,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": False,
        "return_value": (1, 2, 3)
    },
    10: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_data_and_geometry_a,
            feature_dpt_data_and_geometry_b,
            feature_dpt_data_and_geometry_c,
            feature_dpt_data_and_geometry_d,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": True,
        "return_value": ()
    },
    11: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_data_and_geometry_a,
            feature_dpt_data_and_geometry_c,
            feature_dpt_data_and_geometry_c,
            feature_dpt_data_and_geometry_d,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": True,
        "return_value": (2,)
    },
    12: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_data_and_geometry_a,
            feature_dpt_data_and_geometry_c,
            feature_dpt_data_and_geometry_c,
            feature_dpt_data_and_geometry_c,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": True,
        "return_value": (2, 3)
    },
    13: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_data_and_geometry_a,
            feature_dpt_data_and_geometry_c,
            feature_dpt_data_and_geometry_c,
            feature_dpt_data_and_geometry_c,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": False,
        "check_geometry_duplicate": True,
        "return_value": (2, 3)
    },
    14: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            feature_dpt_data_and_geometry_a,
            feature_dpt_data_and_geometry_c,
            feature_dpt_data_and_geometry_c,
            feature_dpt_data_and_geometry_c,
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": False,
        "return_value": (2, 3)
    },
    15: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            {"attributes": {"id": 0, "name": "Alice"}, "geometry": POINT},
            {"attributes": {"id": None, "name": "Bob"}, "geometry": LINESTRING},
            {"attributes": {"id": None, "name": "Patrick"}, "geometry": LINESTRING},
            {"attributes": {"id": 1, "name": "Jane"}, "geometry": POINT},
            {"attributes": {"id": 1, "name": "Jane"}, "geometry": POLYGON},
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": True,
        "return_value": ()
    },
    16: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            {"attributes": {"id": 0, "name": "Alice"}, "geometry": POINT},
            {"attributes": {"id": None, "name": "Bob"}, "geometry": LINESTRING},
            {"attributes": {"id": None, "name": "Patrick"}, "geometry": LINESTRING},
            {"attributes": {"id": 1, "name": "Jane"}, "geometry": POINT},
            {"attributes": {"id": 1, "name": "Jane"}, "geometry": POLYGON},
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": False,
        "check_geometry_duplicate": True,
        "return_value": (2, 3)
    },
    17: {
        "geolayer": feature_list_to_geolayer(feature_list=[
            {"attributes": {"id": 0, "name": "Alice"}, "geometry": POINT},
            {"attributes": {"id": None, "name": "Bob"}, "geometry": LINESTRING},
            {"attributes": {"id": None, "name": "Patrick"}, "geometry": LINESTRING},
            {"attributes": {"id": 1, "name": "Jane"}, "geometry": POINT},
            {"attributes": {"id": 1, "name": "Jane"}, "geometry": POLYGON},
            ],
            geolayer_name='test'
        ),
        "check_attribute_duplicate": True,
        "check_geometry_duplicate": False,
        "return_value": (4,)
    },
}
def test_all():

    # get_feature_attributes_hash
    print(test_function(get_feature_attributes_hash, get_feature_attributes_hash_parameters))

    # get_feature_geometry_hash
    print(test_function(get_feature_geometry_hash, get_feature_geometry_hash_parameters))

    # get_feature_hash
    print(test_function(get_feature_hash, get_feature_hash_parameters))

    # get_duplicate_features
    print(test_function(get_duplicate_features, get_duplicate_features_parameters))

if __name__ == '__main__':
    test_all()
