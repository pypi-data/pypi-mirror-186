import base64
import hashlib

from cryptography.fernet import Fernet

from viggocore.common.subsystem import operation
from viggocore.common import manager, exception


class Create(operation.Create):

    def pre(self, session, file, **kwargs):
        self.file = file

        senha = kwargs.get('senha', None)
        fernet = Fernet(self.manager._get_key_hash())
        senha_hash = str(fernet.encrypt(senha.encode()))

        kwargs['senha'] = senha_hash
        kwargs['certificado'] = ''

        response_pre = super().pre(session=session, **kwargs)
        return response_pre

    def do(self, session, **kwargs):
        encoded_file = base64.b64encode(self.file.read())
        self.entity.certificado = str(encoded_file)

        super().do(session=session, **kwargs)
        return self.entity


class Update(operation.Update):

    def pre(self, session, id, file, **kwargs):
        super().pre(session=session, id=id, **kwargs)
        self.file = file

        senha = kwargs.get('senha', None)
        senha_anterior = kwargs.pop('senha_anterior', None)
        if senha and not senha_anterior:
            raise exception.BadRequest(
                'Para alterar a senha deve informar a senha anterior!')

        elif senha and senha_anterior:
            fernet = Fernet(self.manager._get_key_hash())
            senha_db = fernet.decrypt(self.entity.senha[2:-1].encode()).decode()
            if senha_db != senha_anterior:
                raise exception.BadRequest('A Senha anterior está errada!')

            senha_hash = str(fernet.encrypt(senha.encode()))
            self.senha = senha_hash

        return self.entity.is_stable()

    def do(self, session, **kwargs):
        kwargs.pop('file', None)
        kwargs.pop('senha_anterior', None)
        kwargs['senha'] = self.senha
        if self.file:
            encoded_file = base64.b64encode(self.file.read())
            self.entity.certificado = str(encoded_file)

        super().do(session=session, **kwargs)
        return self.entity


class Manager(manager.CommonManager):

    def __init__(self, driver):
        super(Manager, self).__init__(driver)
        self.create = Create(self)
        self.update = Update(self)

    def _get_key_hash(self):
        KEY = 'PBKDF2WithHmacSHA1'
        key_hash = hashlib.sha256(KEY.encode()).digest()
        return base64.urlsafe_b64encode(key_hash)
