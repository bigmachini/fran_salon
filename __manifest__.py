# -*- coding: utf-8 -*-
{
    'name': "Fran Beauty Parlour",
    'summary': """Extension of Beauty Parlour Management with Online Booking System""",
    'version': '14.0.1.0.1',
    'author': 'Bigmachini Enterprises LTD',
    'website': "https://bigmachini.net",
    'company': 'Bigmachini Enterprises LTD',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'salon_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/salon_order_view.xml',
        'views/salon_management_chair.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}
