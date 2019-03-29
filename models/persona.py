# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class Persona(models.Model):
    _name = 'pruebas.persona'
    _rec_name = 'nombre'
    _description = 'Persona'

    nombre = fields.Char(
        string="Nombre",
        required=False,
    )

    apellido_paterno = fields.Char(
        string="Apellido Paterno",
        required=False,
    )

    apellido_materno = fields.Char(
        string="Apellido Materno",
        required=False,
    )

    import_excel_id = fields.Many2one(
        comodel_name="pruebas.import.excel",
        string="Import Excel",
        required=False,
    )
