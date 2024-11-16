from odoo import models, fields

class TicketSuscripcion(models.Model):
    _inherit = 'helpdesk.ticket'

    contrato_id = fields.Many2one('contrato.suscripcion', 'Contrato de Suscripción')
    horas_utilizadas = fields.Float('Horas Utilizadas')
    es_critico = fields.Boolean('Incidencia Crítica')
