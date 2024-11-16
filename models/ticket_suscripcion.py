from odoo import models, fields, api

class TicketSuscripcion(models.Model):
    _name = 'soporte.ticket'
    _description = 'Ticket de Soporte'

    nombre = fields.Char('Asunto', required=True)
    descripcion = fields.Text('Descripción')
    contrato_id = fields.Many2one('contrato.suscripcion', 'Contrato de Suscripción', required=True)
    cliente_id = fields.Many2one('res.partner', related='contrato_id.cliente_id', string='Cliente', store=True)
    estado = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('en_progreso', 'En Progreso'),
        ('resuelto', 'Resuelto'),
        ('cerrado', 'Cerrado')
    ], 'Estado', default='nuevo')
    horas_utilizadas = fields.Float('Horas Utilizadas', required=True, default=0)
    es_critico = fields.Boolean('Incidencia Crítica', default=False)

    @api.model
    def create(self, vals):
        # Validar que no se excedan las horas del contrato
        contrato = self.env['contrato.suscripcion'].browse(vals['contrato_id'])
        if contrato.horas_restantes < vals['horas_utilizadas']:
            raise ValueError('No se pueden asignar más horas de las disponibles en el contrato.')
        # Actualizar horas restantes en el contrato
        contrato.horas_restantes -= vals['horas_utilizadas']
        return super(TicketSuscripcion, self).create(vals)
