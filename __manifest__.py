# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Fixed Header Listview',
    'version': '15.0.1.0.0',
    'sequence': 1,
    'summary': """
        Sticky Tree View, Fixed Table Header, Changed color and height of ListView, 
    """,
    'description': "This module will help you to change the color and height of ListView",
    'author': 'Abdul Ahad',
    'maintainer': 'VeryCode Studio',
    'license': 'LGPL-3',
    'depends': [
        'web'
    ],
    'assets': {
        'web.assets_backend': [
            'fixed_header_list/static/src/css/list_view.css',
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
