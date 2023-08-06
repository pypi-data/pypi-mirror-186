import copy
import pathlib
import types
import warnings
import inspect
import tempfile
import shutil


def test_dependencies():

    try:
        from osgeo import ogr

        import_ogr_success = True
    except ImportError:
        import_ogr_success = False

    try:
        from osgeo import osr

        import_osr_sucess = True
    except ImportError:
        import_osr_sucess = False

    try:
        import psycopg2
        import psycopg2.extras

        import_psycopg2_success = True
    except ImportError:
        import_psycopg2_success = False

    return {
        "ogr": import_ogr_success,
        "osr": import_osr_sucess,
        "psycopg2": import_psycopg2_success,
    }


def print_errors(in_error):
    if in_error:
        sentence = ""
        for error in in_error:
            (id_parameters, error_message, returned_values) = error
            sentence += "\tThe parameters #{} returned errors: \n".format(id_parameters)
            sentence += "\t\t" + error_message + "\n"
            sentence += "\t\t" + returned_values + "\n"
        return sentence
    else:
        return False


def _get_function_value(exec, param):
    try:
        if type(param) is dict:
            result_value = exec(**param)
        else:
            result_value = exec(param)
    except Exception as e:
        result_value = e.__str__()

    return result_value


def _check_path(result_value, return_value):
    if isinstance(return_value, tuple):
        path_in_tuple = False
        if return_value:

            if isinstance(return_value[0], pathlib.Path):
                if len(return_value) == 2 and return_value[1] == "check":
                    if return_value[0].is_file():
                        result_value = return_value
                else:
                    path_in_tuple = True
                    result_value = []
                    for value in return_value:
                        result_value.append(
                            _check_path(result_value=result_value, return_value=value)
                        )
                    result_value = tuple(result_value)

        # if tuple is not composed of path we skip this test
        if path_in_tuple is False:
            return result_value
    else:
        if return_value.is_file():
            result_value = return_value
        else:
            result_value = f"file {return_value} not found"

    return result_value


def _compare_return_value_and_function_value(
    id_parameters, in_error, function, parameters, return_value
):
    # execute function
    function_value = _get_function_value(exec=function, param=parameters)
    in_error = inspect_result_value(
        id_parameters=id_parameters,
        in_error=in_error,
        return_value=return_value,
        function_value=function_value,
    )

    return in_error


def inspect_result_value(id_parameters, in_error, return_value, function_value):

    # if result_value is different from return_value we check specific cases
    if function_value != return_value:
        if isinstance(return_value, (list, tuple)) and isinstance(
            function_value, (list, tuple)
        ):
            for i, i_return_value in enumerate(return_value):
                i_function_value = function_value[i]
                in_error = inspect_result_value(
                    id_parameters, in_error, i_return_value, i_function_value
                )
        else:
            # test return class object
            if inspect.isclass(return_value):
                if isinstance(function_value, return_value):
                    function_value = return_value

            if isinstance(function_value, tempfile._TemporaryFileWrapper):
                with open(function_value.name, "r") as function_data:
                    if function_data.read() == return_value:
                        function_value = return_value

            # if return is a generator we transform it to tuple
            elif isinstance(function_value, types.GeneratorType):
                function_value = _get_function_value(exec=tuple, param=function_value)

            elif isinstance(function_value, zip):
                function_value = _get_function_value(exec=list, param=function_value)

            # TODO FIX IT
            # check path
            # if return value is a path we just verify if file exists
            elif isinstance(return_value, (pathlib.Path, tuple)):
                function_value = _check_path(
                    result_value=function_value, return_value=return_value
                )

            if test_dependencies()["ogr"]:
                from osgeo import ogr

                if isinstance(function_value, ogr.Geometry):
                    if function_value.Equals(return_value):
                        function_value = True

            # exception for ogr geometries
            if test_dependencies()["ogr"]:
                from osgeo import ogr

                if function_value is True:
                    return_value = True

            if function_value != return_value:
                in_error.append(
                    (
                        id_parameters,
                        "ERROR: return value must be {return_value}".format(
                            return_value=return_value
                        ),
                        "ERROR: function return this {result_value}".format(
                            result_value=function_value
                        ),
                    )
                )

    return in_error


def test_function(function, test_parameters):

    in_error = []
    test_parameters_copy = copy.deepcopy(test_parameters)
    for id_parameters, parameters in test_parameters_copy.items():
        return_value = parameters["return_value"]
        del parameters["return_value"]

        in_error = _compare_return_value_and_function_value(
            id_parameters=id_parameters,
            in_error=in_error,
            function=function,
            parameters=parameters,
            return_value=return_value,
        )

    error_value = print_errors(in_error)
    if error_value:
        sentence = "{function_name} KO\n".format(function_name=function.__name__)
        sentence += error_value
        warnings.warn(sentence)
    else:
        sentence = "{function_name} OK".format(function_name=function.__name__)

    return sentence


def create_test_dir(file_path_base, test_dir_path):
    # create test dir
    dir_test_path = file_path_base(test_dir_path)
    if not dir_test_path.exists():
        dir_test_path.mkdir()

    return dir_test_path


def delete_test_dir(dir_test_path):
    shutil.rmtree(path=dir_test_path)
