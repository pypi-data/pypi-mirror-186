import copy

import geoformat
from geoformat.processing.data.join.join import join, join_left, join_right, join_full

from geoformat.manipulation.geolayer_manipulation import feature_list_to_geolayer

from tests.utils.tests_utils import test_function

from tests.data.geolayers import (
    geolayer_fr_dept_data_only,
    geolayer_fr_dept_data_and_geometry,
    geolayer_fr_dept_population,
    geolayer_fr_dept_population_geometry,
    geolayer_fr_dept_population_geometry_right,
)

from tests.data.features import (
    feature_dpt_data_only_a,
    feature_dpt_data_only_b,
    feature_dpt_data_only_c,
    feature_dpt_data_only_d,
    feature_dpt_population_a,
    feature_dpt_population_b,
    feature_dpt_population_c,
    feature_dpt_population_d,
    feature_dpt_data_and_geometry_a,
    feature_dpt_data_and_geometry_b,
    feature_dpt_data_and_geometry_c,
    feature_dpt_data_and_geometry_d,
)

from geoformat.conf.error_messages import field_missing

geolayer_dpt_full = feature_list_to_geolayer(
    feature_list=copy.deepcopy(
        [
            feature_dpt_data_only_a,
            feature_dpt_data_only_b,
            feature_dpt_data_only_c,
            feature_dpt_data_only_d,
        ]
    ),
    geolayer_name="geolayer_dpt_full",
)

geolayer_dpt_full_with_duplicate = feature_list_to_geolayer(
    feature_list=copy.deepcopy(
        [
            feature_dpt_data_only_a,
            feature_dpt_data_only_b,
            feature_dpt_data_only_b,
            feature_dpt_data_only_c,
            feature_dpt_data_only_d,
            feature_dpt_data_only_d,
        ]
    ),
    geolayer_name="geolayer_dpt_full_with_duplicate",
)

geolayer_dpt_2 = feature_list_to_geolayer(
    feature_list=copy.deepcopy([feature_dpt_data_only_b, feature_dpt_data_only_c]),
    geolayer_name="geolayer_dpt_2",
)

geolayer_dpt_2_with_geom = feature_list_to_geolayer(
    feature_list=copy.deepcopy(
        [feature_dpt_data_and_geometry_b, feature_dpt_data_and_geometry_c]
    ),
    geolayer_name="geolayer_dpt_2_with_geom",
)

geolayer_dpt_pop_full = feature_list_to_geolayer(
    feature_list=copy.deepcopy(
        [
            feature_dpt_population_a,
            feature_dpt_population_b,
            feature_dpt_population_c,
            feature_dpt_population_d,
        ]
    ),
    geolayer_name="geolayer_dpt_pop_full",
)

geolayer_dpt_pop_full_with_duplicate = feature_list_to_geolayer(
    feature_list=copy.deepcopy(
        [
            feature_dpt_population_a,
            feature_dpt_population_b,
            feature_dpt_population_b,
            feature_dpt_population_c,
            feature_dpt_population_d,
            feature_dpt_population_d,
        ]
    ),
    geolayer_name="geolayer_dpt_pop_full_with_duplicate",
)

geolayer_dpt_pop_2 = feature_list_to_geolayer(
    feature_list=copy.deepcopy([feature_dpt_population_a, feature_dpt_population_d]),
    geolayer_name="geolayer_dpt_pop_2",
)

