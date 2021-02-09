# -*- coding: utf-8 -*-
{
    'name': "Sequence limit",

    'description': """
        Restart a sequence when it reaches its limit
    """,

    'author': "Brais Abeijón",

    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'views/ir_sequence.xml',
        'security/ir.model.access.csv',
    ],

}
