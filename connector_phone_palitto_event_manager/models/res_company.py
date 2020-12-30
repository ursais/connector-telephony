from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    server_address = fields.Char('PCS API Server Address')
