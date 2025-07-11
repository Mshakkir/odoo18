{
    'name': 'Saudi Invoice Customization',
    'version': '1.0',
    'depends': ['account','base'],
    'data': [
        'views/custom_invoice_template.xml',
    ],
     'assets': {
        'web.report_assets_common': [
        'custom_sa_invoice/static/src/img/stamp.png',
     ],
    },
    'installable': True,
    'auto_install': False,
}
