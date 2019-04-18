# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sce_frontvoice_introduction = fields.Text(string="Introduction of front voice")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res.update(
            sce_frontvoice_introduction=get_param('sce_frontvoice.introduction'),
        )
        return res

    def set_values(self):
        # if not self.user_has_groups('website.group_website_designer'):
            # raise AccessDenied()
        super(ResConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('sce_frontvoice.introduction', self.sce_frontvoice_introduction)