join_parameters = {
    0: {
        "geolayer_a": geolayer_fr_dept_data_only,
        "geolayer_b": geolayer_fr_dept_population,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_ONLY",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_ONLY",
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
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "NOM_DEPT": "GERS",
                        "INSEE_REG": "76",
                        "POPULATION": 191091,
                        "AREA": 6304.33,
                        "DENSITY": 30.31,
                        "CODE_DEPT1": "32",
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "NOM_DEPT": "LOT-ET-GARONNE",
                        "INSEE_REG": "75",
                        "POPULATION": 332842,
                        "AREA": 5382.87,
                        "DENSITY": 61.83,
                        "CODE_DEPT1": "47",
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "NOM_DEPT": "ISERE",
                        "INSEE_REG": "84",
                        "POPULATION": 1258722,
                        "AREA": 7868.79,
                        "DENSITY": 159.96,
                        "CODE_DEPT1": "38",
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "NOM_DEPT": "PAS-DE-CALAIS",
                        "INSEE_REG": "32",
                        "POPULATION": 1468018,
                        "AREA": 6714.14,
                        "DENSITY": 218.65,
                        "CODE_DEPT1": "62",
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "NOM_DEPT": "ARDENNES",
                        "INSEE_REG": "44",
                        "POPULATION": 273579,
                        "AREA": 5253.13,
                        "DENSITY": 52.08,
                        "CODE_DEPT1": "08",
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "NOM_DEPT": "AUBE",
                        "INSEE_REG": "44",
                        "POPULATION": 310020,
                        "AREA": 6021.83,
                        "DENSITY": 51.48,
                        "CODE_DEPT1": "10",
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "NOM_DEPT": "ALPES-MARITIMES",
                        "INSEE_REG": "93",
                        "POPULATION": 1083310,
                        "AREA": 4291.62,
                        "DENSITY": 252.42,
                        "CODE_DEPT1": "06",
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "NOM_DEPT": "LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 762941,
                        "AREA": 4795.85,
                        "DENSITY": 159.08,
                        "CODE_DEPT1": "42",
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "NOM_DEPT": "HAUTE-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 1362672,
                        "AREA": 6364.82,
                        "DENSITY": 214.09,
                        "CODE_DEPT1": "31",
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "NOM_DEPT": "SAONE-ET-LOIRE",
                        "INSEE_REG": "27",
                        "POPULATION": 553595,
                        "AREA": 8598.33,
                        "DENSITY": 64.38,
                        "CODE_DEPT1": "71",
                    }
                },
                10: {
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
                11: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "NOM_DEPT": "CHARENTE",
                        "INSEE_REG": "75",
                        "POPULATION": 352335,
                        "AREA": 5963.54,
                        "DENSITY": 59.08,
                        "CODE_DEPT1": "16",
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "NOM_DEPT": "MANCHE",
                        "INSEE_REG": "28",
                        "POPULATION": 496883,
                        "AREA": 6015.07,
                        "DENSITY": 82.61,
                        "CODE_DEPT1": "50",
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "NOM_DEPT": "YVELINES",
                        "INSEE_REG": "11",
                        "POPULATION": 1438266,
                        "AREA": 2305.64,
                        "DENSITY": 623.8,
                        "CODE_DEPT1": "78",
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "NOM_DEPT": "DOUBS",
                        "INSEE_REG": "27",
                        "POPULATION": 539067,
                        "AREA": 5248.31,
                        "DENSITY": 102.71,
                        "CODE_DEPT1": "25",
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "NOM_DEPT": "MEUSE",
                        "INSEE_REG": "44",
                        "POPULATION": 187187,
                        "AREA": 6233.18,
                        "DENSITY": 30.03,
                        "CODE_DEPT1": "55",
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "NOM_DEPT": "GIRONDE",
                        "INSEE_REG": "75",
                        "POPULATION": 1583384,
                        "AREA": 10068.74,
                        "DENSITY": 157.26,
                        "CODE_DEPT1": "33",
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "NOM_DEPT": "CALVADOS",
                        "INSEE_REG": "28",
                        "POPULATION": 694002,
                        "AREA": 5588.48,
                        "DENSITY": 124.18,
                        "CODE_DEPT1": "14",
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "NOM_DEPT": "VOSGES",
                        "INSEE_REG": "44",
                        "POPULATION": 367673,
                        "AREA": 5891.56,
                        "DENSITY": 62.41,
                        "CODE_DEPT1": "88",
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "NOM_DEPT": "CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 304256,
                        "AREA": 7292.67,
                        "DENSITY": 41.72,
                        "CODE_DEPT1": "18",
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "NOM_DEPT": "ARDECHE",
                        "INSEE_REG": "84",
                        "POPULATION": 325712,
                        "AREA": 5562.05,
                        "DENSITY": 58.56,
                        "CODE_DEPT1": "07",
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "INSEE_REG": "32",
                        "POPULATION": 534490,
                        "AREA": 7418.97,
                        "DENSITY": 72.04,
                        "CODE_DEPT1": "02",
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "NOM_DEPT": "PYRENEES-ATLANTIQUES",
                        "INSEE_REG": "75",
                        "POPULATION": 677309,
                        "AREA": 7691.6,
                        "DENSITY": 88.06,
                        "CODE_DEPT1": "64",
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "NOM_DEPT": "LOIR-ET-CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 331915,
                        "AREA": 6412.3,
                        "DENSITY": 51.76,
                        "CODE_DEPT1": "41",
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "NOM_DEPT": "MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 1043522,
                        "AREA": 6252.63,
                        "DENSITY": 166.89,
                        "CODE_DEPT1": "57",
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "NOM_DEPT": "VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 436876,
                        "AREA": 7025.24,
                        "DENSITY": 62.19,
                        "CODE_DEPT1": "86",
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "NOM_DEPT": "DORDOGNE",
                        "INSEE_REG": "75",
                        "POPULATION": 413606,
                        "AREA": 9209.9,
                        "DENSITY": 44.91,
                        "CODE_DEPT1": "24",
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "NOM_DEPT": "JURA",
                        "INSEE_REG": "27",
                        "POPULATION": 260188,
                        "AREA": 5040.63,
                        "DENSITY": 51.62,
                        "CODE_DEPT1": "39",
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "NOM_DEPT": "TARN-ET-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 258349,
                        "AREA": 3731.0,
                        "DENSITY": 69.24,
                        "CODE_DEPT1": "82",
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "NOM_DEPT": "MAINE-ET-LOIRE",
                        "INSEE_REG": "52",
                        "POPULATION": 813493,
                        "AREA": 7161.34,
                        "DENSITY": 113.6,
                        "CODE_DEPT1": "49",
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "NOM_DEPT": "RHONE",
                        "INSEE_REG": "84",
                        "POPULATION": 1843319,
                        "AREA": 3253.11,
                        "DENSITY": 566.63,
                        "CODE_DEPT1": "69",
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "NOM_DEPT": "EURE",
                        "INSEE_REG": "28",
                        "POPULATION": 601843,
                        "AREA": 6035.85,
                        "DENSITY": 99.71,
                        "CODE_DEPT1": "27",
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "NOM_DEPT": "AVEYRON",
                        "INSEE_REG": "76",
                        "POPULATION": 279206,
                        "AREA": 8770.69,
                        "DENSITY": 31.83,
                        "CODE_DEPT1": "12",
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "NOM_DEPT": "CREUSE",
                        "INSEE_REG": "75",
                        "POPULATION": 118638,
                        "AREA": 5589.16,
                        "DENSITY": 21.23,
                        "CODE_DEPT1": "23",
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "NOM_DEPT": "LOIRET",
                        "INSEE_REG": "24",
                        "POPULATION": 678008,
                        "AREA": 6804.01,
                        "DENSITY": 99.65,
                        "CODE_DEPT1": "45",
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "NOM_DEPT": "HAUTE-SAONE",
                        "INSEE_REG": "27",
                        "POPULATION": 236659,
                        "AREA": 5382.37,
                        "DENSITY": 43.97,
                        "CODE_DEPT1": "70",
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "NOM_DEPT": "PUY-DE-DOME",
                        "INSEE_REG": "84",
                        "POPULATION": 653742,
                        "AREA": 8003.1,
                        "DENSITY": 81.69,
                        "CODE_DEPT1": "63",
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "NOM_DEPT": "TARN",
                        "INSEE_REG": "76",
                        "POPULATION": 387890,
                        "AREA": 5785.79,
                        "DENSITY": 67.04,
                        "CODE_DEPT1": "81",
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "NOM_DEPT": "SEINE-MARITIME",
                        "INSEE_REG": "28",
                        "POPULATION": 1254378,
                        "AREA": 6318.26,
                        "DENSITY": 198.53,
                        "CODE_DEPT1": "76",
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "NOM_DEPT": "HAUTE-MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 175640,
                        "AREA": 6249.91,
                        "DENSITY": 28.1,
                        "CODE_DEPT1": "52",
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "NOM_DEPT": "GARD",
                        "INSEE_REG": "76",
                        "POPULATION": 744178,
                        "AREA": 5874.71,
                        "DENSITY": 126.67,
                        "CODE_DEPT1": "30",
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "NOM_DEPT": "BAS-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 1125559,
                        "AREA": 4796.37,
                        "DENSITY": 234.67,
                        "CODE_DEPT1": "67",
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "NOM_DEPT": "AUDE",
                        "INSEE_REG": "76",
                        "POPULATION": 370260,
                        "AREA": 6351.35,
                        "DENSITY": 58.3,
                        "CODE_DEPT1": "11",
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "NOM_DEPT": "SEINE-ET-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1403997,
                        "AREA": 5924.64,
                        "DENSITY": 236.98,
                        "CODE_DEPT1": "77",
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "NOM_DEPT": "SOMME",
                        "INSEE_REG": "32",
                        "POPULATION": 572443,
                        "AREA": 6206.58,
                        "DENSITY": 92.23,
                        "CODE_DEPT1": "80",
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "NOM_DEPT": "HAUTE-LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 227283,
                        "AREA": 4996.58,
                        "DENSITY": 45.49,
                        "CODE_DEPT1": "43",
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "NOM_DEPT": "MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 568895,
                        "AREA": 8195.78,
                        "DENSITY": 69.41,
                        "CODE_DEPT1": "51",
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "NOM_DEPT": "HAUTES-PYRENEES",
                        "INSEE_REG": "76",
                        "POPULATION": 228530,
                        "AREA": 4527.89,
                        "DENSITY": 50.47,
                        "CODE_DEPT1": "65",
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "NOM_DEPT": "LOT",
                        "INSEE_REG": "76",
                        "POPULATION": 173828,
                        "AREA": 5221.64,
                        "DENSITY": 33.29,
                        "CODE_DEPT1": "46",
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "NOM_DEPT": "ALPES-DE-HAUTE-PROVENCE",
                        "INSEE_REG": "93",
                        "POPULATION": 163915,
                        "AREA": 6993.79,
                        "DENSITY": 23.44,
                        "CODE_DEPT1": "04",
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "NOM_DEPT": "SARTHE",
                        "INSEE_REG": "52",
                        "POPULATION": 566506,
                        "AREA": 6236.75,
                        "DENSITY": 90.83,
                        "CODE_DEPT1": "72",
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "INSEE_REG": "53",
                        "POPULATION": 750863,
                        "AREA": 6864.07,
                        "DENSITY": 109.39,
                        "CODE_DEPT1": "56",
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "NOM_DEPT": "EURE-ET-LOIR",
                        "INSEE_REG": "24",
                        "POPULATION": 433233,
                        "AREA": 5927.23,
                        "DENSITY": 73.09,
                        "CODE_DEPT1": "28",
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "NOM_DEPT": "CORSE-DU-SUD",
                        "INSEE_REG": "94",
                        "POPULATION": 157249,
                        "AREA": 4028.53,
                        "DENSITY": 39.03,
                        "CODE_DEPT1": "2A",
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "NOM_DEPT": "MEURTHE-ET-MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 733481,
                        "AREA": 5283.29,
                        "DENSITY": 138.83,
                        "CODE_DEPT1": "54",
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "NOM_DEPT": "ORNE",
                        "INSEE_REG": "28",
                        "POPULATION": 283372,
                        "AREA": 6142.73,
                        "DENSITY": 46.13,
                        "CODE_DEPT1": "61",
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "NOM_DEPT": "AIN",
                        "INSEE_REG": "84",
                        "POPULATION": 643350,
                        "AREA": 5773.77,
                        "DENSITY": 111.43,
                        "CODE_DEPT1": "01",
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "NOM_DEPT": "ARIEGE",
                        "INSEE_REG": "76",
                        "POPULATION": 153153,
                        "AREA": 4921.75,
                        "DENSITY": 31.12,
                        "CODE_DEPT1": "09",
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "NOM_DEPT": "CORREZE",
                        "INSEE_REG": "75",
                        "POPULATION": 241464,
                        "AREA": 5888.93,
                        "DENSITY": 41.0,
                        "CODE_DEPT1": "19",
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "NOM_DEPT": "HAUT-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 764030,
                        "AREA": 3526.37,
                        "DENSITY": 216.66,
                        "CODE_DEPT1": "68",
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "NOM_DEPT": "INDRE-ET-LOIRE",
                        "INSEE_REG": "24",
                        "POPULATION": 606511,
                        "AREA": 6147.6,
                        "DENSITY": 98.66,
                        "CODE_DEPT1": "37",
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "NOM_DEPT": "NORD",
                        "INSEE_REG": "32",
                        "POPULATION": 2604361,
                        "AREA": 5774.99,
                        "DENSITY": 450.97,
                        "CODE_DEPT1": "59",
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "NOM_DEPT": "TERRITOIRE DE BELFORT",
                        "INSEE_REG": "27",
                        "POPULATION": 142622,
                        "AREA": 609.64,
                        "DENSITY": 233.94,
                        "CODE_DEPT1": "90",
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "NOM_DEPT": "LOIRE-ATLANTIQUE",
                        "INSEE_REG": "52",
                        "POPULATION": 1394909,
                        "AREA": 6992.78,
                        "DENSITY": 199.48,
                        "CODE_DEPT1": "44",
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "NOM_DEPT": "YONNE",
                        "INSEE_REG": "27",
                        "POPULATION": 338291,
                        "AREA": 7450.97,
                        "DENSITY": 45.4,
                        "CODE_DEPT1": "89",
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "NOM_DEPT": "ILLE-ET-VILAINE",
                        "INSEE_REG": "53",
                        "POPULATION": 1060199,
                        "AREA": 6830.2,
                        "DENSITY": 155.22,
                        "CODE_DEPT1": "35",
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "NOM_DEPT": "LANDES",
                        "INSEE_REG": "75",
                        "POPULATION": 407444,
                        "AREA": 9353.03,
                        "DENSITY": 43.56,
                        "CODE_DEPT1": "40",
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "NOM_DEPT": "FINISTERE",
                        "INSEE_REG": "53",
                        "POPULATION": 909028,
                        "AREA": 6756.76,
                        "DENSITY": 134.54,
                        "CODE_DEPT1": "29",
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "NOM_DEPT": "HAUTE-SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 807360,
                        "AREA": 4596.53,
                        "DENSITY": 175.65,
                        "CODE_DEPT1": "74",
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "NOM_DEPT": "OISE",
                        "INSEE_REG": "32",
                        "POPULATION": 824503,
                        "AREA": 5893.6,
                        "DENSITY": 139.9,
                        "CODE_DEPT1": "60",
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "INSEE_REG": "11",
                        "POPULATION": 1228618,
                        "AREA": 1254.18,
                        "DENSITY": 979.62,
                        "CODE_DEPT1": "95",
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "NOM_DEPT": "NIEVRE",
                        "INSEE_REG": "27",
                        "POPULATION": 207182,
                        "AREA": 6862.87,
                        "DENSITY": 30.19,
                        "CODE_DEPT1": "58",
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "NOM_DEPT": "COTE-D'OR",
                        "INSEE_REG": "27",
                        "POPULATION": 532871,
                        "AREA": 8787.51,
                        "DENSITY": 60.64,
                        "CODE_DEPT1": "21",
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "NOM_DEPT": "ESSONNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1296130,
                        "AREA": 1818.35,
                        "DENSITY": 712.81,
                        "CODE_DEPT1": "91",
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "NOM_DEPT": "DEUX-SEVRES",
                        "INSEE_REG": "75",
                        "POPULATION": 374351,
                        "AREA": 6029.06,
                        "DENSITY": 62.09,
                        "CODE_DEPT1": "79",
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "NOM_DEPT": "COTES-D'ARMOR",
                        "INSEE_REG": "53",
                        "POPULATION": 598814,
                        "AREA": 6963.26,
                        "DENSITY": 86.0,
                        "CODE_DEPT1": "22",
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "NOM_DEPT": "ALLIER",
                        "INSEE_REG": "84",
                        "POPULATION": 337988,
                        "AREA": 7365.26,
                        "DENSITY": 45.89,
                        "CODE_DEPT1": "03",
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "NOM_DEPT": "CHARENTE-MARITIME",
                        "INSEE_REG": "75",
                        "POPULATION": 644303,
                        "AREA": 6913.03,
                        "DENSITY": 93.2,
                        "CODE_DEPT1": "17",
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "NOM_DEPT": "CANTAL",
                        "INSEE_REG": "84",
                        "POPULATION": 145143,
                        "AREA": 5767.47,
                        "DENSITY": 25.17,
                        "CODE_DEPT1": "15",
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "NOM_DEPT": "HERAULT",
                        "INSEE_REG": "76",
                        "POPULATION": 1144892,
                        "AREA": 6231.05,
                        "DENSITY": 183.74,
                        "CODE_DEPT1": "34",
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "NOM_DEPT": "DROME",
                        "INSEE_REG": "84",
                        "POPULATION": 511553,
                        "AREA": 6553.53,
                        "DENSITY": 78.06,
                        "CODE_DEPT1": "26",
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "NOM_DEPT": "PYRENEES-ORIENTALES",
                        "INSEE_REG": "76",
                        "POPULATION": 474452,
                        "AREA": 4147.76,
                        "DENSITY": 114.39,
                        "CODE_DEPT1": "66",
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "NOM_DEPT": "SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 431174,
                        "AREA": 6260.4,
                        "DENSITY": 68.87,
                        "CODE_DEPT1": "73",
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "NOM_DEPT": "HAUTES-ALPES",
                        "INSEE_REG": "93",
                        "POPULATION": 141284,
                        "AREA": 5685.31,
                        "DENSITY": 24.85,
                        "CODE_DEPT1": "05",
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "NOM_DEPT": "VAUCLUSE",
                        "INSEE_REG": "93",
                        "POPULATION": 559479,
                        "AREA": 3577.19,
                        "DENSITY": 156.4,
                        "CODE_DEPT1": "84",
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "NOM_DEPT": "INDRE",
                        "INSEE_REG": "24",
                        "POPULATION": 222232,
                        "AREA": 6887.38,
                        "DENSITY": 32.27,
                        "CODE_DEPT1": "36",
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "NOM_DEPT": "HAUTE-CORSE",
                        "INSEE_REG": "94",
                        "POPULATION": 177689,
                        "AREA": 4719.71,
                        "DENSITY": 37.65,
                        "CODE_DEPT1": "2B",
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "NOM_DEPT": "HAUTE-VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 374426,
                        "AREA": 5549.31,
                        "DENSITY": 67.47,
                        "CODE_DEPT1": "87",
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "NOM_DEPT": "VENDEE",
                        "INSEE_REG": "52",
                        "POPULATION": 675247,
                        "AREA": 6758.23,
                        "DENSITY": 99.91,
                        "CODE_DEPT1": "85",
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "NOM_DEPT": "VAR",
                        "INSEE_REG": "93",
                        "POPULATION": 1058740,
                        "AREA": 6002.84,
                        "DENSITY": 176.37,
                        "CODE_DEPT1": "83",
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "NOM_DEPT": "VAL-DE-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1387926,
                        "AREA": 244.7,
                        "DENSITY": 5671.95,
                        "CODE_DEPT1": "94",
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "NOM_DEPT": "HAUTS-DE-SEINE",
                        "INSEE_REG": "11",
                        "POPULATION": 1609306,
                        "AREA": 175.63,
                        "DENSITY": 9163.05,
                        "CODE_DEPT1": "92",
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "NOM_DEPT": "LOZERE",
                        "INSEE_REG": "76",
                        "POPULATION": 76601,
                        "AREA": 5172.02,
                        "DENSITY": 14.81,
                        "CODE_DEPT1": "48",
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "NOM_DEPT": "BOUCHES-DU-RHONE",
                        "INSEE_REG": "93",
                        "POPULATION": 2024162,
                        "AREA": 5082.57,
                        "DENSITY": 398.26,
                        "CODE_DEPT1": "13",
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "NOM_DEPT": "PARIS",
                        "INSEE_REG": "11",
                        "POPULATION": 2187526,
                        "AREA": 105.44,
                        "DENSITY": 20746.64,
                        "CODE_DEPT1": "75",
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "NOM_DEPT": "SEINE-SAINT-DENIS",
                        "INSEE_REG": "11",
                        "POPULATION": 1623111,
                        "AREA": 236.96,
                        "DENSITY": 6849.73,
                        "CODE_DEPT1": "93",
                    }
                },
            },
        },
    },
    1: {
        "geolayer_a": geolayer_fr_dept_data_only,
        "geolayer_b": geolayer_fr_dept_population,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_WITH_POPULATION",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_WITH_POPULATION",
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
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "NOM_DEPT": "GERS",
                        "INSEE_REG": "76",
                        "POPULATION": 191091,
                        "AREA": 6304.33,
                        "DENSITY": 30.31,
                        "CODE_DEPT1": "32",
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "NOM_DEPT": "LOT-ET-GARONNE",
                        "INSEE_REG": "75",
                        "POPULATION": 332842,
                        "AREA": 5382.87,
                        "DENSITY": 61.83,
                        "CODE_DEPT1": "47",
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "NOM_DEPT": "ISERE",
                        "INSEE_REG": "84",
                        "POPULATION": 1258722,
                        "AREA": 7868.79,
                        "DENSITY": 159.96,
                        "CODE_DEPT1": "38",
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "NOM_DEPT": "PAS-DE-CALAIS",
                        "INSEE_REG": "32",
                        "POPULATION": 1468018,
                        "AREA": 6714.14,
                        "DENSITY": 218.65,
                        "CODE_DEPT1": "62",
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "NOM_DEPT": "ARDENNES",
                        "INSEE_REG": "44",
                        "POPULATION": 273579,
                        "AREA": 5253.13,
                        "DENSITY": 52.08,
                        "CODE_DEPT1": "08",
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "NOM_DEPT": "AUBE",
                        "INSEE_REG": "44",
                        "POPULATION": 310020,
                        "AREA": 6021.83,
                        "DENSITY": 51.48,
                        "CODE_DEPT1": "10",
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "NOM_DEPT": "ALPES-MARITIMES",
                        "INSEE_REG": "93",
                        "POPULATION": 1083310,
                        "AREA": 4291.62,
                        "DENSITY": 252.42,
                        "CODE_DEPT1": "06",
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "NOM_DEPT": "LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 762941,
                        "AREA": 4795.85,
                        "DENSITY": 159.08,
                        "CODE_DEPT1": "42",
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "NOM_DEPT": "HAUTE-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 1362672,
                        "AREA": 6364.82,
                        "DENSITY": 214.09,
                        "CODE_DEPT1": "31",
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "NOM_DEPT": "SAONE-ET-LOIRE",
                        "INSEE_REG": "27",
                        "POPULATION": 553595,
                        "AREA": 8598.33,
                        "DENSITY": 64.38,
                        "CODE_DEPT1": "71",
                    }
                },
                10: {
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
                11: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "NOM_DEPT": "CHARENTE",
                        "INSEE_REG": "75",
                        "POPULATION": 352335,
                        "AREA": 5963.54,
                        "DENSITY": 59.08,
                        "CODE_DEPT1": "16",
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "NOM_DEPT": "MANCHE",
                        "INSEE_REG": "28",
                        "POPULATION": 496883,
                        "AREA": 6015.07,
                        "DENSITY": 82.61,
                        "CODE_DEPT1": "50",
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "NOM_DEPT": "YVELINES",
                        "INSEE_REG": "11",
                        "POPULATION": 1438266,
                        "AREA": 2305.64,
                        "DENSITY": 623.8,
                        "CODE_DEPT1": "78",
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "NOM_DEPT": "DOUBS",
                        "INSEE_REG": "27",
                        "POPULATION": 539067,
                        "AREA": 5248.31,
                        "DENSITY": 102.71,
                        "CODE_DEPT1": "25",
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "NOM_DEPT": "MEUSE",
                        "INSEE_REG": "44",
                        "POPULATION": 187187,
                        "AREA": 6233.18,
                        "DENSITY": 30.03,
                        "CODE_DEPT1": "55",
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "NOM_DEPT": "GIRONDE",
                        "INSEE_REG": "75",
                        "POPULATION": 1583384,
                        "AREA": 10068.74,
                        "DENSITY": 157.26,
                        "CODE_DEPT1": "33",
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "NOM_DEPT": "CALVADOS",
                        "INSEE_REG": "28",
                        "POPULATION": 694002,
                        "AREA": 5588.48,
                        "DENSITY": 124.18,
                        "CODE_DEPT1": "14",
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "NOM_DEPT": "VOSGES",
                        "INSEE_REG": "44",
                        "POPULATION": 367673,
                        "AREA": 5891.56,
                        "DENSITY": 62.41,
                        "CODE_DEPT1": "88",
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "NOM_DEPT": "CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 304256,
                        "AREA": 7292.67,
                        "DENSITY": 41.72,
                        "CODE_DEPT1": "18",
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "NOM_DEPT": "ARDECHE",
                        "INSEE_REG": "84",
                        "POPULATION": 325712,
                        "AREA": 5562.05,
                        "DENSITY": 58.56,
                        "CODE_DEPT1": "07",
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "INSEE_REG": "32",
                        "POPULATION": 534490,
                        "AREA": 7418.97,
                        "DENSITY": 72.04,
                        "CODE_DEPT1": "02",
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "NOM_DEPT": "PYRENEES-ATLANTIQUES",
                        "INSEE_REG": "75",
                        "POPULATION": 677309,
                        "AREA": 7691.6,
                        "DENSITY": 88.06,
                        "CODE_DEPT1": "64",
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "NOM_DEPT": "LOIR-ET-CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 331915,
                        "AREA": 6412.3,
                        "DENSITY": 51.76,
                        "CODE_DEPT1": "41",
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "NOM_DEPT": "MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 1043522,
                        "AREA": 6252.63,
                        "DENSITY": 166.89,
                        "CODE_DEPT1": "57",
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "NOM_DEPT": "VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 436876,
                        "AREA": 7025.24,
                        "DENSITY": 62.19,
                        "CODE_DEPT1": "86",
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "NOM_DEPT": "DORDOGNE",
                        "INSEE_REG": "75",
                        "POPULATION": 413606,
                        "AREA": 9209.9,
                        "DENSITY": 44.91,
                        "CODE_DEPT1": "24",
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "NOM_DEPT": "JURA",
                        "INSEE_REG": "27",
                        "POPULATION": 260188,
                        "AREA": 5040.63,
                        "DENSITY": 51.62,
                        "CODE_DEPT1": "39",
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "NOM_DEPT": "TARN-ET-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 258349,
                        "AREA": 3731.0,
                        "DENSITY": 69.24,
                        "CODE_DEPT1": "82",
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "NOM_DEPT": "MAINE-ET-LOIRE",
                        "INSEE_REG": "52",
                        "POPULATION": 813493,
                        "AREA": 7161.34,
                        "DENSITY": 113.6,
                        "CODE_DEPT1": "49",
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "NOM_DEPT": "RHONE",
                        "INSEE_REG": "84",
                        "POPULATION": 1843319,
                        "AREA": 3253.11,
                        "DENSITY": 566.63,
                        "CODE_DEPT1": "69",
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "NOM_DEPT": "EURE",
                        "INSEE_REG": "28",
                        "POPULATION": 601843,
                        "AREA": 6035.85,
                        "DENSITY": 99.71,
                        "CODE_DEPT1": "27",
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "NOM_DEPT": "AVEYRON",
                        "INSEE_REG": "76",
                        "POPULATION": 279206,
                        "AREA": 8770.69,
                        "DENSITY": 31.83,
                        "CODE_DEPT1": "12",
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "NOM_DEPT": "CREUSE",
                        "INSEE_REG": "75",
                        "POPULATION": 118638,
                        "AREA": 5589.16,
                        "DENSITY": 21.23,
                        "CODE_DEPT1": "23",
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "NOM_DEPT": "LOIRET",
                        "INSEE_REG": "24",
                        "POPULATION": 678008,
                        "AREA": 6804.01,
                        "DENSITY": 99.65,
                        "CODE_DEPT1": "45",
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "NOM_DEPT": "HAUTE-SAONE",
                        "INSEE_REG": "27",
                        "POPULATION": 236659,
                        "AREA": 5382.37,
                        "DENSITY": 43.97,
                        "CODE_DEPT1": "70",
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "NOM_DEPT": "PUY-DE-DOME",
                        "INSEE_REG": "84",
                        "POPULATION": 653742,
                        "AREA": 8003.1,
                        "DENSITY": 81.69,
                        "CODE_DEPT1": "63",
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "NOM_DEPT": "TARN",
                        "INSEE_REG": "76",
                        "POPULATION": 387890,
                        "AREA": 5785.79,
                        "DENSITY": 67.04,
                        "CODE_DEPT1": "81",
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "NOM_DEPT": "SEINE-MARITIME",
                        "INSEE_REG": "28",
                        "POPULATION": 1254378,
                        "AREA": 6318.26,
                        "DENSITY": 198.53,
                        "CODE_DEPT1": "76",
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "NOM_DEPT": "HAUTE-MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 175640,
                        "AREA": 6249.91,
                        "DENSITY": 28.1,
                        "CODE_DEPT1": "52",
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "NOM_DEPT": "GARD",
                        "INSEE_REG": "76",
                        "POPULATION": 744178,
                        "AREA": 5874.71,
                        "DENSITY": 126.67,
                        "CODE_DEPT1": "30",
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "NOM_DEPT": "BAS-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 1125559,
                        "AREA": 4796.37,
                        "DENSITY": 234.67,
                        "CODE_DEPT1": "67",
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "NOM_DEPT": "AUDE",
                        "INSEE_REG": "76",
                        "POPULATION": 370260,
                        "AREA": 6351.35,
                        "DENSITY": 58.3,
                        "CODE_DEPT1": "11",
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "NOM_DEPT": "SEINE-ET-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1403997,
                        "AREA": 5924.64,
                        "DENSITY": 236.98,
                        "CODE_DEPT1": "77",
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "NOM_DEPT": "SOMME",
                        "INSEE_REG": "32",
                        "POPULATION": 572443,
                        "AREA": 6206.58,
                        "DENSITY": 92.23,
                        "CODE_DEPT1": "80",
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "NOM_DEPT": "HAUTE-LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 227283,
                        "AREA": 4996.58,
                        "DENSITY": 45.49,
                        "CODE_DEPT1": "43",
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "NOM_DEPT": "MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 568895,
                        "AREA": 8195.78,
                        "DENSITY": 69.41,
                        "CODE_DEPT1": "51",
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "NOM_DEPT": "HAUTES-PYRENEES",
                        "INSEE_REG": "76",
                        "POPULATION": 228530,
                        "AREA": 4527.89,
                        "DENSITY": 50.47,
                        "CODE_DEPT1": "65",
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "NOM_DEPT": "LOT",
                        "INSEE_REG": "76",
                        "POPULATION": 173828,
                        "AREA": 5221.64,
                        "DENSITY": 33.29,
                        "CODE_DEPT1": "46",
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "NOM_DEPT": "ALPES-DE-HAUTE-PROVENCE",
                        "INSEE_REG": "93",
                        "POPULATION": 163915,
                        "AREA": 6993.79,
                        "DENSITY": 23.44,
                        "CODE_DEPT1": "04",
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "NOM_DEPT": "SARTHE",
                        "INSEE_REG": "52",
                        "POPULATION": 566506,
                        "AREA": 6236.75,
                        "DENSITY": 90.83,
                        "CODE_DEPT1": "72",
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "INSEE_REG": "53",
                        "POPULATION": 750863,
                        "AREA": 6864.07,
                        "DENSITY": 109.39,
                        "CODE_DEPT1": "56",
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "NOM_DEPT": "EURE-ET-LOIR",
                        "INSEE_REG": "24",
                        "POPULATION": 433233,
                        "AREA": 5927.23,
                        "DENSITY": 73.09,
                        "CODE_DEPT1": "28",
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "NOM_DEPT": "CORSE-DU-SUD",
                        "INSEE_REG": "94",
                        "POPULATION": 157249,
                        "AREA": 4028.53,
                        "DENSITY": 39.03,
                        "CODE_DEPT1": "2A",
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "NOM_DEPT": "MEURTHE-ET-MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 733481,
                        "AREA": 5283.29,
                        "DENSITY": 138.83,
                        "CODE_DEPT1": "54",
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "NOM_DEPT": "ORNE",
                        "INSEE_REG": "28",
                        "POPULATION": 283372,
                        "AREA": 6142.73,
                        "DENSITY": 46.13,
                        "CODE_DEPT1": "61",
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "NOM_DEPT": "AIN",
                        "INSEE_REG": "84",
                        "POPULATION": 643350,
                        "AREA": 5773.77,
                        "DENSITY": 111.43,
                        "CODE_DEPT1": "01",
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "NOM_DEPT": "ARIEGE",
                        "INSEE_REG": "76",
                        "POPULATION": 153153,
                        "AREA": 4921.75,
                        "DENSITY": 31.12,
                        "CODE_DEPT1": "09",
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "NOM_DEPT": "CORREZE",
                        "INSEE_REG": "75",
                        "POPULATION": 241464,
                        "AREA": 5888.93,
                        "DENSITY": 41.0,
                        "CODE_DEPT1": "19",
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "NOM_DEPT": "HAUT-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 764030,
                        "AREA": 3526.37,
                        "DENSITY": 216.66,
                        "CODE_DEPT1": "68",
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "NOM_DEPT": "INDRE-ET-LOIRE",
                        "INSEE_REG": "24",
                        "POPULATION": 606511,
                        "AREA": 6147.6,
                        "DENSITY": 98.66,
                        "CODE_DEPT1": "37",
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "NOM_DEPT": "NORD",
                        "INSEE_REG": "32",
                        "POPULATION": 2604361,
                        "AREA": 5774.99,
                        "DENSITY": 450.97,
                        "CODE_DEPT1": "59",
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "NOM_DEPT": "TERRITOIRE DE BELFORT",
                        "INSEE_REG": "27",
                        "POPULATION": 142622,
                        "AREA": 609.64,
                        "DENSITY": 233.94,
                        "CODE_DEPT1": "90",
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "NOM_DEPT": "LOIRE-ATLANTIQUE",
                        "INSEE_REG": "52",
                        "POPULATION": 1394909,
                        "AREA": 6992.78,
                        "DENSITY": 199.48,
                        "CODE_DEPT1": "44",
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "NOM_DEPT": "YONNE",
                        "INSEE_REG": "27",
                        "POPULATION": 338291,
                        "AREA": 7450.97,
                        "DENSITY": 45.4,
                        "CODE_DEPT1": "89",
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "NOM_DEPT": "ILLE-ET-VILAINE",
                        "INSEE_REG": "53",
                        "POPULATION": 1060199,
                        "AREA": 6830.2,
                        "DENSITY": 155.22,
                        "CODE_DEPT1": "35",
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "NOM_DEPT": "LANDES",
                        "INSEE_REG": "75",
                        "POPULATION": 407444,
                        "AREA": 9353.03,
                        "DENSITY": 43.56,
                        "CODE_DEPT1": "40",
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "NOM_DEPT": "FINISTERE",
                        "INSEE_REG": "53",
                        "POPULATION": 909028,
                        "AREA": 6756.76,
                        "DENSITY": 134.54,
                        "CODE_DEPT1": "29",
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "NOM_DEPT": "HAUTE-SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 807360,
                        "AREA": 4596.53,
                        "DENSITY": 175.65,
                        "CODE_DEPT1": "74",
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "NOM_DEPT": "OISE",
                        "INSEE_REG": "32",
                        "POPULATION": 824503,
                        "AREA": 5893.6,
                        "DENSITY": 139.9,
                        "CODE_DEPT1": "60",
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "INSEE_REG": "11",
                        "POPULATION": 1228618,
                        "AREA": 1254.18,
                        "DENSITY": 979.62,
                        "CODE_DEPT1": "95",
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "NOM_DEPT": "NIEVRE",
                        "INSEE_REG": "27",
                        "POPULATION": 207182,
                        "AREA": 6862.87,
                        "DENSITY": 30.19,
                        "CODE_DEPT1": "58",
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "NOM_DEPT": "COTE-D'OR",
                        "INSEE_REG": "27",
                        "POPULATION": 532871,
                        "AREA": 8787.51,
                        "DENSITY": 60.64,
                        "CODE_DEPT1": "21",
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "NOM_DEPT": "ESSONNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1296130,
                        "AREA": 1818.35,
                        "DENSITY": 712.81,
                        "CODE_DEPT1": "91",
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "NOM_DEPT": "DEUX-SEVRES",
                        "INSEE_REG": "75",
                        "POPULATION": 374351,
                        "AREA": 6029.06,
                        "DENSITY": 62.09,
                        "CODE_DEPT1": "79",
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "NOM_DEPT": "COTES-D'ARMOR",
                        "INSEE_REG": "53",
                        "POPULATION": 598814,
                        "AREA": 6963.26,
                        "DENSITY": 86.0,
                        "CODE_DEPT1": "22",
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "NOM_DEPT": "ALLIER",
                        "INSEE_REG": "84",
                        "POPULATION": 337988,
                        "AREA": 7365.26,
                        "DENSITY": 45.89,
                        "CODE_DEPT1": "03",
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "NOM_DEPT": "CHARENTE-MARITIME",
                        "INSEE_REG": "75",
                        "POPULATION": 644303,
                        "AREA": 6913.03,
                        "DENSITY": 93.2,
                        "CODE_DEPT1": "17",
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "NOM_DEPT": "CANTAL",
                        "INSEE_REG": "84",
                        "POPULATION": 145143,
                        "AREA": 5767.47,
                        "DENSITY": 25.17,
                        "CODE_DEPT1": "15",
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "NOM_DEPT": "HERAULT",
                        "INSEE_REG": "76",
                        "POPULATION": 1144892,
                        "AREA": 6231.05,
                        "DENSITY": 183.74,
                        "CODE_DEPT1": "34",
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "NOM_DEPT": "DROME",
                        "INSEE_REG": "84",
                        "POPULATION": 511553,
                        "AREA": 6553.53,
                        "DENSITY": 78.06,
                        "CODE_DEPT1": "26",
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "NOM_DEPT": "PYRENEES-ORIENTALES",
                        "INSEE_REG": "76",
                        "POPULATION": 474452,
                        "AREA": 4147.76,
                        "DENSITY": 114.39,
                        "CODE_DEPT1": "66",
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "NOM_DEPT": "SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 431174,
                        "AREA": 6260.4,
                        "DENSITY": 68.87,
                        "CODE_DEPT1": "73",
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "NOM_DEPT": "HAUTES-ALPES",
                        "INSEE_REG": "93",
                        "POPULATION": 141284,
                        "AREA": 5685.31,
                        "DENSITY": 24.85,
                        "CODE_DEPT1": "05",
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "NOM_DEPT": "VAUCLUSE",
                        "INSEE_REG": "93",
                        "POPULATION": 559479,
                        "AREA": 3577.19,
                        "DENSITY": 156.4,
                        "CODE_DEPT1": "84",
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "NOM_DEPT": "INDRE",
                        "INSEE_REG": "24",
                        "POPULATION": 222232,
                        "AREA": 6887.38,
                        "DENSITY": 32.27,
                        "CODE_DEPT1": "36",
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "NOM_DEPT": "HAUTE-CORSE",
                        "INSEE_REG": "94",
                        "POPULATION": 177689,
                        "AREA": 4719.71,
                        "DENSITY": 37.65,
                        "CODE_DEPT1": "2B",
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "NOM_DEPT": "HAUTE-VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 374426,
                        "AREA": 5549.31,
                        "DENSITY": 67.47,
                        "CODE_DEPT1": "87",
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "NOM_DEPT": "VENDEE",
                        "INSEE_REG": "52",
                        "POPULATION": 675247,
                        "AREA": 6758.23,
                        "DENSITY": 99.91,
                        "CODE_DEPT1": "85",
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "NOM_DEPT": "VAR",
                        "INSEE_REG": "93",
                        "POPULATION": 1058740,
                        "AREA": 6002.84,
                        "DENSITY": 176.37,
                        "CODE_DEPT1": "83",
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "NOM_DEPT": "VAL-DE-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1387926,
                        "AREA": 244.7,
                        "DENSITY": 5671.95,
                        "CODE_DEPT1": "94",
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "NOM_DEPT": "HAUTS-DE-SEINE",
                        "INSEE_REG": "11",
                        "POPULATION": 1609306,
                        "AREA": 175.63,
                        "DENSITY": 9163.05,
                        "CODE_DEPT1": "92",
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "NOM_DEPT": "LOZERE",
                        "INSEE_REG": "76",
                        "POPULATION": 76601,
                        "AREA": 5172.02,
                        "DENSITY": 14.81,
                        "CODE_DEPT1": "48",
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "NOM_DEPT": "BOUCHES-DU-RHONE",
                        "INSEE_REG": "93",
                        "POPULATION": 2024162,
                        "AREA": 5082.57,
                        "DENSITY": 398.26,
                        "CODE_DEPT1": "13",
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "NOM_DEPT": "PARIS",
                        "INSEE_REG": "11",
                        "POPULATION": 2187526,
                        "AREA": 105.44,
                        "DENSITY": 20746.64,
                        "CODE_DEPT1": "75",
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "NOM_DEPT": "SEINE-SAINT-DENIS",
                        "INSEE_REG": "11",
                        "POPULATION": 1623111,
                        "AREA": 236.96,
                        "DENSITY": 6849.73,
                        "CODE_DEPT1": "93",
                    }
                },
            },
        },
    },
    2: {
        "geolayer_a": geolayer_fr_dept_data_only,
        "geolayer_b": geolayer_fr_dept_population,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_WITH_POPULATION",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_WITH_POPULATION",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "NOM_DEPT": "GERS",
                        "POPULATION": 191091,
                        "DENSITY": 30.31,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "NOM_DEPT": "LOT-ET-GARONNE",
                        "POPULATION": 332842,
                        "DENSITY": 61.83,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "NOM_DEPT": "ISERE",
                        "POPULATION": 1258722,
                        "DENSITY": 159.96,
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "NOM_DEPT": "PAS-DE-CALAIS",
                        "POPULATION": 1468018,
                        "DENSITY": 218.65,
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "NOM_DEPT": "ARDENNES",
                        "POPULATION": 273579,
                        "DENSITY": 52.08,
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "NOM_DEPT": "AUBE",
                        "POPULATION": 310020,
                        "DENSITY": 51.48,
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "NOM_DEPT": "ALPES-MARITIMES",
                        "POPULATION": 1083310,
                        "DENSITY": 252.42,
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "NOM_DEPT": "LOIRE",
                        "POPULATION": 762941,
                        "DENSITY": 159.08,
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "NOM_DEPT": "HAUTE-GARONNE",
                        "POPULATION": 1362672,
                        "DENSITY": 214.09,
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "NOM_DEPT": "SAONE-ET-LOIRE",
                        "POPULATION": 553595,
                        "DENSITY": 64.38,
                    }
                },
                10: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "NOM_DEPT": "MAYENNE",
                        "POPULATION": 307445,
                        "DENSITY": 59.03,
                    }
                },
                11: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "NOM_DEPT": "CHARENTE",
                        "POPULATION": 352335,
                        "DENSITY": 59.08,
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "NOM_DEPT": "MANCHE",
                        "POPULATION": 496883,
                        "DENSITY": 82.61,
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "NOM_DEPT": "YVELINES",
                        "POPULATION": 1438266,
                        "DENSITY": 623.8,
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "NOM_DEPT": "DOUBS",
                        "POPULATION": 539067,
                        "DENSITY": 102.71,
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "NOM_DEPT": "MEUSE",
                        "POPULATION": 187187,
                        "DENSITY": 30.03,
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "NOM_DEPT": "GIRONDE",
                        "POPULATION": 1583384,
                        "DENSITY": 157.26,
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "NOM_DEPT": "CALVADOS",
                        "POPULATION": 694002,
                        "DENSITY": 124.18,
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "NOM_DEPT": "VOSGES",
                        "POPULATION": 367673,
                        "DENSITY": 62.41,
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "NOM_DEPT": "CHER",
                        "POPULATION": 304256,
                        "DENSITY": 41.72,
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "NOM_DEPT": "ARDECHE",
                        "POPULATION": 325712,
                        "DENSITY": 58.56,
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "NOM_DEPT": "PYRENEES-ATLANTIQUES",
                        "POPULATION": 677309,
                        "DENSITY": 88.06,
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "NOM_DEPT": "LOIR-ET-CHER",
                        "POPULATION": 331915,
                        "DENSITY": 51.76,
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "NOM_DEPT": "MOSELLE",
                        "POPULATION": 1043522,
                        "DENSITY": 166.89,
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "NOM_DEPT": "VIENNE",
                        "POPULATION": 436876,
                        "DENSITY": 62.19,
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "NOM_DEPT": "DORDOGNE",
                        "POPULATION": 413606,
                        "DENSITY": 44.91,
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "NOM_DEPT": "JURA",
                        "POPULATION": 260188,
                        "DENSITY": 51.62,
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "NOM_DEPT": "TARN-ET-GARONNE",
                        "POPULATION": 258349,
                        "DENSITY": 69.24,
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "NOM_DEPT": "MAINE-ET-LOIRE",
                        "POPULATION": 813493,
                        "DENSITY": 113.6,
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "NOM_DEPT": "RHONE",
                        "POPULATION": 1843319,
                        "DENSITY": 566.63,
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "NOM_DEPT": "EURE",
                        "POPULATION": 601843,
                        "DENSITY": 99.71,
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "NOM_DEPT": "AVEYRON",
                        "POPULATION": 279206,
                        "DENSITY": 31.83,
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "NOM_DEPT": "CREUSE",
                        "POPULATION": 118638,
                        "DENSITY": 21.23,
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "NOM_DEPT": "LOIRET",
                        "POPULATION": 678008,
                        "DENSITY": 99.65,
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "NOM_DEPT": "HAUTE-SAONE",
                        "POPULATION": 236659,
                        "DENSITY": 43.97,
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "NOM_DEPT": "PUY-DE-DOME",
                        "POPULATION": 653742,
                        "DENSITY": 81.69,
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "NOM_DEPT": "TARN",
                        "POPULATION": 387890,
                        "DENSITY": 67.04,
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "NOM_DEPT": "SEINE-MARITIME",
                        "POPULATION": 1254378,
                        "DENSITY": 198.53,
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "NOM_DEPT": "HAUTE-MARNE",
                        "POPULATION": 175640,
                        "DENSITY": 28.1,
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "NOM_DEPT": "GARD",
                        "POPULATION": 744178,
                        "DENSITY": 126.67,
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "NOM_DEPT": "BAS-RHIN",
                        "POPULATION": 1125559,
                        "DENSITY": 234.67,
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "NOM_DEPT": "AUDE",
                        "POPULATION": 370260,
                        "DENSITY": 58.3,
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "NOM_DEPT": "SEINE-ET-MARNE",
                        "POPULATION": 1403997,
                        "DENSITY": 236.98,
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "NOM_DEPT": "SOMME",
                        "POPULATION": 572443,
                        "DENSITY": 92.23,
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "NOM_DEPT": "HAUTE-LOIRE",
                        "POPULATION": 227283,
                        "DENSITY": 45.49,
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "NOM_DEPT": "MARNE",
                        "POPULATION": 568895,
                        "DENSITY": 69.41,
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "NOM_DEPT": "HAUTES-PYRENEES",
                        "POPULATION": 228530,
                        "DENSITY": 50.47,
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "NOM_DEPT": "LOT",
                        "POPULATION": 173828,
                        "DENSITY": 33.29,
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "NOM_DEPT": "ALPES-DE-HAUTE-PROVENCE",
                        "POPULATION": 163915,
                        "DENSITY": 23.44,
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "NOM_DEPT": "SARTHE",
                        "POPULATION": 566506,
                        "DENSITY": 90.83,
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "NOM_DEPT": "EURE-ET-LOIR",
                        "POPULATION": 433233,
                        "DENSITY": 73.09,
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "NOM_DEPT": "CORSE-DU-SUD",
                        "POPULATION": 157249,
                        "DENSITY": 39.03,
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "NOM_DEPT": "MEURTHE-ET-MOSELLE",
                        "POPULATION": 733481,
                        "DENSITY": 138.83,
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "NOM_DEPT": "ORNE",
                        "POPULATION": 283372,
                        "DENSITY": 46.13,
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "NOM_DEPT": "AIN",
                        "POPULATION": 643350,
                        "DENSITY": 111.43,
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "NOM_DEPT": "ARIEGE",
                        "POPULATION": 153153,
                        "DENSITY": 31.12,
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "NOM_DEPT": "CORREZE",
                        "POPULATION": 241464,
                        "DENSITY": 41.0,
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "NOM_DEPT": "HAUT-RHIN",
                        "POPULATION": 764030,
                        "DENSITY": 216.66,
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "NOM_DEPT": "INDRE-ET-LOIRE",
                        "POPULATION": 606511,
                        "DENSITY": 98.66,
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "NOM_DEPT": "NORD",
                        "POPULATION": 2604361,
                        "DENSITY": 450.97,
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "NOM_DEPT": "TERRITOIRE DE BELFORT",
                        "POPULATION": 142622,
                        "DENSITY": 233.94,
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "NOM_DEPT": "LOIRE-ATLANTIQUE",
                        "POPULATION": 1394909,
                        "DENSITY": 199.48,
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "NOM_DEPT": "YONNE",
                        "POPULATION": 338291,
                        "DENSITY": 45.4,
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "NOM_DEPT": "ILLE-ET-VILAINE",
                        "POPULATION": 1060199,
                        "DENSITY": 155.22,
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "NOM_DEPT": "LANDES",
                        "POPULATION": 407444,
                        "DENSITY": 43.56,
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "NOM_DEPT": "FINISTERE",
                        "POPULATION": 909028,
                        "DENSITY": 134.54,
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "NOM_DEPT": "HAUTE-SAVOIE",
                        "POPULATION": 807360,
                        "DENSITY": 175.65,
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "NOM_DEPT": "OISE",
                        "POPULATION": 824503,
                        "DENSITY": 139.9,
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "NOM_DEPT": "NIEVRE",
                        "POPULATION": 207182,
                        "DENSITY": 30.19,
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "NOM_DEPT": "COTE-D'OR",
                        "POPULATION": 532871,
                        "DENSITY": 60.64,
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "NOM_DEPT": "ESSONNE",
                        "POPULATION": 1296130,
                        "DENSITY": 712.81,
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "NOM_DEPT": "DEUX-SEVRES",
                        "POPULATION": 374351,
                        "DENSITY": 62.09,
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "NOM_DEPT": "COTES-D'ARMOR",
                        "POPULATION": 598814,
                        "DENSITY": 86.0,
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "NOM_DEPT": "ALLIER",
                        "POPULATION": 337988,
                        "DENSITY": 45.89,
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "NOM_DEPT": "CHARENTE-MARITIME",
                        "POPULATION": 644303,
                        "DENSITY": 93.2,
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "NOM_DEPT": "CANTAL",
                        "POPULATION": 145143,
                        "DENSITY": 25.17,
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "NOM_DEPT": "HERAULT",
                        "POPULATION": 1144892,
                        "DENSITY": 183.74,
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "NOM_DEPT": "DROME",
                        "POPULATION": 511553,
                        "DENSITY": 78.06,
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "NOM_DEPT": "PYRENEES-ORIENTALES",
                        "POPULATION": 474452,
                        "DENSITY": 114.39,
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "NOM_DEPT": "SAVOIE",
                        "POPULATION": 431174,
                        "DENSITY": 68.87,
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "NOM_DEPT": "HAUTES-ALPES",
                        "POPULATION": 141284,
                        "DENSITY": 24.85,
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "NOM_DEPT": "VAUCLUSE",
                        "POPULATION": 559479,
                        "DENSITY": 156.4,
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "NOM_DEPT": "INDRE",
                        "POPULATION": 222232,
                        "DENSITY": 32.27,
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "NOM_DEPT": "HAUTE-CORSE",
                        "POPULATION": 177689,
                        "DENSITY": 37.65,
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "NOM_DEPT": "HAUTE-VIENNE",
                        "POPULATION": 374426,
                        "DENSITY": 67.47,
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "NOM_DEPT": "VENDEE",
                        "POPULATION": 675247,
                        "DENSITY": 99.91,
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "NOM_DEPT": "VAR",
                        "POPULATION": 1058740,
                        "DENSITY": 176.37,
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "NOM_DEPT": "VAL-DE-MARNE",
                        "POPULATION": 1387926,
                        "DENSITY": 5671.95,
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "NOM_DEPT": "HAUTS-DE-SEINE",
                        "POPULATION": 1609306,
                        "DENSITY": 9163.05,
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "NOM_DEPT": "LOZERE",
                        "POPULATION": 76601,
                        "DENSITY": 14.81,
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "NOM_DEPT": "BOUCHES-DU-RHONE",
                        "POPULATION": 2024162,
                        "DENSITY": 398.26,
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "NOM_DEPT": "PARIS",
                        "POPULATION": 2187526,
                        "DENSITY": 20746.64,
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "NOM_DEPT": "SEINE-SAINT-DENIS",
                        "POPULATION": 1623111,
                        "DENSITY": 6849.73,
                    }
                },
            },
        },
    },
    3: {
        "geolayer_a": geolayer_fr_dept_data_and_geometry,
        "geolayer_b": geolayer_fr_dept_population,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_WITH_POPULATION",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": geolayer_fr_dept_population_geometry,
    },
    4: {
        "geolayer_a": geolayer_dpt_full,
        "geolayer_b": geolayer_dpt_pop_2,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_FULL_LEFT_JOIN_POP_2",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_FULL_LEFT_JOIN_POP_2",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "NOM_DEPT": "MAYENNE",
                        "POPULATION": 307445,
                        "DENSITY": 59.03,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
            },
        },
    },
    5: {
        "geolayer_a": geolayer_dpt_full_with_duplicate,
        "geolayer_b": geolayer_dpt_pop_2,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_FULL_WITH_DUPLICATE_LEFT_JOIN_POP_2",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_FULL_WITH_DUPLICATE_LEFT_JOIN_POP_2",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "NOM_DEPT": "MAYENNE",
                        "POPULATION": 307445,
                        "DENSITY": 59.03,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
            },
        },
    },
    6: {
        "geolayer_a": geolayer_dpt_2,
        "geolayer_b": geolayer_dpt_pop_full,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_LEFT_JOIN_POP_FULL",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_LEFT_JOIN_POP_FULL",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
            },
        },
    },
    7: {
        "geolayer_a": geolayer_dpt_2,
        "geolayer_b": geolayer_dpt_pop_full_with_duplicate,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_LEFT_JOIN_POP_FULL_WITH_DUPLICATE",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_LEFT_JOIN_POP_FULL_WITH_DUPLICATE",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
            },
        },
    },
    8: {
        "geolayer_a": geolayer_dpt_2,
        "geolayer_b": geolayer_dpt_pop_2,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_JOIN_POP_2",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_JOIN_POP_2",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {},
        },
    },
    9: {
        "geolayer_a": geolayer_dpt_2_with_geom,
        "geolayer_b": geolayer_dpt_pop_full,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_JOIN_POP_FULL",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_JOIN_POP_FULL",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6861428.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                    },
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                    },
                },
            },
        },
    },
    10: {
        "geolayer_a": geolayer_dpt_2_with_geom,
        "geolayer_b": geolayer_dpt_pop_full,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_JOIN_POP_FULL",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_JOIN_POP_FULL",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
            },
        },
    },
    11: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2_with_geom,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_JOIN_POP_FULL",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_JOIN_POP_FULL",
                "fields": {
                    "POPULATION": {"type": "Integer", "index": 0},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 3},
                },
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6861428.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                    },
                },
                1: {
                    "attributes": {
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                    },
                },
            },
        },
    },
    12: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2_with_geom,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_JOIN_POP_FULL",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": {"POPULATION": "pop"},
        "rename_output_field_from_geolayer_b": {"CODE_DEPT": "id"},
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_JOIN_POP_FULL",
                "fields": {
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "pop": {"type": "Integer", "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 2},
                    "id": {"type": "String", "width": 2, "index": 3},
                },
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6861428.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "DENSITY": 72.04,
                        "pop": 534490,
                        "NOM_DEPT": "AISNE",
                        "id": "02",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                    },
                },
                1: {
                    "attributes": {
                        "DENSITY": 979.62,
                        "pop": 1228618,
                        "NOM_DEPT": "VAL-D'OISE",
                        "id": "95",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                    },
                },
            },
        },
    },
    13: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2_with_geom,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_JOIN_POP_FULL",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": {
            "CODE_DEPT": "code",
            "POPULATION": "pop",
        },
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": field_missing.format(field_name="CODE_DEPT"),
    },
    14: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "key_id": {"type": "Integer", "index": 0},
                    "price": {"type": "Integer", "index": 1},
                    "count": {"type": "Integer", "index": 2},
                    "probability": {
                        "type": "Real",
                        "width": 1,
                        "precision": 0,
                        "index": 3,
                    },
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "key_id": 164,
                        "price": 4300,
                        "count": 0,
                        "probability": 0.0,
                    }
                }
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "key_id": {"type": "Integer", "index": 0},
                    "price": {"type": "Integer", "index": 1},
                    "count": {"type": "Integer", "index": 2},
                    "probability": {
                        "type": "Real",
                        "width": 1,
                        "precision": 1,
                        "index": 3,
                    },
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "key_id": 0,
                        "price": 5000,
                        "count": 1,
                        "probability": 0.1,
                    }
                },
                1: {
                    "attributes": {
                        "key_id": 164,
                        "price": 4300,
                        "count": 1,
                        "probability": 0.1,
                    }
                },
            },
        },
        "on_field_a": "key_id",
        "on_field_b": "key_id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": {
            "key_id": "key_id_b",
            "price": "price_b",
            "count": "count_b",
            "probability": "probability_b",
        },
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "key_id": {"type": "Integer", "index": 0},
                    "price": {"type": "Integer", "index": 1},
                    "count": {"type": "Integer", "index": 2},
                    "probability": {
                        "type": "Real",
                        "width": 1,
                        "precision": 0,
                        "index": 3,
                    },
                    "key_id_b": {"type": "Integer", "index": 4},
                    "price_b": {"type": "Integer", "index": 5},
                    "count_b": {"type": "Integer", "index": 6},
                    "probability_b": {
                        "type": "Real",
                        "width": 1,
                        "precision": 1,
                        "index": 7,
                    },
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "key_id": 164,
                        "price": 4300,
                        "count": 0,
                        "probability": 0.0,
                        "key_id_b": 164,
                        "price_b": 4300,
                        "count_b": 1,
                        "probability_b": 0.1,
                    }
                }
            },
        },
    },
    15: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice"}},
                1: {"attributes": {"id": None, "name": "Bob"}},
                2: {"attributes": {"id": None, "name": "Patrick"}},
                3: {"attributes": {"id": 1, "name": "Jane"}},
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "age": {"type": "Integer", "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "age": 28}},
                1: {"attributes": {"id": 1, "age": 2}},
            },
        },
        "on_field_a": "id",
        "on_field_b": "id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                    "id1": {"type": "Integer", "index": 2},
                    "age": {"type": "Integer", "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice", "id1": 0, "age": 28}},
                1: {"attributes": {"id": 1, "name": "Jane", "id1": 1, "age": 2}},
            },
        },
    },
    16: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 5, "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice"}},
                1: {"attributes": {"id": 1, "name": "Jane"}},
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "age": {"type": "Integer", "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "age": 28}},
                1: {"attributes": {"id": None, "age": 67}},
                2: {"attributes": {"id": None, "age": 15}},
                3: {"attributes": {"id": 1, "age": 2}},
            },
        },
        "on_field_a": "id",
        "on_field_b": "id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 5, "index": 1},
                    "id1": {"type": "Integer", "index": 2},
                    "age": {"type": "Integer", "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice", "id1": 0, "age": 28}},
                1: {"attributes": {"id": 1, "name": "Jane", "id1": 1, "age": 2}},
            },
        },
    },
    17: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice"}},
                1: {"attributes": {"id": None, "name": "Bob"}},
                2: {"attributes": {"id": None, "name": "Patrick"}},
                3: {"attributes": {"id": 1, "name": "Jane"}},
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "age": {"type": "Integer", "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "age": 28}},
                1: {"attributes": {"id": None, "age": 67}},
                2: {"attributes": {"id": None, "age": 15}},
                3: {"attributes": {"id": 1, "age": 2}},
            },
        },
        "on_field_a": "id",
        "on_field_b": "id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                    "id1": {"type": "Integer", "index": 2},
                    "age": {"type": "Integer", "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice", "id1": 0, "age": 28}},
                1: {"attributes": {"id": 1, "name": "Jane", "id1": 1, "age": 2}},
            },
        },
    },
}

