# Copyright 2019 Vauxoo
# License AGPL-3 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Engineering company Ingepro',
    'summary': '''
    Instance creator for Ingepro. This is the app.
    ''',
    'author': 'Vauxoo',
    'website': 'https://www.vauxoo.com',
    'license': 'AGPL-3',
    'category': 'Installer',
    'version': '12.0.1.0.0',
    'depends': [
        'account_accountant',
        'sale_management',
        'crm',
        'purchase',
        'stock',
        'purchase_discount',
    ],
    'test': [
    ],
    'data': [
        # data
        'data/res_company.xml',
        'data/res_config_settings.xml',
        # views
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
