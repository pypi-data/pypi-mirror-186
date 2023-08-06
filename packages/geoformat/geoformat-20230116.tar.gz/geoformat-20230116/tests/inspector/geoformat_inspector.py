from pathlib import Path
import inspect
import importlib.util
import sys


class GeoformatInspector:
    module_without_test = {
        "geoformat/conf/decorator.py",
        "geoformat/conf/driver_variable.py",
        "geoformat/conf/error_messages.py",
        "geoformat/conf/fields_variable.py",
        "geoformat/conf/geometry_variable.py",
        "geoformat/conf/geoformat_var.py",
        "geoformat/conf/proj_var.py",
        "geoformat/conf/timer.py",
        "geoformat/db/db_request.py",
        "geoformat/driver/ogr/ogr_driver.py",
        "geoformat/driver/common_driver.py",
        "geoformat/explore_data/random_geometry.py",
    }

    function_deprecated = {"clause_where_combination"}

    # list function that are not necessary in geoformat __init__.py
    # the reason why these functions are not in the init are :
    #  - function is a geoformat inside work function (function is useless for basic geoformat working)
    function_not_in_init = {
        "value_to_iterable_value",
        "verify_input_path_is_file",
        "verify_input_path_is_dir",
        "verify_input_path_is_http",
        "path_is_file",
        "path_is_dir",
        "path_is_http",
        "open_http_path",
        "add_extension_path",
        "path_to_file_path",
        "pairwise",
    }

    duplicate_function_exception = {"test_all"}

    def __init__(self, path="None"):
        self.geoformat_root_path = Path(__file__).parent.parent.parent.joinpath()
        self.geoformat_lib_dir_path = self.geoformat_root_path.joinpath("geoformat")
        self.tests_dir_path = self.geoformat_root_path.joinpath("tests")
        self.tests_geoformat_lib_dir = self.geoformat_root_path.joinpath(
            "tests/geoformat"
        )
        self.function_path_dict = None

    def iterate_over_directory_in_geoformat_module2(self, path):

        for inside_path in path.iterdir():
            if inside_path.is_dir() and inside_path.name != "__pycache__":
                yield inside_path
                for p in self.iterate_over_directory_in_geoformat_module2(
                    path=inside_path
                ):
                    yield p

    def get_relative_path(self, path, origin_path):
        return "/".join(path.parts[len(origin_path.parts) :])

    def get_function_path_dict(self):
        d = {}
        for file_path in self.get_geoformat_py_file_path():
            py_path = self.get_py_path(path=file_path, test=False)
            for function_name in self.from_path_get_function_in_it(path=py_path):
                if function_name not in self.duplicate_function_exception:
                    if function_name in d:
                        print(
                            f"\tthis function {function_name} still exists in geoformat ! May be a duplicate ? Or you just should rename it."
                            f"\n\t\t {function_name} in {d[function_name]}"
                            f"\n\t\t {function_name} in {py_path}"
                        )
                    else:
                        d[function_name] = py_path
        return d

    def get_objects_in_geoformat_module(
        self, geoformat_module_import_path, from_list=None, object_type=None
    ):

        if from_list is None:
            from_list = [None]

        function_set = set()

        try:
            module = __import__(
                name=geoformat_module_import_path,
                locals=None,
                globals=None,
                fromlist=from_list,
                level=0,
            )
            for str_obj in dir(module):
                if not str_obj.startswith("_"):  # exclude function that start to '_'
                    obj = getattr(module, str_obj)

                    write_str_obj = True
                    if object_type:
                        if not isinstance(obj, object_type):
                            write_str_obj = False
                    if write_str_obj is True:
                        function_set.update({str_obj})

        except ModuleNotFoundError:
            pass

        return function_set

    def get_module(self, py_path, locals=None, globals=None, fromlist=[None], level=0):

        try:
            module = __import__(
                name=py_path,
                locals=locals,
                globals=globals,
                fromlist=fromlist,
                level=level,
            )

        except ModuleNotFoundError:
            module = None

        return module

    def is_module_function(self, mod, func):
        return inspect.isfunction(func) and inspect.getmodule(func) == mod

    def module_list_functions(self, mod):
        return [
            func.__name__
            for func in mod.__dict__.values()
            if self.is_module_function(mod, func)
        ]

    def from_path_get_function_in_it(self, path, exclude_underscore_func=False):

        module = self.get_module(py_path=path)
        if module:
            for function_name in self.module_list_functions(mod=module):
                if exclude_underscore_func is True:
                    if not function_name.startswith("_"):
                        yield function_name
                else:
                    yield function_name

    def get_geoformat_py_file_path(self):

        for dir_path in self.iterate_over_directory_in_geoformat_module2(
            path=self.geoformat_lib_dir_path
        ):
            # print('dir_path', dir_path)
            py_path_list = [
                path for path in dir_path.glob("*.py") if path.name != "__init__.py"
            ]
            # print('\t', py_path_list)
            if py_path_list:
                for py_path in py_path_list:
                    relative_path_to_py_path_from_root_path = self.get_relative_path(
                        path=py_path, origin_path=self.geoformat_root_path
                    )
                    yield relative_path_to_py_path_from_root_path

    def get_geoformat_functions(self):
        """scan all py file in geoformat and return functions in it"""
        geoformat_function_to_test_set = set()
        for (
            relative_path_to_py_path_from_root_path
        ) in self.get_geoformat_py_file_path():
            # if path is not in module_without_unit_test
            if relative_path_to_py_path_from_root_path not in self.module_without_test:
                relative_py_path = Path(relative_path_to_py_path_from_root_path)

                # get geoformat functions
                relative_geoformat_lib_py_path_str_for_import = ".".join(
                    relative_py_path.parts
                ).replace(".py", "")
                geoformat_function_to_test_set.update(
                    self.from_path_get_function_in_it(
                        path=relative_geoformat_lib_py_path_str_for_import,
                        exclude_underscore_func=True,
                    )
                )

        return geoformat_function_to_test_set

    def get_tested_geoformat_function(self):

        geoformat_tested_function_set = set()
        for (
            relative_path_to_py_path_from_root_path
        ) in self.get_geoformat_py_file_path():

            # if path is not in module_without_unit_test
            if relative_path_to_py_path_from_root_path not in self.module_without_test:
                relative_py_path = Path(relative_path_to_py_path_from_root_path)

                # get tests functions
                relative_tests_py_path = Path("tests").joinpath(relative_py_path)
                relative_tests_py_path_parts = list(relative_tests_py_path.parts)
                relative_tests_py_path_parts[-1] = (
                    "test_" + relative_tests_py_path_parts[-1]
                )
                relative_tests_py_path_str_for_import = ".".join(
                    relative_tests_py_path_parts
                ).replace(".py", "")
                geoformat_tested_function_set.update(
                    self.get_objects_in_geoformat_module(
                        geoformat_module_import_path=relative_tests_py_path_str_for_import,
                        object_type=dict,
                    )
                )

        # filter and only get variable with suffix
        suffix = "_parameters"
        # recreate original name with test function name
        geoformat_tested_function_set = {
            suffix.join(value.split(suffix)[:-1])
            for value in geoformat_tested_function_set
            if value.endswith(suffix)
        }

        return geoformat_tested_function_set

    def print_done(self, no_error):
        if no_error is True:
            print("Done : All clear !")

    def get_py_path(self, path, test=False):

        if test is True:
            path = Path("tests").joinpath(path)
        else:
            path = Path(path)

        py_path_parts = list(path.parts)

        if test is True:
            py_path_parts[-1] = "test_" + py_path_parts[-1]

        py_path = ".".join(py_path_parts).replace(".py", "")

        return py_path

    def get_functions_in_init(self):
        m = __import__(name="geoformat")
        init_function_set = set(
            [str_obj for str_obj in dir(m) if not str_obj.startswith("_")]
        )

        return init_function_set

    def get_test_py_path(self):

        for (
            relative_path_to_py_path_from_root_path
        ) in self.get_geoformat_py_file_path():
            if relative_path_to_py_path_from_root_path not in self.module_without_test:
                relative_py_path = Path(relative_path_to_py_path_from_root_path)
                relative_tests_py_path_str_for_import = self.get_py_path(
                    path=relative_py_path, test=True
                )
                yield relative_tests_py_path_str_for_import

    def get_test_module_that_not_exists(self):

        for relative_tests_py_path_str_for_import in self.get_test_py_path():
            py_path = (
                relative_tests_py_path_str_for_import.replace(".", "/").replace(
                    "tests/", ""
                )
                + ".py"
            )
            py_path = py_path.split("/")
            py_path[-1] = py_path[-1].replace("test_", "")
            py_path = "/".join(py_path)
            if py_path not in self.module_without_test:
                if (
                    self.get_module(py_path=relative_tests_py_path_str_for_import)
                    is None
                ):
                    yield relative_tests_py_path_str_for_import

    def check_tests_dir_structure(self):
        no_error = True
        # dir_list = iterate_over_directory_in_geoformat_module(p=self.geoformat_lib_dir_path)

        # for dir_path in dir_list:
        for dir_path in self.iterate_over_directory_in_geoformat_module2(
            path=self.geoformat_lib_dir_path
        ):
            relative_dir_path = self.get_relative_path(
                path=dir_path, origin_path=self.geoformat_lib_dir_path
            )
            relativ_part_path = Path(relative_dir_path)
            test_geoformat_lib_dir_path = self.tests_geoformat_lib_dir.joinpath(
                relativ_part_path
            )
            if test_geoformat_lib_dir_path.is_dir() is False:
                print(f"tests dir {relativ_part_path} missing !")
                no_error &= False

        self.print_done(no_error=no_error)
        return no_error

    def check_function_in_init(self):
        no_error = True
        # we make difference between geoformat function and function in init
        missing_function_set = (
            self.get_geoformat_functions() - self.get_functions_in_init()
        )
        # we deduce the functions for which it is not necessary that they appear in the init
        missing_function_set = missing_function_set - self.function_not_in_init

        if missing_function_set:
            if self.function_path_dict is None:
                self.function_path_dict = self.get_function_path_dict()

            missing_by_path_order_dict = {}
            for missing_function in missing_function_set:
                missing_function_py_path = self.function_path_dict.get(missing_function)
                if missing_function_py_path:
                    if missing_function_py_path in missing_by_path_order_dict:
                        missing_by_path_order_dict[missing_function_py_path].append(
                            missing_function
                        )
                    else:
                        missing_by_path_order_dict[missing_function_py_path] = [
                            missing_function
                        ]
                else:
                    raise Exception(
                        f"function : {missing_function} not exists in self.function_path_dict variable. May"
                        f" be this function must be put in self.function_not_in_init variable."
                    )

            # print error
            if missing_by_path_order_dict:
                for missing_function_py_path in sorted(
                    list(missing_by_path_order_dict.keys())
                ):
                    print(f"\tmissing at path : {missing_function_py_path}")
                    for missing_function in missing_by_path_order_dict[
                        missing_function_py_path
                    ]:
                        print(f"\t\tfunction : {missing_function}")
                        no_error &= False

        self.print_done(no_error=no_error)
        return no_error

    def check_tests_function(self):

        no_error = True
        geoformat_function_to_test_set = self.get_geoformat_functions()
        geoformat_tested_function_set = self.get_tested_geoformat_function()

        # make difference to get only not tested function
        not_tested_function_set = (
            geoformat_function_to_test_set - geoformat_tested_function_set
        )
        if not_tested_function_set:
            for not_tested_function_name in not_tested_function_set:
                if not_tested_function_name not in self.function_deprecated:
                    print(f"\tfunction : {not_tested_function_name} must be tested")
                    no_error &= False

        self.print_done(no_error=no_error)
        return no_error

    def check_tests_files_structure(self):

        no_error = True
        for (
            relative_tests_py_path_str_for_import
        ) in self.get_test_module_that_not_exists():

            print(
                f'\ttests file {relative_tests_py_path_str_for_import.replace(".", "/")}.py missing'
            )
            no_error &= False

        self.print_done(no_error=no_error)
        return no_error

    def check_function_name(self):
        no_error = True
        self.function_path_dict = self.get_function_path_dict()
        self.print_done(no_error=no_error)
        return no_error

    def check_if_all_test_module_are_import_in_test_all(self):

        no_error = True
        test_all_path = self.geoformat_root_path.joinpath("test_all.py")
        if not test_all_path.exists():
            raise Exception("test_all.py does not exists")
        spec = importlib.util.spec_from_file_location("test_all", test_all_path)
        foo = importlib.util.module_from_spec(spec)
        sys.modules["module.name"] = foo
        spec.loader.exec_module(foo)

        test_all_py_test_set = {
            test_py for test_py in dir(foo) if test_py.startswith("test_")
        }
        geoformat_test_py_set = {
            test_py_path.split(".")[-1] for test_py_path in self.get_test_py_path()
        }
        test_module_that_not_exists = {
            relative_tests_py_path_str_for_import.split(".")[-1]
            for relative_tests_py_path_str_for_import in self.get_test_module_that_not_exists()
        }
        missing_test_in_test_all = (
            geoformat_test_py_set - test_all_py_test_set - test_module_that_not_exists
        )
        for missing_test in missing_test_in_test_all:
            print(f"\t {missing_test} is not referenced in test_all.py")
            no_error &= False

        self.print_done(no_error=no_error)
        return no_error

    def inspect(self):
        d = {
            "check if function name": {
                "method": self.check_function_name,
                "result": None,
            },
            "check test dir structure": {
                "method": self.check_tests_dir_structure,
                "result": None,
            },
            "check test file structure": {
                "method": self.check_tests_files_structure,
                "result": None,
            },
            "check if function are tested": {
                "method": self.check_tests_function,
                "result": None,
            },
            "check if function are referenced in __init__": {
                "method": self.check_function_in_init,
                "result": None,
            },
            "check if all tests are referenced in test_all.py": {
                "method": self.check_if_all_test_module_are_import_in_test_all,
                "result": None,
            },
        }
        for check_name, check_properties in d.items():
            print(f"####### {check_name}")
            # get method
            method = check_properties["method"]
            # execute method and save result
            check_properties["result"] = method()

        error_list = []
        for check_name, check_properties in d.items():
            if check_properties["result"] is False:
                error_list.append(check_name)

        if error_list:
            error_merge = ", ".join(error_list)
            raise Exception(f"Some check are false : {error_merge}")

        return True


if __name__ == "__main__":
    inspector = GeoformatInspector()
    inspector.inspect()
