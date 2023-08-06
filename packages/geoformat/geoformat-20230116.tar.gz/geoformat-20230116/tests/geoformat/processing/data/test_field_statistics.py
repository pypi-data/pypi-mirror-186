from geoformat.processing.data.field_statistics import field_statistics
from tests.utils.tests_utils import test_function
from tests.data.geolayers import geolayer_fr_dept_population

field_statistics_parameters = {
    0: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'SUM']],
        "bessel_correction": True,
        "return_value": {'POPULATION': {'SUM': 64638088}}
    },
    2: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'MEAN']],
        "bessel_correction": True,
        "return_value": {'POPULATION': {'MEAN': 673313.4166666665}}
    },
    3: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'MIN']],
        "bessel_correction": True,
        "return_value": {'POPULATION': {'MIN': 76601}}
    },
    4: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'MAX']],
        "bessel_correction": True,
        "return_value": {'POPULATION': {'MAX': 2604361}}
    },
    5: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'RANGE']],
        "bessel_correction": True,
        "return_value": {'POPULATION': {'RANGE': 2527760}}
    },
    6: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'STD']],
        "bessel_correction": True,
        "return_value": {'POPULATION': {'STD': 515274.66505417065}}
    },
    7: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'COUNT']],
        "bessel_correction": True,
        "return_value": {'POPULATION': {'COUNT': 96}}
    },
    8: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'FIRST']],
        "bessel_correction": True,
        "return_value": {'POPULATION': {'FIRST': 191091}}
    },
    9: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'LAST']],
        "bessel_correction": True,
        "return_value": {'POPULATION': {'LAST': 2187526}}
    },
    10: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'VARIANCE']],
        "bessel_correction": True,
        "return_value": {'POPULATION': {'VARIANCE': 265507980446.68777}}
    },
    11: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [[('POPULATION', 'AREA'), 'WEIGHTED_MEAN']],
        "bessel_correction": True,
        "return_value": {('POPULATION', 'AREA'): {'WEIGHTED_MEAN': 622009.6380951514}}
    },
    12: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [[('POPULATION', 'AREA'), 'COVARIANCE']],
        "bessel_correction": True,
        "return_value": {('POPULATION', 'AREA'): {'COVARIANCE': -293045606.6781337}}
    },
    13: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'SUM']],
        "bessel_correction": False,
        "return_value": {'POPULATION': {'SUM': 64638088}}
    },
    14: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'MEAN']],
        "bessel_correction": False,
        "return_value": {'POPULATION': {'MEAN': 673313.4166666665}}
    },
    15: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'MIN']],
        "bessel_correction": False,
        "return_value": {'POPULATION': {'MIN': 76601}}
    },
    16: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'MAX']],
        "bessel_correction": False,
        "return_value": {'POPULATION': {'MAX': 2604361}}
    },
    17: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'RANGE']],
        "bessel_correction": False,
        "return_value": {'POPULATION': {'RANGE': 2527760}}
    },
    18: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'STD']],
        "bessel_correction": False,
        "return_value": {'POPULATION': {'STD': 512583.9173413801}}
    },
    19: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'COUNT']],
        "bessel_correction": False,
        "return_value": {'POPULATION': {'COUNT': 96}}
    },
    20: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'FIRST']],
        "bessel_correction": False,
        "return_value": {'POPULATION': {'FIRST': 191091}}
    },
    21: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'LAST']],
        "bessel_correction": False,
        "return_value": {'POPULATION': {'LAST': 2187526}}
    },
    22: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'VARIANCE']],
        "bessel_correction": False,
        "return_value": {'POPULATION': {'VARIANCE': 262742272317.0348}}
    },
    23: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [[('POPULATION', 'AREA'), 'WEIGHTED_MEAN']],
        "bessel_correction": False,
        "return_value": {('POPULATION', 'AREA'): {'WEIGHTED_MEAN': 622009.6380951514}}
    },
    24: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [[('POPULATION', 'AREA'), 'COVARIANCE']],
        "bessel_correction": False,
        "return_value": {('POPULATION', 'AREA'): {'COVARIANCE': -293045606.6781337}}
    },
    25: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'ALL']],
        "bessel_correction": True,
        "return_value": {'POPULATION': {'COUNT': 96, 'SUM': 64638088, 'RANGE': 2527760, 'MIN': 76601, 'MEAN': 673313.4166666665, 'MAX': 2604361, 'STD': 515274.66505417065, 'FIRST': 191091, 'LAST': 2187526, 'VARIANCE': 265507980446.68777}}
    },
    26: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [['POPULATION', 'ALL'], ['AREA', 'ALL']],
        "bessel_correction": True,
        "return_value": {'POPULATION': {'COUNT': 96, 'SUM': 64638088, 'RANGE': 2604185.37, 'MIN': 76601, 'MEAN': 673313.4166666665, 'MAX': 2604361, 'STD': 515274.66505417065, 'FIRST': 191091, 'LAST': 2187526, 'VARIANCE': 265507980446.68777}, 'AREA': {'COUNT': 96, 'SUM': 548349.0499999999, 'RANGE': 2604255.56, 'MIN': 105.44, 'MEAN': 5711.969270833332, 'MAX': 10068.74, 'STD': 1942.902658309954, 'FIRST': 6304.33, 'LAST': 105.44, 'VARIANCE': 3774870.7396678855}}
    },
    27: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [[('POPULATION', 'AREA'), 'ALL']],
        "bessel_correction": True,
        "return_value": {('POPULATION', 'AREA'): {'WEIGHTED_MEAN': 622009.6380951514, 'COVARIANCE': -293045606.6781337}}
    },
    28: {
        "geolayer": geolayer_fr_dept_population,
        "statistic_field": [[('POPULATION', 'AREA'), 'ALL'], ['POPULATION', 'ALL']],
        "bessel_correction": True,
        "return_value": {('POPULATION', 'AREA'): {'WEIGHTED_MEAN': 622009.6380951514, 'COVARIANCE': -293045606.6781337}, 'POPULATION': {'COUNT': 96, 'SUM': 64638088, 'RANGE': 2527760, 'MIN': 76601, 'MEAN': 673313.4166666665, 'MAX': 2604361, 'STD': 515274.66505417065, 'FIRST': 191091, 'LAST': 2187526, 'VARIANCE': 265507980446.68777}}
    },
}

def test_all():

    # field_statistics
    print(test_function(field_statistics, field_statistics_parameters))


if __name__ == '__main__':
    test_all()