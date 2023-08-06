import copy
import datetime
import sys

from geoformat.conf.error_messages import python_inferior_to_3_7_forbidden
from geoformat.conf.fields_variable import (
    geoformat_field_type_to_python_type,
    recast_black_list,
    none_value_pattern
)
from geoformat.conf.format_data import (
    value_to_iterable_value,
    is_hexadecimal
)


def update_field_index(fields_metadata, field_name, new_index):
    """
    This function allow to change field's index position.
    
    :param fields_metadata: geolayer fields metadata
    :param field_name: field_name that we want to re index
    :param new_index: new index
    :return: fields_metadata updated
    """
    output_fields_metadata = copy.deepcopy(fields_metadata)
    # check if field exists in output_fields_metadata
    if field_name in output_fields_metadata:
        # if "index" key is in output_fields_metadata
        if 'index' in output_fields_metadata[field_name]:
            field_name_original_index = output_fields_metadata[field_name]['index']
        # if not we create it
        else:
            for i_field, field_name_in_metadata in enumerate(output_fields_metadata):
                output_fields_metadata[field_name_in_metadata]['index'] = int(i_field)
                if field_name_in_metadata == field_name:
                    field_name_original_index = i_field

        if new_index != field_name_original_index:
            # check if new index is superior or equal than 0
            if new_index >= 0:
                # check if new index is not superior than existing
                if new_index < len(output_fields_metadata):
                    for i_field, (field_name_in_metadata, field_metadata) in enumerate(output_fields_metadata.items()):
                        # get index value for field_name_in_metadata / create it if not exists
                        field_name_in_metadata_idx = field_metadata['index']

                        # update index for field name
                        if field_name_in_metadata == field_name:
                            output_fields_metadata[field_name_in_metadata]['index'] = new_index
                        else:
                            # re index other fields
                            # minus index when field index is between field_name_original_index and new_index
                            if field_name_original_index < field_name_in_metadata_idx <= new_index:
                                output_fields_metadata[field_name_in_metadata]['index'] -= 1
                                field_name_in_metadata_idx -= 1

                            # plus indexes when field index is between new_index and field_name_original_index
                            if new_index <= field_name_in_metadata_idx < field_name_original_index:
                                output_fields_metadata[field_name_in_metadata]['index'] += 1
                else:
                    raise Exception('new index filed name cannot be superior to {nb_fields}'.format(
                        nb_fields=len(output_fields_metadata) - 1))
            else:
                raise Exception('new index for field name {field_name} must be superior or equal than 0'.format(
                    field_name=field_name))
    else:
        raise Exception('field name {field_name} not exists'.format(field_name=field_name))

    return output_fields_metadata


