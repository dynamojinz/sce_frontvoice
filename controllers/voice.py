# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import QueryURL
PPG = 4  # Voice Per Page



class FrontVoiceController(http.Controller):
    @http.route('/sce_frontvoice/home/', auth='public', website=True)
    def voice_home(self, **kw):
        get_param = request.env['ir.config_parameter'].sudo().get_param
        values = {
            'introduction': get_param('sce_frontvoice.introduction'),
        }
        return http.request.render('sce_frontvoice.voice_home',values)

    @http.route('/sce_frontvoice/voice/<model("sce_frontvoice.voice"):voice>', auth="public", website=True)
    def voice_view(self, voice, **kw):
        return http.request.render('sce_frontvoice.voice_view',{
            'voice': voice,
            })

    @http.route([
        '/sce_frontvoice/voice',
        '/sce_frontvoice/voice/page/<int:page>',
        '/sce_frontvoice/type/<model("sce_frontvoice.voice.type"):type>',
        # '/sce_frontvoice/category/<model("product.public.category"):category>/page/<int:page>'
    ], type='http', auth="public", website=True)
    def voice_list(self, page=0, category=None, search='', ppg=False, **post):
        # if ppg:
            # try:
                # ppg = int(ppg)
            # except ValueError:
                # ppg = PPG
            # post["ppg"] = ppg
        # else:
            # ppg = PPG

        # attrib_list = request.httprequest.args.getlist('attrib')
        # attrib_values = [[int(x) for x in v.split("-")] for v in attrib_list if v]
        # attributes_ids = {v[0] for v in attrib_values}
        # attrib_set = {v[1] for v in attrib_values}

        VoiceType  = http.request.env['sce_frontvoice.voice.type']
        voice_types = VoiceType.search([])

        # # domain = self._get_search_domain(search, category, attrib_values)
        domain=[('state','=','published'),]
        # keep = QueryURL('/sce_frontvoice/voice', category=category and int(category), search=search, attrib=attrib_list, order=post.get('order'))

        # request.context = dict(request.context, pricelist=False, partner=request.env.user.partner_id)

        # url = "/sce_frontvoice/voice"
        # if search:
            # post["search"] = search
        # if post.get('type_id'):
            # type_id = int(post['type_id'])
        # elif voice_types:
            # type_id = voice_types[0].id
        # else:
            # type_id=1
        # domain.append(('type_id','=',type_id))
        search_key = ""
        if post.get('search_box'):
            search_key = post['search_box'].strip()
            domain.append('|')
            domain.append(('question','ilike',search_key))
            domain.append(('answer','ilike',search_key))
        # if post.get('voice_tag'):
            # domain.append(('tag_ids', '=', int(post['voice_tag'])))

        # # print(domain)
        Voice = request.env['sce_frontvoice.voice']

        # parent_category_ids = []

        # voice_count = Voice.search_count(domain)
        # pager = request.website.pager(url=url, total=voice_count, page=page, step=ppg, scope=7, url_args=post)
        # voices = Voice.search(domain, limit=ppg, offset=pager['offset'], order="name asc")
        voices = Voice.search(domain, order="question asc")


        values = {
            'voice_types': voice_types,
            # 'voice_classes': VoiceClass.search([]),
            # 'voice_tags': VoiceTag.search([]),
            'search': search_key,
            # 'category': category,
            # 'pager': pager,
            'voices': voices,
            # 'type_id': type_id,
            # 'search_count': voice_count,  # common for all searchbox
            # 'rows': PPG,
            # 'keep': keep,
            # 'no_footer': True,
        }
        return request.render("sce_frontvoice.voices", values)

    @http.route('/sce_frontvoice/statistics', auth="public", website=True)
    def statistics_view(self, **kw):
        Statistics = request.env['sce_frontvoice.statistics']

        statistics = Statistics.search([('state','=','published')], limit=1, order='create_date desc')

        return http.request.render('sce_frontvoice.statistics_view',{'statistics':statistics})
