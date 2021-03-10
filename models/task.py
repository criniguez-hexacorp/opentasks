from odoo import api, fields, models


class task(models.Model):
    _name = 'opentasks.task'
    _description = 'Task'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')
    done = fields.Boolean(string='Done')
