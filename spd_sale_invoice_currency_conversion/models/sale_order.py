from odoo import models,fields,api

class InheritSaleOrder(models.Model):
    _inherit='sale.order'

    company_currency_id = fields.Many2one(
        string='Company Currency',
        related='company_id.currency_id', readonly=True,
    )

    conversion_currency_id = fields.Many2one('res.currency',string='Conversion Currency')
    conversion_rate = fields.Monetary(currency_field='conversion_currency_id',string='Conversion Rate',compute='_compute_conversion_rate',store=1)
    conversion_amount_total = fields.Monetary(currency_field='conversion_currency_id',string="Conversion Total", store=True, compute='_compute_conversion_amount_total', tracking=4)

    @api.depends('amount_total','conversion_rate')
    def _compute_conversion_amount_total(self):
        for rec in self:
            rec.conversion_amount_total = rec.amount_total * rec.conversion_rate

    @api.depends('conversion_currency_id','conversion_currency_id.rate_ids','conversion_currency_id.rate_ids.company_rate')
    def _compute_conversion_rate(self):
        for rec in self:
            if rec.conversion_currency_id and rec.conversion_currency_id.rate_ids:
                highest_id = max(rec.conversion_currency_id.rate_ids.mapped('id'), default=0)
                rate_record = rec.conversion_currency_id.rate_ids.filtered(lambda r: r.id == highest_id)
                rec.conversion_rate = rate_record.company_rate if rate_record else 0

    def action_refresh_conversion_rate(self):
        self._compute_conversion_rate()

