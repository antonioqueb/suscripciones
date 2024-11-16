from odoo import models, fields, api
from datetime import timedelta

class ContratoSuscripcion(models.Model):
    _name = 'contrato.suscripcion'
    _description = 'Contrato de Suscripción'

    nombre = fields.Char('Nombre del Contrato', required=True)
    cliente_id = fields.Many2one('res.partner', 'Cliente', required=True)
    plan_id = fields.Many2one('plan.suscripcion', 'Plan de Suscripción', required=True)
    fecha_inicio = fields.Date('Fecha de Inicio', required=True, default=fields.Date.today)
    fecha_fin = fields.Date('Fecha de Fin')
    estado = fields.Selection([
        ('activo', 'Activo'),
        ('vencido', 'Vencido'),
        ('cancelado', 'Cancelado')
    ], 'Estado', default='activo')
    horas_restantes = fields.Integer('Horas Restantes', compute='_compute_horas_restantes')

    @api.depends('plan_id', 'estado')
    def _compute_horas_restantes(self):
        for contrato in self:
            contrato.horas_restantes = contrato.plan_id.horas_incluidas if contrato.estado == 'activo' else 0

    @api.onchange('plan_id')
    def _onchange_plan(self):
        if self.plan_id:
            meses = {'mensual': 1, 'trimestral': 3, 'anual': 12}[self.plan_id.ciclo_facturacion]
            self.fecha_fin = self.fecha_inicio + timedelta(days=30 * meses)
