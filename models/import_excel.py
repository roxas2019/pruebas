# -*- coding: utf-8 -*-

from odoo import models, fields, api
from xlrd import open_workbook
import os
import logging
_logger = logging.getLogger(__name__)


class ImportExcel(models.Model):
    _name = 'pruebas.import.excel'
    _rec_name = 'name'
    _description = 'Importar Excel'

    name = fields.Char(
        string="Name",
        required=False,
    )

    personas = fields.One2many(
        comodel_name="pruebas.persona",
        inverse_name="import_excel_id",
        string="Personas",
        required=False,
    )

    def importar_excel(self):
        filename = 'personas.xls'
        ROOT = os.path.abspath(os.sep)
        _logger.info('ROOT: {0}'.format(ROOT))
        filepath = os.path.join('/opt/odoo/project_live_sessions/pruebas/models/', filename)
        wb = open_workbook(filepath)
        self.personas -= self.personas
        personas = []
        for s in wb.sheets():
            _logger.info('Sheet: {0}'.format(s.name))
            for row in range(s.nrows):
                values = []
                persona = {}
                i = 1
                for col in range(s.ncols):
                    values.append(s.cell(row, col).value)
                    if i == 1:
                        persona['nombre'] = s.cell(row, col).value
                    if i == 2:
                        persona['apellido_paterno'] = s.cell(row, col).value
                    if i == 3:
                        persona['apellido_materno'] = s.cell(row, col).value
                    i += 1
                _logger.info(','.join(values))
                personas += [(0, 0, persona)]
        self.personas = personas
        return