join_left_parameters = {
    0: {
        "geolayer_a": geolayer_fr_dept_data_only,
        "geolayer_b": geolayer_fr_dept_population,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_ONLY",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_ONLY",
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
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "NOM_DEPT": "GERS",
                        "INSEE_REG": "76",
                        "POPULATION": 191091,
                        "AREA": 6304.33,
                        "DENSITY": 30.31,
                        "CODE_DEPT1": "32",
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "NOM_DEPT": "LOT-ET-GARONNE",
                        "INSEE_REG": "75",
                        "POPULATION": 332842,
                        "AREA": 5382.87,
                        "DENSITY": 61.83,
                        "CODE_DEPT1": "47",
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "NOM_DEPT": "ISERE",
                        "INSEE_REG": "84",
                        "POPULATION": 1258722,
                        "AREA": 7868.79,
                        "DENSITY": 159.96,
                        "CODE_DEPT1": "38",
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "NOM_DEPT": "PAS-DE-CALAIS",
                        "INSEE_REG": "32",
                        "POPULATION": 1468018,
                        "AREA": 6714.14,
                        "DENSITY": 218.65,
                        "CODE_DEPT1": "62",
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "NOM_DEPT": "ARDENNES",
                        "INSEE_REG": "44",
                        "POPULATION": 273579,
                        "AREA": 5253.13,
                        "DENSITY": 52.08,
                        "CODE_DEPT1": "08",
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "NOM_DEPT": "AUBE",
                        "INSEE_REG": "44",
                        "POPULATION": 310020,
                        "AREA": 6021.83,
                        "DENSITY": 51.48,
                        "CODE_DEPT1": "10",
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "NOM_DEPT": "ALPES-MARITIMES",
                        "INSEE_REG": "93",
                        "POPULATION": 1083310,
                        "AREA": 4291.62,
                        "DENSITY": 252.42,
                        "CODE_DEPT1": "06",
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "NOM_DEPT": "LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 762941,
                        "AREA": 4795.85,
                        "DENSITY": 159.08,
                        "CODE_DEPT1": "42",
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "NOM_DEPT": "HAUTE-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 1362672,
                        "AREA": 6364.82,
                        "DENSITY": 214.09,
                        "CODE_DEPT1": "31",
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "NOM_DEPT": "SAONE-ET-LOIRE",
                        "INSEE_REG": "27",
                        "POPULATION": 553595,
                        "AREA": 8598.33,
                        "DENSITY": 64.38,
                        "CODE_DEPT1": "71",
                    }
                },
                10: {
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
                11: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "NOM_DEPT": "CHARENTE",
                        "INSEE_REG": "75",
                        "POPULATION": 352335,
                        "AREA": 5963.54,
                        "DENSITY": 59.08,
                        "CODE_DEPT1": "16",
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "NOM_DEPT": "MANCHE",
                        "INSEE_REG": "28",
                        "POPULATION": 496883,
                        "AREA": 6015.07,
                        "DENSITY": 82.61,
                        "CODE_DEPT1": "50",
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "NOM_DEPT": "YVELINES",
                        "INSEE_REG": "11",
                        "POPULATION": 1438266,
                        "AREA": 2305.64,
                        "DENSITY": 623.8,
                        "CODE_DEPT1": "78",
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "NOM_DEPT": "DOUBS",
                        "INSEE_REG": "27",
                        "POPULATION": 539067,
                        "AREA": 5248.31,
                        "DENSITY": 102.71,
                        "CODE_DEPT1": "25",
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "NOM_DEPT": "MEUSE",
                        "INSEE_REG": "44",
                        "POPULATION": 187187,
                        "AREA": 6233.18,
                        "DENSITY": 30.03,
                        "CODE_DEPT1": "55",
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "NOM_DEPT": "GIRONDE",
                        "INSEE_REG": "75",
                        "POPULATION": 1583384,
                        "AREA": 10068.74,
                        "DENSITY": 157.26,
                        "CODE_DEPT1": "33",
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "NOM_DEPT": "CALVADOS",
                        "INSEE_REG": "28",
                        "POPULATION": 694002,
                        "AREA": 5588.48,
                        "DENSITY": 124.18,
                        "CODE_DEPT1": "14",
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "NOM_DEPT": "VOSGES",
                        "INSEE_REG": "44",
                        "POPULATION": 367673,
                        "AREA": 5891.56,
                        "DENSITY": 62.41,
                        "CODE_DEPT1": "88",
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "NOM_DEPT": "CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 304256,
                        "AREA": 7292.67,
                        "DENSITY": 41.72,
                        "CODE_DEPT1": "18",
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "NOM_DEPT": "ARDECHE",
                        "INSEE_REG": "84",
                        "POPULATION": 325712,
                        "AREA": 5562.05,
                        "DENSITY": 58.56,
                        "CODE_DEPT1": "07",
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "INSEE_REG": "32",
                        "POPULATION": 534490,
                        "AREA": 7418.97,
                        "DENSITY": 72.04,
                        "CODE_DEPT1": "02",
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "NOM_DEPT": "PYRENEES-ATLANTIQUES",
                        "INSEE_REG": "75",
                        "POPULATION": 677309,
                        "AREA": 7691.6,
                        "DENSITY": 88.06,
                        "CODE_DEPT1": "64",
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "NOM_DEPT": "LOIR-ET-CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 331915,
                        "AREA": 6412.3,
                        "DENSITY": 51.76,
                        "CODE_DEPT1": "41",
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "NOM_DEPT": "MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 1043522,
                        "AREA": 6252.63,
                        "DENSITY": 166.89,
                        "CODE_DEPT1": "57",
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "NOM_DEPT": "VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 436876,
                        "AREA": 7025.24,
                        "DENSITY": 62.19,
                        "CODE_DEPT1": "86",
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "NOM_DEPT": "DORDOGNE",
                        "INSEE_REG": "75",
                        "POPULATION": 413606,
                        "AREA": 9209.9,
                        "DENSITY": 44.91,
                        "CODE_DEPT1": "24",
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "NOM_DEPT": "JURA",
                        "INSEE_REG": "27",
                        "POPULATION": 260188,
                        "AREA": 5040.63,
                        "DENSITY": 51.62,
                        "CODE_DEPT1": "39",
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "NOM_DEPT": "TARN-ET-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 258349,
                        "AREA": 3731.0,
                        "DENSITY": 69.24,
                        "CODE_DEPT1": "82",
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "NOM_DEPT": "MAINE-ET-LOIRE",
                        "INSEE_REG": "52",
                        "POPULATION": 813493,
                        "AREA": 7161.34,
                        "DENSITY": 113.6,
                        "CODE_DEPT1": "49",
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "NOM_DEPT": "RHONE",
                        "INSEE_REG": "84",
                        "POPULATION": 1843319,
                        "AREA": 3253.11,
                        "DENSITY": 566.63,
                        "CODE_DEPT1": "69",
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "NOM_DEPT": "EURE",
                        "INSEE_REG": "28",
                        "POPULATION": 601843,
                        "AREA": 6035.85,
                        "DENSITY": 99.71,
                        "CODE_DEPT1": "27",
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "NOM_DEPT": "AVEYRON",
                        "INSEE_REG": "76",
                        "POPULATION": 279206,
                        "AREA": 8770.69,
                        "DENSITY": 31.83,
                        "CODE_DEPT1": "12",
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "NOM_DEPT": "CREUSE",
                        "INSEE_REG": "75",
                        "POPULATION": 118638,
                        "AREA": 5589.16,
                        "DENSITY": 21.23,
                        "CODE_DEPT1": "23",
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "NOM_DEPT": "LOIRET",
                        "INSEE_REG": "24",
                        "POPULATION": 678008,
                        "AREA": 6804.01,
                        "DENSITY": 99.65,
                        "CODE_DEPT1": "45",
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "NOM_DEPT": "HAUTE-SAONE",
                        "INSEE_REG": "27",
                        "POPULATION": 236659,
                        "AREA": 5382.37,
                        "DENSITY": 43.97,
                        "CODE_DEPT1": "70",
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "NOM_DEPT": "PUY-DE-DOME",
                        "INSEE_REG": "84",
                        "POPULATION": 653742,
                        "AREA": 8003.1,
                        "DENSITY": 81.69,
                        "CODE_DEPT1": "63",
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "NOM_DEPT": "TARN",
                        "INSEE_REG": "76",
                        "POPULATION": 387890,
                        "AREA": 5785.79,
                        "DENSITY": 67.04,
                        "CODE_DEPT1": "81",
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "NOM_DEPT": "SEINE-MARITIME",
                        "INSEE_REG": "28",
                        "POPULATION": 1254378,
                        "AREA": 6318.26,
                        "DENSITY": 198.53,
                        "CODE_DEPT1": "76",
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "NOM_DEPT": "HAUTE-MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 175640,
                        "AREA": 6249.91,
                        "DENSITY": 28.1,
                        "CODE_DEPT1": "52",
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "NOM_DEPT": "GARD",
                        "INSEE_REG": "76",
                        "POPULATION": 744178,
                        "AREA": 5874.71,
                        "DENSITY": 126.67,
                        "CODE_DEPT1": "30",
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "NOM_DEPT": "BAS-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 1125559,
                        "AREA": 4796.37,
                        "DENSITY": 234.67,
                        "CODE_DEPT1": "67",
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "NOM_DEPT": "AUDE",
                        "INSEE_REG": "76",
                        "POPULATION": 370260,
                        "AREA": 6351.35,
                        "DENSITY": 58.3,
                        "CODE_DEPT1": "11",
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "NOM_DEPT": "SEINE-ET-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1403997,
                        "AREA": 5924.64,
                        "DENSITY": 236.98,
                        "CODE_DEPT1": "77",
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "NOM_DEPT": "SOMME",
                        "INSEE_REG": "32",
                        "POPULATION": 572443,
                        "AREA": 6206.58,
                        "DENSITY": 92.23,
                        "CODE_DEPT1": "80",
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "NOM_DEPT": "HAUTE-LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 227283,
                        "AREA": 4996.58,
                        "DENSITY": 45.49,
                        "CODE_DEPT1": "43",
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "NOM_DEPT": "MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 568895,
                        "AREA": 8195.78,
                        "DENSITY": 69.41,
                        "CODE_DEPT1": "51",
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "NOM_DEPT": "HAUTES-PYRENEES",
                        "INSEE_REG": "76",
                        "POPULATION": 228530,
                        "AREA": 4527.89,
                        "DENSITY": 50.47,
                        "CODE_DEPT1": "65",
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "NOM_DEPT": "LOT",
                        "INSEE_REG": "76",
                        "POPULATION": 173828,
                        "AREA": 5221.64,
                        "DENSITY": 33.29,
                        "CODE_DEPT1": "46",
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "NOM_DEPT": "ALPES-DE-HAUTE-PROVENCE",
                        "INSEE_REG": "93",
                        "POPULATION": 163915,
                        "AREA": 6993.79,
                        "DENSITY": 23.44,
                        "CODE_DEPT1": "04",
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "NOM_DEPT": "SARTHE",
                        "INSEE_REG": "52",
                        "POPULATION": 566506,
                        "AREA": 6236.75,
                        "DENSITY": 90.83,
                        "CODE_DEPT1": "72",
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "INSEE_REG": "53",
                        "POPULATION": 750863,
                        "AREA": 6864.07,
                        "DENSITY": 109.39,
                        "CODE_DEPT1": "56",
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "NOM_DEPT": "EURE-ET-LOIR",
                        "INSEE_REG": "24",
                        "POPULATION": 433233,
                        "AREA": 5927.23,
                        "DENSITY": 73.09,
                        "CODE_DEPT1": "28",
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "NOM_DEPT": "CORSE-DU-SUD",
                        "INSEE_REG": "94",
                        "POPULATION": 157249,
                        "AREA": 4028.53,
                        "DENSITY": 39.03,
                        "CODE_DEPT1": "2A",
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "NOM_DEPT": "MEURTHE-ET-MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 733481,
                        "AREA": 5283.29,
                        "DENSITY": 138.83,
                        "CODE_DEPT1": "54",
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "NOM_DEPT": "ORNE",
                        "INSEE_REG": "28",
                        "POPULATION": 283372,
                        "AREA": 6142.73,
                        "DENSITY": 46.13,
                        "CODE_DEPT1": "61",
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "NOM_DEPT": "AIN",
                        "INSEE_REG": "84",
                        "POPULATION": 643350,
                        "AREA": 5773.77,
                        "DENSITY": 111.43,
                        "CODE_DEPT1": "01",
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "NOM_DEPT": "ARIEGE",
                        "INSEE_REG": "76",
                        "POPULATION": 153153,
                        "AREA": 4921.75,
                        "DENSITY": 31.12,
                        "CODE_DEPT1": "09",
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "NOM_DEPT": "CORREZE",
                        "INSEE_REG": "75",
                        "POPULATION": 241464,
                        "AREA": 5888.93,
                        "DENSITY": 41.0,
                        "CODE_DEPT1": "19",
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "NOM_DEPT": "HAUT-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 764030,
                        "AREA": 3526.37,
                        "DENSITY": 216.66,
                        "CODE_DEPT1": "68",
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "NOM_DEPT": "INDRE-ET-LOIRE",
                        "INSEE_REG": "24",
                        "POPULATION": 606511,
                        "AREA": 6147.6,
                        "DENSITY": 98.66,
                        "CODE_DEPT1": "37",
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "NOM_DEPT": "NORD",
                        "INSEE_REG": "32",
                        "POPULATION": 2604361,
                        "AREA": 5774.99,
                        "DENSITY": 450.97,
                        "CODE_DEPT1": "59",
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "NOM_DEPT": "TERRITOIRE DE BELFORT",
                        "INSEE_REG": "27",
                        "POPULATION": 142622,
                        "AREA": 609.64,
                        "DENSITY": 233.94,
                        "CODE_DEPT1": "90",
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "NOM_DEPT": "LOIRE-ATLANTIQUE",
                        "INSEE_REG": "52",
                        "POPULATION": 1394909,
                        "AREA": 6992.78,
                        "DENSITY": 199.48,
                        "CODE_DEPT1": "44",
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "NOM_DEPT": "YONNE",
                        "INSEE_REG": "27",
                        "POPULATION": 338291,
                        "AREA": 7450.97,
                        "DENSITY": 45.4,
                        "CODE_DEPT1": "89",
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "NOM_DEPT": "ILLE-ET-VILAINE",
                        "INSEE_REG": "53",
                        "POPULATION": 1060199,
                        "AREA": 6830.2,
                        "DENSITY": 155.22,
                        "CODE_DEPT1": "35",
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "NOM_DEPT": "LANDES",
                        "INSEE_REG": "75",
                        "POPULATION": 407444,
                        "AREA": 9353.03,
                        "DENSITY": 43.56,
                        "CODE_DEPT1": "40",
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "NOM_DEPT": "FINISTERE",
                        "INSEE_REG": "53",
                        "POPULATION": 909028,
                        "AREA": 6756.76,
                        "DENSITY": 134.54,
                        "CODE_DEPT1": "29",
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "NOM_DEPT": "HAUTE-SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 807360,
                        "AREA": 4596.53,
                        "DENSITY": 175.65,
                        "CODE_DEPT1": "74",
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "NOM_DEPT": "OISE",
                        "INSEE_REG": "32",
                        "POPULATION": 824503,
                        "AREA": 5893.6,
                        "DENSITY": 139.9,
                        "CODE_DEPT1": "60",
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "INSEE_REG": "11",
                        "POPULATION": 1228618,
                        "AREA": 1254.18,
                        "DENSITY": 979.62,
                        "CODE_DEPT1": "95",
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "NOM_DEPT": "NIEVRE",
                        "INSEE_REG": "27",
                        "POPULATION": 207182,
                        "AREA": 6862.87,
                        "DENSITY": 30.19,
                        "CODE_DEPT1": "58",
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "NOM_DEPT": "COTE-D'OR",
                        "INSEE_REG": "27",
                        "POPULATION": 532871,
                        "AREA": 8787.51,
                        "DENSITY": 60.64,
                        "CODE_DEPT1": "21",
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "NOM_DEPT": "ESSONNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1296130,
                        "AREA": 1818.35,
                        "DENSITY": 712.81,
                        "CODE_DEPT1": "91",
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "NOM_DEPT": "DEUX-SEVRES",
                        "INSEE_REG": "75",
                        "POPULATION": 374351,
                        "AREA": 6029.06,
                        "DENSITY": 62.09,
                        "CODE_DEPT1": "79",
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "NOM_DEPT": "COTES-D'ARMOR",
                        "INSEE_REG": "53",
                        "POPULATION": 598814,
                        "AREA": 6963.26,
                        "DENSITY": 86.0,
                        "CODE_DEPT1": "22",
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "NOM_DEPT": "ALLIER",
                        "INSEE_REG": "84",
                        "POPULATION": 337988,
                        "AREA": 7365.26,
                        "DENSITY": 45.89,
                        "CODE_DEPT1": "03",
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "NOM_DEPT": "CHARENTE-MARITIME",
                        "INSEE_REG": "75",
                        "POPULATION": 644303,
                        "AREA": 6913.03,
                        "DENSITY": 93.2,
                        "CODE_DEPT1": "17",
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "NOM_DEPT": "CANTAL",
                        "INSEE_REG": "84",
                        "POPULATION": 145143,
                        "AREA": 5767.47,
                        "DENSITY": 25.17,
                        "CODE_DEPT1": "15",
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "NOM_DEPT": "HERAULT",
                        "INSEE_REG": "76",
                        "POPULATION": 1144892,
                        "AREA": 6231.05,
                        "DENSITY": 183.74,
                        "CODE_DEPT1": "34",
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "NOM_DEPT": "DROME",
                        "INSEE_REG": "84",
                        "POPULATION": 511553,
                        "AREA": 6553.53,
                        "DENSITY": 78.06,
                        "CODE_DEPT1": "26",
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "NOM_DEPT": "PYRENEES-ORIENTALES",
                        "INSEE_REG": "76",
                        "POPULATION": 474452,
                        "AREA": 4147.76,
                        "DENSITY": 114.39,
                        "CODE_DEPT1": "66",
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "NOM_DEPT": "SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 431174,
                        "AREA": 6260.4,
                        "DENSITY": 68.87,
                        "CODE_DEPT1": "73",
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "NOM_DEPT": "HAUTES-ALPES",
                        "INSEE_REG": "93",
                        "POPULATION": 141284,
                        "AREA": 5685.31,
                        "DENSITY": 24.85,
                        "CODE_DEPT1": "05",
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "NOM_DEPT": "VAUCLUSE",
                        "INSEE_REG": "93",
                        "POPULATION": 559479,
                        "AREA": 3577.19,
                        "DENSITY": 156.4,
                        "CODE_DEPT1": "84",
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "NOM_DEPT": "INDRE",
                        "INSEE_REG": "24",
                        "POPULATION": 222232,
                        "AREA": 6887.38,
                        "DENSITY": 32.27,
                        "CODE_DEPT1": "36",
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "NOM_DEPT": "HAUTE-CORSE",
                        "INSEE_REG": "94",
                        "POPULATION": 177689,
                        "AREA": 4719.71,
                        "DENSITY": 37.65,
                        "CODE_DEPT1": "2B",
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "NOM_DEPT": "HAUTE-VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 374426,
                        "AREA": 5549.31,
                        "DENSITY": 67.47,
                        "CODE_DEPT1": "87",
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "NOM_DEPT": "VENDEE",
                        "INSEE_REG": "52",
                        "POPULATION": 675247,
                        "AREA": 6758.23,
                        "DENSITY": 99.91,
                        "CODE_DEPT1": "85",
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "NOM_DEPT": "VAR",
                        "INSEE_REG": "93",
                        "POPULATION": 1058740,
                        "AREA": 6002.84,
                        "DENSITY": 176.37,
                        "CODE_DEPT1": "83",
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "NOM_DEPT": "VAL-DE-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1387926,
                        "AREA": 244.7,
                        "DENSITY": 5671.95,
                        "CODE_DEPT1": "94",
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "NOM_DEPT": "HAUTS-DE-SEINE",
                        "INSEE_REG": "11",
                        "POPULATION": 1609306,
                        "AREA": 175.63,
                        "DENSITY": 9163.05,
                        "CODE_DEPT1": "92",
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "NOM_DEPT": "LOZERE",
                        "INSEE_REG": "76",
                        "POPULATION": 76601,
                        "AREA": 5172.02,
                        "DENSITY": 14.81,
                        "CODE_DEPT1": "48",
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "NOM_DEPT": "BOUCHES-DU-RHONE",
                        "INSEE_REG": "93",
                        "POPULATION": 2024162,
                        "AREA": 5082.57,
                        "DENSITY": 398.26,
                        "CODE_DEPT1": "13",
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "NOM_DEPT": "PARIS",
                        "INSEE_REG": "11",
                        "POPULATION": 2187526,
                        "AREA": 105.44,
                        "DENSITY": 20746.64,
                        "CODE_DEPT1": "75",
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "NOM_DEPT": "SEINE-SAINT-DENIS",
                        "INSEE_REG": "11",
                        "POPULATION": 1623111,
                        "AREA": 236.96,
                        "DENSITY": 6849.73,
                        "CODE_DEPT1": "93",
                    }
                },
            },
        },
    },
    1: {
        "geolayer_a": geolayer_fr_dept_data_only,
        "geolayer_b": geolayer_fr_dept_population,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_WITH_POPULATION",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_WITH_POPULATION",
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
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "NOM_DEPT": "GERS",
                        "INSEE_REG": "76",
                        "POPULATION": 191091,
                        "AREA": 6304.33,
                        "DENSITY": 30.31,
                        "CODE_DEPT1": "32",
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "NOM_DEPT": "LOT-ET-GARONNE",
                        "INSEE_REG": "75",
                        "POPULATION": 332842,
                        "AREA": 5382.87,
                        "DENSITY": 61.83,
                        "CODE_DEPT1": "47",
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "NOM_DEPT": "ISERE",
                        "INSEE_REG": "84",
                        "POPULATION": 1258722,
                        "AREA": 7868.79,
                        "DENSITY": 159.96,
                        "CODE_DEPT1": "38",
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "NOM_DEPT": "PAS-DE-CALAIS",
                        "INSEE_REG": "32",
                        "POPULATION": 1468018,
                        "AREA": 6714.14,
                        "DENSITY": 218.65,
                        "CODE_DEPT1": "62",
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "NOM_DEPT": "ARDENNES",
                        "INSEE_REG": "44",
                        "POPULATION": 273579,
                        "AREA": 5253.13,
                        "DENSITY": 52.08,
                        "CODE_DEPT1": "08",
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "NOM_DEPT": "AUBE",
                        "INSEE_REG": "44",
                        "POPULATION": 310020,
                        "AREA": 6021.83,
                        "DENSITY": 51.48,
                        "CODE_DEPT1": "10",
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "NOM_DEPT": "ALPES-MARITIMES",
                        "INSEE_REG": "93",
                        "POPULATION": 1083310,
                        "AREA": 4291.62,
                        "DENSITY": 252.42,
                        "CODE_DEPT1": "06",
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "NOM_DEPT": "LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 762941,
                        "AREA": 4795.85,
                        "DENSITY": 159.08,
                        "CODE_DEPT1": "42",
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "NOM_DEPT": "HAUTE-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 1362672,
                        "AREA": 6364.82,
                        "DENSITY": 214.09,
                        "CODE_DEPT1": "31",
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "NOM_DEPT": "SAONE-ET-LOIRE",
                        "INSEE_REG": "27",
                        "POPULATION": 553595,
                        "AREA": 8598.33,
                        "DENSITY": 64.38,
                        "CODE_DEPT1": "71",
                    }
                },
                10: {
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
                11: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "NOM_DEPT": "CHARENTE",
                        "INSEE_REG": "75",
                        "POPULATION": 352335,
                        "AREA": 5963.54,
                        "DENSITY": 59.08,
                        "CODE_DEPT1": "16",
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "NOM_DEPT": "MANCHE",
                        "INSEE_REG": "28",
                        "POPULATION": 496883,
                        "AREA": 6015.07,
                        "DENSITY": 82.61,
                        "CODE_DEPT1": "50",
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "NOM_DEPT": "YVELINES",
                        "INSEE_REG": "11",
                        "POPULATION": 1438266,
                        "AREA": 2305.64,
                        "DENSITY": 623.8,
                        "CODE_DEPT1": "78",
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "NOM_DEPT": "DOUBS",
                        "INSEE_REG": "27",
                        "POPULATION": 539067,
                        "AREA": 5248.31,
                        "DENSITY": 102.71,
                        "CODE_DEPT1": "25",
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "NOM_DEPT": "MEUSE",
                        "INSEE_REG": "44",
                        "POPULATION": 187187,
                        "AREA": 6233.18,
                        "DENSITY": 30.03,
                        "CODE_DEPT1": "55",
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "NOM_DEPT": "GIRONDE",
                        "INSEE_REG": "75",
                        "POPULATION": 1583384,
                        "AREA": 10068.74,
                        "DENSITY": 157.26,
                        "CODE_DEPT1": "33",
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "NOM_DEPT": "CALVADOS",
                        "INSEE_REG": "28",
                        "POPULATION": 694002,
                        "AREA": 5588.48,
                        "DENSITY": 124.18,
                        "CODE_DEPT1": "14",
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "NOM_DEPT": "VOSGES",
                        "INSEE_REG": "44",
                        "POPULATION": 367673,
                        "AREA": 5891.56,
                        "DENSITY": 62.41,
                        "CODE_DEPT1": "88",
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "NOM_DEPT": "CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 304256,
                        "AREA": 7292.67,
                        "DENSITY": 41.72,
                        "CODE_DEPT1": "18",
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "NOM_DEPT": "ARDECHE",
                        "INSEE_REG": "84",
                        "POPULATION": 325712,
                        "AREA": 5562.05,
                        "DENSITY": 58.56,
                        "CODE_DEPT1": "07",
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "INSEE_REG": "32",
                        "POPULATION": 534490,
                        "AREA": 7418.97,
                        "DENSITY": 72.04,
                        "CODE_DEPT1": "02",
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "NOM_DEPT": "PYRENEES-ATLANTIQUES",
                        "INSEE_REG": "75",
                        "POPULATION": 677309,
                        "AREA": 7691.6,
                        "DENSITY": 88.06,
                        "CODE_DEPT1": "64",
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "NOM_DEPT": "LOIR-ET-CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 331915,
                        "AREA": 6412.3,
                        "DENSITY": 51.76,
                        "CODE_DEPT1": "41",
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "NOM_DEPT": "MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 1043522,
                        "AREA": 6252.63,
                        "DENSITY": 166.89,
                        "CODE_DEPT1": "57",
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "NOM_DEPT": "VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 436876,
                        "AREA": 7025.24,
                        "DENSITY": 62.19,
                        "CODE_DEPT1": "86",
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "NOM_DEPT": "DORDOGNE",
                        "INSEE_REG": "75",
                        "POPULATION": 413606,
                        "AREA": 9209.9,
                        "DENSITY": 44.91,
                        "CODE_DEPT1": "24",
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "NOM_DEPT": "JURA",
                        "INSEE_REG": "27",
                        "POPULATION": 260188,
                        "AREA": 5040.63,
                        "DENSITY": 51.62,
                        "CODE_DEPT1": "39",
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "NOM_DEPT": "TARN-ET-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 258349,
                        "AREA": 3731.0,
                        "DENSITY": 69.24,
                        "CODE_DEPT1": "82",
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "NOM_DEPT": "MAINE-ET-LOIRE",
                        "INSEE_REG": "52",
                        "POPULATION": 813493,
                        "AREA": 7161.34,
                        "DENSITY": 113.6,
                        "CODE_DEPT1": "49",
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "NOM_DEPT": "RHONE",
                        "INSEE_REG": "84",
                        "POPULATION": 1843319,
                        "AREA": 3253.11,
                        "DENSITY": 566.63,
                        "CODE_DEPT1": "69",
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "NOM_DEPT": "EURE",
                        "INSEE_REG": "28",
                        "POPULATION": 601843,
                        "AREA": 6035.85,
                        "DENSITY": 99.71,
                        "CODE_DEPT1": "27",
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "NOM_DEPT": "AVEYRON",
                        "INSEE_REG": "76",
                        "POPULATION": 279206,
                        "AREA": 8770.69,
                        "DENSITY": 31.83,
                        "CODE_DEPT1": "12",
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "NOM_DEPT": "CREUSE",
                        "INSEE_REG": "75",
                        "POPULATION": 118638,
                        "AREA": 5589.16,
                        "DENSITY": 21.23,
                        "CODE_DEPT1": "23",
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "NOM_DEPT": "LOIRET",
                        "INSEE_REG": "24",
                        "POPULATION": 678008,
                        "AREA": 6804.01,
                        "DENSITY": 99.65,
                        "CODE_DEPT1": "45",
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "NOM_DEPT": "HAUTE-SAONE",
                        "INSEE_REG": "27",
                        "POPULATION": 236659,
                        "AREA": 5382.37,
                        "DENSITY": 43.97,
                        "CODE_DEPT1": "70",
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "NOM_DEPT": "PUY-DE-DOME",
                        "INSEE_REG": "84",
                        "POPULATION": 653742,
                        "AREA": 8003.1,
                        "DENSITY": 81.69,
                        "CODE_DEPT1": "63",
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "NOM_DEPT": "TARN",
                        "INSEE_REG": "76",
                        "POPULATION": 387890,
                        "AREA": 5785.79,
                        "DENSITY": 67.04,
                        "CODE_DEPT1": "81",
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "NOM_DEPT": "SEINE-MARITIME",
                        "INSEE_REG": "28",
                        "POPULATION": 1254378,
                        "AREA": 6318.26,
                        "DENSITY": 198.53,
                        "CODE_DEPT1": "76",
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "NOM_DEPT": "HAUTE-MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 175640,
                        "AREA": 6249.91,
                        "DENSITY": 28.1,
                        "CODE_DEPT1": "52",
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "NOM_DEPT": "GARD",
                        "INSEE_REG": "76",
                        "POPULATION": 744178,
                        "AREA": 5874.71,
                        "DENSITY": 126.67,
                        "CODE_DEPT1": "30",
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "NOM_DEPT": "BAS-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 1125559,
                        "AREA": 4796.37,
                        "DENSITY": 234.67,
                        "CODE_DEPT1": "67",
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "NOM_DEPT": "AUDE",
                        "INSEE_REG": "76",
                        "POPULATION": 370260,
                        "AREA": 6351.35,
                        "DENSITY": 58.3,
                        "CODE_DEPT1": "11",
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "NOM_DEPT": "SEINE-ET-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1403997,
                        "AREA": 5924.64,
                        "DENSITY": 236.98,
                        "CODE_DEPT1": "77",
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "NOM_DEPT": "SOMME",
                        "INSEE_REG": "32",
                        "POPULATION": 572443,
                        "AREA": 6206.58,
                        "DENSITY": 92.23,
                        "CODE_DEPT1": "80",
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "NOM_DEPT": "HAUTE-LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 227283,
                        "AREA": 4996.58,
                        "DENSITY": 45.49,
                        "CODE_DEPT1": "43",
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "NOM_DEPT": "MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 568895,
                        "AREA": 8195.78,
                        "DENSITY": 69.41,
                        "CODE_DEPT1": "51",
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "NOM_DEPT": "HAUTES-PYRENEES",
                        "INSEE_REG": "76",
                        "POPULATION": 228530,
                        "AREA": 4527.89,
                        "DENSITY": 50.47,
                        "CODE_DEPT1": "65",
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "NOM_DEPT": "LOT",
                        "INSEE_REG": "76",
                        "POPULATION": 173828,
                        "AREA": 5221.64,
                        "DENSITY": 33.29,
                        "CODE_DEPT1": "46",
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "NOM_DEPT": "ALPES-DE-HAUTE-PROVENCE",
                        "INSEE_REG": "93",
                        "POPULATION": 163915,
                        "AREA": 6993.79,
                        "DENSITY": 23.44,
                        "CODE_DEPT1": "04",
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "NOM_DEPT": "SARTHE",
                        "INSEE_REG": "52",
                        "POPULATION": 566506,
                        "AREA": 6236.75,
                        "DENSITY": 90.83,
                        "CODE_DEPT1": "72",
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "INSEE_REG": "53",
                        "POPULATION": 750863,
                        "AREA": 6864.07,
                        "DENSITY": 109.39,
                        "CODE_DEPT1": "56",
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "NOM_DEPT": "EURE-ET-LOIR",
                        "INSEE_REG": "24",
                        "POPULATION": 433233,
                        "AREA": 5927.23,
                        "DENSITY": 73.09,
                        "CODE_DEPT1": "28",
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "NOM_DEPT": "CORSE-DU-SUD",
                        "INSEE_REG": "94",
                        "POPULATION": 157249,
                        "AREA": 4028.53,
                        "DENSITY": 39.03,
                        "CODE_DEPT1": "2A",
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "NOM_DEPT": "MEURTHE-ET-MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 733481,
                        "AREA": 5283.29,
                        "DENSITY": 138.83,
                        "CODE_DEPT1": "54",
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "NOM_DEPT": "ORNE",
                        "INSEE_REG": "28",
                        "POPULATION": 283372,
                        "AREA": 6142.73,
                        "DENSITY": 46.13,
                        "CODE_DEPT1": "61",
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "NOM_DEPT": "AIN",
                        "INSEE_REG": "84",
                        "POPULATION": 643350,
                        "AREA": 5773.77,
                        "DENSITY": 111.43,
                        "CODE_DEPT1": "01",
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "NOM_DEPT": "ARIEGE",
                        "INSEE_REG": "76",
                        "POPULATION": 153153,
                        "AREA": 4921.75,
                        "DENSITY": 31.12,
                        "CODE_DEPT1": "09",
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "NOM_DEPT": "CORREZE",
                        "INSEE_REG": "75",
                        "POPULATION": 241464,
                        "AREA": 5888.93,
                        "DENSITY": 41.0,
                        "CODE_DEPT1": "19",
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "NOM_DEPT": "HAUT-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 764030,
                        "AREA": 3526.37,
                        "DENSITY": 216.66,
                        "CODE_DEPT1": "68",
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "NOM_DEPT": "INDRE-ET-LOIRE",
                        "INSEE_REG": "24",
                        "POPULATION": 606511,
                        "AREA": 6147.6,
                        "DENSITY": 98.66,
                        "CODE_DEPT1": "37",
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "NOM_DEPT": "NORD",
                        "INSEE_REG": "32",
                        "POPULATION": 2604361,
                        "AREA": 5774.99,
                        "DENSITY": 450.97,
                        "CODE_DEPT1": "59",
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "NOM_DEPT": "TERRITOIRE DE BELFORT",
                        "INSEE_REG": "27",
                        "POPULATION": 142622,
                        "AREA": 609.64,
                        "DENSITY": 233.94,
                        "CODE_DEPT1": "90",
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "NOM_DEPT": "LOIRE-ATLANTIQUE",
                        "INSEE_REG": "52",
                        "POPULATION": 1394909,
                        "AREA": 6992.78,
                        "DENSITY": 199.48,
                        "CODE_DEPT1": "44",
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "NOM_DEPT": "YONNE",
                        "INSEE_REG": "27",
                        "POPULATION": 338291,
                        "AREA": 7450.97,
                        "DENSITY": 45.4,
                        "CODE_DEPT1": "89",
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "NOM_DEPT": "ILLE-ET-VILAINE",
                        "INSEE_REG": "53",
                        "POPULATION": 1060199,
                        "AREA": 6830.2,
                        "DENSITY": 155.22,
                        "CODE_DEPT1": "35",
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "NOM_DEPT": "LANDES",
                        "INSEE_REG": "75",
                        "POPULATION": 407444,
                        "AREA": 9353.03,
                        "DENSITY": 43.56,
                        "CODE_DEPT1": "40",
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "NOM_DEPT": "FINISTERE",
                        "INSEE_REG": "53",
                        "POPULATION": 909028,
                        "AREA": 6756.76,
                        "DENSITY": 134.54,
                        "CODE_DEPT1": "29",
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "NOM_DEPT": "HAUTE-SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 807360,
                        "AREA": 4596.53,
                        "DENSITY": 175.65,
                        "CODE_DEPT1": "74",
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "NOM_DEPT": "OISE",
                        "INSEE_REG": "32",
                        "POPULATION": 824503,
                        "AREA": 5893.6,
                        "DENSITY": 139.9,
                        "CODE_DEPT1": "60",
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "INSEE_REG": "11",
                        "POPULATION": 1228618,
                        "AREA": 1254.18,
                        "DENSITY": 979.62,
                        "CODE_DEPT1": "95",
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "NOM_DEPT": "NIEVRE",
                        "INSEE_REG": "27",
                        "POPULATION": 207182,
                        "AREA": 6862.87,
                        "DENSITY": 30.19,
                        "CODE_DEPT1": "58",
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "NOM_DEPT": "COTE-D'OR",
                        "INSEE_REG": "27",
                        "POPULATION": 532871,
                        "AREA": 8787.51,
                        "DENSITY": 60.64,
                        "CODE_DEPT1": "21",
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "NOM_DEPT": "ESSONNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1296130,
                        "AREA": 1818.35,
                        "DENSITY": 712.81,
                        "CODE_DEPT1": "91",
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "NOM_DEPT": "DEUX-SEVRES",
                        "INSEE_REG": "75",
                        "POPULATION": 374351,
                        "AREA": 6029.06,
                        "DENSITY": 62.09,
                        "CODE_DEPT1": "79",
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "NOM_DEPT": "COTES-D'ARMOR",
                        "INSEE_REG": "53",
                        "POPULATION": 598814,
                        "AREA": 6963.26,
                        "DENSITY": 86.0,
                        "CODE_DEPT1": "22",
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "NOM_DEPT": "ALLIER",
                        "INSEE_REG": "84",
                        "POPULATION": 337988,
                        "AREA": 7365.26,
                        "DENSITY": 45.89,
                        "CODE_DEPT1": "03",
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "NOM_DEPT": "CHARENTE-MARITIME",
                        "INSEE_REG": "75",
                        "POPULATION": 644303,
                        "AREA": 6913.03,
                        "DENSITY": 93.2,
                        "CODE_DEPT1": "17",
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "NOM_DEPT": "CANTAL",
                        "INSEE_REG": "84",
                        "POPULATION": 145143,
                        "AREA": 5767.47,
                        "DENSITY": 25.17,
                        "CODE_DEPT1": "15",
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "NOM_DEPT": "HERAULT",
                        "INSEE_REG": "76",
                        "POPULATION": 1144892,
                        "AREA": 6231.05,
                        "DENSITY": 183.74,
                        "CODE_DEPT1": "34",
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "NOM_DEPT": "DROME",
                        "INSEE_REG": "84",
                        "POPULATION": 511553,
                        "AREA": 6553.53,
                        "DENSITY": 78.06,
                        "CODE_DEPT1": "26",
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "NOM_DEPT": "PYRENEES-ORIENTALES",
                        "INSEE_REG": "76",
                        "POPULATION": 474452,
                        "AREA": 4147.76,
                        "DENSITY": 114.39,
                        "CODE_DEPT1": "66",
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "NOM_DEPT": "SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 431174,
                        "AREA": 6260.4,
                        "DENSITY": 68.87,
                        "CODE_DEPT1": "73",
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "NOM_DEPT": "HAUTES-ALPES",
                        "INSEE_REG": "93",
                        "POPULATION": 141284,
                        "AREA": 5685.31,
                        "DENSITY": 24.85,
                        "CODE_DEPT1": "05",
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "NOM_DEPT": "VAUCLUSE",
                        "INSEE_REG": "93",
                        "POPULATION": 559479,
                        "AREA": 3577.19,
                        "DENSITY": 156.4,
                        "CODE_DEPT1": "84",
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "NOM_DEPT": "INDRE",
                        "INSEE_REG": "24",
                        "POPULATION": 222232,
                        "AREA": 6887.38,
                        "DENSITY": 32.27,
                        "CODE_DEPT1": "36",
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "NOM_DEPT": "HAUTE-CORSE",
                        "INSEE_REG": "94",
                        "POPULATION": 177689,
                        "AREA": 4719.71,
                        "DENSITY": 37.65,
                        "CODE_DEPT1": "2B",
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "NOM_DEPT": "HAUTE-VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 374426,
                        "AREA": 5549.31,
                        "DENSITY": 67.47,
                        "CODE_DEPT1": "87",
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "NOM_DEPT": "VENDEE",
                        "INSEE_REG": "52",
                        "POPULATION": 675247,
                        "AREA": 6758.23,
                        "DENSITY": 99.91,
                        "CODE_DEPT1": "85",
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "NOM_DEPT": "VAR",
                        "INSEE_REG": "93",
                        "POPULATION": 1058740,
                        "AREA": 6002.84,
                        "DENSITY": 176.37,
                        "CODE_DEPT1": "83",
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "NOM_DEPT": "VAL-DE-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1387926,
                        "AREA": 244.7,
                        "DENSITY": 5671.95,
                        "CODE_DEPT1": "94",
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "NOM_DEPT": "HAUTS-DE-SEINE",
                        "INSEE_REG": "11",
                        "POPULATION": 1609306,
                        "AREA": 175.63,
                        "DENSITY": 9163.05,
                        "CODE_DEPT1": "92",
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "NOM_DEPT": "LOZERE",
                        "INSEE_REG": "76",
                        "POPULATION": 76601,
                        "AREA": 5172.02,
                        "DENSITY": 14.81,
                        "CODE_DEPT1": "48",
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "NOM_DEPT": "BOUCHES-DU-RHONE",
                        "INSEE_REG": "93",
                        "POPULATION": 2024162,
                        "AREA": 5082.57,
                        "DENSITY": 398.26,
                        "CODE_DEPT1": "13",
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "NOM_DEPT": "PARIS",
                        "INSEE_REG": "11",
                        "POPULATION": 2187526,
                        "AREA": 105.44,
                        "DENSITY": 20746.64,
                        "CODE_DEPT1": "75",
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "NOM_DEPT": "SEINE-SAINT-DENIS",
                        "INSEE_REG": "11",
                        "POPULATION": 1623111,
                        "AREA": 236.96,
                        "DENSITY": 6849.73,
                        "CODE_DEPT1": "93",
                    }
                },
            },
        },
    },
    2: {
        "geolayer_a": geolayer_fr_dept_data_only,
        "geolayer_b": geolayer_fr_dept_population,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_WITH_POPULATION",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_WITH_POPULATION",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "NOM_DEPT": "GERS",
                        "POPULATION": 191091,
                        "DENSITY": 30.31,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "NOM_DEPT": "LOT-ET-GARONNE",
                        "POPULATION": 332842,
                        "DENSITY": 61.83,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "NOM_DEPT": "ISERE",
                        "POPULATION": 1258722,
                        "DENSITY": 159.96,
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "NOM_DEPT": "PAS-DE-CALAIS",
                        "POPULATION": 1468018,
                        "DENSITY": 218.65,
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "NOM_DEPT": "ARDENNES",
                        "POPULATION": 273579,
                        "DENSITY": 52.08,
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "NOM_DEPT": "AUBE",
                        "POPULATION": 310020,
                        "DENSITY": 51.48,
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "NOM_DEPT": "ALPES-MARITIMES",
                        "POPULATION": 1083310,
                        "DENSITY": 252.42,
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "NOM_DEPT": "LOIRE",
                        "POPULATION": 762941,
                        "DENSITY": 159.08,
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "NOM_DEPT": "HAUTE-GARONNE",
                        "POPULATION": 1362672,
                        "DENSITY": 214.09,
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "NOM_DEPT": "SAONE-ET-LOIRE",
                        "POPULATION": 553595,
                        "DENSITY": 64.38,
                    }
                },
                10: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "NOM_DEPT": "MAYENNE",
                        "POPULATION": 307445,
                        "DENSITY": 59.03,
                    }
                },
                11: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "NOM_DEPT": "CHARENTE",
                        "POPULATION": 352335,
                        "DENSITY": 59.08,
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "NOM_DEPT": "MANCHE",
                        "POPULATION": 496883,
                        "DENSITY": 82.61,
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "NOM_DEPT": "YVELINES",
                        "POPULATION": 1438266,
                        "DENSITY": 623.8,
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "NOM_DEPT": "DOUBS",
                        "POPULATION": 539067,
                        "DENSITY": 102.71,
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "NOM_DEPT": "MEUSE",
                        "POPULATION": 187187,
                        "DENSITY": 30.03,
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "NOM_DEPT": "GIRONDE",
                        "POPULATION": 1583384,
                        "DENSITY": 157.26,
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "NOM_DEPT": "CALVADOS",
                        "POPULATION": 694002,
                        "DENSITY": 124.18,
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "NOM_DEPT": "VOSGES",
                        "POPULATION": 367673,
                        "DENSITY": 62.41,
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "NOM_DEPT": "CHER",
                        "POPULATION": 304256,
                        "DENSITY": 41.72,
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "NOM_DEPT": "ARDECHE",
                        "POPULATION": 325712,
                        "DENSITY": 58.56,
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "NOM_DEPT": "PYRENEES-ATLANTIQUES",
                        "POPULATION": 677309,
                        "DENSITY": 88.06,
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "NOM_DEPT": "LOIR-ET-CHER",
                        "POPULATION": 331915,
                        "DENSITY": 51.76,
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "NOM_DEPT": "MOSELLE",
                        "POPULATION": 1043522,
                        "DENSITY": 166.89,
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "NOM_DEPT": "VIENNE",
                        "POPULATION": 436876,
                        "DENSITY": 62.19,
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "NOM_DEPT": "DORDOGNE",
                        "POPULATION": 413606,
                        "DENSITY": 44.91,
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "NOM_DEPT": "JURA",
                        "POPULATION": 260188,
                        "DENSITY": 51.62,
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "NOM_DEPT": "TARN-ET-GARONNE",
                        "POPULATION": 258349,
                        "DENSITY": 69.24,
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "NOM_DEPT": "MAINE-ET-LOIRE",
                        "POPULATION": 813493,
                        "DENSITY": 113.6,
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "NOM_DEPT": "RHONE",
                        "POPULATION": 1843319,
                        "DENSITY": 566.63,
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "NOM_DEPT": "EURE",
                        "POPULATION": 601843,
                        "DENSITY": 99.71,
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "NOM_DEPT": "AVEYRON",
                        "POPULATION": 279206,
                        "DENSITY": 31.83,
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "NOM_DEPT": "CREUSE",
                        "POPULATION": 118638,
                        "DENSITY": 21.23,
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "NOM_DEPT": "LOIRET",
                        "POPULATION": 678008,
                        "DENSITY": 99.65,
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "NOM_DEPT": "HAUTE-SAONE",
                        "POPULATION": 236659,
                        "DENSITY": 43.97,
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "NOM_DEPT": "PUY-DE-DOME",
                        "POPULATION": 653742,
                        "DENSITY": 81.69,
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "NOM_DEPT": "TARN",
                        "POPULATION": 387890,
                        "DENSITY": 67.04,
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "NOM_DEPT": "SEINE-MARITIME",
                        "POPULATION": 1254378,
                        "DENSITY": 198.53,
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "NOM_DEPT": "HAUTE-MARNE",
                        "POPULATION": 175640,
                        "DENSITY": 28.1,
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "NOM_DEPT": "GARD",
                        "POPULATION": 744178,
                        "DENSITY": 126.67,
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "NOM_DEPT": "BAS-RHIN",
                        "POPULATION": 1125559,
                        "DENSITY": 234.67,
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "NOM_DEPT": "AUDE",
                        "POPULATION": 370260,
                        "DENSITY": 58.3,
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "NOM_DEPT": "SEINE-ET-MARNE",
                        "POPULATION": 1403997,
                        "DENSITY": 236.98,
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "NOM_DEPT": "SOMME",
                        "POPULATION": 572443,
                        "DENSITY": 92.23,
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "NOM_DEPT": "HAUTE-LOIRE",
                        "POPULATION": 227283,
                        "DENSITY": 45.49,
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "NOM_DEPT": "MARNE",
                        "POPULATION": 568895,
                        "DENSITY": 69.41,
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "NOM_DEPT": "HAUTES-PYRENEES",
                        "POPULATION": 228530,
                        "DENSITY": 50.47,
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "NOM_DEPT": "LOT",
                        "POPULATION": 173828,
                        "DENSITY": 33.29,
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "NOM_DEPT": "ALPES-DE-HAUTE-PROVENCE",
                        "POPULATION": 163915,
                        "DENSITY": 23.44,
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "NOM_DEPT": "SARTHE",
                        "POPULATION": 566506,
                        "DENSITY": 90.83,
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "NOM_DEPT": "EURE-ET-LOIR",
                        "POPULATION": 433233,
                        "DENSITY": 73.09,
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "NOM_DEPT": "CORSE-DU-SUD",
                        "POPULATION": 157249,
                        "DENSITY": 39.03,
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "NOM_DEPT": "MEURTHE-ET-MOSELLE",
                        "POPULATION": 733481,
                        "DENSITY": 138.83,
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "NOM_DEPT": "ORNE",
                        "POPULATION": 283372,
                        "DENSITY": 46.13,
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "NOM_DEPT": "AIN",
                        "POPULATION": 643350,
                        "DENSITY": 111.43,
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "NOM_DEPT": "ARIEGE",
                        "POPULATION": 153153,
                        "DENSITY": 31.12,
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "NOM_DEPT": "CORREZE",
                        "POPULATION": 241464,
                        "DENSITY": 41.0,
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "NOM_DEPT": "HAUT-RHIN",
                        "POPULATION": 764030,
                        "DENSITY": 216.66,
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "NOM_DEPT": "INDRE-ET-LOIRE",
                        "POPULATION": 606511,
                        "DENSITY": 98.66,
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "NOM_DEPT": "NORD",
                        "POPULATION": 2604361,
                        "DENSITY": 450.97,
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "NOM_DEPT": "TERRITOIRE DE BELFORT",
                        "POPULATION": 142622,
                        "DENSITY": 233.94,
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "NOM_DEPT": "LOIRE-ATLANTIQUE",
                        "POPULATION": 1394909,
                        "DENSITY": 199.48,
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "NOM_DEPT": "YONNE",
                        "POPULATION": 338291,
                        "DENSITY": 45.4,
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "NOM_DEPT": "ILLE-ET-VILAINE",
                        "POPULATION": 1060199,
                        "DENSITY": 155.22,
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "NOM_DEPT": "LANDES",
                        "POPULATION": 407444,
                        "DENSITY": 43.56,
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "NOM_DEPT": "FINISTERE",
                        "POPULATION": 909028,
                        "DENSITY": 134.54,
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "NOM_DEPT": "HAUTE-SAVOIE",
                        "POPULATION": 807360,
                        "DENSITY": 175.65,
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "NOM_DEPT": "OISE",
                        "POPULATION": 824503,
                        "DENSITY": 139.9,
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "NOM_DEPT": "NIEVRE",
                        "POPULATION": 207182,
                        "DENSITY": 30.19,
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "NOM_DEPT": "COTE-D'OR",
                        "POPULATION": 532871,
                        "DENSITY": 60.64,
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "NOM_DEPT": "ESSONNE",
                        "POPULATION": 1296130,
                        "DENSITY": 712.81,
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "NOM_DEPT": "DEUX-SEVRES",
                        "POPULATION": 374351,
                        "DENSITY": 62.09,
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "NOM_DEPT": "COTES-D'ARMOR",
                        "POPULATION": 598814,
                        "DENSITY": 86.0,
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "NOM_DEPT": "ALLIER",
                        "POPULATION": 337988,
                        "DENSITY": 45.89,
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "NOM_DEPT": "CHARENTE-MARITIME",
                        "POPULATION": 644303,
                        "DENSITY": 93.2,
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "NOM_DEPT": "CANTAL",
                        "POPULATION": 145143,
                        "DENSITY": 25.17,
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "NOM_DEPT": "HERAULT",
                        "POPULATION": 1144892,
                        "DENSITY": 183.74,
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "NOM_DEPT": "DROME",
                        "POPULATION": 511553,
                        "DENSITY": 78.06,
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "NOM_DEPT": "PYRENEES-ORIENTALES",
                        "POPULATION": 474452,
                        "DENSITY": 114.39,
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "NOM_DEPT": "SAVOIE",
                        "POPULATION": 431174,
                        "DENSITY": 68.87,
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "NOM_DEPT": "HAUTES-ALPES",
                        "POPULATION": 141284,
                        "DENSITY": 24.85,
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "NOM_DEPT": "VAUCLUSE",
                        "POPULATION": 559479,
                        "DENSITY": 156.4,
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "NOM_DEPT": "INDRE",
                        "POPULATION": 222232,
                        "DENSITY": 32.27,
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "NOM_DEPT": "HAUTE-CORSE",
                        "POPULATION": 177689,
                        "DENSITY": 37.65,
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "NOM_DEPT": "HAUTE-VIENNE",
                        "POPULATION": 374426,
                        "DENSITY": 67.47,
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "NOM_DEPT": "VENDEE",
                        "POPULATION": 675247,
                        "DENSITY": 99.91,
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "NOM_DEPT": "VAR",
                        "POPULATION": 1058740,
                        "DENSITY": 176.37,
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "NOM_DEPT": "VAL-DE-MARNE",
                        "POPULATION": 1387926,
                        "DENSITY": 5671.95,
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "NOM_DEPT": "HAUTS-DE-SEINE",
                        "POPULATION": 1609306,
                        "DENSITY": 9163.05,
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "NOM_DEPT": "LOZERE",
                        "POPULATION": 76601,
                        "DENSITY": 14.81,
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "NOM_DEPT": "BOUCHES-DU-RHONE",
                        "POPULATION": 2024162,
                        "DENSITY": 398.26,
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "NOM_DEPT": "PARIS",
                        "POPULATION": 2187526,
                        "DENSITY": 20746.64,
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "NOM_DEPT": "SEINE-SAINT-DENIS",
                        "POPULATION": 1623111,
                        "DENSITY": 6849.73,
                    }
                },
            },
        },
    },
    3: {
        "geolayer_a": geolayer_fr_dept_data_and_geometry,
        "geolayer_b": geolayer_fr_dept_population,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_WITH_POPULATION",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": geolayer_fr_dept_population_geometry,
    },
    4: {
        "geolayer_a": geolayer_dpt_full,
        "geolayer_b": geolayer_dpt_pop_2,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_FULL_LEFT_JOIN_POP_2",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_FULL_LEFT_JOIN_POP_2",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "NOM_DEPT": "MAYENNE",
                        "POPULATION": 307445,
                        "DENSITY": 59.03,
                    }
                },
                1: {"attributes": {"CODE_DEPT": "02", "NOM_DEPT": "AISNE"}},
                2: {"attributes": {"CODE_DEPT": "95", "NOM_DEPT": "VAL-D'OISE"}},
                3: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
            },
        },
    },
    5: {
        "geolayer_a": geolayer_dpt_full_with_duplicate,
        "geolayer_b": geolayer_dpt_pop_2,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_FULL_WITH_DUPLICATE_LEFT_JOIN_POP_2",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_FULL_WITH_DUPLICATE_LEFT_JOIN_POP_2",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "NOM_DEPT": "MAYENNE",
                        "POPULATION": 307445,
                        "DENSITY": 59.03,
                    }
                },
                1: {"attributes": {"CODE_DEPT": "02", "NOM_DEPT": "AISNE"}},
                2: {"attributes": {"CODE_DEPT": "02", "NOM_DEPT": "AISNE"}},
                3: {"attributes": {"CODE_DEPT": "95", "NOM_DEPT": "VAL-D'OISE"}},
                4: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
            },
        },
    },
    6: {
        "geolayer_a": geolayer_dpt_2,
        "geolayer_b": geolayer_dpt_pop_full,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_LEFT_JOIN_POP_FULL",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_LEFT_JOIN_POP_FULL",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
            },
        },
    },
    7: {
        "geolayer_a": geolayer_dpt_2,
        "geolayer_b": geolayer_dpt_pop_full_with_duplicate,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_LEFT_JOIN_POP_FULL_WITH_DUPLICATE",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_LEFT_JOIN_POP_FULL_WITH_DUPLICATE",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
            },
        },
    },
    8: {
        "geolayer_a": geolayer_dpt_2,
        "geolayer_b": geolayer_dpt_pop_2,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_LEFT_JOIN_POP_2",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_LEFT_JOIN_POP_2",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"CODE_DEPT": "02", "NOM_DEPT": "AISNE"}},
                1: {"attributes": {"CODE_DEPT": "95", "NOM_DEPT": "VAL-D'OISE"}},
            },
        },
    },
    9: {
        "geolayer_a": geolayer_dpt_2_with_geom,
        "geolayer_b": geolayer_dpt_pop_full,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_LEFT_JOIN_POP_FULL",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_LEFT_JOIN_POP_FULL",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6861428.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                    },
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                    },
                },
            },
        },
    },
    10: {
        "geolayer_a": geolayer_dpt_2_with_geom,
        "geolayer_b": geolayer_dpt_pop_full,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_LEFT_JOIN_POP_FULL",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_LEFT_JOIN_POP_FULL",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
            },
        },
    },
    11: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2_with_geom,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_LEFT_JOIN_POP_FULL",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_LEFT_JOIN_POP_FULL",
                "fields": {
                    "POPULATION": {"type": "Integer", "index": 0},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 3},
                },
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6861428.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {"attributes": {"POPULATION": 307445, "DENSITY": 59.03}},
                1: {
                    "attributes": {
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                    },
                },
                2: {
                    "attributes": {
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                    },
                },
                3: {"attributes": {"POPULATION": 750863, "DENSITY": 109.39}},
            },
        },
    },
    12: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2_with_geom,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_LEFT_JOIN_POP_FULL",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": {"POPULATION": "pop"},
        "rename_output_field_from_geolayer_b": {"CODE_DEPT": "id"},
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_LEFT_JOIN_POP_FULL",
                "fields": {
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "pop": {"type": "Integer", "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 2},
                    "id": {"type": "String", "width": 2, "index": 3},
                },
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6861428.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {"attributes": {"DENSITY": 59.03, "pop": 307445}},
                1: {
                    "attributes": {
                        "DENSITY": 72.04,
                        "pop": 534490,
                        "NOM_DEPT": "AISNE",
                        "id": "02",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                    },
                },
                2: {
                    "attributes": {
                        "DENSITY": 979.62,
                        "pop": 1228618,
                        "NOM_DEPT": "VAL-D'OISE",
                        "id": "95",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                    },
                },
                3: {"attributes": {"DENSITY": 109.39, "pop": 750863}},
            },
        },
    },
    13: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2_with_geom,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_LEFT_JOIN_POP_FULL",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": {
            "CODE_DEPT": "code",
            "POPULATION": "pop",
        },
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": field_missing.format(field_name="CODE_DEPT"),
    },
    14: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "key_id": {"type": "Integer", "index": 0},
                    "price": {"type": "Integer", "index": 1},
                    "count": {"type": "Integer", "index": 2},
                    "probability": {
                        "type": "Real",
                        "width": 1,
                        "precision": 0,
                        "index": 3,
                    },
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "key_id": 164,
                        "price": 4300,
                        "count": 0,
                        "probability": 0.0,
                    }
                }
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "key_id": {"type": "Integer", "index": 0},
                    "price": {"type": "Integer", "index": 1},
                    "count": {"type": "Integer", "index": 2},
                    "probability": {
                        "type": "Real",
                        "width": 1,
                        "precision": 1,
                        "index": 3,
                    },
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "key_id": 0,
                        "price": 5000,
                        "count": 1,
                        "probability": 0.1,
                    }
                },
                1: {
                    "attributes": {
                        "key_id": 164,
                        "price": 4300,
                        "count": 1,
                        "probability": 0.1,
                    }
                },
            },
        },
        "on_field_a": "key_id",
        "on_field_b": "key_id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": {
            "key_id": "key_id_b",
            "price": "price_b",
            "count": "count_b",
            "probability": "probability_b",
        },
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "key_id": {"type": "Integer", "index": 0},
                    "price": {"type": "Integer", "index": 1},
                    "count": {"type": "Integer", "index": 2},
                    "probability": {
                        "type": "Real",
                        "width": 1,
                        "precision": 0,
                        "index": 3,
                    },
                    "key_id_b": {"type": "Integer", "index": 4},
                    "price_b": {"type": "Integer", "index": 5},
                    "count_b": {"type": "Integer", "index": 6},
                    "probability_b": {
                        "type": "Real",
                        "width": 1,
                        "precision": 1,
                        "index": 7,
                    },
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "key_id": 164,
                        "price": 4300,
                        "count": 0,
                        "probability": 0.0,
                        "key_id_b": 164,
                        "price_b": 4300,
                        "count_b": 1,
                        "probability_b": 0.1,
                    }
                }
            },
        },
    },
    15: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice"}},
                1: {"attributes": {"id": None, "name": "Bob"}},
                2: {"attributes": {"id": None, "name": "Patrick"}},
                3: {"attributes": {"id": 1, "name": "Jane"}},
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "age": {"type": "Integer", "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "age": 28}},
                1: {"attributes": {"id": 1, "age": 2}},
            },
        },
        "on_field_a": "id",
        "on_field_b": "id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                    "id1": {"type": "Integer", "index": 2},
                    "age": {"type": "Integer", "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice", "id1": 0, "age": 28}},
                1: {"attributes": {"id": None, "name": "Bob"}},
                2: {"attributes": {"id": None, "name": "Patrick"}},
                3: {"attributes": {"id": 1, "name": "Jane", "id1": 1, "age": 2}},
            },
        },
    },
    16: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 5, "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice"}},
                1: {"attributes": {"id": 1, "name": "Jane"}},
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "age": {"type": "Integer", "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "age": 28}},
                1: {"attributes": {"id": None, "age": 67}},
                2: {"attributes": {"id": None, "age": 15}},
                3: {"attributes": {"id": 1, "age": 2}},
            },
        },
        "on_field_a": "id",
        "on_field_b": "id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 5, "index": 1},
                    "id1": {"type": "Integer", "index": 2},
                    "age": {"type": "Integer", "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice", "id1": 0, "age": 28}},
                1: {"attributes": {"id": 1, "name": "Jane", "id1": 1, "age": 2}},
            },
        },
    },
    17: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice"}},
                1: {"attributes": {"id": None, "name": "Bob"}},
                2: {"attributes": {"id": None, "name": "Patrick"}},
                3: {"attributes": {"id": 1, "name": "Jane"}},
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "age": {"type": "Integer", "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "age": 28}},
                1: {"attributes": {"id": None, "age": 67}},
                2: {"attributes": {"id": None, "age": 15}},
                3: {"attributes": {"id": 1, "age": 2}},
            },
        },
        "on_field_a": "id",
        "on_field_b": "id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                    "id1": {"type": "Integer", "index": 2},
                    "age": {"type": "Integer", "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice", "id1": 0, "age": 28}},
                1: {"attributes": {"id": None, "name": "Bob"}},
                2: {"attributes": {"id": None, "name": "Patrick"}},
                3: {"attributes": {"id": 1, "name": "Jane", "id1": 1, "age": 2}},
            },
        },
    },
}

