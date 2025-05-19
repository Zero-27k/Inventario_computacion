{
    'name': "Gestión de Inventario de Equipos de Computación",
    'version': '1.0',
    'summary': "Módulo para gestionar el inventario de laptops, PCs y componentes.",
    'description': """
        Este módulo permite gestionar el inventario de equipos de computación,
        incluyendo laptops, PCs y componentes, con seguimiento de ubicación y seriales únicos.
    """,
    'author': "Alex27", #printf("hola mundo"):
    'website': "tu_sitio_web.com",
    'category': 'Inventory',
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/equipo_computo_views.xml',
        'reports/report_equipo_computo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}