import uuid
import csv

import flask
from viggocore.common import exception, utils
from viggocore.common.subsystem import controller
from datetime import date, datetime
from sqlalchemy import exc as sqlexc


class Controller(controller.Controller):

    def convert_string_to_date(self, date: str):
        return datetime.strptime(date, '%d/%m/%Y')
    
    def get_ex(self, ex: str):
        if ex == '':
            return None
        else:
            return int(ex)

    def verificar_se_existe(self, ncmibpt_file_line, sigla_uf):
        filter_dict = {
            "ncm": int(ncmibpt_file_line['codigo']),
            "uf": sigla_uf,
            "chave": ncmibpt_file_line['chave'],
            "versao": ncmibpt_file_line['versao'],
            "extipi":  self.get_ex(ncmibpt_file_line['ex'])
        }
        entities = self.manager.list(**filter_dict)
        if len(entities) > 0:
            entity = entities[0]
        else:
            entity = None
        return entity

    def make_ncmibpt_dict(self, ncmibpt_file_line, sigla_uf):

        ncmibpt_dict = {
            'ncm': int(ncmibpt_file_line['codigo']),
            'uf': sigla_uf,
            'chave': ncmibpt_file_line['chave'],
            'versao': ncmibpt_file_line['versao'],
            'descricao': ncmibpt_file_line['descricao'], 
            'aliq_nacional': float(ncmibpt_file_line['nacionalfederal']),
            'aliq_importacao': float(ncmibpt_file_line['importadosfederal']),
            'aliq_estadual': float(ncmibpt_file_line['estadual']),
            'aliq_municipal': float(ncmibpt_file_line['municipal']),
            'inicio_vigencia': self.convert_string_to_date(
                ncmibpt_file_line['vigenciainicio']),
            'fim_vigencia': self.convert_string_to_date(
                ncmibpt_file_line['vigenciafim']),
            'extipi': self.get_ex(ncmibpt_file_line['ex']),
            'tipo': self.get_ex(ncmibpt_file_line['tipo'])
        }
        return ncmibpt_dict

    def cadastrar_por_arquivo(self):
        file = flask.request.files.get('file', None)
        sigla_uf = flask.request.form.get('sigla_uf', None)
        edocs = []
        erros = []
        tipo = file.mimetype.split('/')[-1].upper()

        if tipo == 'CSV':
            filename = file.filename
            file_content = file.read()
            ncmibpt_file_lines = csv.DictReader(
                file_content.decode('unicode_escape').splitlines(),
                delimiter=';')

            line_count = 0
            qtd_sucesso = 0
            for ncmibpt_file_line in ncmibpt_file_lines:
                ncmibpt_dict = self.make_ncmibpt_dict(
                    ncmibpt_file_line, sigla_uf)
                entity = self.verificar_se_existe(
                    ncmibpt_file_line, sigla_uf)

                if line_count != 0:
                    try:
                        if entity is None:
                            ncmibpt = self.manager.create(**ncmibpt_dict)
                        else:
                            ncmibpt = self.manager.update(
                                id=entity.id, **ncmibpt_dict)
                        qtd_sucesso += 1
                    except exception.ViggoCoreException as exc:
                        erros.append({'ncm': ncmibpt_dict['ncm'],
                                     'ex': ncmibpt_dict['extipi'],
                                     'tipo': ncmibpt_dict['tipo'],
                                     'msg_erro': exc.message})
                    except sqlexc.DataError as exc:
                        erros.append({'ncm': ncmibpt_dict['ncm'],
                                     'ex': ncmibpt_dict['extipi'],
                                     'tipo': ncmibpt_dict['tipo'],
                                     'msg_erro': str(exc)})
                    except Exception as exc:
                        erros.append({'ncm': ncmibpt_dict['ncm'],
                                     'ex': ncmibpt_dict['extipi'],
                                     'tipo': ncmibpt_dict['tipo'],
                                     'msg_erro': exc.message})
                else:
                    line_count += 1
        else:
            msg = 'A aplicação só permite arquivos .csv'
            return flask.Response(response=msg,
                                  status=400)

        response = {
            'filename': filename,
            'sigla_uf': sigla_uf,
            'qtd_sucesso': qtd_sucesso,
            'qtd_erros': len(erros),
            'erros': erros}

        return flask.Response(response=utils.to_json(response),
                              status=201,
                              mimetype="application/json")
