class Enviador:

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email enválido: {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass