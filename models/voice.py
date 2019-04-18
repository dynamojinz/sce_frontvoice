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
    # def action_publish(self):
        # # message = _("A new voice was published:\nSN:%s\nType:%s\nTitle:%s") % (self.name, self.type_id.name, self.title)
        # title = _("A new voice was published")
        # markdown = _("## %s\n- SN:%s\n- Type:%s\n- Title:%s") % (title, self.name, self.type_id.name, self.title)
        # # url = "http://cs.sce-re.com:8049/sce_frontvoice/voice/%d" % (self.id)
        # redirect = "/sce_frontvoice/voice/%d" % (self.id)
        # # url = "http://localhost:8069/sce_dingtalk/oauth/script/%s?redirect=%s" % (self._name, urllib.parse.quote(redirect),)
        # users = self.env.ref('sce_frontvoice.designlib_user').users
        # user_list = [user for user,domain in [user.login.split('@') for user in users] if domain=='sce-re.com']
        # for i in range(int(len(user_list)/20)+1):
            # send_list = user_list[i*20:i*20+20]
            # if len(send_list)>0:
                # # print(",".join(send_list))
                # self.dingtalk_send_action_card_message(",".join(send_list), title, markdown, redirect)
        # # Test
        # # self.dingtalk_send_action_card_message('jinz, liuzaih', title, markdown, redirect)
        # self.state = 'published'

    # def action_cancel_publish(self):
        # self.state = 'draft'

