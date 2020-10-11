from unittest.mock import Mock

import pytest

from libpythongian import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    a_url = 'https://avatars1.githubusercontent.com/u/69526289?v=4'
    resp_mock.json.return_value = {
        'login': 'gvaresi', 'id': 69526289,
        'avatar_url': a_url,
    }
    get_mock = mocker.patch('libpythongian.github_api.requests.get')
    get_mock.return_value = resp_mock
    return a_url


def teste_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('gvaresi')
    assert avatar_url == url


def teste_buscar_avatar_integracao():
    url = github_api.buscar_avatar('Gian-Varesi')
    assert 'https://avatars0.githubusercontent.com/u/72698241?v=4' == url
