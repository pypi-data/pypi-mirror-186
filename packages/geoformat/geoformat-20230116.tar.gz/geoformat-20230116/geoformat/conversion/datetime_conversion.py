def format_datetime_object_to_str_value(datetime_value, format=['year', 'month', 'day']):
    """
    reformat to string value a datetime object you can choose an output pattern with format option parameter.

    :param datetime_value:
    :param format:
    :return:
    """

    if isinstance(format, str):
        format = [format]

    return_value = ''
    for v in format:
        if v == 'year':
            return_value += str(datetime_value.year).zfill(4)
        elif v == "month":
            return_value += str(datetime_value.month).zfill(2)
        elif v == "day":
            return_value += str(datetime_value.day).zfill(2)
        elif v == "hour":
            return_value += str(datetime_value.hour).zfill(2)
        elif v == "second":
            return_value += str(datetime_value.second).zfill(2)
        elif v == "microsecond":
            return_value += str(datetime_value.microsecond).zfill(6)
        else:
            raise Exception()

    return return_value