def recast_field_value(
    field_value,
    recast_value_to_python_type,
    resize_value_width,
    resize_value_precision,
    none_value_pattern=none_value_pattern
):
    """
    Recast a typed value (field_value) to another typed (recast_to_type) value.

    :param field_value: field value in feature
    :param recast_value_to_python_type: recast field_value to python type
    :param resize_value_width: new width for value
    :param resize_value_precision: new precision for value
    :param none_value_pattern: set of values that can be considered as None (usefull when you convert format from a
    driver to another).
    :return: recast value
    """

    python_type = recast_value_to_python_type
    collection_type = None

    if isinstance(recast_value_to_python_type, tuple):
        python_type, collection_type = recast_value_to_python_type

    # check if result must be return in list or not
    return_to_list = False
    if collection_type is not None:
        # if value is not None
        if not isinstance(field_value, list):
            if field_value not in none_value_pattern:
                return_to_list = True
        else:
            return_to_list = True

    # put value in list
    if isinstance(field_value, list):
        field_value_list = field_value
        if collection_type is None:
            field_value_list = [python_type(field_value)]
    else:
        field_value_list = [field_value]

    for i_value, field_value in enumerate(field_value_list):
        field_value_type = type(field_value)
        # if value is a list we iterate overt it
        if field_value_type == list:
            field_value_list[i_value] = recast_field_value(
                field_value=field_value,
                recast_value_to_python_type=recast_value_to_python_type,
                resize_value_width=resize_value_width,
                resize_value_precision=resize_value_precision,
                none_value_pattern=none_value_pattern
            )
        else:
            # we cannot retype a None value
            if field_value not in none_value_pattern:
                # recast value
                if field_value_type != python_type:
                    # recast bytes
                    if python_type is bytes and field_value_type is str:
                        # if field_value is hexadecimal we convert it to bytes
                        if is_hexadecimal(field_value):
                            field_value = bytes.fromhex(field_value)
                        else:
                            field_value = eval(field_value)
                    elif python_type is str and field_value_type is bytes:
                        # recast bytes to hexadecimal string
                        field_value = field_value.hex()
                    # recast date, time datetime value
                    elif python_type in {datetime.date, datetime.time,
                                                         datetime.datetime} and field_value_type is str:
                        if sys.version_info >= (3, 7):
                            field_value = python_type.fromisoformat(field_value)
                        else:
                            raise Exception(python_inferior_to_3_7_forbidden)
                    elif python_type is datetime.date and field_value_type is datetime.datetime:
                        field_value = field_value.date()
                    elif python_type is datetime.time and field_value_type is datetime.datetime:
                        field_value = field_value.time()
                    elif python_type is datetime.datetime and field_value_type is datetime.date:
                        field_value = datetime.datetime.combine(field_value, datetime.time.min)
                    # recast boolean
                    elif python_type is bool and field_value_type is str and field_value.upper() == 'FALSE':
                        field_value = False
                    # recast str None value
                    elif field_value_type is str and field_value == '':
                        field_value = None
                    else:
                        try:
                            field_value = python_type(field_value)
                        except ValueError:
                            raise ValueError('value : {field_value} is not compatible with '
                                             '{python_type} type'.format(
                                field_value=field_value,
                                python_type=python_type)
                            )

                # change precision
                if python_type == float and resize_value_precision and field_value:
                    field_value = round(field_value, resize_value_precision)
                # change width
                if python_type in {str, float} and resize_value_width:
                    if field_value is not None:
                        if python_type is float:
                            field_value = str(field_value)
                            resize_value_width += 1  # add comma width
                        field_value = field_value[:resize_value_width]
                        if python_type is float:
                            field_value = float(field_value)
            else:
                field_value = None

            # save value
            field_value_list[i_value] = field_value

    if return_to_list:
        output_value = field_value_list
    else:
        output_value = field_value_list[0]

    return output_value


