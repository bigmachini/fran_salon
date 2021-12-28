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


class ServiceCategory(models.Model):
    _name = 'salon.service.category'

    name = fields.Char('Category Name', required=True)
    salon_service_ids = fields.One2many('salon.service', 'salon_service_category_id')

    _sql_constraints = [
        ('unique_category_name', 'unique(name)', 'Service Category already exists')]

    @api.model
    def create(self, vals):
        name = vals.get('name', None)
        if name:
            name = name.upper()
            names = self.search([('name', '=', name)])
            if names:
                raise ValidationError(
                    _(f"Service ({name}) Already exists"))
            vals['name'] = name
            res = super().create(vals)
            return res

    def write(self, vals):
        name = vals.get('name', None)
        if name:
            vals['name'] = name.upper()
        write_res = super(ServiceCategory, self).write(vals)
        return write_res


class SalonService(models.Model):
    _inherit = 'salon.service'

    salon_service_category_id = fields.Many2one('salon.service.category', required=True)
    price_lower = fields.Monetary(string="Price (Lower)")
    price = fields.Monetary(string="Price (Upper)")

    def _validate_price(self, lower, upper):
        if not float(lower) <= float(upper):
            raise ValidationError(
                _(f"Service {self.name}: Lower Price {lower} can't be higher than {upper}"))

    def write(self, vals):
        name = vals.get('name', None)
        lower_price = vals.get('price_lower', None)
        upper_price = vals.get('price', None)
        if lower_price and upper_price:
            pass
        elif lower_price:
            upper_price = self.price
        elif upper_price:
            lower_price = self.price_lower

        if upper_price or lower_price:
            self._validate_price(lower_price, upper_price)

        if name:
            vals['name'] = name.upper()
        write_res = super(SalonService, self).write(vals)
        return write_res

    @api.model
    def create(self, vals):
        name = vals.get('name', None)
        salon_service_category_id = vals.get('salon_service_category_id', None)
        if name and salon_service_category_id:
            name = name.upper()
            names = self.search(
                [('name', '=', name), ('salon_service_category_id', '=', int(salon_service_category_id))])
            if names:
                salon_service_category = self.env['salon.service.category'].browse(int(salon_service_category_id))
                raise ValidationError(
                    _(f"Service ({name}) Already exists in Category {salon_service_category.name}"))
            vals['name'] = name
            res = super().create(vals)
            return res
