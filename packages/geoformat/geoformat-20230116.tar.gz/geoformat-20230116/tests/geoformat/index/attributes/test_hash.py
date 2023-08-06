from geoformat.index.attributes.hash import create_attribute_index

from tests.data.geolayers import geolayer_fr_dept_population
from tests.data.index import geolayer_fr_dept_population_CODE_DEPT_hash_index

from tests.utils.tests_utils import test_function

create_attribute_index_parameters = {
    0: {
        "geolayer": geolayer_fr_dept_population,
        "field_name": "CODE_DEPT",
        "return_value": geolayer_fr_dept_population_CODE_DEPT_hash_index
    },
    1: {
        "geolayer": geolayer_fr_dept_population,
        "field_name": "INSEE_REG",
        "return_value": {'type': 'hashtable', 'index': {'76': [0, 8, 28, 31, 36, 40, 42, 47, 48, 57, 77, 79, 92], '75': [1, 13, 16, 22, 25, 26, 32, 56, 64, 75, 83, 87], '84': [2, 6, 20, 30, 35, 44, 55, 66, 74, 76, 78, 80], '32': [3, 21, 46, 59, 67], '44': [4, 5, 15, 18, 24, 39, 41, 45, 54, 58], '93': [7, 49, 82, 84, 89, 93], '27': [9, 14, 27, 34, 60, 62, 69, 72], '52': [10, 29, 50, 61, 88], '11': [11, 43, 68, 71, 90, 91, 94, 95], '28': [12, 17, 37, 38, 70], '24': [19, 23, 33, 53, 81, 85], '53': [51, 63, 65, 73], '94': [52, 86]}}
    }
}

def test_all():

    # create_attribute_index
    print(test_function(create_attribute_index, create_attribute_index_parameters))

if __name__ == '__main__':
    test_all()