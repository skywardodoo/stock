##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    # Compatibility field for migrated databases where legacy inherited views
    # still reference this historical field.
    stylesheet_id = fields.Many2one("ir.attachment", string="Legacy Stylesheet")

    # Used by custom stock confirmation mail flow.
    stock_mail_confirmation_template_id = fields.Many2one(
        "mail.template",
        string="Stock Mail Confirmation Template",
    )
