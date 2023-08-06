from orderlyweb_api.result_models import VersionDetails

test_result = VersionDetails({
    'date': '2018-10-11T10:57:02Z',
    'description': 'desc',
    'display_name': 'display',
    'id': '20181011-105702-1e08a5be',
    'name': 'minimal',
    'published': False,
    'artefacts':
        [
            {'format': 'STATICGRAPH',
             'description': 'graph',
             'files': []
             }
        ],
    'resources': [],
    'data_info':
        [
            {'name': 'dat',
             'csv_size': 801,
             'rds_size': 583
             }
        ],
    'parameter_values': {'key': 'value'}
})


def test_version_details():
    assert test_result.id == '20181011-105702-1e08a5be'
    assert test_result.name == 'minimal'
    assert test_result.description == 'desc'
    assert test_result.display_name == 'display'
    assert test_result.published is False
    assert test_result.date == '2018-10-11T10:57:02Z'
    assert test_result.artefacts == [
        {
            'format': 'STATICGRAPH',
            'description': 'graph',
            'files': []
        }
    ]
    assert test_result.resources == []
    assert test_result.data_info == [
        {
            'name': 'dat',
            'csv_size': 801,
            'rds_size': 583
        }
    ]
    assert test_result.parameter_values == {'key': 'value'}
