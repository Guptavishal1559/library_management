{
    'name': 'Library Management System',
    'description': 'It is a library management system software',
    'author': 'Vishal Gupta',
    'website': 'https://www.skyscendbs.com',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'data/book_dept_sequence.xml',
        'views/stock_view.xml',
        'views/book_dept.xml',
        'views/book_issue.xml',
        'views/language_view.xml',
        'views/type_view.xml',
        'views/author_details_view.xml',
        'views/user_view.xml'
    ],
    'auto_install': True,
    'installable': True,
    'application': True,
}