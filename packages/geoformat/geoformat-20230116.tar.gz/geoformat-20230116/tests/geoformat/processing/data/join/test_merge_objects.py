import copy
from tests.utils.tests_utils import test_function

from geoformat.conf.error_messages import (
    variable_wrong_formatting,
    field_exists,
    metadata_geometry_ref_not_found,
    metadata_geometry_ref_type_not_match,
    geometry_ref_feature,
)


from geoformat.processing.data.join.merge_objects import (
    merge_metadata,
    merge_feature,
)

from tests.data.metadata import (
    metadata_fr_dept_data_and_geometry,
    metadata_fr_dept_data_only,
    metadata_fr_dept_population,
    metadata_fr_dept_population_geometry,
)

from tests.data.features import (
    feature_dpt_data_only_a,
    feature_dpt_geometry_only_a,
    feature_dpt_data_and_geometry_a,
    feature_dpt_population_a,
    feature_dpt_population_geometry_a,
)

merge_metadata_parameters = {
    0: {
        "metadata_a": copy.deepcopy(metadata_fr_dept_data_and_geometry),
        "metadata_b": copy.deepcopy(metadata_fr_dept_data_and_geometry),
        "geolayer_name": "merge_FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "geometry_ref": "metadata_a",
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "merge_FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                    "CODE_DEPT1": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT1": {"type": "String", "width": 23, "index": 3},
                },
                "geometry_ref": {"type": {"Polygon", "MultiPolygon"}, "crs": 2154},
            },
            "fields_correspondance_a": {},
            "fields_correspondance_b": {"CODE_DEPT": "CODE_DEPT1", "NOM_DEPT": "NOM_DEPT1"}
        },
    },
    1: {
        "metadata_a": copy.deepcopy(metadata_fr_dept_data_only),
        "metadata_b": copy.deepcopy(metadata_fr_dept_data_and_geometry),
        "geolayer_name": "merge_FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "geometry_ref": "metadata_a",
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "merge_FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                    "CODE_DEPT1": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT1": {"type": "String", "width": 23, "index": 3},
                },
            },
            "fields_correspondance_a": {},
            "fields_correspondance_b": {"CODE_DEPT": "CODE_DEPT1", "NOM_DEPT": "NOM_DEPT1"}
        },
    },
    2: {
        "metadata_a": copy.deepcopy(metadata_fr_dept_data_only),
        "metadata_b": copy.deepcopy(metadata_fr_dept_data_and_geometry),
        "geolayer_name": "merge_FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "geometry_ref": "metadata_a",
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "merge_FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                    "CODE_DEPT1": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT1": {"type": "String", "width": 23, "index": 3},
                },
            },
            "fields_correspondance_a": {},
            "fields_correspondance_b": {"CODE_DEPT": "CODE_DEPT1", "NOM_DEPT": "NOM_DEPT1"}
        },
    },
    3: {
        "metadata_a": copy.deepcopy(metadata_fr_dept_data_only),
        "metadata_b": copy.deepcopy(metadata_fr_dept_data_and_geometry),
        "geolayer_name": "merge_FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "geometry_ref": "metadata_b",
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "merge_FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                    "CODE_DEPT1": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT1": {"type": "String", "width": 23, "index": 3},
                },
                "geometry_ref": {"type": {"MultiPolygon", "Polygon"}, "crs": 2154},
            },
            "fields_correspondance_a": {},
            "fields_correspondance_b": {"CODE_DEPT": "CODE_DEPT1", "NOM_DEPT": "NOM_DEPT1"}
        },
    },
    4: {
        "metadata_a": copy.deepcopy(metadata_fr_dept_data_only),
        "metadata_b": copy.deepcopy(metadata_fr_dept_data_and_geometry),
        "geolayer_name": "merge_FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
        "field_name_filter_a": [],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "geometry_ref": "metadata_b",
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "merge_FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                },
                "geometry_ref": {"type": {"Polygon", "MultiPolygon"}, "crs": 2154},
            },
            "fields_correspondance_a": {},
            "fields_correspondance_b": {},
        },
    },
    5: {
        "metadata_a": copy.deepcopy(metadata_fr_dept_data_only),
        "metadata_b": copy.deepcopy(metadata_fr_dept_data_only),
        "geolayer_name": "FRANCE_DPT",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "geometry_ref": "metadata_b",
        "rename_output_field_from_geolayer_a": {"CODE_DEPT": "id_dept", "NOM_DEPT": "name"},
        "rename_output_field_from_geolayer_b": {"CODE_DEPT": "CODE_DPT", "NOM_DEPT": "nom"},
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT",
                "fields": {
                    "id_dept": {"type": "String", "width": 2, "index": 0},
                    "name": {"type": "String", "width": 23, "index": 1},
                    "CODE_DPT": {"type": "String", "width": 2, "index": 2},
                    "nom": {"type": "String", "width": 23, "index": 3},
                },
            },
            "fields_correspondance_a": {"CODE_DEPT": "id_dept", "NOM_DEPT": "name"},
            "fields_correspondance_b": {"CODE_DEPT": "CODE_DPT", "NOM_DEPT": "nom"},
        },
    },
    6: {
        "metadata_a": copy.deepcopy(metadata_fr_dept_data_only),
        "metadata_b": copy.deepcopy(metadata_fr_dept_data_only),
        "geolayer_name": "FRANCE_DPT",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "geometry_ref": "metadata_b",
        "rename_output_field_from_geolayer_a": {"NOM_DEPT": "name"},
        "rename_output_field_from_geolayer_b": {"NOM_DEPT": "nom"},
        "return_value": field_exists.format(field_name="CODE_DEPT"),
    },
    7: {
        "metadata_a": copy.deepcopy(metadata_fr_dept_data_only),
        "metadata_b": copy.deepcopy(metadata_fr_dept_population),
        "geolayer_name": "FRANCE_DPT",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "geometry_ref": "metadata_b",
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                    "CODE_DEPT1": {"type": "String", "width": 2, "index": 2},
                    "INSEE_REG": {"type": "String", "width": 2, "index": 3},
                    "POPULATION": {"type": "Integer", "index": 4},
                    "AREA": {"type": "Real", "width": 7, "precision": 2, "index": 5},
                    "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 6},
                },
            },
            "fields_correspondance_a": {},
            "fields_correspondance_b": {"CODE_DEPT": "CODE_DEPT1"},
        },
    },
    8: {
        "metadata_a": copy.deepcopy(metadata_fr_dept_data_and_geometry),
        "metadata_b": copy.deepcopy(metadata_fr_dept_population),
        "geolayer_name": "FRANCE_DPT_WITH_POPULATION",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "geometry_ref": "metadata_a",
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": metadata_fr_dept_population_geometry,
            "fields_correspondance_a": {},
            "fields_correspondance_b": {},
        },
    },
}

