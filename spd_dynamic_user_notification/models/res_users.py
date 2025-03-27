# -*- coding: utf-8 -*-
from odoo import _, api, exceptions, fields, models
from odoo.addons.bus.models.bus import channel_with_db, json_dump


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.depends("create_date")
    def _compute_channel_names(self):
        for record in self:
            record.notify_success_channel_name = json_dump(channel_with_db(self.env.cr.dbname, record.partner_id))
            record.notify_danger_channel_name = json_dump(channel_with_db(self.env.cr.dbname, record.partner_id))
            record.notify_warning_channel_name = json_dump(channel_with_db(self.env.cr.dbname, record.partner_id))
            record.notify_info_channel_name = json_dump(channel_with_db(self.env.cr.dbname, record.partner_id))
            record.notify_default_channel_name = json_dump(channel_with_db(self.env.cr.dbname, record.partner_id))

    notify_success_channel_name = fields.Char(compute="_compute_channel_names")
    notify_danger_channel_name = fields.Char(compute="_compute_channel_names")
    notify_warning_channel_name = fields.Char(compute="_compute_channel_names")
    notify_info_channel_name = fields.Char(compute="_compute_channel_names")
    notify_default_channel_name = fields.Char(compute="_compute_channel_names")

    def generate_notification_on_record_create(self, notification_config_id=False, record=False):
        """This method prepares required data to generate the notification when record is created for selected model in
            automated action"""
        if notification_config_id:
            notification_id = self.env['notification.config'].sudo().browse(notification_config_id)
            name_field = self.env['ir.model.fields'].search(
                [('model_id', '=', notification_id.model_id.id), ('name', '=', 'name')], limit=1)
            name = ''
            if name_field:
                name = record.name
            if notification_id:
                partner_ids = []
                for user in notification_id.notify_user_ids:
                    partner_ids.append(user.partner_id.id)
                message = f'{notification_id.model_id.name} is created {name}'
                record.message_post(body=message, partner_ids=partner_ids)

    def generate_notification_on_state_change(self, notification_config_id=False, record=False, state=False):
        """This method prepares required data to generate the notification when state change of selected field in
            automated action"""
        if notification_config_id:
            notification_id = self.env['notification.config'].sudo().browse(notification_config_id)
            name_field = self.env['ir.model.fields'].search(
                [('model_id', '=', notification_id.model_id.id), ('name', '=', 'name')], limit=1)
            name = ''
            if name_field:
                name = record.name
            if notification_id:
                partner_ids = []
                for user in notification_id.notify_user_ids:
                    partner_ids.append(user.partner_id.id)
                message = f'{notification_id.model_id.name} {name} status updated to {state}'
                record.message_post(body=message, partner_ids=partner_ids)