join_right_parameters = {
    0: {
        "geolayer_a": geolayer_fr_dept_population,
        "geolayer_b": geolayer_fr_dept_data_only,
        "on_field_b": "CODE_DEPT",
        "on_field_a": "CODE_DEPT",
        "output_geolayer_name": "fr_dept_data_only_right_join_fr_dept_population",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "fr_dept_data_only_right_join_fr_dept_population",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "INSEE_REG": {"type": "String", "width": 2, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "AREA": {"type": "Real", "width": 7, "precision": 2, "index": 3},
                    "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 4},
                    "CODE_DEPT1": {"type": "String", "width": 2, "index": 5},
                    "NOM_DEPT": {"type": "String", "width": 23, "index": 6},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "NOM_DEPT": "GERS",
                        "INSEE_REG": "76",
                        "POPULATION": 191091,
                        "AREA": 6304.33,
                        "DENSITY": 30.31,
                        "CODE_DEPT1": "32",
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "NOM_DEPT": "LOT-ET-GARONNE",
                        "INSEE_REG": "75",
                        "POPULATION": 332842,
                        "AREA": 5382.87,
                        "DENSITY": 61.83,
                        "CODE_DEPT1": "47",
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "NOM_DEPT": "ISERE",
                        "INSEE_REG": "84",
                        "POPULATION": 1258722,
                        "AREA": 7868.79,
                        "DENSITY": 159.96,
                        "CODE_DEPT1": "38",
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "NOM_DEPT": "PAS-DE-CALAIS",
                        "INSEE_REG": "32",
                        "POPULATION": 1468018,
                        "AREA": 6714.14,
                        "DENSITY": 218.65,
                        "CODE_DEPT1": "62",
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "NOM_DEPT": "ARDENNES",
                        "INSEE_REG": "44",
                        "POPULATION": 273579,
                        "AREA": 5253.13,
                        "DENSITY": 52.08,
                        "CODE_DEPT1": "08",
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "NOM_DEPT": "AUBE",
                        "INSEE_REG": "44",
                        "POPULATION": 310020,
                        "AREA": 6021.83,
                        "DENSITY": 51.48,
                        "CODE_DEPT1": "10",
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "NOM_DEPT": "ALPES-MARITIMES",
                        "INSEE_REG": "93",
                        "POPULATION": 1083310,
                        "AREA": 4291.62,
                        "DENSITY": 252.42,
                        "CODE_DEPT1": "06",
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "NOM_DEPT": "LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 762941,
                        "AREA": 4795.85,
                        "DENSITY": 159.08,
                        "CODE_DEPT1": "42",
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "NOM_DEPT": "HAUTE-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 1362672,
                        "AREA": 6364.82,
                        "DENSITY": 214.09,
                        "CODE_DEPT1": "31",
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "NOM_DEPT": "SAONE-ET-LOIRE",
                        "INSEE_REG": "27",
                        "POPULATION": 553595,
                        "AREA": 8598.33,
                        "DENSITY": 64.38,
                        "CODE_DEPT1": "71",
                    }
                },
                10: {
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
                11: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "NOM_DEPT": "CHARENTE",
                        "INSEE_REG": "75",
                        "POPULATION": 352335,
                        "AREA": 5963.54,
                        "DENSITY": 59.08,
                        "CODE_DEPT1": "16",
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "NOM_DEPT": "MANCHE",
                        "INSEE_REG": "28",
                        "POPULATION": 496883,
                        "AREA": 6015.07,
                        "DENSITY": 82.61,
                        "CODE_DEPT1": "50",
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "NOM_DEPT": "YVELINES",
                        "INSEE_REG": "11",
                        "POPULATION": 1438266,
                        "AREA": 2305.64,
                        "DENSITY": 623.8,
                        "CODE_DEPT1": "78",
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "NOM_DEPT": "DOUBS",
                        "INSEE_REG": "27",
                        "POPULATION": 539067,
                        "AREA": 5248.31,
                        "DENSITY": 102.71,
                        "CODE_DEPT1": "25",
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "NOM_DEPT": "MEUSE",
                        "INSEE_REG": "44",
                        "POPULATION": 187187,
                        "AREA": 6233.18,
                        "DENSITY": 30.03,
                        "CODE_DEPT1": "55",
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "NOM_DEPT": "GIRONDE",
                        "INSEE_REG": "75",
                        "POPULATION": 1583384,
                        "AREA": 10068.74,
                        "DENSITY": 157.26,
                        "CODE_DEPT1": "33",
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "NOM_DEPT": "CALVADOS",
                        "INSEE_REG": "28",
                        "POPULATION": 694002,
                        "AREA": 5588.48,
                        "DENSITY": 124.18,
                        "CODE_DEPT1": "14",
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "NOM_DEPT": "VOSGES",
                        "INSEE_REG": "44",
                        "POPULATION": 367673,
                        "AREA": 5891.56,
                        "DENSITY": 62.41,
                        "CODE_DEPT1": "88",
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "NOM_DEPT": "CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 304256,
                        "AREA": 7292.67,
                        "DENSITY": 41.72,
                        "CODE_DEPT1": "18",
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "NOM_DEPT": "ARDECHE",
                        "INSEE_REG": "84",
                        "POPULATION": 325712,
                        "AREA": 5562.05,
                        "DENSITY": 58.56,
                        "CODE_DEPT1": "07",
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "INSEE_REG": "32",
                        "POPULATION": 534490,
                        "AREA": 7418.97,
                        "DENSITY": 72.04,
                        "CODE_DEPT1": "02",
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "NOM_DEPT": "PYRENEES-ATLANTIQUES",
                        "INSEE_REG": "75",
                        "POPULATION": 677309,
                        "AREA": 7691.6,
                        "DENSITY": 88.06,
                        "CODE_DEPT1": "64",
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "NOM_DEPT": "LOIR-ET-CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 331915,
                        "AREA": 6412.3,
                        "DENSITY": 51.76,
                        "CODE_DEPT1": "41",
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "NOM_DEPT": "MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 1043522,
                        "AREA": 6252.63,
                        "DENSITY": 166.89,
                        "CODE_DEPT1": "57",
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "NOM_DEPT": "VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 436876,
                        "AREA": 7025.24,
                        "DENSITY": 62.19,
                        "CODE_DEPT1": "86",
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "NOM_DEPT": "DORDOGNE",
                        "INSEE_REG": "75",
                        "POPULATION": 413606,
                        "AREA": 9209.9,
                        "DENSITY": 44.91,
                        "CODE_DEPT1": "24",
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "NOM_DEPT": "JURA",
                        "INSEE_REG": "27",
                        "POPULATION": 260188,
                        "AREA": 5040.63,
                        "DENSITY": 51.62,
                        "CODE_DEPT1": "39",
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "NOM_DEPT": "TARN-ET-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 258349,
                        "AREA": 3731.0,
                        "DENSITY": 69.24,
                        "CODE_DEPT1": "82",
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "NOM_DEPT": "MAINE-ET-LOIRE",
                        "INSEE_REG": "52",
                        "POPULATION": 813493,
                        "AREA": 7161.34,
                        "DENSITY": 113.6,
                        "CODE_DEPT1": "49",
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "NOM_DEPT": "RHONE",
                        "INSEE_REG": "84",
                        "POPULATION": 1843319,
                        "AREA": 3253.11,
                        "DENSITY": 566.63,
                        "CODE_DEPT1": "69",
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "NOM_DEPT": "EURE",
                        "INSEE_REG": "28",
                        "POPULATION": 601843,
                        "AREA": 6035.85,
                        "DENSITY": 99.71,
                        "CODE_DEPT1": "27",
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "NOM_DEPT": "AVEYRON",
                        "INSEE_REG": "76",
                        "POPULATION": 279206,
                        "AREA": 8770.69,
                        "DENSITY": 31.83,
                        "CODE_DEPT1": "12",
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "NOM_DEPT": "CREUSE",
                        "INSEE_REG": "75",
                        "POPULATION": 118638,
                        "AREA": 5589.16,
                        "DENSITY": 21.23,
                        "CODE_DEPT1": "23",
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "NOM_DEPT": "LOIRET",
                        "INSEE_REG": "24",
                        "POPULATION": 678008,
                        "AREA": 6804.01,
                        "DENSITY": 99.65,
                        "CODE_DEPT1": "45",
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "NOM_DEPT": "HAUTE-SAONE",
                        "INSEE_REG": "27",
                        "POPULATION": 236659,
                        "AREA": 5382.37,
                        "DENSITY": 43.97,
                        "CODE_DEPT1": "70",
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "NOM_DEPT": "PUY-DE-DOME",
                        "INSEE_REG": "84",
                        "POPULATION": 653742,
                        "AREA": 8003.1,
                        "DENSITY": 81.69,
                        "CODE_DEPT1": "63",
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "NOM_DEPT": "TARN",
                        "INSEE_REG": "76",
                        "POPULATION": 387890,
                        "AREA": 5785.79,
                        "DENSITY": 67.04,
                        "CODE_DEPT1": "81",
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "NOM_DEPT": "SEINE-MARITIME",
                        "INSEE_REG": "28",
                        "POPULATION": 1254378,
                        "AREA": 6318.26,
                        "DENSITY": 198.53,
                        "CODE_DEPT1": "76",
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "NOM_DEPT": "HAUTE-MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 175640,
                        "AREA": 6249.91,
                        "DENSITY": 28.1,
                        "CODE_DEPT1": "52",
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "NOM_DEPT": "GARD",
                        "INSEE_REG": "76",
                        "POPULATION": 744178,
                        "AREA": 5874.71,
                        "DENSITY": 126.67,
                        "CODE_DEPT1": "30",
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "NOM_DEPT": "BAS-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 1125559,
                        "AREA": 4796.37,
                        "DENSITY": 234.67,
                        "CODE_DEPT1": "67",
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "NOM_DEPT": "AUDE",
                        "INSEE_REG": "76",
                        "POPULATION": 370260,
                        "AREA": 6351.35,
                        "DENSITY": 58.3,
                        "CODE_DEPT1": "11",
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "NOM_DEPT": "SEINE-ET-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1403997,
                        "AREA": 5924.64,
                        "DENSITY": 236.98,
                        "CODE_DEPT1": "77",
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "NOM_DEPT": "SOMME",
                        "INSEE_REG": "32",
                        "POPULATION": 572443,
                        "AREA": 6206.58,
                        "DENSITY": 92.23,
                        "CODE_DEPT1": "80",
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "NOM_DEPT": "HAUTE-LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 227283,
                        "AREA": 4996.58,
                        "DENSITY": 45.49,
                        "CODE_DEPT1": "43",
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "NOM_DEPT": "MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 568895,
                        "AREA": 8195.78,
                        "DENSITY": 69.41,
                        "CODE_DEPT1": "51",
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "NOM_DEPT": "HAUTES-PYRENEES",
                        "INSEE_REG": "76",
                        "POPULATION": 228530,
                        "AREA": 4527.89,
                        "DENSITY": 50.47,
                        "CODE_DEPT1": "65",
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "NOM_DEPT": "LOT",
                        "INSEE_REG": "76",
                        "POPULATION": 173828,
                        "AREA": 5221.64,
                        "DENSITY": 33.29,
                        "CODE_DEPT1": "46",
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "NOM_DEPT": "ALPES-DE-HAUTE-PROVENCE",
                        "INSEE_REG": "93",
                        "POPULATION": 163915,
                        "AREA": 6993.79,
                        "DENSITY": 23.44,
                        "CODE_DEPT1": "04",
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "NOM_DEPT": "SARTHE",
                        "INSEE_REG": "52",
                        "POPULATION": 566506,
                        "AREA": 6236.75,
                        "DENSITY": 90.83,
                        "CODE_DEPT1": "72",
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "INSEE_REG": "53",
                        "POPULATION": 750863,
                        "AREA": 6864.07,
                        "DENSITY": 109.39,
                        "CODE_DEPT1": "56",
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "NOM_DEPT": "EURE-ET-LOIR",
                        "INSEE_REG": "24",
                        "POPULATION": 433233,
                        "AREA": 5927.23,
                        "DENSITY": 73.09,
                        "CODE_DEPT1": "28",
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "NOM_DEPT": "CORSE-DU-SUD",
                        "INSEE_REG": "94",
                        "POPULATION": 157249,
                        "AREA": 4028.53,
                        "DENSITY": 39.03,
                        "CODE_DEPT1": "2A",
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "NOM_DEPT": "MEURTHE-ET-MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 733481,
                        "AREA": 5283.29,
                        "DENSITY": 138.83,
                        "CODE_DEPT1": "54",
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "NOM_DEPT": "ORNE",
                        "INSEE_REG": "28",
                        "POPULATION": 283372,
                        "AREA": 6142.73,
                        "DENSITY": 46.13,
                        "CODE_DEPT1": "61",
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "NOM_DEPT": "AIN",
                        "INSEE_REG": "84",
                        "POPULATION": 643350,
                        "AREA": 5773.77,
                        "DENSITY": 111.43,
                        "CODE_DEPT1": "01",
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "NOM_DEPT": "ARIEGE",
                        "INSEE_REG": "76",
                        "POPULATION": 153153,
                        "AREA": 4921.75,
                        "DENSITY": 31.12,
                        "CODE_DEPT1": "09",
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "NOM_DEPT": "CORREZE",
                        "INSEE_REG": "75",
                        "POPULATION": 241464,
                        "AREA": 5888.93,
                        "DENSITY": 41.0,
                        "CODE_DEPT1": "19",
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "NOM_DEPT": "HAUT-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 764030,
                        "AREA": 3526.37,
                        "DENSITY": 216.66,
                        "CODE_DEPT1": "68",
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "NOM_DEPT": "INDRE-ET-LOIRE",
                        "INSEE_REG": "24",
                        "POPULATION": 606511,
                        "AREA": 6147.6,
                        "DENSITY": 98.66,
                        "CODE_DEPT1": "37",
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "NOM_DEPT": "NORD",
                        "INSEE_REG": "32",
                        "POPULATION": 2604361,
                        "AREA": 5774.99,
                        "DENSITY": 450.97,
                        "CODE_DEPT1": "59",
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "NOM_DEPT": "TERRITOIRE DE BELFORT",
                        "INSEE_REG": "27",
                        "POPULATION": 142622,
                        "AREA": 609.64,
                        "DENSITY": 233.94,
                        "CODE_DEPT1": "90",
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "NOM_DEPT": "LOIRE-ATLANTIQUE",
                        "INSEE_REG": "52",
                        "POPULATION": 1394909,
                        "AREA": 6992.78,
                        "DENSITY": 199.48,
                        "CODE_DEPT1": "44",
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "NOM_DEPT": "YONNE",
                        "INSEE_REG": "27",
                        "POPULATION": 338291,
                        "AREA": 7450.97,
                        "DENSITY": 45.4,
                        "CODE_DEPT1": "89",
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "NOM_DEPT": "ILLE-ET-VILAINE",
                        "INSEE_REG": "53",
                        "POPULATION": 1060199,
                        "AREA": 6830.2,
                        "DENSITY": 155.22,
                        "CODE_DEPT1": "35",
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "NOM_DEPT": "LANDES",
                        "INSEE_REG": "75",
                        "POPULATION": 407444,
                        "AREA": 9353.03,
                        "DENSITY": 43.56,
                        "CODE_DEPT1": "40",
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "NOM_DEPT": "FINISTERE",
                        "INSEE_REG": "53",
                        "POPULATION": 909028,
                        "AREA": 6756.76,
                        "DENSITY": 134.54,
                        "CODE_DEPT1": "29",
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "NOM_DEPT": "HAUTE-SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 807360,
                        "AREA": 4596.53,
                        "DENSITY": 175.65,
                        "CODE_DEPT1": "74",
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "NOM_DEPT": "OISE",
                        "INSEE_REG": "32",
                        "POPULATION": 824503,
                        "AREA": 5893.6,
                        "DENSITY": 139.9,
                        "CODE_DEPT1": "60",
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "INSEE_REG": "11",
                        "POPULATION": 1228618,
                        "AREA": 1254.18,
                        "DENSITY": 979.62,
                        "CODE_DEPT1": "95",
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "NOM_DEPT": "NIEVRE",
                        "INSEE_REG": "27",
                        "POPULATION": 207182,
                        "AREA": 6862.87,
                        "DENSITY": 30.19,
                        "CODE_DEPT1": "58",
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "NOM_DEPT": "COTE-D'OR",
                        "INSEE_REG": "27",
                        "POPULATION": 532871,
                        "AREA": 8787.51,
                        "DENSITY": 60.64,
                        "CODE_DEPT1": "21",
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "NOM_DEPT": "ESSONNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1296130,
                        "AREA": 1818.35,
                        "DENSITY": 712.81,
                        "CODE_DEPT1": "91",
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "NOM_DEPT": "DEUX-SEVRES",
                        "INSEE_REG": "75",
                        "POPULATION": 374351,
                        "AREA": 6029.06,
                        "DENSITY": 62.09,
                        "CODE_DEPT1": "79",
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "NOM_DEPT": "COTES-D'ARMOR",
                        "INSEE_REG": "53",
                        "POPULATION": 598814,
                        "AREA": 6963.26,
                        "DENSITY": 86.0,
                        "CODE_DEPT1": "22",
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "NOM_DEPT": "ALLIER",
                        "INSEE_REG": "84",
                        "POPULATION": 337988,
                        "AREA": 7365.26,
                        "DENSITY": 45.89,
                        "CODE_DEPT1": "03",
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "NOM_DEPT": "CHARENTE-MARITIME",
                        "INSEE_REG": "75",
                        "POPULATION": 644303,
                        "AREA": 6913.03,
                        "DENSITY": 93.2,
                        "CODE_DEPT1": "17",
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "NOM_DEPT": "CANTAL",
                        "INSEE_REG": "84",
                        "POPULATION": 145143,
                        "AREA": 5767.47,
                        "DENSITY": 25.17,
                        "CODE_DEPT1": "15",
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "NOM_DEPT": "HERAULT",
                        "INSEE_REG": "76",
                        "POPULATION": 1144892,
                        "AREA": 6231.05,
                        "DENSITY": 183.74,
                        "CODE_DEPT1": "34",
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "NOM_DEPT": "DROME",
                        "INSEE_REG": "84",
                        "POPULATION": 511553,
                        "AREA": 6553.53,
                        "DENSITY": 78.06,
                        "CODE_DEPT1": "26",
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "NOM_DEPT": "PYRENEES-ORIENTALES",
                        "INSEE_REG": "76",
                        "POPULATION": 474452,
                        "AREA": 4147.76,
                        "DENSITY": 114.39,
                        "CODE_DEPT1": "66",
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "NOM_DEPT": "SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 431174,
                        "AREA": 6260.4,
                        "DENSITY": 68.87,
                        "CODE_DEPT1": "73",
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "NOM_DEPT": "HAUTES-ALPES",
                        "INSEE_REG": "93",
                        "POPULATION": 141284,
                        "AREA": 5685.31,
                        "DENSITY": 24.85,
                        "CODE_DEPT1": "05",
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "NOM_DEPT": "VAUCLUSE",
                        "INSEE_REG": "93",
                        "POPULATION": 559479,
                        "AREA": 3577.19,
                        "DENSITY": 156.4,
                        "CODE_DEPT1": "84",
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "NOM_DEPT": "INDRE",
                        "INSEE_REG": "24",
                        "POPULATION": 222232,
                        "AREA": 6887.38,
                        "DENSITY": 32.27,
                        "CODE_DEPT1": "36",
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "NOM_DEPT": "HAUTE-CORSE",
                        "INSEE_REG": "94",
                        "POPULATION": 177689,
                        "AREA": 4719.71,
                        "DENSITY": 37.65,
                        "CODE_DEPT1": "2B",
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "NOM_DEPT": "HAUTE-VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 374426,
                        "AREA": 5549.31,
                        "DENSITY": 67.47,
                        "CODE_DEPT1": "87",
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "NOM_DEPT": "VENDEE",
                        "INSEE_REG": "52",
                        "POPULATION": 675247,
                        "AREA": 6758.23,
                        "DENSITY": 99.91,
                        "CODE_DEPT1": "85",
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "NOM_DEPT": "VAR",
                        "INSEE_REG": "93",
                        "POPULATION": 1058740,
                        "AREA": 6002.84,
                        "DENSITY": 176.37,
                        "CODE_DEPT1": "83",
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "NOM_DEPT": "VAL-DE-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1387926,
                        "AREA": 244.7,
                        "DENSITY": 5671.95,
                        "CODE_DEPT1": "94",
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "NOM_DEPT": "HAUTS-DE-SEINE",
                        "INSEE_REG": "11",
                        "POPULATION": 1609306,
                        "AREA": 175.63,
                        "DENSITY": 9163.05,
                        "CODE_DEPT1": "92",
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "NOM_DEPT": "LOZERE",
                        "INSEE_REG": "76",
                        "POPULATION": 76601,
                        "AREA": 5172.02,
                        "DENSITY": 14.81,
                        "CODE_DEPT1": "48",
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "NOM_DEPT": "BOUCHES-DU-RHONE",
                        "INSEE_REG": "93",
                        "POPULATION": 2024162,
                        "AREA": 5082.57,
                        "DENSITY": 398.26,
                        "CODE_DEPT1": "13",
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "NOM_DEPT": "PARIS",
                        "INSEE_REG": "11",
                        "POPULATION": 2187526,
                        "AREA": 105.44,
                        "DENSITY": 20746.64,
                        "CODE_DEPT1": "75",
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "NOM_DEPT": "SEINE-SAINT-DENIS",
                        "INSEE_REG": "11",
                        "POPULATION": 1623111,
                        "AREA": 236.96,
                        "DENSITY": 6849.73,
                        "CODE_DEPT1": "93",
                    }
                },
            },
        },
    },
    1: {
        "geolayer_a": geolayer_fr_dept_population,
        "geolayer_b": geolayer_fr_dept_data_only,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "fr_dept_population_right_join_fr_dept_data_only",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "fr_dept_population_right_join_fr_dept_data_only",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "INSEE_REG": {"type": "String", "width": 2, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "AREA": {"type": "Real", "width": 7, "precision": 2, "index": 3},
                    "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 4},
                    "CODE_DEPT1": {"type": "String", "width": 2, "index": 5},
                    "NOM_DEPT": {"type": "String", "width": 23, "index": 6},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "NOM_DEPT": "GERS",
                        "INSEE_REG": "76",
                        "POPULATION": 191091,
                        "AREA": 6304.33,
                        "DENSITY": 30.31,
                        "CODE_DEPT1": "32",
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "NOM_DEPT": "LOT-ET-GARONNE",
                        "INSEE_REG": "75",
                        "POPULATION": 332842,
                        "AREA": 5382.87,
                        "DENSITY": 61.83,
                        "CODE_DEPT1": "47",
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "NOM_DEPT": "ISERE",
                        "INSEE_REG": "84",
                        "POPULATION": 1258722,
                        "AREA": 7868.79,
                        "DENSITY": 159.96,
                        "CODE_DEPT1": "38",
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "NOM_DEPT": "PAS-DE-CALAIS",
                        "INSEE_REG": "32",
                        "POPULATION": 1468018,
                        "AREA": 6714.14,
                        "DENSITY": 218.65,
                        "CODE_DEPT1": "62",
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "NOM_DEPT": "ARDENNES",
                        "INSEE_REG": "44",
                        "POPULATION": 273579,
                        "AREA": 5253.13,
                        "DENSITY": 52.08,
                        "CODE_DEPT1": "08",
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "NOM_DEPT": "AUBE",
                        "INSEE_REG": "44",
                        "POPULATION": 310020,
                        "AREA": 6021.83,
                        "DENSITY": 51.48,
                        "CODE_DEPT1": "10",
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "NOM_DEPT": "ALPES-MARITIMES",
                        "INSEE_REG": "93",
                        "POPULATION": 1083310,
                        "AREA": 4291.62,
                        "DENSITY": 252.42,
                        "CODE_DEPT1": "06",
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "NOM_DEPT": "LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 762941,
                        "AREA": 4795.85,
                        "DENSITY": 159.08,
                        "CODE_DEPT1": "42",
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "NOM_DEPT": "HAUTE-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 1362672,
                        "AREA": 6364.82,
                        "DENSITY": 214.09,
                        "CODE_DEPT1": "31",
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "NOM_DEPT": "SAONE-ET-LOIRE",
                        "INSEE_REG": "27",
                        "POPULATION": 553595,
                        "AREA": 8598.33,
                        "DENSITY": 64.38,
                        "CODE_DEPT1": "71",
                    }
                },
                10: {
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
                11: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "NOM_DEPT": "CHARENTE",
                        "INSEE_REG": "75",
                        "POPULATION": 352335,
                        "AREA": 5963.54,
                        "DENSITY": 59.08,
                        "CODE_DEPT1": "16",
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "NOM_DEPT": "MANCHE",
                        "INSEE_REG": "28",
                        "POPULATION": 496883,
                        "AREA": 6015.07,
                        "DENSITY": 82.61,
                        "CODE_DEPT1": "50",
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "NOM_DEPT": "YVELINES",
                        "INSEE_REG": "11",
                        "POPULATION": 1438266,
                        "AREA": 2305.64,
                        "DENSITY": 623.8,
                        "CODE_DEPT1": "78",
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "NOM_DEPT": "DOUBS",
                        "INSEE_REG": "27",
                        "POPULATION": 539067,
                        "AREA": 5248.31,
                        "DENSITY": 102.71,
                        "CODE_DEPT1": "25",
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "NOM_DEPT": "MEUSE",
                        "INSEE_REG": "44",
                        "POPULATION": 187187,
                        "AREA": 6233.18,
                        "DENSITY": 30.03,
                        "CODE_DEPT1": "55",
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "NOM_DEPT": "GIRONDE",
                        "INSEE_REG": "75",
                        "POPULATION": 1583384,
                        "AREA": 10068.74,
                        "DENSITY": 157.26,
                        "CODE_DEPT1": "33",
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "NOM_DEPT": "CALVADOS",
                        "INSEE_REG": "28",
                        "POPULATION": 694002,
                        "AREA": 5588.48,
                        "DENSITY": 124.18,
                        "CODE_DEPT1": "14",
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "NOM_DEPT": "VOSGES",
                        "INSEE_REG": "44",
                        "POPULATION": 367673,
                        "AREA": 5891.56,
                        "DENSITY": 62.41,
                        "CODE_DEPT1": "88",
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "NOM_DEPT": "CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 304256,
                        "AREA": 7292.67,
                        "DENSITY": 41.72,
                        "CODE_DEPT1": "18",
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "NOM_DEPT": "ARDECHE",
                        "INSEE_REG": "84",
                        "POPULATION": 325712,
                        "AREA": 5562.05,
                        "DENSITY": 58.56,
                        "CODE_DEPT1": "07",
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "INSEE_REG": "32",
                        "POPULATION": 534490,
                        "AREA": 7418.97,
                        "DENSITY": 72.04,
                        "CODE_DEPT1": "02",
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "NOM_DEPT": "PYRENEES-ATLANTIQUES",
                        "INSEE_REG": "75",
                        "POPULATION": 677309,
                        "AREA": 7691.6,
                        "DENSITY": 88.06,
                        "CODE_DEPT1": "64",
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "NOM_DEPT": "LOIR-ET-CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 331915,
                        "AREA": 6412.3,
                        "DENSITY": 51.76,
                        "CODE_DEPT1": "41",
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "NOM_DEPT": "MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 1043522,
                        "AREA": 6252.63,
                        "DENSITY": 166.89,
                        "CODE_DEPT1": "57",
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "NOM_DEPT": "VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 436876,
                        "AREA": 7025.24,
                        "DENSITY": 62.19,
                        "CODE_DEPT1": "86",
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "NOM_DEPT": "DORDOGNE",
                        "INSEE_REG": "75",
                        "POPULATION": 413606,
                        "AREA": 9209.9,
                        "DENSITY": 44.91,
                        "CODE_DEPT1": "24",
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "NOM_DEPT": "JURA",
                        "INSEE_REG": "27",
                        "POPULATION": 260188,
                        "AREA": 5040.63,
                        "DENSITY": 51.62,
                        "CODE_DEPT1": "39",
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "NOM_DEPT": "TARN-ET-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 258349,
                        "AREA": 3731.0,
                        "DENSITY": 69.24,
                        "CODE_DEPT1": "82",
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "NOM_DEPT": "MAINE-ET-LOIRE",
                        "INSEE_REG": "52",
                        "POPULATION": 813493,
                        "AREA": 7161.34,
                        "DENSITY": 113.6,
                        "CODE_DEPT1": "49",
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "NOM_DEPT": "RHONE",
                        "INSEE_REG": "84",
                        "POPULATION": 1843319,
                        "AREA": 3253.11,
                        "DENSITY": 566.63,
                        "CODE_DEPT1": "69",
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "NOM_DEPT": "EURE",
                        "INSEE_REG": "28",
                        "POPULATION": 601843,
                        "AREA": 6035.85,
                        "DENSITY": 99.71,
                        "CODE_DEPT1": "27",
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "NOM_DEPT": "AVEYRON",
                        "INSEE_REG": "76",
                        "POPULATION": 279206,
                        "AREA": 8770.69,
                        "DENSITY": 31.83,
                        "CODE_DEPT1": "12",
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "NOM_DEPT": "CREUSE",
                        "INSEE_REG": "75",
                        "POPULATION": 118638,
                        "AREA": 5589.16,
                        "DENSITY": 21.23,
                        "CODE_DEPT1": "23",
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "NOM_DEPT": "LOIRET",
                        "INSEE_REG": "24",
                        "POPULATION": 678008,
                        "AREA": 6804.01,
                        "DENSITY": 99.65,
                        "CODE_DEPT1": "45",
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "NOM_DEPT": "HAUTE-SAONE",
                        "INSEE_REG": "27",
                        "POPULATION": 236659,
                        "AREA": 5382.37,
                        "DENSITY": 43.97,
                        "CODE_DEPT1": "70",
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "NOM_DEPT": "PUY-DE-DOME",
                        "INSEE_REG": "84",
                        "POPULATION": 653742,
                        "AREA": 8003.1,
                        "DENSITY": 81.69,
                        "CODE_DEPT1": "63",
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "NOM_DEPT": "TARN",
                        "INSEE_REG": "76",
                        "POPULATION": 387890,
                        "AREA": 5785.79,
                        "DENSITY": 67.04,
                        "CODE_DEPT1": "81",
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "NOM_DEPT": "SEINE-MARITIME",
                        "INSEE_REG": "28",
                        "POPULATION": 1254378,
                        "AREA": 6318.26,
                        "DENSITY": 198.53,
                        "CODE_DEPT1": "76",
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "NOM_DEPT": "HAUTE-MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 175640,
                        "AREA": 6249.91,
                        "DENSITY": 28.1,
                        "CODE_DEPT1": "52",
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "NOM_DEPT": "GARD",
                        "INSEE_REG": "76",
                        "POPULATION": 744178,
                        "AREA": 5874.71,
                        "DENSITY": 126.67,
                        "CODE_DEPT1": "30",
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "NOM_DEPT": "BAS-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 1125559,
                        "AREA": 4796.37,
                        "DENSITY": 234.67,
                        "CODE_DEPT1": "67",
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "NOM_DEPT": "AUDE",
                        "INSEE_REG": "76",
                        "POPULATION": 370260,
                        "AREA": 6351.35,
                        "DENSITY": 58.3,
                        "CODE_DEPT1": "11",
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "NOM_DEPT": "SEINE-ET-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1403997,
                        "AREA": 5924.64,
                        "DENSITY": 236.98,
                        "CODE_DEPT1": "77",
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "NOM_DEPT": "SOMME",
                        "INSEE_REG": "32",
                        "POPULATION": 572443,
                        "AREA": 6206.58,
                        "DENSITY": 92.23,
                        "CODE_DEPT1": "80",
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "NOM_DEPT": "HAUTE-LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 227283,
                        "AREA": 4996.58,
                        "DENSITY": 45.49,
                        "CODE_DEPT1": "43",
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "NOM_DEPT": "MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 568895,
                        "AREA": 8195.78,
                        "DENSITY": 69.41,
                        "CODE_DEPT1": "51",
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "NOM_DEPT": "HAUTES-PYRENEES",
                        "INSEE_REG": "76",
                        "POPULATION": 228530,
                        "AREA": 4527.89,
                        "DENSITY": 50.47,
                        "CODE_DEPT1": "65",
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "NOM_DEPT": "LOT",
                        "INSEE_REG": "76",
                        "POPULATION": 173828,
                        "AREA": 5221.64,
                        "DENSITY": 33.29,
                        "CODE_DEPT1": "46",
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "NOM_DEPT": "ALPES-DE-HAUTE-PROVENCE",
                        "INSEE_REG": "93",
                        "POPULATION": 163915,
                        "AREA": 6993.79,
                        "DENSITY": 23.44,
                        "CODE_DEPT1": "04",
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "NOM_DEPT": "SARTHE",
                        "INSEE_REG": "52",
                        "POPULATION": 566506,
                        "AREA": 6236.75,
                        "DENSITY": 90.83,
                        "CODE_DEPT1": "72",
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "INSEE_REG": "53",
                        "POPULATION": 750863,
                        "AREA": 6864.07,
                        "DENSITY": 109.39,
                        "CODE_DEPT1": "56",
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "NOM_DEPT": "EURE-ET-LOIR",
                        "INSEE_REG": "24",
                        "POPULATION": 433233,
                        "AREA": 5927.23,
                        "DENSITY": 73.09,
                        "CODE_DEPT1": "28",
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "NOM_DEPT": "CORSE-DU-SUD",
                        "INSEE_REG": "94",
                        "POPULATION": 157249,
                        "AREA": 4028.53,
                        "DENSITY": 39.03,
                        "CODE_DEPT1": "2A",
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "NOM_DEPT": "MEURTHE-ET-MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 733481,
                        "AREA": 5283.29,
                        "DENSITY": 138.83,
                        "CODE_DEPT1": "54",
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "NOM_DEPT": "ORNE",
                        "INSEE_REG": "28",
                        "POPULATION": 283372,
                        "AREA": 6142.73,
                        "DENSITY": 46.13,
                        "CODE_DEPT1": "61",
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "NOM_DEPT": "AIN",
                        "INSEE_REG": "84",
                        "POPULATION": 643350,
                        "AREA": 5773.77,
                        "DENSITY": 111.43,
                        "CODE_DEPT1": "01",
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "NOM_DEPT": "ARIEGE",
                        "INSEE_REG": "76",
                        "POPULATION": 153153,
                        "AREA": 4921.75,
                        "DENSITY": 31.12,
                        "CODE_DEPT1": "09",
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "NOM_DEPT": "CORREZE",
                        "INSEE_REG": "75",
                        "POPULATION": 241464,
                        "AREA": 5888.93,
                        "DENSITY": 41.0,
                        "CODE_DEPT1": "19",
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "NOM_DEPT": "HAUT-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 764030,
                        "AREA": 3526.37,
                        "DENSITY": 216.66,
                        "CODE_DEPT1": "68",
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "NOM_DEPT": "INDRE-ET-LOIRE",
                        "INSEE_REG": "24",
                        "POPULATION": 606511,
                        "AREA": 6147.6,
                        "DENSITY": 98.66,
                        "CODE_DEPT1": "37",
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "NOM_DEPT": "NORD",
                        "INSEE_REG": "32",
                        "POPULATION": 2604361,
                        "AREA": 5774.99,
                        "DENSITY": 450.97,
                        "CODE_DEPT1": "59",
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "NOM_DEPT": "TERRITOIRE DE BELFORT",
                        "INSEE_REG": "27",
                        "POPULATION": 142622,
                        "AREA": 609.64,
                        "DENSITY": 233.94,
                        "CODE_DEPT1": "90",
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "NOM_DEPT": "LOIRE-ATLANTIQUE",
                        "INSEE_REG": "52",
                        "POPULATION": 1394909,
                        "AREA": 6992.78,
                        "DENSITY": 199.48,
                        "CODE_DEPT1": "44",
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "NOM_DEPT": "YONNE",
                        "INSEE_REG": "27",
                        "POPULATION": 338291,
                        "AREA": 7450.97,
                        "DENSITY": 45.4,
                        "CODE_DEPT1": "89",
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "NOM_DEPT": "ILLE-ET-VILAINE",
                        "INSEE_REG": "53",
                        "POPULATION": 1060199,
                        "AREA": 6830.2,
                        "DENSITY": 155.22,
                        "CODE_DEPT1": "35",
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "NOM_DEPT": "LANDES",
                        "INSEE_REG": "75",
                        "POPULATION": 407444,
                        "AREA": 9353.03,
                        "DENSITY": 43.56,
                        "CODE_DEPT1": "40",
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "NOM_DEPT": "FINISTERE",
                        "INSEE_REG": "53",
                        "POPULATION": 909028,
                        "AREA": 6756.76,
                        "DENSITY": 134.54,
                        "CODE_DEPT1": "29",
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "NOM_DEPT": "HAUTE-SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 807360,
                        "AREA": 4596.53,
                        "DENSITY": 175.65,
                        "CODE_DEPT1": "74",
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "NOM_DEPT": "OISE",
                        "INSEE_REG": "32",
                        "POPULATION": 824503,
                        "AREA": 5893.6,
                        "DENSITY": 139.9,
                        "CODE_DEPT1": "60",
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "INSEE_REG": "11",
                        "POPULATION": 1228618,
                        "AREA": 1254.18,
                        "DENSITY": 979.62,
                        "CODE_DEPT1": "95",
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "NOM_DEPT": "NIEVRE",
                        "INSEE_REG": "27",
                        "POPULATION": 207182,
                        "AREA": 6862.87,
                        "DENSITY": 30.19,
                        "CODE_DEPT1": "58",
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "NOM_DEPT": "COTE-D'OR",
                        "INSEE_REG": "27",
                        "POPULATION": 532871,
                        "AREA": 8787.51,
                        "DENSITY": 60.64,
                        "CODE_DEPT1": "21",
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "NOM_DEPT": "ESSONNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1296130,
                        "AREA": 1818.35,
                        "DENSITY": 712.81,
                        "CODE_DEPT1": "91",
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "NOM_DEPT": "DEUX-SEVRES",
                        "INSEE_REG": "75",
                        "POPULATION": 374351,
                        "AREA": 6029.06,
                        "DENSITY": 62.09,
                        "CODE_DEPT1": "79",
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "NOM_DEPT": "COTES-D'ARMOR",
                        "INSEE_REG": "53",
                        "POPULATION": 598814,
                        "AREA": 6963.26,
                        "DENSITY": 86.0,
                        "CODE_DEPT1": "22",
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "NOM_DEPT": "ALLIER",
                        "INSEE_REG": "84",
                        "POPULATION": 337988,
                        "AREA": 7365.26,
                        "DENSITY": 45.89,
                        "CODE_DEPT1": "03",
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "NOM_DEPT": "CHARENTE-MARITIME",
                        "INSEE_REG": "75",
                        "POPULATION": 644303,
                        "AREA": 6913.03,
                        "DENSITY": 93.2,
                        "CODE_DEPT1": "17",
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "NOM_DEPT": "CANTAL",
                        "INSEE_REG": "84",
                        "POPULATION": 145143,
                        "AREA": 5767.47,
                        "DENSITY": 25.17,
                        "CODE_DEPT1": "15",
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "NOM_DEPT": "HERAULT",
                        "INSEE_REG": "76",
                        "POPULATION": 1144892,
                        "AREA": 6231.05,
                        "DENSITY": 183.74,
                        "CODE_DEPT1": "34",
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "NOM_DEPT": "DROME",
                        "INSEE_REG": "84",
                        "POPULATION": 511553,
                        "AREA": 6553.53,
                        "DENSITY": 78.06,
                        "CODE_DEPT1": "26",
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "NOM_DEPT": "PYRENEES-ORIENTALES",
                        "INSEE_REG": "76",
                        "POPULATION": 474452,
                        "AREA": 4147.76,
                        "DENSITY": 114.39,
                        "CODE_DEPT1": "66",
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "NOM_DEPT": "SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 431174,
                        "AREA": 6260.4,
                        "DENSITY": 68.87,
                        "CODE_DEPT1": "73",
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "NOM_DEPT": "HAUTES-ALPES",
                        "INSEE_REG": "93",
                        "POPULATION": 141284,
                        "AREA": 5685.31,
                        "DENSITY": 24.85,
                        "CODE_DEPT1": "05",
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "NOM_DEPT": "VAUCLUSE",
                        "INSEE_REG": "93",
                        "POPULATION": 559479,
                        "AREA": 3577.19,
                        "DENSITY": 156.4,
                        "CODE_DEPT1": "84",
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "NOM_DEPT": "INDRE",
                        "INSEE_REG": "24",
                        "POPULATION": 222232,
                        "AREA": 6887.38,
                        "DENSITY": 32.27,
                        "CODE_DEPT1": "36",
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "NOM_DEPT": "HAUTE-CORSE",
                        "INSEE_REG": "94",
                        "POPULATION": 177689,
                        "AREA": 4719.71,
                        "DENSITY": 37.65,
                        "CODE_DEPT1": "2B",
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "NOM_DEPT": "HAUTE-VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 374426,
                        "AREA": 5549.31,
                        "DENSITY": 67.47,
                        "CODE_DEPT1": "87",
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "NOM_DEPT": "VENDEE",
                        "INSEE_REG": "52",
                        "POPULATION": 675247,
                        "AREA": 6758.23,
                        "DENSITY": 99.91,
                        "CODE_DEPT1": "85",
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "NOM_DEPT": "VAR",
                        "INSEE_REG": "93",
                        "POPULATION": 1058740,
                        "AREA": 6002.84,
                        "DENSITY": 176.37,
                        "CODE_DEPT1": "83",
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "NOM_DEPT": "VAL-DE-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1387926,
                        "AREA": 244.7,
                        "DENSITY": 5671.95,
                        "CODE_DEPT1": "94",
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "NOM_DEPT": "HAUTS-DE-SEINE",
                        "INSEE_REG": "11",
                        "POPULATION": 1609306,
                        "AREA": 175.63,
                        "DENSITY": 9163.05,
                        "CODE_DEPT1": "92",
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "NOM_DEPT": "LOZERE",
                        "INSEE_REG": "76",
                        "POPULATION": 76601,
                        "AREA": 5172.02,
                        "DENSITY": 14.81,
                        "CODE_DEPT1": "48",
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "NOM_DEPT": "BOUCHES-DU-RHONE",
                        "INSEE_REG": "93",
                        "POPULATION": 2024162,
                        "AREA": 5082.57,
                        "DENSITY": 398.26,
                        "CODE_DEPT1": "13",
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "NOM_DEPT": "PARIS",
                        "INSEE_REG": "11",
                        "POPULATION": 2187526,
                        "AREA": 105.44,
                        "DENSITY": 20746.64,
                        "CODE_DEPT1": "75",
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "NOM_DEPT": "SEINE-SAINT-DENIS",
                        "INSEE_REG": "11",
                        "POPULATION": 1623111,
                        "AREA": 236.96,
                        "DENSITY": 6849.73,
                        "CODE_DEPT1": "93",
                    }
                },
            },
        },
    },
    2: {
        "geolayer_a": geolayer_fr_dept_population,
        "geolayer_b": geolayer_fr_dept_data_only,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "fr_dept_data_only_right_join_fr_dept_population",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "fr_dept_data_only_right_join_fr_dept_population",
                "fields": {
                    "POPULATION": {"type": "Integer", "index": 0},
                    "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 1},
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT": {"type": "String", "width": 23, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "NOM_DEPT": "GERS",
                        "POPULATION": 191091,
                        "DENSITY": 30.31,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "NOM_DEPT": "LOT-ET-GARONNE",
                        "POPULATION": 332842,
                        "DENSITY": 61.83,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "NOM_DEPT": "ISERE",
                        "POPULATION": 1258722,
                        "DENSITY": 159.96,
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "NOM_DEPT": "PAS-DE-CALAIS",
                        "POPULATION": 1468018,
                        "DENSITY": 218.65,
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "NOM_DEPT": "ARDENNES",
                        "POPULATION": 273579,
                        "DENSITY": 52.08,
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "NOM_DEPT": "AUBE",
                        "POPULATION": 310020,
                        "DENSITY": 51.48,
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "NOM_DEPT": "ALPES-MARITIMES",
                        "POPULATION": 1083310,
                        "DENSITY": 252.42,
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "NOM_DEPT": "LOIRE",
                        "POPULATION": 762941,
                        "DENSITY": 159.08,
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "NOM_DEPT": "HAUTE-GARONNE",
                        "POPULATION": 1362672,
                        "DENSITY": 214.09,
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "NOM_DEPT": "SAONE-ET-LOIRE",
                        "POPULATION": 553595,
                        "DENSITY": 64.38,
                    }
                },
                10: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "NOM_DEPT": "MAYENNE",
                        "POPULATION": 307445,
                        "DENSITY": 59.03,
                    }
                },
                11: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "NOM_DEPT": "CHARENTE",
                        "POPULATION": 352335,
                        "DENSITY": 59.08,
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "NOM_DEPT": "MANCHE",
                        "POPULATION": 496883,
                        "DENSITY": 82.61,
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "NOM_DEPT": "YVELINES",
                        "POPULATION": 1438266,
                        "DENSITY": 623.8,
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "NOM_DEPT": "DOUBS",
                        "POPULATION": 539067,
                        "DENSITY": 102.71,
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "NOM_DEPT": "MEUSE",
                        "POPULATION": 187187,
                        "DENSITY": 30.03,
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "NOM_DEPT": "GIRONDE",
                        "POPULATION": 1583384,
                        "DENSITY": 157.26,
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "NOM_DEPT": "CALVADOS",
                        "POPULATION": 694002,
                        "DENSITY": 124.18,
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "NOM_DEPT": "VOSGES",
                        "POPULATION": 367673,
                        "DENSITY": 62.41,
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "NOM_DEPT": "CHER",
                        "POPULATION": 304256,
                        "DENSITY": 41.72,
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "NOM_DEPT": "ARDECHE",
                        "POPULATION": 325712,
                        "DENSITY": 58.56,
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "NOM_DEPT": "PYRENEES-ATLANTIQUES",
                        "POPULATION": 677309,
                        "DENSITY": 88.06,
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "NOM_DEPT": "LOIR-ET-CHER",
                        "POPULATION": 331915,
                        "DENSITY": 51.76,
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "NOM_DEPT": "MOSELLE",
                        "POPULATION": 1043522,
                        "DENSITY": 166.89,
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "NOM_DEPT": "VIENNE",
                        "POPULATION": 436876,
                        "DENSITY": 62.19,
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "NOM_DEPT": "DORDOGNE",
                        "POPULATION": 413606,
                        "DENSITY": 44.91,
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "NOM_DEPT": "JURA",
                        "POPULATION": 260188,
                        "DENSITY": 51.62,
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "NOM_DEPT": "TARN-ET-GARONNE",
                        "POPULATION": 258349,
                        "DENSITY": 69.24,
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "NOM_DEPT": "MAINE-ET-LOIRE",
                        "POPULATION": 813493,
                        "DENSITY": 113.6,
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "NOM_DEPT": "RHONE",
                        "POPULATION": 1843319,
                        "DENSITY": 566.63,
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "NOM_DEPT": "EURE",
                        "POPULATION": 601843,
                        "DENSITY": 99.71,
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "NOM_DEPT": "AVEYRON",
                        "POPULATION": 279206,
                        "DENSITY": 31.83,
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "NOM_DEPT": "CREUSE",
                        "POPULATION": 118638,
                        "DENSITY": 21.23,
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "NOM_DEPT": "LOIRET",
                        "POPULATION": 678008,
                        "DENSITY": 99.65,
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "NOM_DEPT": "HAUTE-SAONE",
                        "POPULATION": 236659,
                        "DENSITY": 43.97,
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "NOM_DEPT": "PUY-DE-DOME",
                        "POPULATION": 653742,
                        "DENSITY": 81.69,
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "NOM_DEPT": "TARN",
                        "POPULATION": 387890,
                        "DENSITY": 67.04,
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "NOM_DEPT": "SEINE-MARITIME",
                        "POPULATION": 1254378,
                        "DENSITY": 198.53,
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "NOM_DEPT": "HAUTE-MARNE",
                        "POPULATION": 175640,
                        "DENSITY": 28.1,
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "NOM_DEPT": "GARD",
                        "POPULATION": 744178,
                        "DENSITY": 126.67,
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "NOM_DEPT": "BAS-RHIN",
                        "POPULATION": 1125559,
                        "DENSITY": 234.67,
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "NOM_DEPT": "AUDE",
                        "POPULATION": 370260,
                        "DENSITY": 58.3,
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "NOM_DEPT": "SEINE-ET-MARNE",
                        "POPULATION": 1403997,
                        "DENSITY": 236.98,
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "NOM_DEPT": "SOMME",
                        "POPULATION": 572443,
                        "DENSITY": 92.23,
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "NOM_DEPT": "HAUTE-LOIRE",
                        "POPULATION": 227283,
                        "DENSITY": 45.49,
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "NOM_DEPT": "MARNE",
                        "POPULATION": 568895,
                        "DENSITY": 69.41,
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "NOM_DEPT": "HAUTES-PYRENEES",
                        "POPULATION": 228530,
                        "DENSITY": 50.47,
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "NOM_DEPT": "LOT",
                        "POPULATION": 173828,
                        "DENSITY": 33.29,
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "NOM_DEPT": "ALPES-DE-HAUTE-PROVENCE",
                        "POPULATION": 163915,
                        "DENSITY": 23.44,
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "NOM_DEPT": "SARTHE",
                        "POPULATION": 566506,
                        "DENSITY": 90.83,
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "NOM_DEPT": "EURE-ET-LOIR",
                        "POPULATION": 433233,
                        "DENSITY": 73.09,
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "NOM_DEPT": "CORSE-DU-SUD",
                        "POPULATION": 157249,
                        "DENSITY": 39.03,
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "NOM_DEPT": "MEURTHE-ET-MOSELLE",
                        "POPULATION": 733481,
                        "DENSITY": 138.83,
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "NOM_DEPT": "ORNE",
                        "POPULATION": 283372,
                        "DENSITY": 46.13,
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "NOM_DEPT": "AIN",
                        "POPULATION": 643350,
                        "DENSITY": 111.43,
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "NOM_DEPT": "ARIEGE",
                        "POPULATION": 153153,
                        "DENSITY": 31.12,
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "NOM_DEPT": "CORREZE",
                        "POPULATION": 241464,
                        "DENSITY": 41.0,
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "NOM_DEPT": "HAUT-RHIN",
                        "POPULATION": 764030,
                        "DENSITY": 216.66,
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "NOM_DEPT": "INDRE-ET-LOIRE",
                        "POPULATION": 606511,
                        "DENSITY": 98.66,
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "NOM_DEPT": "NORD",
                        "POPULATION": 2604361,
                        "DENSITY": 450.97,
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "NOM_DEPT": "TERRITOIRE DE BELFORT",
                        "POPULATION": 142622,
                        "DENSITY": 233.94,
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "NOM_DEPT": "LOIRE-ATLANTIQUE",
                        "POPULATION": 1394909,
                        "DENSITY": 199.48,
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "NOM_DEPT": "YONNE",
                        "POPULATION": 338291,
                        "DENSITY": 45.4,
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "NOM_DEPT": "ILLE-ET-VILAINE",
                        "POPULATION": 1060199,
                        "DENSITY": 155.22,
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "NOM_DEPT": "LANDES",
                        "POPULATION": 407444,
                        "DENSITY": 43.56,
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "NOM_DEPT": "FINISTERE",
                        "POPULATION": 909028,
                        "DENSITY": 134.54,
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "NOM_DEPT": "HAUTE-SAVOIE",
                        "POPULATION": 807360,
                        "DENSITY": 175.65,
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "NOM_DEPT": "OISE",
                        "POPULATION": 824503,
                        "DENSITY": 139.9,
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "NOM_DEPT": "NIEVRE",
                        "POPULATION": 207182,
                        "DENSITY": 30.19,
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "NOM_DEPT": "COTE-D'OR",
                        "POPULATION": 532871,
                        "DENSITY": 60.64,
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "NOM_DEPT": "ESSONNE",
                        "POPULATION": 1296130,
                        "DENSITY": 712.81,
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "NOM_DEPT": "DEUX-SEVRES",
                        "POPULATION": 374351,
                        "DENSITY": 62.09,
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "NOM_DEPT": "COTES-D'ARMOR",
                        "POPULATION": 598814,
                        "DENSITY": 86.0,
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "NOM_DEPT": "ALLIER",
                        "POPULATION": 337988,
                        "DENSITY": 45.89,
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "NOM_DEPT": "CHARENTE-MARITIME",
                        "POPULATION": 644303,
                        "DENSITY": 93.2,
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "NOM_DEPT": "CANTAL",
                        "POPULATION": 145143,
                        "DENSITY": 25.17,
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "NOM_DEPT": "HERAULT",
                        "POPULATION": 1144892,
                        "DENSITY": 183.74,
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "NOM_DEPT": "DROME",
                        "POPULATION": 511553,
                        "DENSITY": 78.06,
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "NOM_DEPT": "PYRENEES-ORIENTALES",
                        "POPULATION": 474452,
                        "DENSITY": 114.39,
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "NOM_DEPT": "SAVOIE",
                        "POPULATION": 431174,
                        "DENSITY": 68.87,
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "NOM_DEPT": "HAUTES-ALPES",
                        "POPULATION": 141284,
                        "DENSITY": 24.85,
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "NOM_DEPT": "VAUCLUSE",
                        "POPULATION": 559479,
                        "DENSITY": 156.4,
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "NOM_DEPT": "INDRE",
                        "POPULATION": 222232,
                        "DENSITY": 32.27,
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "NOM_DEPT": "HAUTE-CORSE",
                        "POPULATION": 177689,
                        "DENSITY": 37.65,
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "NOM_DEPT": "HAUTE-VIENNE",
                        "POPULATION": 374426,
                        "DENSITY": 67.47,
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "NOM_DEPT": "VENDEE",
                        "POPULATION": 675247,
                        "DENSITY": 99.91,
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "NOM_DEPT": "VAR",
                        "POPULATION": 1058740,
                        "DENSITY": 176.37,
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "NOM_DEPT": "VAL-DE-MARNE",
                        "POPULATION": 1387926,
                        "DENSITY": 5671.95,
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "NOM_DEPT": "HAUTS-DE-SEINE",
                        "POPULATION": 1609306,
                        "DENSITY": 9163.05,
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "NOM_DEPT": "LOZERE",
                        "POPULATION": 76601,
                        "DENSITY": 14.81,
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "NOM_DEPT": "BOUCHES-DU-RHONE",
                        "POPULATION": 2024162,
                        "DENSITY": 398.26,
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "NOM_DEPT": "PARIS",
                        "POPULATION": 2187526,
                        "DENSITY": 20746.64,
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "NOM_DEPT": "SEINE-SAINT-DENIS",
                        "POPULATION": 1623111,
                        "DENSITY": 6849.73,
                    }
                },
            },
        },
    },
    3: {
        "geolayer_a": geolayer_fr_dept_population,
        "geolayer_b": geolayer_fr_dept_data_and_geometry,
        "on_field_b": "CODE_DEPT",
        "on_field_a": "CODE_DEPT",
        "output_geolayer_name": "fr_dept_data_and_geometry_right_join_fr_dept_population",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": geolayer_fr_dept_population_geometry_right,
    },
    4: {
        "geolayer_a": geolayer_dpt_pop_2,
        "geolayer_b": geolayer_dpt_full,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "dpt_pop_2_right_join_dpt_full",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "dpt_pop_2_right_join_dpt_full",
                "fields": {
                    "POPULATION": {"type": "Integer", "index": 0},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "NOM_DEPT": "MAYENNE",
                        "POPULATION": 307445,
                        "DENSITY": 59.03,
                    }
                },
                1: {"attributes": {"CODE_DEPT": "02", "NOM_DEPT": "AISNE"}},
                2: {"attributes": {"CODE_DEPT": "95", "NOM_DEPT": "VAL-D'OISE"}},
                3: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
            },
        },
    },
    5: {
        "geolayer_a": geolayer_dpt_pop_2,
        "geolayer_b": geolayer_dpt_full_with_duplicate,
        "on_field_b": "CODE_DEPT",
        "on_field_a": "CODE_DEPT",
        "output_geolayer_name": "dpt_pop_2_right_join_dpt_full_with_duplicate",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "dpt_pop_2_right_join_dpt_full_with_duplicate",
                "fields": {
                    "POPULATION": {"type": "Integer", "index": 0},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "NOM_DEPT": "MAYENNE",
                        "POPULATION": 307445,
                        "DENSITY": 59.03,
                    }
                },
                1: {"attributes": {"CODE_DEPT": "02", "NOM_DEPT": "AISNE"}},
                2: {"attributes": {"CODE_DEPT": "02", "NOM_DEPT": "AISNE"}},
                3: {"attributes": {"CODE_DEPT": "95", "NOM_DEPT": "VAL-D'OISE"}},
                4: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
            },
        },
    },
    6: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2,
        "on_field_b": "CODE_DEPT",
        "on_field_a": "CODE_DEPT",
        "output_geolayer_name": "dpt_pop_ful_right_join_dpt_2",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "dpt_pop_ful_right_join_dpt_2",
                "fields": {
                    "POPULATION": {"type": "Integer", "index": 0},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
            },
        },
    },
    7: {
        "geolayer_a": geolayer_dpt_pop_full_with_duplicate,
        "geolayer_b": geolayer_dpt_2,
        "on_field_b": "CODE_DEPT",
        "on_field_a": "CODE_DEPT",
        "output_geolayer_name": "dpt_pop_full_with_duplicate_right_join_dpt_2",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "dpt_pop_full_with_duplicate_right_join_dpt_2",
                "fields": {
                    "POPULATION": {"type": "Integer", "index": 0},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
            },
        },
    },
    8: {
        "geolayer_a": geolayer_dpt_pop_2,
        "geolayer_b": geolayer_dpt_2,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_RIGHT_JOIN_POP_2",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_RIGHT_JOIN_POP_2",
                "fields": {
                    "POPULATION": {"type": "Integer", "index": 0},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"CODE_DEPT": "02", "NOM_DEPT": "AISNE"}},
                1: {"attributes": {"CODE_DEPT": "95", "NOM_DEPT": "VAL-D'OISE"}},
            },
        },
    },
    9: {
        "geolayer_a": geolayer_dpt_2_with_geom,
        "geolayer_b": geolayer_dpt_pop_full,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_RIGHT_JOIN_POP_FULL",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_RIGHT_JOIN_POP_FULL",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6861428.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {"attributes": {"POPULATION": 307445, "DENSITY": 59.03}},
                1: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                    },
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                    },
                },
                3: {"attributes": {"POPULATION": 750863, "DENSITY": 109.39}},
            },
        },
    },
    10: {
        "geolayer_a": geolayer_dpt_2_with_geom,
        "geolayer_b": geolayer_dpt_pop_full,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_RIGHT_JOIN_POP_FULL",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_RIGHT_JOIN_POP_FULL",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"POPULATION": 307445, "DENSITY": 59.03}},
                1: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    },
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    },
                },
                3: {"attributes": {"POPULATION": 750863, "DENSITY": 109.39}},
            },
        },
    },
    11: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2_with_geom,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_RIGHT_JOIN_POP_FULL",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_RIGHT_JOIN_POP_FULL",
                "fields": {
                    "POPULATION": {"type": "Integer", "index": 0},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 3},
                },
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6861428.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                    },
                },
                1: {
                    "attributes": {
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                    },
                },
            },
        },
    },
    12: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2_with_geom,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_RIGHT_JOIN_POP_FULL",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": {"POPULATION": "pop"},
        "rename_output_field_from_geolayer_b": {"CODE_DEPT": "id"},
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_RIGHT_JOIN_POP_FULL",
                "fields": {
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "pop": {"type": "Integer", "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 2},
                    "id": {"type": "String", "width": 2, "index": 3},
                },
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6861428.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "DENSITY": 72.04,
                        "pop": 534490,
                        "NOM_DEPT": "AISNE",
                        "id": "02",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                    },
                },
                1: {
                    "attributes": {
                        "DENSITY": 979.62,
                        "pop": 1228618,
                        "NOM_DEPT": "VAL-D'OISE",
                        "id": "95",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                    },
                },
            },
        },
    },
    13: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2_with_geom,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_RIGHT_JOIN_POP_FULL",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": {
            "CODE_DEPT": "code",
            "POPULATION": "pop",
        },
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": field_missing.format(field_name="CODE_DEPT"),
    },
    14: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "key_id": {"type": "Integer", "index": 0},
                    "price": {"type": "Integer", "index": 1},
                    "count": {"type": "Integer", "index": 2},
                    "probability": {
                        "type": "Real",
                        "width": 1,
                        "precision": 0,
                        "index": 3,
                    },
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "key_id": 164,
                        "price": 4300,
                        "count": 0,
                        "probability": 0.0,
                    }
                }
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "key_id": {"type": "Integer", "index": 0},
                    "price": {"type": "Integer", "index": 1},
                    "count": {"type": "Integer", "index": 2},
                    "probability": {
                        "type": "Real",
                        "width": 1,
                        "precision": 1,
                        "index": 3,
                    },
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "key_id": 0,
                        "price": 5000,
                        "count": 1,
                        "probability": 0.1,
                    }
                },
                1: {
                    "attributes": {
                        "key_id": 164,
                        "price": 4300,
                        "count": 1,
                        "probability": 0.1,
                    }
                },
            },
        },
        "on_field_a": "key_id",
        "on_field_b": "key_id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": {
            "key_id": "key_id_b",
            "price": "price_b",
            "count": "count_b",
            "probability": "probability_b",
        },
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "key_id": {"type": "Integer", "index": 0},
                    "price": {"type": "Integer", "index": 1},
                    "count": {"type": "Integer", "index": 2},
                    "probability": {
                        "type": "Real",
                        "width": 1,
                        "precision": 0,
                        "index": 3,
                    },
                    "key_id_b": {"type": "Integer", "index": 4},
                    "price_b": {"type": "Integer", "index": 5},
                    "count_b": {"type": "Integer", "index": 6},
                    "probability_b": {
                        "type": "Real",
                        "width": 1,
                        "precision": 1,
                        "index": 7,
                    },
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "key_id_b": 0,
                        "price_b": 5000,
                        "count_b": 1,
                        "probability_b": 0.1,
                    }
                },
                1: {
                    "attributes": {
                        "key_id": 164,
                        "price": 4300,
                        "count": 0,
                        "probability": 0.0,
                        "key_id_b": 164,
                        "price_b": 4300,
                        "count_b": 1,
                        "probability_b": 0.1,
                    }
                },
            },
        },
    },
    15: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice"}},
                1: {"attributes": {"id": None, "name": "Bob"}},
                2: {"attributes": {"id": None, "name": "Patrick"}},
                3: {"attributes": {"id": 1, "name": "Jane"}},
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "age": {"type": "Integer", "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "age": 28}},
                1: {"attributes": {"id": 1, "age": 2}},
            },
        },
        "on_field_a": "id",
        "on_field_b": "id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                    "id1": {"type": "Integer", "index": 2},
                    "age": {"type": "Integer", "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice", "id1": 0, "age": 28}},
                1: {"attributes": {"id": 1, "name": "Jane", "id1": 1, "age": 2}},
            },
        },
    },
    16: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 5, "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice"}},
                1: {"attributes": {"id": 1, "name": "Jane"}},
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "age": {"type": "Integer", "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "age": 28}},
                1: {"attributes": {"id": None, "age": 67}},
                2: {"attributes": {"id": None, "age": 15}},
                3: {"attributes": {"id": 1, "age": 2}},
            },
        },
        "on_field_a": "id",
        "on_field_b": "id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 5, "index": 1},
                    "id1": {"type": "Integer", "index": 2},
                    "age": {"type": "Integer", "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice", "id1": 0, "age": 28}},
                1: {"attributes": {"id1": None, "age": 67}},
                2: {"attributes": {"id1": None, "age": 15}},
                3: {"attributes": {"id": 1, "name": "Jane", "id1": 1, "age": 2}},
            },
        },
    },
    17: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice"}},
                1: {"attributes": {"id": None, "name": "Bob"}},
                2: {"attributes": {"id": None, "name": "Patrick"}},
                3: {"attributes": {"id": 1, "name": "Jane"}},
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "age": {"type": "Integer", "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "age": 28}},
                1: {"attributes": {"id": None, "age": 67}},
                2: {"attributes": {"id": None, "age": 15}},
                3: {"attributes": {"id": 1, "age": 2}},
            },
        },
        "on_field_a": "id",
        "on_field_b": "id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                    "id1": {"type": "Integer", "index": 2},
                    "age": {"type": "Integer", "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice", "id1": 0, "age": 28}},
                1: {"attributes": {"id1": None, "age": 67}},
                2: {"attributes": {"id1": None, "age": 15}},
                3: {"attributes": {"id": 1, "name": "Jane", "id1": 1, "age": 2}},
            },
        },
    },
}

