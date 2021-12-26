from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SalonGroup(models.Model):
    _name = 'salon.group'

    name = fields.Char('Group Name', required=True)
    salon_group_service_ids = fields.One2many('salon.group.service', 'salon_group_id')
    salon_chair_ids = fields.One2many('salon.chair', 'salon_group_id')

    _sql_constraints = [
        ('unique_group_name', 'unique(name)', 'Name already exists')]

    @api.model
    def create(self, vals):
        name = vals.get('name', None)
        if name:
            name = name.upper()
            names = self.search([('name', '=', name)])
            if names:
                raise ValidationError(
                    _(f"Group ({name}) Already exists"))
            vals['name'] = name
            res = super().create(vals)
            return res

    def write(self, vals):
        name = vals.get('name', None)
        if name:
            vals['name'] = name.upper()
        write_res = super(SalonGroup, self).write(vals)
        return write_res


class SalonGroupService(models.Model):
    _name = 'salon.group.service'

    salon_group_id = fields.Many2one('salon.group', required=True)
    salon_service_id = fields.Many2one('salon.service', required=True)

    _sql_constraints = [
        ('unique_service_group', 'unique(salon_group_id,salon_service_id)', 'Service already linked to group.')]


class SalonChair(models.Model):
    _inherit = 'salon.chair'

    salon_group_id = fields.Many2one('salon.group', required=True)
