{
    'name': 'Saudi Invoice Customization',
    'version': '1.0',
    'depends': ['account','base'],
    'license': 'LGPL-3',
    'data': [
        'views/custom_invoice_template.xml',
        'views/report_action.xml',
    ],
     'assets': {
        'web.report_assets_common': [
        'custom_sa_invoice/static/src/img/stamp.png',
     ],
    },
    'installable': True,
    'auto_install': False,
}
