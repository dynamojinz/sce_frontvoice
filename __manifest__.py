# -*- coding: utf-8 -*-
{
    'name': "SCE Front Voice",

    'summary': """
        SCE front voice
        Developed for Process Department.""",

    'description': """
        Long description of module's purpose
        Searching
        Viewing
        Etc.
    """,

    'author': "Jin Zan",
    'website': "http://www.sce-re.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','sce_sso','sce_dingtalk'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/voice_views.xml',
        'views/res_config_settings_views.xml',
        'views/voice_templates.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
