from odoo import models, fields

class PlanSuscripcion(models.Model):
    _name = 'plan.suscripcion'
    _description = 'Plan de Suscripción'

    nombre = fields.Char('Nombre del Plan', required=True)
    descripcion = fields.Text('Descripción')
    ciclo_facturacion = fields.Selection([
        ('mensual', 'Mensual'),
        ('trimestral', 'Trimestral'),
        ('anual', 'Anual')
    ], 'Ciclo de Facturación', required=True)
    precio = fields.Float('Precio', required=True)
    horas_incluidas = fields.Integer('Horas Incluidas', default=0)
    servicios_incluidos = fields.Many2many('product.product', string='Servicios Incluidos')
    tipo_plan = fields.Selection([
        ('basico', 'Básico'),
        ('avanzado', 'Avanzado'),
        ('premium', 'Premium')
    ], 'Tipo de Plan', required=True)
