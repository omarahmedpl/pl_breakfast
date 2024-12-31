{
    'name': 'Breakfast',
    'version': '0.1',
    'summary': 'A module to calculate the breakfast',
    'description': '',
    'category': '',
    'author': 'Omar Ahmed',
    'website': '',
    'license': '',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/breakfast_menuitem.xml',
        'views/order_items_form_view.xml',
        'views/order_details_templates.xml'
    ],
    'demo': [''],
    'assets': {
        'web.assets_backend': [
            'pl_breakfast/static/src/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
}