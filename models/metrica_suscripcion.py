from odoo import models, fields

class MetricaSuscripcion(models.Model):
    _name = 'metrica.suscripcion'
    _description = 'Métricas de Suscripciones'

    contrato_id = fields.Many2one('contrato.suscripcion', 'Contrato Relacionado')
    ingresos_recurrentes = fields.Float('Ingresos Recurrentes')
    horas_usadas = fields.Float('Horas Consumidas')
    tasa_retencion = fields.Float('Tasa de Retención (%)')
    costo_soporte = fields.Float('Costo de Soporte')
    clientes_riesgo = fields.Integer('Clientes en Riesgo')
