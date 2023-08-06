from geoformat import print_metadata_field_table


def compare_geolayer(geolayer_a, geolayer_b, metadata_only=False):

    # compare this two version
    geolayer_a_metadata = print_metadata_field_table(geolayer_a)
    geolayer_b_metadata = print_metadata_field_table(geolayer_b)


    print('FIELDS METADATA')

    metadata_list = [geolayer_a_metadata, geolayer_b_metadata]
    lines = [metadata_list[i].splitlines() for i in range(len(metadata_list))]
    for l in zip(*lines):
        print(*l, sep='\t')

    if metadata_only is False:
        print('FEATURES')
        for i_feat in geolayer_a['features']:
            geolayer_a_feature = geolayer_a['features'].get(i_feat)
            geolayer_b_feature = geolayer_b['features'].get(i_feat, {})
            if geolayer_a_feature != geolayer_b_feature:
                if geolayer_a_feature.get('attributes') != geolayer_b_feature.get('attributes'):
                    print(i_feat, 'attributes_diff')
                    print('\t', geolayer_a_feature.get('attributes'))
                    print('\t', geolayer_b_feature.get('attributes'))
                if geolayer_a_feature.get('geometry') != geolayer_b_feature.get('geometry'):
                    print(i_feat, 'geometry_diff')
                    print('\t', geolayer_a_feature.get('geometry'))
                    print('\t', geolayer_b_feature.get('geometry'))
