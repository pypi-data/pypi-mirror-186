# -*- coding: utf-8 -*-
{
    'name': "sm_teletacs",

    'summary': """
        Create extra expenses for carsharing usages""",

    'author': "Som Mobilitat",
    'website': "https://www.sommobilitat.coop",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'vertical-carsharing',
    'version': '12.0.0.0.5',

    # any module necessary for this one to work correctly
    'depends': ['base','vertical_carsharing','sm_partago_usage'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views_teletac.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
