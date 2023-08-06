from pathlib import Path

from tests.utils.tests_utils import test_function

from geoformat.conf.path import (
    add_extension_path,
    path_to_file_path,
    path_is_file,
    verify_input_path_is_file,
    path_is_http,
    verify_input_path_is_http,
    path_is_dir,
    path_not_a_dir,
    verify_input_path_is_dir,
    open_http_path,
)

from geoformat.conf.error_messages import (
    path_not_valid,
    path_http_not_valid,
    path_not_http,
)
from http.client import HTTPResponse

add_extension_path_parameters = {
    0: {
        "path": Path("data/geojson/test"),
        "add_extension": None,
        "return_value": Path("data/geojson/test"),
    },
    1: {
        "path": Path("data/geojson/test"),
        "add_extension": ".geojson",
        "return_value": Path("data/geojson/test.geojson"),
    },
    2: {
        "path": Path("data/geojson/test.geojson"),
        "add_extension": ".kml",
        "return_value": Path("data/geojson/test.geojson.kml"),
    },
}

path_is_file_parameters = {
    0: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath(
            "geoformat/conf/path.py"
        ),
        "return_value": True,
    },
    1: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath("geoformat/conf"),
        "return_value": False,
    },
    2: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath("geoformat/foo"),
        "return_value": False,
    },
}

verify_input_path_is_file_parameters = {
    0: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath(
            "geoformat/conf/path.py"
        ),
        "return_value": Path(__file__).parent.parent.parent.parent.joinpath(
            "geoformat/conf/path.py"
        ),
    },
    1: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath("geoformat/conf"),
        "return_value": path_not_valid.format(
            path=Path(__file__).parent.parent.parent.parent.joinpath("geoformat/conf")
        ),
    },
    2: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath("geoformat/foo"),
        "return_value": path_not_valid.format(
            path=Path(__file__).parent.parent.parent.parent.joinpath("geoformat/foo")
        ),
    },
}

open_http_path_parameters = {
    0: {
        "path": "https://foo/bar",
        "headers": None,
        "return_value": "<urlopen error [Errno -2] Name or service not known>",
    },
    1: {
        "path": "https://france-geojson.gregoiredavid.fr/repo/regions.geojson",
        "headers": None,
        "return_value": HTTPResponse,
    },
}

path_is_http_parameters = {
    0: {
        "path": "https://france-geojson.gregoiredavid.fr/repo/regions.geojson",
        "headers": None,
        "return_value": (True, 200),
    },
    1: {
        "path": "https://datahub.io/core/geo-countries/r/countries.geojson",
        "headers": None,
        "return_value": (True, 200),
    },
    2: {
        "path": "https://france-geojson.gregoiredavid.fr/repo/toto.geojson",
        "headers": None,
        "return_value": (False, 404),
    },
    3: {
        "path": "https://foo/bar",
        "headers": None,
        "return_value": (False, 404),
    },
    4: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath(
            "geoformat/conf/path.py"
        ),
        "headers": None,
        "return_value": (False, None),
    },
}

path_is_dir_parameters = {
    0: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath(
            "geoformat/conf/path.py"
        ),
        "return_value": False,
    },
    1: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath("geoformat/conf"),
        "return_value": True,
    },
    2: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath("geoformat/foo"),
        "return_value": False,
    },
}

verify_input_path_is_dir_parameters = {
    0: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath(
            "geoformat/conf/path.py"
        ),
        "return_value": path_not_a_dir.format(
            path=Path(__file__).parent.parent.parent.parent.joinpath(
                "geoformat/conf/path.py"
            )
        ),
    },
    1: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath("geoformat/conf"),
        "return_value": Path(__file__).parent.parent.parent.parent.joinpath(
            "geoformat/conf"
        ),
    },
    2: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath("geoformat/foo"),
        "return_value": path_not_a_dir.format(
            path=Path(__file__).parent.parent.parent.parent.joinpath("geoformat/foo")
        ),
    },
}

