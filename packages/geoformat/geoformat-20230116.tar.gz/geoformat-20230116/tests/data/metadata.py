from tests.data.fields_metadata import (
    geolayer_data_fields_metadata_complete,
    geolayer_attributes_only_fields_metadata,
)

metadata_fr_dept_data_and_geometry = {
    "name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
    "fields": geolayer_data_fields_metadata_complete,
    "geometry_ref": {"type": {"MultiPolygon", "Polygon"}, "crs": 2154},
}

metadata_fr_dept_data_only = {
    "name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_ONLY",
    "fields": geolayer_data_fields_metadata_complete,
}

metadata_fr_dept_geometry_only = {
    "name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_GEOMETRY_ONLY",
    "geometry_ref": {
        "type": {"MultiPolygon", "Polygon"},
        "extent": (124277.0, 6050136.0, 1242213.0, 7110430.0),
        "crs": 2154,
    },
}

metadata_fr_dept_population = {
    "name": "dept_population",
    "fields": {
        "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
        "INSEE_REG": {"type": "String", "width": 2, "index": 1},
        "POPULATION": {"type": "Integer", "index": 2},
        "AREA": {"type": "Real", "width": 7, "precision": 2, "index": 3},
        "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 4},
    },
}

metadata_fr_dept_population_geometry = {
    "name": "FRANCE_DPT_WITH_POPULATION",
    "fields": {
        "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
        "NOM_DEPT": {"type": "String", "width": 23, "index": 1},
        "POPULATION": {"type": "Integer", "index": 2},
        "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 3},
    },
    "geometry_ref": {"type": {"Polygon", "MultiPolygon"}, "crs": 2154},
}

metadata_fr_dept_population_geometry_right = {
    "name": "fr_dept_data_and_geometry_right_join_fr_dept_population",
    "fields": {
        "POPULATION": {"type": "Integer", "index": 0},
        "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 1},
        "CODE_DEPT": {"type": "String", "width": 2, "index": 2},
        "NOM_DEPT": {"type": "String", "width": 23, "index": 3},
    },
    "geometry_ref": {"type": {"Polygon", "MultiPolygon"}, "crs": 2154},
}

metadata_paris_velib = {
    "name": "geolayer_paris_velib",
    "fields": {
        "Identifiant station": {"type": "Integer", "index": 0},
        "Nom station": {"type": "String", "width": 45, "index": 1},
        "Station en fonctionnement": {"type": "String", "width": 3, "index": 2},
        "Capacité de la station": {"type": "Integer", "index": 3},
        "Nombre bornettes libres": {"type": "Integer", "index": 4},
        "Nombre total vélos disponibles": {"type": "Integer", "index": 5},
        "Vélos mécaniques disponibles": {"type": "Integer", "index": 6},
        "Vélos électriques disponibles": {"type": "Integer", "index": 7},
        "Borne de paiement disponible": {"type": "String", "width": 3, "index": 8},
        "Retour vélib possible": {"type": "String", "width": 3, "index": 9},
        "Actualisation de la donnée": {"type": "DateTime", "index": 10},
        "Coordonnées géographiques": {
            "type": "RealList",
            "width": 13,
            "precision": 11,
            "index": 11,
        },
        "Nom communes équipées": {"type": "String", "width": 20, "index": 12},
    },
}

metadata_attributes_to_force_in_str = {
    "name": "attributes_to_force_only_forced",
    "fields": {
        "field_integer": {"type": "Real", "width": 9, "precision": 5, "index": 0},
        "field_integer_list": {"type": "String", "width": 13, "index": 1},
        "field_real": {"type": "String", "width": 7, "index": 2},
        "field_real_list": {"type": "String", "width": 19, "index": 3},
        "field_string": {"type": "String", "width": 26, "index": 4},
        "field_date": {"type": "Date", "index": 5},
        "field_time": {"type": "String", "width": 15, "index": 6},
        "field_binary": {"type": "String", "width": 201, "index": 7},
        "field_boolean": {"type": "String", "width": 5, "index": 8},
        "field_string_list": {"type": "String", "width": 16, "index": 9},
        "field_datetime": {"type": "DateTime", "index": 10},
    },
}

metadata_attributes_only = {
    "name": "attributes_only",
    "fields": geolayer_attributes_only_fields_metadata,
}

metadata_geometry_only_all_geometries_type = {
    "name": "all_geometry_type_only",
    "geometry_ref": {
        "type": {
            "Point",
            "LineString",
            "Polygon",
            "MultiPoint",
            "MultiLineString",
            "MultiPolygon",
            "GeometryCollection",
        },
        "crs": 4326,
    },
}

metadata_geometry_2d = {
    "name": 'geolayer_geometry',
    "geometry_ref": {"type": {"GeometryCollection"}}
}

metadata_geometry_3d = {
    "name": 'geolayer_geometry',
    "geometry_ref": {"type": {"GeometryCollection25D"}}
}

metadata_paris_tokyo = {
    "name": "paris_tokyo",
    "fields": {
        "name": {"type": "String", "width": 5, "index": 0},
        "country": {"type": "String", "width": 6, "index": 1},
    },
    "geometry_ref": {
        "type": {"Point"},
    },
}