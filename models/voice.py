# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools, _
import urllib

class VoiceType(models.Model):
    _name = 'sce_frontvoice.voice.type'
    name = fields.Char()
    code = fields.Char()
    voice_count = fields.Integer(compute='_compute_voice_count',store=False)

    @api.multi
    def _compute_voice_count(self):
        read_group_res = self.env['sce_frontvoice.voice'].read_group(
                [('state','=','published'),('type_id','in',self.ids)],
                ['type_id'],['type_id'])
        read_data = dict((res['type_id'][0],res['type_id_count']) for res in read_group_res)
        for record in self:
            record.voice_count = read_data.get(record.id, 0)


class Voice(models.Model):
    _name = 'sce_frontvoice.voice'
    # _inherit='sce_dingtalk.mixin'

    question = fields.Text(string="Question")
    answer= fields.Text("Answer")
    name = fields.Char(compute="_compute_name", store=False)
    type_id = fields.Many2one('sce_frontvoice.voice.type')
    # 发布控制
    state = fields.Selection(selection=[
        ('draft','Draft'),
        ('published','Published'),
        ], default='published')


    def _compute_name(self):
        self.name = self.question

class Statistics(models.Model):
    _name = 'sce_frontvoice.statistics'

    name = fields.Char()
    url = fields.Char()
    # 图片
    image = fields.Binary('Image', attachment=True,
            help="This field holds the image of the fault.")
    # 发布控制
    state = fields.Selection(selection=[
        ('draft','Draft'),
        ('published','Published'),
        ], default='published')

class Intros(models.Model):
    _name = "sce_frontvoice.intros"
    intros = fields.Text(required=True)
    items = fields.Integer(required=True)