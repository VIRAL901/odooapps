# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Candidroot Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class RecnameDescription(models.Model):
    _name = 'recname.description'

    name = fields.Char('Name')
    model_id = fields.Many2one('ir.model', required=True, string="Model", ondelete='cascade')
    model_name = fields.Char("Model Name", related="model_id.model", store=True)
    field_ids = fields.Many2many('ir.model.fields', string='Field',
                                 domain="[('model_id', '=', model_id),('ttype', '=', ['char','text','integer','float','many2one'])]",
                                 help="If set, this field will be stored in the sparse structure of the "
                                      "serialization field, instead of having its own database column. "
                                      "This cannot be changed after creation.",
                                 )

    seprator = fields.Char("Seprator")

    @api.constrains('seprator')
    def _check_seprator(self):
        for rec in self:
            if rec.seprator and len(rec.seprator) != 1:
                raise ValidationError(_("Separator field must be one special character."))


class BaseModelExtend(models.AbstractModel):
    _inherit = 'base'

    def _compute_field_value(self, field):
        dynamic_objects = self.env['recname.description'].sudo().search([
            ('model_name', '=', self._name)], limit=1
        )
        if dynamic_objects and field.compute in ['_compute_display_name', '_compute_complete_name']:
            fields.determine('_compute_dynamic_display_name', self)
        else:
            fields.determine(field.compute, self)

        if field.store and any(self._ids):
            # check constraints of the fields that have been computed
            fnames = [f.name for f in self.pool.field_computed[field]]
            self.filtered('id')._validate_fields(fnames)
    def dynamic_name_get(self, dynamic_objects):
        """ dynamic_name_get() -> [(id, name), ...]

        Returns a textual representation for the records in ``self``.
        By default this is the value of the ``display_name`` field.

        :return: list of pairs ``(id, text_repr)`` for each records
        :rtype: list(tuple)
        """
        result = []
        seprator = dynamic_objects.seprator or ' '
        for rec in self:
            data = rec.read()[0]
            record_data = []
            for field in dynamic_objects.field_ids:
                if field.ttype in ['char', 'text']:
                    if data[field.name]:
                        record_data.append(data[field.name])
                elif field.ttype in ['integer', 'float']:
                    if data[field.name]:
                        record_data.append(str(data[field.name]))
                elif field.ttype in ['many2one']:
                    if len(data[field.name]) == 2:
                        record_data.append(data[field.name][1])
            if record_data:
                name = ('' + seprator + '').join(record_data)
            else:
                name = rec.name
            result.append((rec.id, name))
        return result

    @api.depends(lambda self: (self._rec_name,) if self._rec_name else ())
    def _compute_dynamic_display_name(self):
        dynamic_objects = self.env['recname.description'].sudo().search([
           ('model_name', '=', self._name)], limit=1
        )
        if dynamic_objects:
            names = dict(self.dynamic_name_get(dynamic_objects))
        else:
            names = dict(self.name_get())
        for record in self:
            record.display_name = names.get(record.id, False)
