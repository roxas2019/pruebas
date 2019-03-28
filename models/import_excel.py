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

    def importar_excel(self):
        filename = 'simple.xls'
        ROOT = os.path.abspath(os.sep)
        _logger.info('ROOT: {0}'.format(ROOT))
        filepath = os.path.join('/opt/odoo/project_live_sessions/pruebas/models/', filename)
        wb = open_workbook(filepath)
        for s in wb.sheets():
            _logger.info('Sheet: {0}'.format(s.name))
            for row in range(s.nrows):
                values = []
                for col in range(s.ncols):
                    values.append(s.cell(row, col).value)
                _logger.info(','.join(values))
        return
