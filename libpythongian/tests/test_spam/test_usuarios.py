from libpythongian.spam.modelos import Usuario


def test_salvar_usuarios(sessao):
    usuario = Usuario(nome='Gian', email='gian@remotesystem.com.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Gian', email='gian@remotesystem.com.br'),
        Usuario(nome='Varesi', email='gian@remotesystem.com.br')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