join_full_parameters = {
    0: {
        "geolayer_a": geolayer_fr_dept_data_only,
        "geolayer_b": geolayer_fr_dept_population,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_ONLY",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_ONLY",
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
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "NOM_DEPT": "GERS",
                        "INSEE_REG": "76",
                        "POPULATION": 191091,
                        "AREA": 6304.33,
                        "DENSITY": 30.31,
                        "CODE_DEPT1": "32",
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "NOM_DEPT": "LOT-ET-GARONNE",
                        "INSEE_REG": "75",
                        "POPULATION": 332842,
                        "AREA": 5382.87,
                        "DENSITY": 61.83,
                        "CODE_DEPT1": "47",
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "NOM_DEPT": "ISERE",
                        "INSEE_REG": "84",
                        "POPULATION": 1258722,
                        "AREA": 7868.79,
                        "DENSITY": 159.96,
                        "CODE_DEPT1": "38",
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "NOM_DEPT": "PAS-DE-CALAIS",
                        "INSEE_REG": "32",
                        "POPULATION": 1468018,
                        "AREA": 6714.14,
                        "DENSITY": 218.65,
                        "CODE_DEPT1": "62",
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "NOM_DEPT": "ARDENNES",
                        "INSEE_REG": "44",
                        "POPULATION": 273579,
                        "AREA": 5253.13,
                        "DENSITY": 52.08,
                        "CODE_DEPT1": "08",
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "NOM_DEPT": "AUBE",
                        "INSEE_REG": "44",
                        "POPULATION": 310020,
                        "AREA": 6021.83,
                        "DENSITY": 51.48,
                        "CODE_DEPT1": "10",
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "NOM_DEPT": "ALPES-MARITIMES",
                        "INSEE_REG": "93",
                        "POPULATION": 1083310,
                        "AREA": 4291.62,
                        "DENSITY": 252.42,
                        "CODE_DEPT1": "06",
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "NOM_DEPT": "LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 762941,
                        "AREA": 4795.85,
                        "DENSITY": 159.08,
                        "CODE_DEPT1": "42",
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "NOM_DEPT": "HAUTE-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 1362672,
                        "AREA": 6364.82,
                        "DENSITY": 214.09,
                        "CODE_DEPT1": "31",
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "NOM_DEPT": "SAONE-ET-LOIRE",
                        "INSEE_REG": "27",
                        "POPULATION": 553595,
                        "AREA": 8598.33,
                        "DENSITY": 64.38,
                        "CODE_DEPT1": "71",
                    }
                },
                10: {
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
                11: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "NOM_DEPT": "CHARENTE",
                        "INSEE_REG": "75",
                        "POPULATION": 352335,
                        "AREA": 5963.54,
                        "DENSITY": 59.08,
                        "CODE_DEPT1": "16",
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "NOM_DEPT": "MANCHE",
                        "INSEE_REG": "28",
                        "POPULATION": 496883,
                        "AREA": 6015.07,
                        "DENSITY": 82.61,
                        "CODE_DEPT1": "50",
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "NOM_DEPT": "YVELINES",
                        "INSEE_REG": "11",
                        "POPULATION": 1438266,
                        "AREA": 2305.64,
                        "DENSITY": 623.8,
                        "CODE_DEPT1": "78",
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "NOM_DEPT": "DOUBS",
                        "INSEE_REG": "27",
                        "POPULATION": 539067,
                        "AREA": 5248.31,
                        "DENSITY": 102.71,
                        "CODE_DEPT1": "25",
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "NOM_DEPT": "MEUSE",
                        "INSEE_REG": "44",
                        "POPULATION": 187187,
                        "AREA": 6233.18,
                        "DENSITY": 30.03,
                        "CODE_DEPT1": "55",
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "NOM_DEPT": "GIRONDE",
                        "INSEE_REG": "75",
                        "POPULATION": 1583384,
                        "AREA": 10068.74,
                        "DENSITY": 157.26,
                        "CODE_DEPT1": "33",
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "NOM_DEPT": "CALVADOS",
                        "INSEE_REG": "28",
                        "POPULATION": 694002,
                        "AREA": 5588.48,
                        "DENSITY": 124.18,
                        "CODE_DEPT1": "14",
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "NOM_DEPT": "VOSGES",
                        "INSEE_REG": "44",
                        "POPULATION": 367673,
                        "AREA": 5891.56,
                        "DENSITY": 62.41,
                        "CODE_DEPT1": "88",
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "NOM_DEPT": "CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 304256,
                        "AREA": 7292.67,
                        "DENSITY": 41.72,
                        "CODE_DEPT1": "18",
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "NOM_DEPT": "ARDECHE",
                        "INSEE_REG": "84",
                        "POPULATION": 325712,
                        "AREA": 5562.05,
                        "DENSITY": 58.56,
                        "CODE_DEPT1": "07",
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "INSEE_REG": "32",
                        "POPULATION": 534490,
                        "AREA": 7418.97,
                        "DENSITY": 72.04,
                        "CODE_DEPT1": "02",
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "NOM_DEPT": "PYRENEES-ATLANTIQUES",
                        "INSEE_REG": "75",
                        "POPULATION": 677309,
                        "AREA": 7691.6,
                        "DENSITY": 88.06,
                        "CODE_DEPT1": "64",
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "NOM_DEPT": "LOIR-ET-CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 331915,
                        "AREA": 6412.3,
                        "DENSITY": 51.76,
                        "CODE_DEPT1": "41",
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "NOM_DEPT": "MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 1043522,
                        "AREA": 6252.63,
                        "DENSITY": 166.89,
                        "CODE_DEPT1": "57",
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "NOM_DEPT": "VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 436876,
                        "AREA": 7025.24,
                        "DENSITY": 62.19,
                        "CODE_DEPT1": "86",
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "NOM_DEPT": "DORDOGNE",
                        "INSEE_REG": "75",
                        "POPULATION": 413606,
                        "AREA": 9209.9,
                        "DENSITY": 44.91,
                        "CODE_DEPT1": "24",
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "NOM_DEPT": "JURA",
                        "INSEE_REG": "27",
                        "POPULATION": 260188,
                        "AREA": 5040.63,
                        "DENSITY": 51.62,
                        "CODE_DEPT1": "39",
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "NOM_DEPT": "TARN-ET-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 258349,
                        "AREA": 3731.0,
                        "DENSITY": 69.24,
                        "CODE_DEPT1": "82",
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "NOM_DEPT": "MAINE-ET-LOIRE",
                        "INSEE_REG": "52",
                        "POPULATION": 813493,
                        "AREA": 7161.34,
                        "DENSITY": 113.6,
                        "CODE_DEPT1": "49",
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "NOM_DEPT": "RHONE",
                        "INSEE_REG": "84",
                        "POPULATION": 1843319,
                        "AREA": 3253.11,
                        "DENSITY": 566.63,
                        "CODE_DEPT1": "69",
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "NOM_DEPT": "EURE",
                        "INSEE_REG": "28",
                        "POPULATION": 601843,
                        "AREA": 6035.85,
                        "DENSITY": 99.71,
                        "CODE_DEPT1": "27",
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "NOM_DEPT": "AVEYRON",
                        "INSEE_REG": "76",
                        "POPULATION": 279206,
                        "AREA": 8770.69,
                        "DENSITY": 31.83,
                        "CODE_DEPT1": "12",
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "NOM_DEPT": "CREUSE",
                        "INSEE_REG": "75",
                        "POPULATION": 118638,
                        "AREA": 5589.16,
                        "DENSITY": 21.23,
                        "CODE_DEPT1": "23",
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "NOM_DEPT": "LOIRET",
                        "INSEE_REG": "24",
                        "POPULATION": 678008,
                        "AREA": 6804.01,
                        "DENSITY": 99.65,
                        "CODE_DEPT1": "45",
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "NOM_DEPT": "HAUTE-SAONE",
                        "INSEE_REG": "27",
                        "POPULATION": 236659,
                        "AREA": 5382.37,
                        "DENSITY": 43.97,
                        "CODE_DEPT1": "70",
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "NOM_DEPT": "PUY-DE-DOME",
                        "INSEE_REG": "84",
                        "POPULATION": 653742,
                        "AREA": 8003.1,
                        "DENSITY": 81.69,
                        "CODE_DEPT1": "63",
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "NOM_DEPT": "TARN",
                        "INSEE_REG": "76",
                        "POPULATION": 387890,
                        "AREA": 5785.79,
                        "DENSITY": 67.04,
                        "CODE_DEPT1": "81",
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "NOM_DEPT": "SEINE-MARITIME",
                        "INSEE_REG": "28",
                        "POPULATION": 1254378,
                        "AREA": 6318.26,
                        "DENSITY": 198.53,
                        "CODE_DEPT1": "76",
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "NOM_DEPT": "HAUTE-MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 175640,
                        "AREA": 6249.91,
                        "DENSITY": 28.1,
                        "CODE_DEPT1": "52",
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "NOM_DEPT": "GARD",
                        "INSEE_REG": "76",
                        "POPULATION": 744178,
                        "AREA": 5874.71,
                        "DENSITY": 126.67,
                        "CODE_DEPT1": "30",
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "NOM_DEPT": "BAS-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 1125559,
                        "AREA": 4796.37,
                        "DENSITY": 234.67,
                        "CODE_DEPT1": "67",
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "NOM_DEPT": "AUDE",
                        "INSEE_REG": "76",
                        "POPULATION": 370260,
                        "AREA": 6351.35,
                        "DENSITY": 58.3,
                        "CODE_DEPT1": "11",
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "NOM_DEPT": "SEINE-ET-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1403997,
                        "AREA": 5924.64,
                        "DENSITY": 236.98,
                        "CODE_DEPT1": "77",
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "NOM_DEPT": "SOMME",
                        "INSEE_REG": "32",
                        "POPULATION": 572443,
                        "AREA": 6206.58,
                        "DENSITY": 92.23,
                        "CODE_DEPT1": "80",
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "NOM_DEPT": "HAUTE-LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 227283,
                        "AREA": 4996.58,
                        "DENSITY": 45.49,
                        "CODE_DEPT1": "43",
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "NOM_DEPT": "MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 568895,
                        "AREA": 8195.78,
                        "DENSITY": 69.41,
                        "CODE_DEPT1": "51",
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "NOM_DEPT": "HAUTES-PYRENEES",
                        "INSEE_REG": "76",
                        "POPULATION": 228530,
                        "AREA": 4527.89,
                        "DENSITY": 50.47,
                        "CODE_DEPT1": "65",
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "NOM_DEPT": "LOT",
                        "INSEE_REG": "76",
                        "POPULATION": 173828,
                        "AREA": 5221.64,
                        "DENSITY": 33.29,
                        "CODE_DEPT1": "46",
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "NOM_DEPT": "ALPES-DE-HAUTE-PROVENCE",
                        "INSEE_REG": "93",
                        "POPULATION": 163915,
                        "AREA": 6993.79,
                        "DENSITY": 23.44,
                        "CODE_DEPT1": "04",
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "NOM_DEPT": "SARTHE",
                        "INSEE_REG": "52",
                        "POPULATION": 566506,
                        "AREA": 6236.75,
                        "DENSITY": 90.83,
                        "CODE_DEPT1": "72",
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "INSEE_REG": "53",
                        "POPULATION": 750863,
                        "AREA": 6864.07,
                        "DENSITY": 109.39,
                        "CODE_DEPT1": "56",
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "NOM_DEPT": "EURE-ET-LOIR",
                        "INSEE_REG": "24",
                        "POPULATION": 433233,
                        "AREA": 5927.23,
                        "DENSITY": 73.09,
                        "CODE_DEPT1": "28",
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "NOM_DEPT": "CORSE-DU-SUD",
                        "INSEE_REG": "94",
                        "POPULATION": 157249,
                        "AREA": 4028.53,
                        "DENSITY": 39.03,
                        "CODE_DEPT1": "2A",
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "NOM_DEPT": "MEURTHE-ET-MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 733481,
                        "AREA": 5283.29,
                        "DENSITY": 138.83,
                        "CODE_DEPT1": "54",
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "NOM_DEPT": "ORNE",
                        "INSEE_REG": "28",
                        "POPULATION": 283372,
                        "AREA": 6142.73,
                        "DENSITY": 46.13,
                        "CODE_DEPT1": "61",
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "NOM_DEPT": "AIN",
                        "INSEE_REG": "84",
                        "POPULATION": 643350,
                        "AREA": 5773.77,
                        "DENSITY": 111.43,
                        "CODE_DEPT1": "01",
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "NOM_DEPT": "ARIEGE",
                        "INSEE_REG": "76",
                        "POPULATION": 153153,
                        "AREA": 4921.75,
                        "DENSITY": 31.12,
                        "CODE_DEPT1": "09",
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "NOM_DEPT": "CORREZE",
                        "INSEE_REG": "75",
                        "POPULATION": 241464,
                        "AREA": 5888.93,
                        "DENSITY": 41.0,
                        "CODE_DEPT1": "19",
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "NOM_DEPT": "HAUT-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 764030,
                        "AREA": 3526.37,
                        "DENSITY": 216.66,
                        "CODE_DEPT1": "68",
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "NOM_DEPT": "INDRE-ET-LOIRE",
                        "INSEE_REG": "24",
                        "POPULATION": 606511,
                        "AREA": 6147.6,
                        "DENSITY": 98.66,
                        "CODE_DEPT1": "37",
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "NOM_DEPT": "NORD",
                        "INSEE_REG": "32",
                        "POPULATION": 2604361,
                        "AREA": 5774.99,
                        "DENSITY": 450.97,
                        "CODE_DEPT1": "59",
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "NOM_DEPT": "TERRITOIRE DE BELFORT",
                        "INSEE_REG": "27",
                        "POPULATION": 142622,
                        "AREA": 609.64,
                        "DENSITY": 233.94,
                        "CODE_DEPT1": "90",
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "NOM_DEPT": "LOIRE-ATLANTIQUE",
                        "INSEE_REG": "52",
                        "POPULATION": 1394909,
                        "AREA": 6992.78,
                        "DENSITY": 199.48,
                        "CODE_DEPT1": "44",
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "NOM_DEPT": "YONNE",
                        "INSEE_REG": "27",
                        "POPULATION": 338291,
                        "AREA": 7450.97,
                        "DENSITY": 45.4,
                        "CODE_DEPT1": "89",
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "NOM_DEPT": "ILLE-ET-VILAINE",
                        "INSEE_REG": "53",
                        "POPULATION": 1060199,
                        "AREA": 6830.2,
                        "DENSITY": 155.22,
                        "CODE_DEPT1": "35",
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "NOM_DEPT": "LANDES",
                        "INSEE_REG": "75",
                        "POPULATION": 407444,
                        "AREA": 9353.03,
                        "DENSITY": 43.56,
                        "CODE_DEPT1": "40",
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "NOM_DEPT": "FINISTERE",
                        "INSEE_REG": "53",
                        "POPULATION": 909028,
                        "AREA": 6756.76,
                        "DENSITY": 134.54,
                        "CODE_DEPT1": "29",
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "NOM_DEPT": "HAUTE-SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 807360,
                        "AREA": 4596.53,
                        "DENSITY": 175.65,
                        "CODE_DEPT1": "74",
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "NOM_DEPT": "OISE",
                        "INSEE_REG": "32",
                        "POPULATION": 824503,
                        "AREA": 5893.6,
                        "DENSITY": 139.9,
                        "CODE_DEPT1": "60",
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "INSEE_REG": "11",
                        "POPULATION": 1228618,
                        "AREA": 1254.18,
                        "DENSITY": 979.62,
                        "CODE_DEPT1": "95",
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "NOM_DEPT": "NIEVRE",
                        "INSEE_REG": "27",
                        "POPULATION": 207182,
                        "AREA": 6862.87,
                        "DENSITY": 30.19,
                        "CODE_DEPT1": "58",
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "NOM_DEPT": "COTE-D'OR",
                        "INSEE_REG": "27",
                        "POPULATION": 532871,
                        "AREA": 8787.51,
                        "DENSITY": 60.64,
                        "CODE_DEPT1": "21",
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "NOM_DEPT": "ESSONNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1296130,
                        "AREA": 1818.35,
                        "DENSITY": 712.81,
                        "CODE_DEPT1": "91",
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "NOM_DEPT": "DEUX-SEVRES",
                        "INSEE_REG": "75",
                        "POPULATION": 374351,
                        "AREA": 6029.06,
                        "DENSITY": 62.09,
                        "CODE_DEPT1": "79",
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "NOM_DEPT": "COTES-D'ARMOR",
                        "INSEE_REG": "53",
                        "POPULATION": 598814,
                        "AREA": 6963.26,
                        "DENSITY": 86.0,
                        "CODE_DEPT1": "22",
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "NOM_DEPT": "ALLIER",
                        "INSEE_REG": "84",
                        "POPULATION": 337988,
                        "AREA": 7365.26,
                        "DENSITY": 45.89,
                        "CODE_DEPT1": "03",
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "NOM_DEPT": "CHARENTE-MARITIME",
                        "INSEE_REG": "75",
                        "POPULATION": 644303,
                        "AREA": 6913.03,
                        "DENSITY": 93.2,
                        "CODE_DEPT1": "17",
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "NOM_DEPT": "CANTAL",
                        "INSEE_REG": "84",
                        "POPULATION": 145143,
                        "AREA": 5767.47,
                        "DENSITY": 25.17,
                        "CODE_DEPT1": "15",
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "NOM_DEPT": "HERAULT",
                        "INSEE_REG": "76",
                        "POPULATION": 1144892,
                        "AREA": 6231.05,
                        "DENSITY": 183.74,
                        "CODE_DEPT1": "34",
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "NOM_DEPT": "DROME",
                        "INSEE_REG": "84",
                        "POPULATION": 511553,
                        "AREA": 6553.53,
                        "DENSITY": 78.06,
                        "CODE_DEPT1": "26",
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "NOM_DEPT": "PYRENEES-ORIENTALES",
                        "INSEE_REG": "76",
                        "POPULATION": 474452,
                        "AREA": 4147.76,
                        "DENSITY": 114.39,
                        "CODE_DEPT1": "66",
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "NOM_DEPT": "SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 431174,
                        "AREA": 6260.4,
                        "DENSITY": 68.87,
                        "CODE_DEPT1": "73",
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "NOM_DEPT": "HAUTES-ALPES",
                        "INSEE_REG": "93",
                        "POPULATION": 141284,
                        "AREA": 5685.31,
                        "DENSITY": 24.85,
                        "CODE_DEPT1": "05",
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "NOM_DEPT": "VAUCLUSE",
                        "INSEE_REG": "93",
                        "POPULATION": 559479,
                        "AREA": 3577.19,
                        "DENSITY": 156.4,
                        "CODE_DEPT1": "84",
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "NOM_DEPT": "INDRE",
                        "INSEE_REG": "24",
                        "POPULATION": 222232,
                        "AREA": 6887.38,
                        "DENSITY": 32.27,
                        "CODE_DEPT1": "36",
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "NOM_DEPT": "HAUTE-CORSE",
                        "INSEE_REG": "94",
                        "POPULATION": 177689,
                        "AREA": 4719.71,
                        "DENSITY": 37.65,
                        "CODE_DEPT1": "2B",
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "NOM_DEPT": "HAUTE-VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 374426,
                        "AREA": 5549.31,
                        "DENSITY": 67.47,
                        "CODE_DEPT1": "87",
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "NOM_DEPT": "VENDEE",
                        "INSEE_REG": "52",
                        "POPULATION": 675247,
                        "AREA": 6758.23,
                        "DENSITY": 99.91,
                        "CODE_DEPT1": "85",
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "NOM_DEPT": "VAR",
                        "INSEE_REG": "93",
                        "POPULATION": 1058740,
                        "AREA": 6002.84,
                        "DENSITY": 176.37,
                        "CODE_DEPT1": "83",
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "NOM_DEPT": "VAL-DE-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1387926,
                        "AREA": 244.7,
                        "DENSITY": 5671.95,
                        "CODE_DEPT1": "94",
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "NOM_DEPT": "HAUTS-DE-SEINE",
                        "INSEE_REG": "11",
                        "POPULATION": 1609306,
                        "AREA": 175.63,
                        "DENSITY": 9163.05,
                        "CODE_DEPT1": "92",
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "NOM_DEPT": "LOZERE",
                        "INSEE_REG": "76",
                        "POPULATION": 76601,
                        "AREA": 5172.02,
                        "DENSITY": 14.81,
                        "CODE_DEPT1": "48",
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "NOM_DEPT": "BOUCHES-DU-RHONE",
                        "INSEE_REG": "93",
                        "POPULATION": 2024162,
                        "AREA": 5082.57,
                        "DENSITY": 398.26,
                        "CODE_DEPT1": "13",
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "NOM_DEPT": "PARIS",
                        "INSEE_REG": "11",
                        "POPULATION": 2187526,
                        "AREA": 105.44,
                        "DENSITY": 20746.64,
                        "CODE_DEPT1": "75",
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "NOM_DEPT": "SEINE-SAINT-DENIS",
                        "INSEE_REG": "11",
                        "POPULATION": 1623111,
                        "AREA": 236.96,
                        "DENSITY": 6849.73,
                        "CODE_DEPT1": "93",
                    }
                },
            },
        },
    },
    1: {
        "geolayer_a": geolayer_fr_dept_data_only,
        "geolayer_b": geolayer_fr_dept_population,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_WITH_POPULATION",
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_WITH_POPULATION",
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
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "NOM_DEPT": "GERS",
                        "INSEE_REG": "76",
                        "POPULATION": 191091,
                        "AREA": 6304.33,
                        "DENSITY": 30.31,
                        "CODE_DEPT1": "32",
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "NOM_DEPT": "LOT-ET-GARONNE",
                        "INSEE_REG": "75",
                        "POPULATION": 332842,
                        "AREA": 5382.87,
                        "DENSITY": 61.83,
                        "CODE_DEPT1": "47",
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "NOM_DEPT": "ISERE",
                        "INSEE_REG": "84",
                        "POPULATION": 1258722,
                        "AREA": 7868.79,
                        "DENSITY": 159.96,
                        "CODE_DEPT1": "38",
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "NOM_DEPT": "PAS-DE-CALAIS",
                        "INSEE_REG": "32",
                        "POPULATION": 1468018,
                        "AREA": 6714.14,
                        "DENSITY": 218.65,
                        "CODE_DEPT1": "62",
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "NOM_DEPT": "ARDENNES",
                        "INSEE_REG": "44",
                        "POPULATION": 273579,
                        "AREA": 5253.13,
                        "DENSITY": 52.08,
                        "CODE_DEPT1": "08",
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "NOM_DEPT": "AUBE",
                        "INSEE_REG": "44",
                        "POPULATION": 310020,
                        "AREA": 6021.83,
                        "DENSITY": 51.48,
                        "CODE_DEPT1": "10",
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "NOM_DEPT": "ALPES-MARITIMES",
                        "INSEE_REG": "93",
                        "POPULATION": 1083310,
                        "AREA": 4291.62,
                        "DENSITY": 252.42,
                        "CODE_DEPT1": "06",
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "NOM_DEPT": "LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 762941,
                        "AREA": 4795.85,
                        "DENSITY": 159.08,
                        "CODE_DEPT1": "42",
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "NOM_DEPT": "HAUTE-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 1362672,
                        "AREA": 6364.82,
                        "DENSITY": 214.09,
                        "CODE_DEPT1": "31",
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "NOM_DEPT": "SAONE-ET-LOIRE",
                        "INSEE_REG": "27",
                        "POPULATION": 553595,
                        "AREA": 8598.33,
                        "DENSITY": 64.38,
                        "CODE_DEPT1": "71",
                    }
                },
                10: {
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
                11: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "NOM_DEPT": "CHARENTE",
                        "INSEE_REG": "75",
                        "POPULATION": 352335,
                        "AREA": 5963.54,
                        "DENSITY": 59.08,
                        "CODE_DEPT1": "16",
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "NOM_DEPT": "MANCHE",
                        "INSEE_REG": "28",
                        "POPULATION": 496883,
                        "AREA": 6015.07,
                        "DENSITY": 82.61,
                        "CODE_DEPT1": "50",
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "NOM_DEPT": "YVELINES",
                        "INSEE_REG": "11",
                        "POPULATION": 1438266,
                        "AREA": 2305.64,
                        "DENSITY": 623.8,
                        "CODE_DEPT1": "78",
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "NOM_DEPT": "DOUBS",
                        "INSEE_REG": "27",
                        "POPULATION": 539067,
                        "AREA": 5248.31,
                        "DENSITY": 102.71,
                        "CODE_DEPT1": "25",
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "NOM_DEPT": "MEUSE",
                        "INSEE_REG": "44",
                        "POPULATION": 187187,
                        "AREA": 6233.18,
                        "DENSITY": 30.03,
                        "CODE_DEPT1": "55",
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "NOM_DEPT": "GIRONDE",
                        "INSEE_REG": "75",
                        "POPULATION": 1583384,
                        "AREA": 10068.74,
                        "DENSITY": 157.26,
                        "CODE_DEPT1": "33",
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "NOM_DEPT": "CALVADOS",
                        "INSEE_REG": "28",
                        "POPULATION": 694002,
                        "AREA": 5588.48,
                        "DENSITY": 124.18,
                        "CODE_DEPT1": "14",
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "NOM_DEPT": "VOSGES",
                        "INSEE_REG": "44",
                        "POPULATION": 367673,
                        "AREA": 5891.56,
                        "DENSITY": 62.41,
                        "CODE_DEPT1": "88",
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "NOM_DEPT": "CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 304256,
                        "AREA": 7292.67,
                        "DENSITY": 41.72,
                        "CODE_DEPT1": "18",
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "NOM_DEPT": "ARDECHE",
                        "INSEE_REG": "84",
                        "POPULATION": 325712,
                        "AREA": 5562.05,
                        "DENSITY": 58.56,
                        "CODE_DEPT1": "07",
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "INSEE_REG": "32",
                        "POPULATION": 534490,
                        "AREA": 7418.97,
                        "DENSITY": 72.04,
                        "CODE_DEPT1": "02",
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "NOM_DEPT": "PYRENEES-ATLANTIQUES",
                        "INSEE_REG": "75",
                        "POPULATION": 677309,
                        "AREA": 7691.6,
                        "DENSITY": 88.06,
                        "CODE_DEPT1": "64",
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "NOM_DEPT": "LOIR-ET-CHER",
                        "INSEE_REG": "24",
                        "POPULATION": 331915,
                        "AREA": 6412.3,
                        "DENSITY": 51.76,
                        "CODE_DEPT1": "41",
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "NOM_DEPT": "MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 1043522,
                        "AREA": 6252.63,
                        "DENSITY": 166.89,
                        "CODE_DEPT1": "57",
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "NOM_DEPT": "VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 436876,
                        "AREA": 7025.24,
                        "DENSITY": 62.19,
                        "CODE_DEPT1": "86",
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "NOM_DEPT": "DORDOGNE",
                        "INSEE_REG": "75",
                        "POPULATION": 413606,
                        "AREA": 9209.9,
                        "DENSITY": 44.91,
                        "CODE_DEPT1": "24",
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "NOM_DEPT": "JURA",
                        "INSEE_REG": "27",
                        "POPULATION": 260188,
                        "AREA": 5040.63,
                        "DENSITY": 51.62,
                        "CODE_DEPT1": "39",
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "NOM_DEPT": "TARN-ET-GARONNE",
                        "INSEE_REG": "76",
                        "POPULATION": 258349,
                        "AREA": 3731.0,
                        "DENSITY": 69.24,
                        "CODE_DEPT1": "82",
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "NOM_DEPT": "MAINE-ET-LOIRE",
                        "INSEE_REG": "52",
                        "POPULATION": 813493,
                        "AREA": 7161.34,
                        "DENSITY": 113.6,
                        "CODE_DEPT1": "49",
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "NOM_DEPT": "RHONE",
                        "INSEE_REG": "84",
                        "POPULATION": 1843319,
                        "AREA": 3253.11,
                        "DENSITY": 566.63,
                        "CODE_DEPT1": "69",
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "NOM_DEPT": "EURE",
                        "INSEE_REG": "28",
                        "POPULATION": 601843,
                        "AREA": 6035.85,
                        "DENSITY": 99.71,
                        "CODE_DEPT1": "27",
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "NOM_DEPT": "AVEYRON",
                        "INSEE_REG": "76",
                        "POPULATION": 279206,
                        "AREA": 8770.69,
                        "DENSITY": 31.83,
                        "CODE_DEPT1": "12",
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "NOM_DEPT": "CREUSE",
                        "INSEE_REG": "75",
                        "POPULATION": 118638,
                        "AREA": 5589.16,
                        "DENSITY": 21.23,
                        "CODE_DEPT1": "23",
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "NOM_DEPT": "LOIRET",
                        "INSEE_REG": "24",
                        "POPULATION": 678008,
                        "AREA": 6804.01,
                        "DENSITY": 99.65,
                        "CODE_DEPT1": "45",
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "NOM_DEPT": "HAUTE-SAONE",
                        "INSEE_REG": "27",
                        "POPULATION": 236659,
                        "AREA": 5382.37,
                        "DENSITY": 43.97,
                        "CODE_DEPT1": "70",
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "NOM_DEPT": "PUY-DE-DOME",
                        "INSEE_REG": "84",
                        "POPULATION": 653742,
                        "AREA": 8003.1,
                        "DENSITY": 81.69,
                        "CODE_DEPT1": "63",
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "NOM_DEPT": "TARN",
                        "INSEE_REG": "76",
                        "POPULATION": 387890,
                        "AREA": 5785.79,
                        "DENSITY": 67.04,
                        "CODE_DEPT1": "81",
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "NOM_DEPT": "SEINE-MARITIME",
                        "INSEE_REG": "28",
                        "POPULATION": 1254378,
                        "AREA": 6318.26,
                        "DENSITY": 198.53,
                        "CODE_DEPT1": "76",
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "NOM_DEPT": "HAUTE-MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 175640,
                        "AREA": 6249.91,
                        "DENSITY": 28.1,
                        "CODE_DEPT1": "52",
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "NOM_DEPT": "GARD",
                        "INSEE_REG": "76",
                        "POPULATION": 744178,
                        "AREA": 5874.71,
                        "DENSITY": 126.67,
                        "CODE_DEPT1": "30",
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "NOM_DEPT": "BAS-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 1125559,
                        "AREA": 4796.37,
                        "DENSITY": 234.67,
                        "CODE_DEPT1": "67",
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "NOM_DEPT": "AUDE",
                        "INSEE_REG": "76",
                        "POPULATION": 370260,
                        "AREA": 6351.35,
                        "DENSITY": 58.3,
                        "CODE_DEPT1": "11",
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "NOM_DEPT": "SEINE-ET-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1403997,
                        "AREA": 5924.64,
                        "DENSITY": 236.98,
                        "CODE_DEPT1": "77",
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "NOM_DEPT": "SOMME",
                        "INSEE_REG": "32",
                        "POPULATION": 572443,
                        "AREA": 6206.58,
                        "DENSITY": 92.23,
                        "CODE_DEPT1": "80",
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "NOM_DEPT": "HAUTE-LOIRE",
                        "INSEE_REG": "84",
                        "POPULATION": 227283,
                        "AREA": 4996.58,
                        "DENSITY": 45.49,
                        "CODE_DEPT1": "43",
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "NOM_DEPT": "MARNE",
                        "INSEE_REG": "44",
                        "POPULATION": 568895,
                        "AREA": 8195.78,
                        "DENSITY": 69.41,
                        "CODE_DEPT1": "51",
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "NOM_DEPT": "HAUTES-PYRENEES",
                        "INSEE_REG": "76",
                        "POPULATION": 228530,
                        "AREA": 4527.89,
                        "DENSITY": 50.47,
                        "CODE_DEPT1": "65",
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "NOM_DEPT": "LOT",
                        "INSEE_REG": "76",
                        "POPULATION": 173828,
                        "AREA": 5221.64,
                        "DENSITY": 33.29,
                        "CODE_DEPT1": "46",
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "NOM_DEPT": "ALPES-DE-HAUTE-PROVENCE",
                        "INSEE_REG": "93",
                        "POPULATION": 163915,
                        "AREA": 6993.79,
                        "DENSITY": 23.44,
                        "CODE_DEPT1": "04",
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "NOM_DEPT": "SARTHE",
                        "INSEE_REG": "52",
                        "POPULATION": 566506,
                        "AREA": 6236.75,
                        "DENSITY": 90.83,
                        "CODE_DEPT1": "72",
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "INSEE_REG": "53",
                        "POPULATION": 750863,
                        "AREA": 6864.07,
                        "DENSITY": 109.39,
                        "CODE_DEPT1": "56",
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "NOM_DEPT": "EURE-ET-LOIR",
                        "INSEE_REG": "24",
                        "POPULATION": 433233,
                        "AREA": 5927.23,
                        "DENSITY": 73.09,
                        "CODE_DEPT1": "28",
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "NOM_DEPT": "CORSE-DU-SUD",
                        "INSEE_REG": "94",
                        "POPULATION": 157249,
                        "AREA": 4028.53,
                        "DENSITY": 39.03,
                        "CODE_DEPT1": "2A",
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "NOM_DEPT": "MEURTHE-ET-MOSELLE",
                        "INSEE_REG": "44",
                        "POPULATION": 733481,
                        "AREA": 5283.29,
                        "DENSITY": 138.83,
                        "CODE_DEPT1": "54",
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "NOM_DEPT": "ORNE",
                        "INSEE_REG": "28",
                        "POPULATION": 283372,
                        "AREA": 6142.73,
                        "DENSITY": 46.13,
                        "CODE_DEPT1": "61",
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "NOM_DEPT": "AIN",
                        "INSEE_REG": "84",
                        "POPULATION": 643350,
                        "AREA": 5773.77,
                        "DENSITY": 111.43,
                        "CODE_DEPT1": "01",
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "NOM_DEPT": "ARIEGE",
                        "INSEE_REG": "76",
                        "POPULATION": 153153,
                        "AREA": 4921.75,
                        "DENSITY": 31.12,
                        "CODE_DEPT1": "09",
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "NOM_DEPT": "CORREZE",
                        "INSEE_REG": "75",
                        "POPULATION": 241464,
                        "AREA": 5888.93,
                        "DENSITY": 41.0,
                        "CODE_DEPT1": "19",
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "NOM_DEPT": "HAUT-RHIN",
                        "INSEE_REG": "44",
                        "POPULATION": 764030,
                        "AREA": 3526.37,
                        "DENSITY": 216.66,
                        "CODE_DEPT1": "68",
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "NOM_DEPT": "INDRE-ET-LOIRE",
                        "INSEE_REG": "24",
                        "POPULATION": 606511,
                        "AREA": 6147.6,
                        "DENSITY": 98.66,
                        "CODE_DEPT1": "37",
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "NOM_DEPT": "NORD",
                        "INSEE_REG": "32",
                        "POPULATION": 2604361,
                        "AREA": 5774.99,
                        "DENSITY": 450.97,
                        "CODE_DEPT1": "59",
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "NOM_DEPT": "TERRITOIRE DE BELFORT",
                        "INSEE_REG": "27",
                        "POPULATION": 142622,
                        "AREA": 609.64,
                        "DENSITY": 233.94,
                        "CODE_DEPT1": "90",
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "NOM_DEPT": "LOIRE-ATLANTIQUE",
                        "INSEE_REG": "52",
                        "POPULATION": 1394909,
                        "AREA": 6992.78,
                        "DENSITY": 199.48,
                        "CODE_DEPT1": "44",
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "NOM_DEPT": "YONNE",
                        "INSEE_REG": "27",
                        "POPULATION": 338291,
                        "AREA": 7450.97,
                        "DENSITY": 45.4,
                        "CODE_DEPT1": "89",
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "NOM_DEPT": "ILLE-ET-VILAINE",
                        "INSEE_REG": "53",
                        "POPULATION": 1060199,
                        "AREA": 6830.2,
                        "DENSITY": 155.22,
                        "CODE_DEPT1": "35",
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "NOM_DEPT": "LANDES",
                        "INSEE_REG": "75",
                        "POPULATION": 407444,
                        "AREA": 9353.03,
                        "DENSITY": 43.56,
                        "CODE_DEPT1": "40",
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "NOM_DEPT": "FINISTERE",
                        "INSEE_REG": "53",
                        "POPULATION": 909028,
                        "AREA": 6756.76,
                        "DENSITY": 134.54,
                        "CODE_DEPT1": "29",
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "NOM_DEPT": "HAUTE-SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 807360,
                        "AREA": 4596.53,
                        "DENSITY": 175.65,
                        "CODE_DEPT1": "74",
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "NOM_DEPT": "OISE",
                        "INSEE_REG": "32",
                        "POPULATION": 824503,
                        "AREA": 5893.6,
                        "DENSITY": 139.9,
                        "CODE_DEPT1": "60",
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "INSEE_REG": "11",
                        "POPULATION": 1228618,
                        "AREA": 1254.18,
                        "DENSITY": 979.62,
                        "CODE_DEPT1": "95",
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "NOM_DEPT": "NIEVRE",
                        "INSEE_REG": "27",
                        "POPULATION": 207182,
                        "AREA": 6862.87,
                        "DENSITY": 30.19,
                        "CODE_DEPT1": "58",
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "NOM_DEPT": "COTE-D'OR",
                        "INSEE_REG": "27",
                        "POPULATION": 532871,
                        "AREA": 8787.51,
                        "DENSITY": 60.64,
                        "CODE_DEPT1": "21",
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "NOM_DEPT": "ESSONNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1296130,
                        "AREA": 1818.35,
                        "DENSITY": 712.81,
                        "CODE_DEPT1": "91",
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "NOM_DEPT": "DEUX-SEVRES",
                        "INSEE_REG": "75",
                        "POPULATION": 374351,
                        "AREA": 6029.06,
                        "DENSITY": 62.09,
                        "CODE_DEPT1": "79",
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "NOM_DEPT": "COTES-D'ARMOR",
                        "INSEE_REG": "53",
                        "POPULATION": 598814,
                        "AREA": 6963.26,
                        "DENSITY": 86.0,
                        "CODE_DEPT1": "22",
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "NOM_DEPT": "ALLIER",
                        "INSEE_REG": "84",
                        "POPULATION": 337988,
                        "AREA": 7365.26,
                        "DENSITY": 45.89,
                        "CODE_DEPT1": "03",
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "NOM_DEPT": "CHARENTE-MARITIME",
                        "INSEE_REG": "75",
                        "POPULATION": 644303,
                        "AREA": 6913.03,
                        "DENSITY": 93.2,
                        "CODE_DEPT1": "17",
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "NOM_DEPT": "CANTAL",
                        "INSEE_REG": "84",
                        "POPULATION": 145143,
                        "AREA": 5767.47,
                        "DENSITY": 25.17,
                        "CODE_DEPT1": "15",
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "NOM_DEPT": "HERAULT",
                        "INSEE_REG": "76",
                        "POPULATION": 1144892,
                        "AREA": 6231.05,
                        "DENSITY": 183.74,
                        "CODE_DEPT1": "34",
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "NOM_DEPT": "DROME",
                        "INSEE_REG": "84",
                        "POPULATION": 511553,
                        "AREA": 6553.53,
                        "DENSITY": 78.06,
                        "CODE_DEPT1": "26",
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "NOM_DEPT": "PYRENEES-ORIENTALES",
                        "INSEE_REG": "76",
                        "POPULATION": 474452,
                        "AREA": 4147.76,
                        "DENSITY": 114.39,
                        "CODE_DEPT1": "66",
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "NOM_DEPT": "SAVOIE",
                        "INSEE_REG": "84",
                        "POPULATION": 431174,
                        "AREA": 6260.4,
                        "DENSITY": 68.87,
                        "CODE_DEPT1": "73",
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "NOM_DEPT": "HAUTES-ALPES",
                        "INSEE_REG": "93",
                        "POPULATION": 141284,
                        "AREA": 5685.31,
                        "DENSITY": 24.85,
                        "CODE_DEPT1": "05",
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "NOM_DEPT": "VAUCLUSE",
                        "INSEE_REG": "93",
                        "POPULATION": 559479,
                        "AREA": 3577.19,
                        "DENSITY": 156.4,
                        "CODE_DEPT1": "84",
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "NOM_DEPT": "INDRE",
                        "INSEE_REG": "24",
                        "POPULATION": 222232,
                        "AREA": 6887.38,
                        "DENSITY": 32.27,
                        "CODE_DEPT1": "36",
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "NOM_DEPT": "HAUTE-CORSE",
                        "INSEE_REG": "94",
                        "POPULATION": 177689,
                        "AREA": 4719.71,
                        "DENSITY": 37.65,
                        "CODE_DEPT1": "2B",
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "NOM_DEPT": "HAUTE-VIENNE",
                        "INSEE_REG": "75",
                        "POPULATION": 374426,
                        "AREA": 5549.31,
                        "DENSITY": 67.47,
                        "CODE_DEPT1": "87",
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "NOM_DEPT": "VENDEE",
                        "INSEE_REG": "52",
                        "POPULATION": 675247,
                        "AREA": 6758.23,
                        "DENSITY": 99.91,
                        "CODE_DEPT1": "85",
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "NOM_DEPT": "VAR",
                        "INSEE_REG": "93",
                        "POPULATION": 1058740,
                        "AREA": 6002.84,
                        "DENSITY": 176.37,
                        "CODE_DEPT1": "83",
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "NOM_DEPT": "VAL-DE-MARNE",
                        "INSEE_REG": "11",
                        "POPULATION": 1387926,
                        "AREA": 244.7,
                        "DENSITY": 5671.95,
                        "CODE_DEPT1": "94",
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "NOM_DEPT": "HAUTS-DE-SEINE",
                        "INSEE_REG": "11",
                        "POPULATION": 1609306,
                        "AREA": 175.63,
                        "DENSITY": 9163.05,
                        "CODE_DEPT1": "92",
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "NOM_DEPT": "LOZERE",
                        "INSEE_REG": "76",
                        "POPULATION": 76601,
                        "AREA": 5172.02,
                        "DENSITY": 14.81,
                        "CODE_DEPT1": "48",
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "NOM_DEPT": "BOUCHES-DU-RHONE",
                        "INSEE_REG": "93",
                        "POPULATION": 2024162,
                        "AREA": 5082.57,
                        "DENSITY": 398.26,
                        "CODE_DEPT1": "13",
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "NOM_DEPT": "PARIS",
                        "INSEE_REG": "11",
                        "POPULATION": 2187526,
                        "AREA": 105.44,
                        "DENSITY": 20746.64,
                        "CODE_DEPT1": "75",
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "NOM_DEPT": "SEINE-SAINT-DENIS",
                        "INSEE_REG": "11",
                        "POPULATION": 1623111,
                        "AREA": 236.96,
                        "DENSITY": 6849.73,
                        "CODE_DEPT1": "93",
                    }
                },
            },
        },
    },
    2: {
        "geolayer_a": geolayer_fr_dept_data_only,
        "geolayer_b": geolayer_fr_dept_population,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_WITH_POPULATION",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_WITH_POPULATION",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "NOM_DEPT": "GERS",
                        "POPULATION": 191091,
                        "DENSITY": 30.31,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "NOM_DEPT": "LOT-ET-GARONNE",
                        "POPULATION": 332842,
                        "DENSITY": 61.83,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "NOM_DEPT": "ISERE",
                        "POPULATION": 1258722,
                        "DENSITY": 159.96,
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "NOM_DEPT": "PAS-DE-CALAIS",
                        "POPULATION": 1468018,
                        "DENSITY": 218.65,
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "NOM_DEPT": "ARDENNES",
                        "POPULATION": 273579,
                        "DENSITY": 52.08,
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "NOM_DEPT": "AUBE",
                        "POPULATION": 310020,
                        "DENSITY": 51.48,
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "NOM_DEPT": "ALPES-MARITIMES",
                        "POPULATION": 1083310,
                        "DENSITY": 252.42,
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "NOM_DEPT": "LOIRE",
                        "POPULATION": 762941,
                        "DENSITY": 159.08,
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "NOM_DEPT": "HAUTE-GARONNE",
                        "POPULATION": 1362672,
                        "DENSITY": 214.09,
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "NOM_DEPT": "SAONE-ET-LOIRE",
                        "POPULATION": 553595,
                        "DENSITY": 64.38,
                    }
                },
                10: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "NOM_DEPT": "MAYENNE",
                        "POPULATION": 307445,
                        "DENSITY": 59.03,
                    }
                },
                11: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "NOM_DEPT": "CHARENTE",
                        "POPULATION": 352335,
                        "DENSITY": 59.08,
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "NOM_DEPT": "MANCHE",
                        "POPULATION": 496883,
                        "DENSITY": 82.61,
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "NOM_DEPT": "YVELINES",
                        "POPULATION": 1438266,
                        "DENSITY": 623.8,
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "NOM_DEPT": "DOUBS",
                        "POPULATION": 539067,
                        "DENSITY": 102.71,
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "NOM_DEPT": "MEUSE",
                        "POPULATION": 187187,
                        "DENSITY": 30.03,
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "NOM_DEPT": "GIRONDE",
                        "POPULATION": 1583384,
                        "DENSITY": 157.26,
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "NOM_DEPT": "CALVADOS",
                        "POPULATION": 694002,
                        "DENSITY": 124.18,
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "NOM_DEPT": "VOSGES",
                        "POPULATION": 367673,
                        "DENSITY": 62.41,
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "NOM_DEPT": "CHER",
                        "POPULATION": 304256,
                        "DENSITY": 41.72,
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "NOM_DEPT": "ARDECHE",
                        "POPULATION": 325712,
                        "DENSITY": 58.56,
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "NOM_DEPT": "PYRENEES-ATLANTIQUES",
                        "POPULATION": 677309,
                        "DENSITY": 88.06,
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "NOM_DEPT": "LOIR-ET-CHER",
                        "POPULATION": 331915,
                        "DENSITY": 51.76,
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "NOM_DEPT": "MOSELLE",
                        "POPULATION": 1043522,
                        "DENSITY": 166.89,
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "NOM_DEPT": "VIENNE",
                        "POPULATION": 436876,
                        "DENSITY": 62.19,
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "NOM_DEPT": "DORDOGNE",
                        "POPULATION": 413606,
                        "DENSITY": 44.91,
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "NOM_DEPT": "JURA",
                        "POPULATION": 260188,
                        "DENSITY": 51.62,
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "NOM_DEPT": "TARN-ET-GARONNE",
                        "POPULATION": 258349,
                        "DENSITY": 69.24,
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "NOM_DEPT": "MAINE-ET-LOIRE",
                        "POPULATION": 813493,
                        "DENSITY": 113.6,
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "NOM_DEPT": "RHONE",
                        "POPULATION": 1843319,
                        "DENSITY": 566.63,
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "NOM_DEPT": "EURE",
                        "POPULATION": 601843,
                        "DENSITY": 99.71,
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "NOM_DEPT": "AVEYRON",
                        "POPULATION": 279206,
                        "DENSITY": 31.83,
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "NOM_DEPT": "CREUSE",
                        "POPULATION": 118638,
                        "DENSITY": 21.23,
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "NOM_DEPT": "LOIRET",
                        "POPULATION": 678008,
                        "DENSITY": 99.65,
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "NOM_DEPT": "HAUTE-SAONE",
                        "POPULATION": 236659,
                        "DENSITY": 43.97,
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "NOM_DEPT": "PUY-DE-DOME",
                        "POPULATION": 653742,
                        "DENSITY": 81.69,
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "NOM_DEPT": "TARN",
                        "POPULATION": 387890,
                        "DENSITY": 67.04,
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "NOM_DEPT": "SEINE-MARITIME",
                        "POPULATION": 1254378,
                        "DENSITY": 198.53,
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "NOM_DEPT": "HAUTE-MARNE",
                        "POPULATION": 175640,
                        "DENSITY": 28.1,
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "NOM_DEPT": "GARD",
                        "POPULATION": 744178,
                        "DENSITY": 126.67,
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "NOM_DEPT": "BAS-RHIN",
                        "POPULATION": 1125559,
                        "DENSITY": 234.67,
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "NOM_DEPT": "AUDE",
                        "POPULATION": 370260,
                        "DENSITY": 58.3,
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "NOM_DEPT": "SEINE-ET-MARNE",
                        "POPULATION": 1403997,
                        "DENSITY": 236.98,
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "NOM_DEPT": "SOMME",
                        "POPULATION": 572443,
                        "DENSITY": 92.23,
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "NOM_DEPT": "HAUTE-LOIRE",
                        "POPULATION": 227283,
                        "DENSITY": 45.49,
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "NOM_DEPT": "MARNE",
                        "POPULATION": 568895,
                        "DENSITY": 69.41,
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "NOM_DEPT": "HAUTES-PYRENEES",
                        "POPULATION": 228530,
                        "DENSITY": 50.47,
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "NOM_DEPT": "LOT",
                        "POPULATION": 173828,
                        "DENSITY": 33.29,
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "NOM_DEPT": "ALPES-DE-HAUTE-PROVENCE",
                        "POPULATION": 163915,
                        "DENSITY": 23.44,
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "NOM_DEPT": "SARTHE",
                        "POPULATION": 566506,
                        "DENSITY": 90.83,
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "NOM_DEPT": "EURE-ET-LOIR",
                        "POPULATION": 433233,
                        "DENSITY": 73.09,
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "NOM_DEPT": "CORSE-DU-SUD",
                        "POPULATION": 157249,
                        "DENSITY": 39.03,
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "NOM_DEPT": "MEURTHE-ET-MOSELLE",
                        "POPULATION": 733481,
                        "DENSITY": 138.83,
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "NOM_DEPT": "ORNE",
                        "POPULATION": 283372,
                        "DENSITY": 46.13,
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "NOM_DEPT": "AIN",
                        "POPULATION": 643350,
                        "DENSITY": 111.43,
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "NOM_DEPT": "ARIEGE",
                        "POPULATION": 153153,
                        "DENSITY": 31.12,
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "NOM_DEPT": "CORREZE",
                        "POPULATION": 241464,
                        "DENSITY": 41.0,
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "NOM_DEPT": "HAUT-RHIN",
                        "POPULATION": 764030,
                        "DENSITY": 216.66,
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "NOM_DEPT": "INDRE-ET-LOIRE",
                        "POPULATION": 606511,
                        "DENSITY": 98.66,
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "NOM_DEPT": "NORD",
                        "POPULATION": 2604361,
                        "DENSITY": 450.97,
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "NOM_DEPT": "TERRITOIRE DE BELFORT",
                        "POPULATION": 142622,
                        "DENSITY": 233.94,
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "NOM_DEPT": "LOIRE-ATLANTIQUE",
                        "POPULATION": 1394909,
                        "DENSITY": 199.48,
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "NOM_DEPT": "YONNE",
                        "POPULATION": 338291,
                        "DENSITY": 45.4,
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "NOM_DEPT": "ILLE-ET-VILAINE",
                        "POPULATION": 1060199,
                        "DENSITY": 155.22,
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "NOM_DEPT": "LANDES",
                        "POPULATION": 407444,
                        "DENSITY": 43.56,
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "NOM_DEPT": "FINISTERE",
                        "POPULATION": 909028,
                        "DENSITY": 134.54,
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "NOM_DEPT": "HAUTE-SAVOIE",
                        "POPULATION": 807360,
                        "DENSITY": 175.65,
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "NOM_DEPT": "OISE",
                        "POPULATION": 824503,
                        "DENSITY": 139.9,
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "NOM_DEPT": "NIEVRE",
                        "POPULATION": 207182,
                        "DENSITY": 30.19,
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "NOM_DEPT": "COTE-D'OR",
                        "POPULATION": 532871,
                        "DENSITY": 60.64,
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "NOM_DEPT": "ESSONNE",
                        "POPULATION": 1296130,
                        "DENSITY": 712.81,
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "NOM_DEPT": "DEUX-SEVRES",
                        "POPULATION": 374351,
                        "DENSITY": 62.09,
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "NOM_DEPT": "COTES-D'ARMOR",
                        "POPULATION": 598814,
                        "DENSITY": 86.0,
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "NOM_DEPT": "ALLIER",
                        "POPULATION": 337988,
                        "DENSITY": 45.89,
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "NOM_DEPT": "CHARENTE-MARITIME",
                        "POPULATION": 644303,
                        "DENSITY": 93.2,
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "NOM_DEPT": "CANTAL",
                        "POPULATION": 145143,
                        "DENSITY": 25.17,
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "NOM_DEPT": "HERAULT",
                        "POPULATION": 1144892,
                        "DENSITY": 183.74,
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "NOM_DEPT": "DROME",
                        "POPULATION": 511553,
                        "DENSITY": 78.06,
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "NOM_DEPT": "PYRENEES-ORIENTALES",
                        "POPULATION": 474452,
                        "DENSITY": 114.39,
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "NOM_DEPT": "SAVOIE",
                        "POPULATION": 431174,
                        "DENSITY": 68.87,
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "NOM_DEPT": "HAUTES-ALPES",
                        "POPULATION": 141284,
                        "DENSITY": 24.85,
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "NOM_DEPT": "VAUCLUSE",
                        "POPULATION": 559479,
                        "DENSITY": 156.4,
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "NOM_DEPT": "INDRE",
                        "POPULATION": 222232,
                        "DENSITY": 32.27,
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "NOM_DEPT": "HAUTE-CORSE",
                        "POPULATION": 177689,
                        "DENSITY": 37.65,
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "NOM_DEPT": "HAUTE-VIENNE",
                        "POPULATION": 374426,
                        "DENSITY": 67.47,
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "NOM_DEPT": "VENDEE",
                        "POPULATION": 675247,
                        "DENSITY": 99.91,
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "NOM_DEPT": "VAR",
                        "POPULATION": 1058740,
                        "DENSITY": 176.37,
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "NOM_DEPT": "VAL-DE-MARNE",
                        "POPULATION": 1387926,
                        "DENSITY": 5671.95,
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "NOM_DEPT": "HAUTS-DE-SEINE",
                        "POPULATION": 1609306,
                        "DENSITY": 9163.05,
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "NOM_DEPT": "LOZERE",
                        "POPULATION": 76601,
                        "DENSITY": 14.81,
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "NOM_DEPT": "BOUCHES-DU-RHONE",
                        "POPULATION": 2024162,
                        "DENSITY": 398.26,
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "NOM_DEPT": "PARIS",
                        "POPULATION": 2187526,
                        "DENSITY": 20746.64,
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "NOM_DEPT": "SEINE-SAINT-DENIS",
                        "POPULATION": 1623111,
                        "DENSITY": 6849.73,
                    }
                },
            },
        },
    },
    3: {
        "geolayer_a": geolayer_fr_dept_data_and_geometry,
        "geolayer_b": geolayer_fr_dept_population,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_WITH_POPULATION",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": geolayer_fr_dept_population_geometry,
    },
    4: {
        "geolayer_a": geolayer_dpt_full,
        "geolayer_b": geolayer_dpt_pop_2,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_FULL_FULL_JOIN_POP_2",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_FULL_FULL_JOIN_POP_2",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "NOM_DEPT": "MAYENNE",
                        "POPULATION": 307445,
                        "DENSITY": 59.03,
                    }
                },
                1: {"attributes": {"CODE_DEPT": "02", "NOM_DEPT": "AISNE"}},
                2: {"attributes": {"CODE_DEPT": "95", "NOM_DEPT": "VAL-D'OISE"}},
                3: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
            },
        },
    },
    5: {
        "geolayer_a": geolayer_dpt_full_with_duplicate,
        "geolayer_b": geolayer_dpt_pop_2,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_FULL_WITH_DUPLICATE_FULL_JOIN_POP_2",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_FULL_WITH_DUPLICATE_FULL_JOIN_POP_2",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "NOM_DEPT": "MAYENNE",
                        "POPULATION": 307445,
                        "DENSITY": 59.03,
                    }
                },
                1: {"attributes": {"CODE_DEPT": "02", "NOM_DEPT": "AISNE"}},
                2: {"attributes": {"CODE_DEPT": "02", "NOM_DEPT": "AISNE"}},
                3: {"attributes": {"CODE_DEPT": "95", "NOM_DEPT": "VAL-D'OISE"}},
                4: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "NOM_DEPT": "MORBIHAN",
                        "POPULATION": 750863,
                        "DENSITY": 109.39,
                    }
                },
            },
        },
    },
    6: {
        "geolayer_a": geolayer_dpt_2,
        "geolayer_b": geolayer_dpt_pop_full,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_FULL_JOIN_POP_FULL",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_FULL_JOIN_POP_FULL",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"POPULATION": 307445, "DENSITY": 59.03}},
                1: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
                3: {"attributes": {"POPULATION": 750863, "DENSITY": 109.39}},
            },
        },
    },
    7: {
        "geolayer_a": geolayer_dpt_2,
        "geolayer_b": geolayer_dpt_pop_full_with_duplicate,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_FULL_JOIN_POP_FULL_WITH_DUPLICATE",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_FULL_JOIN_POP_FULL_WITH_DUPLICATE",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"POPULATION": 307445, "DENSITY": 59.03}},
                1: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    }
                },
                4: {"attributes": {"POPULATION": 750863, "DENSITY": 109.39}},
                5: {"attributes": {"POPULATION": 750863, "DENSITY": 109.39}},
            },
        },
    },
    8: {
        "geolayer_a": geolayer_dpt_2,
        "geolayer_b": geolayer_dpt_pop_2,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_FULL_JOIN_POP_2",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_FULL_JOIN_POP_2",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"CODE_DEPT": "02", "NOM_DEPT": "AISNE"}},
                1: {"attributes": {"CODE_DEPT": "95", "NOM_DEPT": "VAL-D'OISE"}},
                2: {"attributes": {"POPULATION": 307445, "DENSITY": 59.03}},
                3: {"attributes": {"POPULATION": 750863, "DENSITY": 109.39}},
            },
        },
    },
    9: {
        "geolayer_a": geolayer_dpt_2_with_geom,
        "geolayer_b": geolayer_dpt_pop_full,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_FULL_JOIN_POP_FULL",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_FULL_JOIN_POP_FULL",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6861428.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {"attributes": {"POPULATION": 307445, "DENSITY": 59.03}},
                1: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                    },
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                    },
                },
                3: {"attributes": {"POPULATION": 750863, "DENSITY": 109.39}},
            },
        },
    },
    10: {
        "geolayer_a": geolayer_dpt_2_with_geom,
        "geolayer_b": geolayer_dpt_pop_full,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_FULL_JOIN_POP_FULL",
        "field_name_filter_a": ["CODE_DEPT", "NOM_DEPT"],
        "field_name_filter_b": ["POPULATION", "DENSITY"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_FULL_JOIN_POP_FULL",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"POPULATION": 307445, "DENSITY": 59.03}},
                1: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                    },
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                    },
                },
                3: {"attributes": {"POPULATION": 750863, "DENSITY": 109.39}},
            },
        },
    },
    11: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2_with_geom,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_FULL_JOIN_POP_FULL",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_FULL_JOIN_POP_FULL",
                "fields": {
                    "POPULATION": {"type": "Integer", "index": 0},
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 2},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 3},
                },
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6861428.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {"attributes": {"POPULATION": 307445, "DENSITY": 59.03}},
                1: {
                    "attributes": {
                        "POPULATION": 534490,
                        "DENSITY": 72.04,
                        "CODE_DEPT": "02",
                        "NOM_DEPT": "AISNE",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                    },
                },
                2: {
                    "attributes": {
                        "POPULATION": 1228618,
                        "DENSITY": 979.62,
                        "CODE_DEPT": "95",
                        "NOM_DEPT": "VAL-D'OISE",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                    },
                },
                3: {"attributes": {"POPULATION": 750863, "DENSITY": 109.39}},
            },
        },
    },
    12: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2_with_geom,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_FULL_JOIN_POP_FULL",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": {"POPULATION": "pop"},
        "rename_output_field_from_geolayer_b": {"CODE_DEPT": "id"},
        "geometry_ref": "geolayer_b",
        "return_value": {
            "metadata": {
                "name": "FRANCE_DPT_2_WITH_GEOM_FULL_JOIN_POP_FULL",
                "fields": {
                    "DENSITY": {"type": "Real", "width": 5, "precision": 2, "index": 1},
                    "pop": {"type": "Integer", "index": 0},
                    "NOM_DEPT": {"type": "String", "width": 10, "index": 2},
                    "id": {"type": "String", "width": 2, "index": 3},
                },
                "geometry_ref": {
                    "type": {"Polygon"},
                    "extent": (598361.0, 6861428.0, 790134.0, 6997000.0),
                },
            },
            "features": {
                0: {"attributes": {"DENSITY": 59.03, "pop": 307445}},
                1: {
                    "attributes": {
                        "DENSITY": 72.04,
                        "pop": 534490,
                        "NOM_DEPT": "AISNE",
                        "id": "02",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (698137.0, 6861428.0, 790134.0, 6997000.0),
                    },
                },
                2: {
                    "attributes": {
                        "DENSITY": 979.62,
                        "pop": 1228618,
                        "NOM_DEPT": "VAL-D'OISE",
                        "id": "95",
                    },
                    "geometry": {
                        "type": "Polygon",
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
                        "bbox": (598361.0, 6867928.0, 670084.0, 6904387.0),
                    },
                },
                3: {"attributes": {"DENSITY": 109.39, "pop": 750863}},
            },
        },
    },
    13: {
        "geolayer_a": geolayer_dpt_pop_full,
        "geolayer_b": geolayer_dpt_2_with_geom,
        "on_field_a": "CODE_DEPT",
        "on_field_b": "CODE_DEPT",
        "output_geolayer_name": "FRANCE_DPT_2_WITH_GEOM_FULL_JOIN_POP_FULL",
        "field_name_filter_a": ["POPULATION", "DENSITY"],
        "field_name_filter_b": ["CODE_DEPT", "NOM_DEPT"],
        "rename_output_field_from_geolayer_a": {
            "CODE_DEPT": "code",
            "POPULATION": "pop",
        },
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_b",
        "return_value": field_missing.format(field_name="CODE_DEPT"),
    },
    14: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "key_id": {"type": "Integer", "index": 0},
                    "price": {"type": "Integer", "index": 1},
                    "count": {"type": "Integer", "index": 2},
                    "probability": {
                        "type": "Real",
                        "width": 1,
                        "precision": 0,
                        "index": 3,
                    },
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "key_id": 164,
                        "price": 4300,
                        "count": 0,
                        "probability": 0.0,
                    }
                }
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "key_id": {"type": "Integer", "index": 0},
                    "price": {"type": "Integer", "index": 1},
                    "count": {"type": "Integer", "index": 2},
                    "probability": {
                        "type": "Real",
                        "width": 1,
                        "precision": 1,
                        "index": 3,
                    },
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "key_id": 0,
                        "price": 5000,
                        "count": 1,
                        "probability": 0.1,
                    }
                },
                1: {
                    "attributes": {
                        "key_id": 164,
                        "price": 4300,
                        "count": 1,
                        "probability": 0.1,
                    }
                },
            },
        },
        "on_field_a": "key_id",
        "on_field_b": "key_id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": {
            "key_id": "key_id_b",
            "price": "price_b",
            "count": "count_b",
            "probability": "probability_b",
        },
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "key_id": {"type": "Integer", "index": 0},
                    "price": {"type": "Integer", "index": 1},
                    "count": {"type": "Integer", "index": 2},
                    "probability": {
                        "type": "Real",
                        "width": 1,
                        "precision": 0,
                        "index": 3,
                    },
                    "key_id_b": {"type": "Integer", "index": 4},
                    "price_b": {"type": "Integer", "index": 5},
                    "count_b": {"type": "Integer", "index": 6},
                    "probability_b": {
                        "type": "Real",
                        "width": 1,
                        "precision": 1,
                        "index": 7,
                    },
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "key_id_b": 0,
                        "price_b": 5000,
                        "count_b": 1,
                        "probability_b": 0.1,
                    }
                },
                1: {
                    "attributes": {
                        "key_id": 164,
                        "price": 4300,
                        "count": 0,
                        "probability": 0.0,
                        "key_id_b": 164,
                        "price_b": 4300,
                        "count_b": 1,
                        "probability_b": 0.1,
                    }
                },
            },
        },
    },
    15: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice"}},
                1: {"attributes": {"id": None, "name": "Bob"}},
                2: {"attributes": {"id": None, "name": "Patrick"}},
                3: {"attributes": {"id": 1, "name": "Jane"}},
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "age": {"type": "Integer", "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "age": 28}},
                1: {"attributes": {"id": 1, "age": 2}},
            },
        },
        "on_field_a": "id",
        "on_field_b": "id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                    "id1": {"type": "Integer", "index": 2},
                    "age": {"type": "Integer", "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice", "id1": 0, "age": 28}},
                1: {"attributes": {"id": None, "name": "Bob"}},
                2: {"attributes": {"id": None, "name": "Patrick"}},
                3: {"attributes": {"id": 1, "name": "Jane", "id1": 1, "age": 2}},
            },
        },
    },
    16: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 5, "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice"}},
                1: {"attributes": {"id": 1, "name": "Jane"}},
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "age": {"type": "Integer", "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "age": 28}},
                1: {"attributes": {"id": None, "age": 67}},
                2: {"attributes": {"id": None, "age": 15}},
                3: {"attributes": {"id": 1, "age": 2}},
            },
        },
        "on_field_a": "id",
        "on_field_b": "id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 5, "index": 1},
                    "id1": {"type": "Integer", "index": 2},
                    "age": {"type": "Integer", "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice", "id1": 0, "age": 28}},
                1: {"attributes": {"id1": None, "age": 67}},
                2: {"attributes": {"id1": None, "age": 15}},
                3: {"attributes": {"id": 1, "name": "Jane", "id1": 1, "age": 2}},
            },
        },
    },
    17: {
        "geolayer_a": {
            "metadata": {
                "name": "geolayer_a",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice"}},
                1: {"attributes": {"id": None, "name": "Bob"}},
                2: {"attributes": {"id": None, "name": "Patrick"}},
                3: {"attributes": {"id": 1, "name": "Jane"}},
            },
        },
        "geolayer_b": {
            "metadata": {
                "name": "geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "age": {"type": "Integer", "index": 1},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "age": 28}},
                1: {"attributes": {"id": None, "age": 67}},
                2: {"attributes": {"id": None, "age": 15}},
                3: {"attributes": {"id": 1, "age": 2}},
            },
        },
        "on_field_a": "id",
        "on_field_b": "id",
        "output_geolayer_name": None,
        "field_name_filter_a": None,
        "field_name_filter_b": None,
        "rename_output_field_from_geolayer_a": "auto",
        "rename_output_field_from_geolayer_b": "auto",
        "geometry_ref": "geolayer_a",
        "return_value": {
            "metadata": {
                "name": "geolayer_a_join_geolayer_b",
                "fields": {
                    "id": {"type": "Integer", "index": 0},
                    "name": {"type": "String", "width": 7, "index": 1},
                    "id1": {"type": "Integer", "index": 2},
                    "age": {"type": "Integer", "index": 3},
                },
            },
            "features": {
                0: {"attributes": {"id": 0, "name": "Alice", "id1": 0, "age": 28}},
                1: {"attributes": {"id": 1, "name": "Jane", "id1": 1, "age": 2}},
                2: {"attributes": {"id": None, "name": "Bob"}},
                3: {"attributes": {"id": None, "name": "Patrick"}},
                4: {"attributes": {"id1": None, "age": 67}},
                5: {"attributes": {"id1": None, "age": 15}},
            },
        },
    },
}


def test_all():
    # join
    print(test_function(join, join_parameters))

    # join left
    print(test_function(join_left, join_left_parameters))

    # join right
    print(test_function(join_right, join_right_parameters))

    # join full
    print(test_function(join_full, join_full_parameters))


if __name__ == "__main__":
    test_all()