def recast_field(
    geolayer_to_recast,
    field_name_to_recast,
    recast_to_geoformat_type=None,
    rename_to=None,
    resize_width=None,
    resize_precision=None,
    reindex=None,
    none_value_pattern=none_value_pattern
):
    """
    This function allow to recast a field.

    :param geolayer_to_recast: geolayer that you want to recast
    :param field_name_to_recast: field name that we want to recast
    :param recast_to_geoformat_type: if you want to change field type enter a new field type
    :param rename_to: if you want rename field enter new field name
    :param resize_width: if you want to resize width enter new width
    :param resize_precision: if you want to change field precision enter new precision
    :param reindex: if you want to change field index position enter new index.
    :param none_value_pattern: set of values that can be considered as None (usefull when you convert format from a
    driver to another).
    :return: field recasted on geolayer
    """

    # update metadata
    geolayer_to_recast = copy.deepcopy(geolayer_to_recast)
    input_field_metadata = geolayer_to_recast['metadata']['fields'][field_name_to_recast]
    input_field_type = input_field_metadata['type']
    # check if recasting is compatible with actual type
    if recast_to_geoformat_type in recast_black_list[input_field_type]:
        raise Exception("Input type {input_type} cannot recast to {recast_type} type".format(
            input_type=input_field_type,
            recast_type=recast_to_geoformat_type
        ))

    if recast_to_geoformat_type is not None:
        output_field_metadata = {'type': recast_to_geoformat_type}
    else:
        output_field_metadata = {'type': input_field_metadata['type']}

    # width
    if output_field_metadata['type'] in {'Real', 'RealList', 'String', 'StringList'}:
        if resize_width is not None:
            output_field_metadata['width'] = resize_width
        else:
            if "width" in input_field_metadata:
                output_field_metadata['width'] = input_field_metadata['width']
                # if we swap from Real to String  because of the comma width must take +1
                if 'Real' in input_field_metadata['type'] and 'String' in output_field_metadata['type']:
                    output_field_metadata['width'] += 1
                resize_width = output_field_metadata['width']
            else:
                raise Exception("resize_width must be filled for type : {data_type}".format(
                    data_type=output_field_metadata['type']))

    # precision
    if output_field_metadata['type'] in {'Real', 'RealList'}:
        if resize_precision is not None:
            output_field_metadata['precision'] = resize_precision
        else:
            if "precision" in input_field_metadata:
                output_field_metadata['precision'] = input_field_metadata['precision']
                resize_precision = output_field_metadata['precision']
            else:
                raise Exception(
                    "resize_precision must be filled for {data_type} type".format(
                        data_type=output_field_metadata['type']))

    # add index if exists
    if 'index' in input_field_metadata:
        output_field_metadata['index'] = input_field_metadata['index']

    # write output metadata in geolayer_to_recast
    if input_field_metadata != output_field_metadata:
        geolayer_to_recast['metadata']['fields'][field_name_to_recast] = output_field_metadata

    # re index
    if reindex is not None:
        output_fields_metadata = update_field_index(
            fields_metadata=geolayer_to_recast['metadata']['fields'],
            field_name=field_name_to_recast,
            new_index=reindex
        )
        geolayer_to_recast['metadata']['fields'] = output_fields_metadata

    # rename field in metadata
    if rename_to is not None:
        if rename_to in geolayer_to_recast['metadata']['fields']:
            raise Exception('field {rename_to} still exists on geolayer'.format(rename_to=rename_to))
        if rename_to != field_name_to_recast:
            geolayer_to_recast['metadata']['fields'][rename_to] = geolayer_to_recast['metadata']['fields'][
                field_name_to_recast]
            del geolayer_to_recast['metadata']['fields'][field_name_to_recast]

    # define python type to recast
    recast_to_python_type = geoformat_field_type_to_python_type[output_field_metadata['type']]

    # value in list or not
    if output_field_metadata['type'] in {'IntegerList', 'RealList', 'StringList'}:
        in_list = True
    else:
        in_list = False

    # loop over features
    for i_feat, feature in geolayer_to_recast['features'].items():
        # if attributes in feature
        if 'attributes' in feature:
            if field_name_to_recast in feature['attributes']:
                feature_field_name_value = feature['attributes'][field_name_to_recast]
                feature_field_name_type = type(feature_field_name_value)

                if feature_field_name_type == list:
                    # if value in list and output is not in list we have to recast value in str
                    if in_list is False:
                        feature_field_name_value = str(feature_field_name_value)
                else:
                    if feature_field_name_value in none_value_pattern:
                        feature_field_name_value = None
                    else:
                        # if result must be in list
                        if in_list is True:
                            try:
                                eval_feature_field_name_value = eval(feature_field_name_value)
                                # force eval_feature_field_name_value to be in list type
                                eval_feature_field_name_value = value_to_iterable_value(eval_feature_field_name_value, list)
                            except (TypeError, NameError, ValueError, SyntaxError):
                                eval_feature_field_name_value = [feature_field_name_value]
                            # put value in list in any case
                            if isinstance(eval_feature_field_name_value, list):
                                feature_field_name_value = eval_feature_field_name_value
                            else:
                                feature_field_name_value = [eval_feature_field_name_value]

                # recast value(s)
                feature_field_name_value = recast_field_value(
                    field_value=feature_field_name_value,
                    recast_value_to_python_type=recast_to_python_type,
                    resize_value_width=resize_width,
                    resize_value_precision=resize_precision,
                    none_value_pattern=none_value_pattern
                )

                # saving recasting data
                feature['attributes'][field_name_to_recast] = feature_field_name_value

                # update field_name change
                if rename_to is not None:
                    feature['attributes'][rename_to] = feature['attributes'][field_name_to_recast]
                    del feature['attributes'][field_name_to_recast]

    return geolayer_to_recast
