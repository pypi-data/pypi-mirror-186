import datetime

from geoformat.processing.data.clauses import (
    clause_where,
    clause_group_by,
    clause_order_by
)
from tests.data.geolayers import (
    geolayer_fr_dept_data_only,
    geolayer_fr_dept_population,
    geolayer_attributes_only,
    geolayer_attributes_to_force_only_forced,
    geolayer_btc_price_sample
)

from tests.utils.tests_utils import test_function

from geoformat.conf.error_messages import field_missing



clause_where_parameters = {
    0: {
        "geolayer": geolayer_fr_dept_data_only,
        "field_name": "NOM_DEPT",
        "predicate": "=",
        "values": "MEUSE",
        "return_value": [15]
    },
    1: {
        "geolayer": geolayer_fr_dept_data_only,
        "field_name": "CODE_DEPT",
        "predicate": "<",
        "values": "10",
        "return_value": [4, 6, 20, 21, 49, 56, 57, 76, 83]
    },
    2: {
        "geolayer": geolayer_fr_dept_data_only,
        "field_name": "CODE_DEPT",
        "predicate": ">",
        "values": "90",
        "return_value": [70, 73, 90, 91, 95]
    },
    3: {
        "geolayer": geolayer_fr_dept_data_only,
        "field_name": "NOM_DEPT",
        "predicate": "IN",
        "values": ["HAUTE-SAONE", "PUY-DE-DOME", "TARN", "SEINE-MARITIME"],
        "return_value": [35, 36, 37, 38]
    },
    4: {
        "geolayer": geolayer_attributes_only,
        "field_name": "field_not_exists",
        "predicate": "=",
        "values": "foo",
        "return_value": field_missing.format(field_name="field_not_exists")
    },
    6: {
        "geolayer": geolayer_attributes_to_force_only_forced,
        "field_name": "field_string",
        "predicate": "IS",
        "values": None,
        "return_value": [0]
    },
    7: {
        "geolayer": geolayer_btc_price_sample,
        "field_name": "USD_PRICE_CLOSE",
        "predicate": "IS",
        "values": None,
        "return_value": [21, 22]
    },
    8: {
        "geolayer": geolayer_btc_price_sample,
        "field_name": "USD_PRICE_CLOSE",
        "predicate": "IS NOT",
        "values": None,
        "return_value": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    },
    9: {
        "geolayer": geolayer_btc_price_sample,
        "field_name": "USD_PRICE_CLOSE",
        "predicate": ">",
        "values": 39000,
        "return_value": [0, 1, 7]
    },
    10: {
        "geolayer": geolayer_btc_price_sample,
        "field_name": "USD_PRICE_CLOSE",
        "predicate": "<",
        "values": 39000,
        "return_value": [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    },
    11: {
        "geolayer": geolayer_btc_price_sample,
        "field_name": "USD_PRICE_CLOSE",
        "predicate": "BETWEEN",
        "values": [28000, 31000],
        "return_value": [12, 14, 15, 16, 17, 19, 20]
    },
    12: {
        "geolayer": geolayer_btc_price_sample,
        "field_name": "DATE",
        "predicate": "BETWEEN",
        "values": [datetime.date(2022, 5, 1), datetime.date(2022, 5, 9)],
        "return_value": [4, 5, 6, 7, 8, 9, 10, 11, 12]
    },
    13: {
        "geolayer": geolayer_btc_price_sample,
        "field_name": "DATE",
        "predicate": ">",
        "values":  datetime.date(2022, 5, 9),
        "return_value": [13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    },
    14: {
        "geolayer": geolayer_btc_price_sample,
        "field_name": "DATE",
        "predicate": "<",
        "values":  datetime.date(2022, 5, 9),
        "return_value": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    },
    15: {
        "geolayer": geolayer_btc_price_sample,
        "field_name": "DATE",
        "predicate": "IN",
        "values":  [datetime.date(2022, 5, 9), datetime.date(2022, 5, 6), datetime.date(2022, 5, 12)],
        "return_value": [9, 12, 15]
    },
}

clause_group_by_parameters = {
    0: {
        "geolayer": geolayer_fr_dept_population,
        "field_name_list": 'INSEE_REG',
        "return_value": {('76',): [0, 8, 28, 31, 36, 40, 42, 47, 48, 57, 77, 79, 92], ('75',): [1, 13, 16, 22, 25, 26, 32, 56, 64, 75, 83, 87], ('84',): [2, 6, 20, 30, 35, 44, 55, 66, 74, 76, 78, 80], ('32',): [3, 21, 46, 59, 67], ('44',): [4, 5, 15, 18, 24, 39, 41, 45, 54, 58], ('93',): [7, 49, 82, 84, 89, 93], ('27',): [9, 14, 27, 34, 60, 62, 69, 72], ('52',): [10, 29, 50, 61, 88], ('11',): [11, 43, 68, 71, 90, 91, 94, 95], ('28',): [12, 17, 37, 38, 70], ('24',): [19, 23, 33, 53, 81, 85], ('53',): [51, 63, 65, 73], ('94',): [52, 86]}
    },
}


clause_order_by_parameters = {
    0: {
        "geolayer": geolayer_fr_dept_population,
        "order_parameters": 'CODE_DEPT',
        "return_value": [55, 21, 74, 49, 82, 7, 20, 4, 57, 5, 42, 31, 93, 17, 76, 13, 75, 19, 56, 72, 73, 32, 26, 14, 78, 37, 53, 65, 52, 86, 40, 8, 0, 16, 77, 63, 85, 81, 2, 27, 64, 23, 6, 44, 61, 33, 47, 1, 92, 29, 12, 45, 39, 10, 54, 15, 51, 24, 69, 59, 67, 70, 3, 35, 22, 48, 79, 41, 58, 30, 34, 9, 50, 80, 66, 95, 38, 43, 11, 83, 46, 36, 28, 89, 84, 88, 25, 87, 18, 62, 60, 71, 91, 94, 90, 68]
    },
    1: {
        "geolayer": geolayer_fr_dept_population,
        "order_parameters": [('CODE_DEPT', 'ASC')],
        "return_value": [55, 21, 74, 49, 82, 7, 20, 4, 57, 5, 42, 31, 93, 17, 76, 13, 75, 19, 56, 72, 73, 32, 26, 14, 78, 37, 53, 65, 52, 86, 40, 8, 0, 16, 77, 63, 85, 81, 2, 27, 64, 23, 6, 44, 61, 33, 47, 1, 92, 29, 12, 45, 39, 10, 54, 15, 51, 24, 69, 59, 67, 70, 3, 35, 22, 48, 79, 41, 58, 30, 34, 9, 50, 80, 66, 95, 38, 43, 11, 83, 46, 36, 28, 89, 84, 88, 25, 87, 18, 62, 60, 71, 91, 94, 90, 68]
    },
    3: {
        "geolayer": geolayer_fr_dept_population,
        "order_parameters": [('CODE_DEPT', 'DESC')],
        "return_value": list(reversed([55, 21, 74, 49, 82, 7, 20, 4, 57, 5, 42, 31, 93, 17, 76, 13, 75, 19, 56, 72, 73, 32, 26, 14, 78, 37, 53, 65, 52, 86, 40, 8, 0, 16, 77, 63, 85, 81, 2, 27, 64, 23, 6, 44, 61, 33, 47, 1, 92, 29, 12, 45, 39, 10, 54, 15, 51, 24, 69, 59, 67, 70, 3, 35, 22, 48, 79, 41, 58, 30, 34, 9, 50, 80, 66, 95, 38, 43, 11, 83, 46, 36, 28, 89, 84, 88, 25, 87, 18, 62, 60, 71, 91, 94, 90, 68]))
    },
    2: {
        "geolayer": geolayer_fr_dept_population,
        "order_parameters": [('INSEE_REG', 'ASC'), ('CODE_DEPT', 'DESC')],
        "return_value": [68, 90, 94, 91, 71, 11, 43, 95, 33, 23, 81, 85, 53, 19, 60, 62, 9, 34, 69, 27, 14, 72, 38, 70, 12, 37, 17, 46, 3, 67, 59, 21, 18, 58, 41, 24, 15, 54, 39, 45, 5, 4, 88, 50, 10, 29, 61, 51, 63, 65, 73, 87, 25, 83, 22, 1, 64, 16, 26, 32, 56, 75, 13, 28, 36, 79, 48, 92, 47, 77, 0, 8, 40, 31, 42, 57, 66, 80, 30, 35, 44, 6, 2, 78, 76, 20, 74, 55, 84, 89, 93, 7, 82, 49, 86, 52]
    },
}

def test_all():

    # clause_where
    print(test_function(clause_where, clause_where_parameters))

    # clause_group_by
    print(test_function(clause_group_by, clause_group_by_parameters))

    # clause_order_by
    print(test_function(clause_order_by, clause_order_by_parameters))



if __name__ == '__main__':
    test_all()
