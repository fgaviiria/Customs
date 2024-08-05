{
    'name': "pos fg",

    'description': """
        Odoo programming test
    """,
    'installable': True,
    'author': "My Company",
    'version': '1.0',

    'depends': ['point_of_sale', 'account'],
    'data': [
        'views/new_fields.xml',
        'views/v_qr.xml',
    ],
    'qweb': [

    ],

    'assets': {

        'point_of_sale.assets': [
            'pos_fg/static/src/xml/Screens/pos_lang.xml',
            'pos_fg/static/src/xml/Screens/check_orderline.xml',
            'pos_fg/static/src/js/ticket.js',
            # 'pos_fg/static/src/js/check.js',
            'pos_fg/static/src/xml/Screens/ticket_pos.xml',
        ],
    },
}
