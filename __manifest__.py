{
    'name': 'Gestión Avanzada de Suscripciones',
    'version': '1.0',
    'license': 'LGPL-3',
    'author': 'Consultoría de Software',
    'category': 'Servicios',
    'depends': ['base', 'sale_management', 'account', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/plan_suscripcion_views.xml',
        'views/contrato_suscripcion_views.xml',
        'views/ticket_suscripcion_views.xml',
        'views/metrica_suscripcion_views.xml',  # Asegúrate de incluirlo
        'views/menu_views.xml',
        'data/planes_suscripcion_data.xml',
        'data/cron_jobs.xml',
        'data/emails_automaticos.xml',
    ],
    'installable': True,
    'application': True,
}