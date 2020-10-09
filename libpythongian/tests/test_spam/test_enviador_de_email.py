import pytest

from libpythongian.spam.enviador_de_email import Enviador, Email_Invalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['gian@remotsystem.com.br',
     'adm@remotesystem.com.br']
)
def test_remetente_01(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'varesi@ig.com.br',
        'Envio de email padrao',
        'Enviando email em lote.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['1', 'adm.remotesystem.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    with pytest.raises(Email_Invalido):
        enviador.enviar(
            remetente,
            'varesi@ig.com.br',
            'Envio de email padrao',
            'Enviando email em lote.'
        )
