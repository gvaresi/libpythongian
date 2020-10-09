class Enviador:

    def enviar(self, remetente, destinatario, assunto, mensagem):
        if '@' not in remetente:
            raise Email_Invalido(f'Email de remetente invalido: {remetente}')
        return remetente


class Email_Invalido(Exception):
    pass
