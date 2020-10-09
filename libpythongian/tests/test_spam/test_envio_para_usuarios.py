from unittest.mock import Mock

import pytest
# from libpythongian.spam.enviador_de_email import Enviador
from libpythongian.spam.main import Enviador_de_Spam
from libpythongian.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Gian', email='gian@remotesystem.com.br'),
            Usuario(nome='Varesi', email='adm@remotesystem.com.br')
        ],
        [
            Usuario(nome='Gian', email='gian@remotesystem.com.br')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = Enviador_de_Spam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'adm@remotesystem.com.br',
        'Arrumamos a sua infraestrutura',
        'Entre em contato e saiba mais sobre nossos seviços'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gian', email='gian@remotesystem.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = Enviador_de_Spam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'info@remotesystem.com.br',
        'Arrumamos a sua infraestrutura',
        'Entre em contato e saiba mais sobre nossos seviços'
    )

    enviador.enviar.assert_called_once_with(
        'info@remotesystem.com.br',
        'gian@remotesystem.com.br',
        'Arrumamos a sua infraestrutura',
        'Entre em contato e saiba mais sobre nossos seviços'
    )