merge_feature_parameters = {
    0: {
        "feature_a": copy.deepcopy(
            {
                "geometry": {
                    "type": feature_dpt_geometry_only_a["geometry"]["type"],
                    "coordinates": feature_dpt_geometry_only_a["geometry"][
                        "coordinates"
                    ],
                }
            }
        ),
        "feature_b": copy.deepcopy(feature_dpt_data_only_a),
        "merge_metadata": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_fields_a": None,
        "rename_fields_b": None,
        "geometry_ref": "feature_a",
        "return_value": feature_dpt_data_and_geometry_a,
    },
    1: {
        "feature_a": copy.deepcopy(feature_dpt_data_only_a),
        "feature_b": copy.deepcopy(feature_dpt_geometry_only_a),
        "merge_metadata": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_fields_a": None,
        "rename_fields_b": None,
        "geometry_ref": "feature_a",
        "return_value": feature_dpt_data_only_a,
    },
    2: {
        "feature_a": copy.deepcopy(feature_dpt_data_only_a),
        "feature_b": copy.deepcopy(
            {
                "geometry": {
                    "type": feature_dpt_geometry_only_a["geometry"]["type"],
                    "coordinates": feature_dpt_geometry_only_a["geometry"][
                        "coordinates"
                    ],
                }
            }
        ),
        "merge_metadata": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_fields_a": None,
        "rename_fields_b": None,
        "geometry_ref": "feature_b",
        "return_value": feature_dpt_data_and_geometry_a,
    },
    3: {
        "feature_a": copy.deepcopy(feature_dpt_data_only_a),
        "feature_b": copy.deepcopy(feature_dpt_population_a),
        "merge_metadata": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_fields_a": None,
        "rename_fields_b": None,
        "geometry_ref": "feature_a",
        "return_value": field_exists.format(field_name="CODE_DEPT"),
    },
    4: {
        "feature_a": copy.deepcopy(feature_dpt_data_only_a),
        "feature_b": copy.deepcopy(feature_dpt_population_a),
        "merge_metadata": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_fields_a": None,
        "rename_fields_b": {"CODE_DEPT": "CODE_DEPT1"},
        "geometry_ref": "feature_a",
        "return_value": {
            "attributes": {
                "CODE_DEPT": "53",
                "NOM_DEPT": "MAYENNE",
                "INSEE_REG": "52",
                "POPULATION": 307445,
                "AREA": 5208.37,
                "DENSITY": 59.03,
                "CODE_DEPT1": "53",
            }
        },
    },
    5: {
        "feature_a": copy.deepcopy(feature_dpt_data_only_a),
        "feature_b": copy.deepcopy(feature_dpt_population_a),
        "merge_metadata": {
            "name": "FRANCE_DPT_WITH_POPULATION",
            "fields": {
                "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                "POPULATION": {"type": "Integer", "index": 2},
                "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 3},
            },
        },
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_fields_a": None,
        "rename_fields_b": None,
        "geometry_ref": "feature_a",
        "return_value": {
            "attributes": {
                "CODE_DEPT": "53",
                "NOM_DEPT": "MAYENNE",
                "POPULATION": 307445,
                "DENSITY": 59.03,
            }
        },
    },
    6: {
        "feature_a": copy.deepcopy(feature_dpt_population_a),
        "feature_b": copy.deepcopy(feature_dpt_geometry_only_a),
        "merge_metadata": {
            "name": "FRANCE_DPT_WITH_POPULATION",
            "fields": {
                "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                "POPULATION": {"type": "Integer", "index": 2},
                "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 3},
            },
        },
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT", "POPULATION", "DENSITY"],
        "field_name_filter_b": [],
        "rename_fields_a": None,
        "rename_fields_b": None,
        "geometry_ref": "feature_b",
        "return_value": metadata_geometry_ref_not_found,
    },
    7: {
        "feature_a": copy.deepcopy(feature_dpt_population_a),
        "feature_b": copy.deepcopy(
            {
                "geometry": {
                    "type": feature_dpt_geometry_only_a["geometry"]["type"],
                    "coordinates": feature_dpt_geometry_only_a["geometry"][
                        "coordinates"
                    ],
                }
            }
        ),
        "merge_metadata": {
            "name": "FRANCE_DPT_WITH_POPULATION",
            "fields": {
                "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                "POPULATION": {"type": "Integer", "index": 2},
                "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 3},
            },
            "geometry_ref": {"type": {"Polygon"}},
        },
        "field_name_filter_a": ["CODE_DEPT", "POPULATION", "DENSITY"],
        "field_name_filter_b": None,
        "rename_fields_a": None,
        "rename_fields_b": None,
        "geometry_ref": "feature_b",
        "return_value": {
            "attributes": {"CODE_DEPT": "53", "POPULATION": 307445, "DENSITY": 59.03},
            "geometry": {
                "type": "Polygon",
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
    },
    8: {
        "feature_a": copy.deepcopy(feature_dpt_population_a),
        "feature_b": copy.deepcopy(feature_dpt_geometry_only_a),
        "merge_metadata": {
            "name": "FRANCE_DPT_WITH_POPULATION",
            "fields": {
                "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                "POPULATION": {"type": "Integer", "index": 2},
                "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 3},
            },
            "geometry_ref": {"type": {"Point"}},
        },
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT", "POPULATION", "DENSITY"],
        "field_name_filter_b": [],
        "rename_fields_a": None,
        "rename_fields_b": None,
        "geometry_ref": "feature_b",
        "return_value": metadata_geometry_ref_type_not_match,
    },
    9: {
        "feature_a": copy.deepcopy(feature_dpt_geometry_only_a),
        "feature_b": copy.deepcopy(feature_dpt_data_only_a),
        "merge_metadata": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_fields_a": None,
        "rename_fields_b": None,
        "geometry_ref": "feature_c",
        "return_value": geometry_ref_feature,
    },
    10: {
        "feature_a": copy.deepcopy(feature_dpt_population_a),
        "feature_b": copy.deepcopy(feature_dpt_data_and_geometry_a),
        "merge_metadata": metadata_fr_dept_population_geometry,
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_fields_a": None,
        "rename_fields_b": None,
        "geometry_ref": "feature_b",
        "return_value": feature_dpt_population_geometry_a,
    },
}


def test_all():

    # merge metadata
    print(test_function(merge_metadata, merge_metadata_parameters))

    # merge feature
    print(test_function(merge_feature, merge_feature_parameters))


if __name__ == "__main__":
    test_all()
