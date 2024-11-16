{
    'name': 'Gestión Avanzada de Suscripciones',
    'version': '1.0',
    'author': 'Consultoría de Software',
    'category': 'Servicios',
    'depends': ['base', 'sale_management', 'account', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/plan_suscripcion_views.xml',  # Define las acciones aquí primero
        'views/contrato_suscripcion_views.xml',  # Define las acciones necesarias para contratos
        'views/menu_views.xml',  # Carga los menús después de las acciones
        'views/ticket_suscripcion_views.xml',
        'views/metrica_suscripcion_views.xml',
        'data/planes_suscripcion_data.xml',
        'data/cron_jobs.xml',
        'data/emails_automaticos.xml',
    ],
    'installable': True,
    'application': True,
}
