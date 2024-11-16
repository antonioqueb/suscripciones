from odoo import models, fields

class MetricaSuscripcion(models.Model):
    _name = 'metrica.suscripcion'
    _description = 'Métrica de Suscripción'

    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha = fields.Date(string='Fecha', required=True)
    valor = fields.Float(string='Valor', required=True)