verify_input_path_is_http_parameters = {
    0: {
        "path": "https://france-geojson.gregoiredavid.fr/repo/regions.geojson",
        "headers": None,
        "return_value": "https://france-geojson.gregoiredavid.fr/repo/regions.geojson",
    },
    1: {
        "path": "https://datahub.io/core/geo-countries/r/countries.geojson",
        "headers": None,
        "return_value": "https://datahub.io/core/geo-countries/r/countries.geojson",
    },
    2: {
        "path": "https://france-geojson.gregoiredavid.fr/repo/toto.geojson",
        "headers": None,
        "return_value": path_http_not_valid.format(
            path="https://france-geojson.gregoiredavid.fr/repo/toto.geojson", code=404
        ),
    },
    3: {
        "path": "https://foo/bar",
        "headers": None,
        "return_value": path_http_not_valid.format(path="https://foo/bar", code=404),
    },
    4: {
        "path": Path(__file__).parent.parent.parent.parent.joinpath(
            "geoformat/conf/path.py"
        ),
        "headers": None,
        "return_value": path_not_http.format(
            path=Path(__file__).parent.parent.parent.parent.joinpath(
                "geoformat/conf/path.py"
            )
        ),
    },
}

path_to_file_path_parameters = {
    0: {
        "path": Path(__file__).parent.parent.parent.joinpath("data").as_posix(),
        "geolayer_name": "test",
        "overwrite": True,
        "add_extension": None,
        "return_value": Path(__file__).parent.parent.parent.joinpath("data/test"),
    },
    1: {
        "path": Path(__file__).parent.parent.parent.joinpath("data/test").as_posix(),
        "geolayer_name": "test",
        "overwrite": True,
        "add_extension": None,
        "return_value": Path(__file__).parent.parent.parent.joinpath("data/test"),
    },
    2: {
        "path": Path(__file__).parent.parent.parent.joinpath("data/test").as_posix(),
        "geolayer_name": "test",
        "overwrite": True,
        "add_extension": ".geojson",
        "return_value": Path(__file__).parent.parent.parent.joinpath(
            "data/test.geojson"
        ),
    },
    3: {
        "path": Path(__file__).parent.parent.parent.joinpath("data"),
        "geolayer_name": "test",
        "overwrite": True,
        "add_extension": None,
        "return_value": Path(__file__).parent.parent.parent.joinpath("data/test"),
    },
    4: {
        "path": Path(__file__).parent.parent.parent.joinpath("data/test"),
        "geolayer_name": "test",
        "overwrite": True,
        "add_extension": None,
        "return_value": Path(__file__).parent.parent.parent.joinpath("data/test"),
    },
    5: {
        "path": Path(__file__).parent.parent.parent.joinpath("data/test"),
        "geolayer_name": "test",
        "overwrite": True,
        "add_extension": ".geojson",
        "return_value": Path(__file__).parent.parent.parent.joinpath(
            "data/test.geojson"
        ),
    },
}


def test_all():

    # add_extension_path
    print(test_function(add_extension_path, add_extension_path_parameters))

    # path_is_file
    print(test_function(path_is_file, path_is_file_parameters))

    # verify_input_path_is_file
    print(
        test_function(verify_input_path_is_file, verify_input_path_is_file_parameters)
    )

    # open_http_path
    print(test_function(open_http_path, open_http_path_parameters))

    # path_is_http
    print(test_function(path_is_http, path_is_http_parameters))

    # path_is_dir
    print(test_function(path_is_dir, path_is_dir_parameters))

    # verify_input_path_is_dir
    print(test_function(verify_input_path_is_dir, verify_input_path_is_dir_parameters))

    # verify_input_path_is_http
    print(
        test_function(verify_input_path_is_http, verify_input_path_is_http_parameters)
    )

    # path_to_file_path
    print(test_function(path_to_file_path, path_to_file_path_parameters))


if __name__ == "__main__":
    test_all()
