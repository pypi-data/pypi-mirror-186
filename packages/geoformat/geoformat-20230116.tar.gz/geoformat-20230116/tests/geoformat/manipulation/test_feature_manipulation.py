import datetime

from geoformat.conf.error_messages import field_exists

from geoformat.manipulation.feature_manipulation import (
    rename_field_in_feature,
    drop_field_in_feature,
    drop_field_that_not_exists_in_feature
)

from tests.data.features import (
    feature_dpt_data_only_a,
    feature_dpt_geometry_only_a,
    feature_dpt_data_and_geometry_a,
    feature_attributes_only
)

from tests.utils.tests_utils import test_function

rename_field_in_feature_parameters = {
    0: {
        "feature": feature_attributes_only,
        "old_field_name": "field_string_list",
        "new_field_name": "string_list",
        "return_value": {
            'attributes': {'field_integer': 586, 'field_integer_list': [5879, 8557], 'field_real': 8789.97568,
                           'field_real_list': [89798.3654, 8757.97568], 'field_string': 'salut', 'field_none': None,
                           'field_date': datetime.date(2020, 3, 31), 'field_time': datetime.time(11, 22, 10, 999),
                           'field_datetime': datetime.datetime(2020, 3, 31, 11, 22, 10, 999),
                           'field_binary': b'\x00\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01?\xf0\x00\x00\x00\x00\x00\x00?\xf0\x00\x00\x00\x00\x00\x00',
                           'field_boolean': True, 'string_list': ['bonjour', 'monsieur']}},
    },
    1: {
        "feature": feature_attributes_only,
        "old_field_name": "foo",
        "new_field_name": "string_list",
        "return_value": feature_attributes_only,
    },
    3: {
        "feature": feature_attributes_only,
        "old_field_name": "field_string_list",
        "new_field_name": "field_string",
        "return_value": field_exists.format(field_name="field_string"),
    }
}

drop_field_in_feature_parameters = {
    0: {
        "feature": feature_dpt_data_only_a,
        "field_name_or_field_name_list": 'FOO',
        "return_value": feature_dpt_data_only_a
    },
    1: {
        "feature": feature_dpt_data_only_a,
        "field_name_or_field_name_list": ['FOO', 'bar'],
        "return_value": feature_dpt_data_only_a
    },
    2: {
        "feature": feature_dpt_data_only_a,
        "field_name_or_field_name_list": 'CODE_DEPT',
        "return_value": {"attributes": {"NOM_DEPT": "MAYENNE"}}
    },
    3: {
        "feature": feature_dpt_data_only_a,
        "field_name_or_field_name_list": ['CODE_DEPT', 'NOM_DEPT'],
        "return_value": {}
    },
    4: {
        "feature": feature_dpt_geometry_only_a,
        "field_name_or_field_name_list": 'foo',
        "return_value": feature_dpt_geometry_only_a
    },
    5: {
        "feature": feature_dpt_data_and_geometry_a,
        "field_name_or_field_name_list": ['foo', 'BAR'],
        "return_value": feature_dpt_data_and_geometry_a
    },
    6: {
        "feature": feature_dpt_data_and_geometry_a,
        "field_name_or_field_name_list": 'CODE_DEPT',
        "return_value": {
            "attributes": {"NOM_DEPT": "MAYENNE"},
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
        }
    },
    7: {
        "feature": feature_dpt_data_and_geometry_a,
        "field_name_or_field_name_list": ['NOM_DEPT', 'CODE_DEPT'],
        "return_value": {
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
        }
    },
}

drop_field_that_not_exists_in_feature_parameters = {
    0: {
        "feature": feature_dpt_data_only_a,
        "not_deleting_field_name_or_field_name_list": 'FOO',
        "return_value": {}
    },
    1: {
        "feature": feature_dpt_data_only_a,
        "not_deleting_field_name_or_field_name_list": ['CODE_DEPT', 'NOM_DEPT'],
        "return_value": feature_dpt_data_only_a
    },
    2: {
        "feature": feature_dpt_data_only_a,
        "not_deleting_field_name_or_field_name_list": 'NOM_DEPT',
        "return_value": {"attributes": {"NOM_DEPT": "MAYENNE"}}
    },
    3: {
        "feature": feature_dpt_geometry_only_a,
        "not_deleting_field_name_or_field_name_list": 'foo',
        "return_value": feature_dpt_geometry_only_a
    },
    4: {
        "feature": feature_dpt_data_and_geometry_a,
        "not_deleting_field_name_or_field_name_list": 'NOM_DEPT',
        "return_value": {
            "attributes": {"NOM_DEPT": "MAYENNE"},
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
        }
    },
}


def test_all():
    # rename_field_in_feature
    print(test_function(rename_field_in_feature, rename_field_in_feature_parameters))

    # drop_field_in_feature
    print(test_function(drop_field_in_feature, drop_field_in_feature_parameters))

    # drop_field_in_feature
    print(test_function(drop_field_that_not_exists_in_feature, drop_field_that_not_exists_in_feature_parameters))


if __name__ == '__main__':
    drop_field_that_not_exists_in_feature(**{        "feature": feature_dpt_data_only_a,
        "not_deleting_field_name_or_field_name_list": 'FOO',})
    test_all()
