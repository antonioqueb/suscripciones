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
    prorratear = fields.Boolean('Facturación Prorrateada', default=False)
    descuento_renovacion = fields.Float('Descuento por Renovación (%)', default=0.0)

    @api.depends('plan_id', 'estado')
    def _compute_horas_restantes(self):
        for contrato in self:
            contrato.horas_restantes = contrato.plan_id.horas_incluidas if contrato.estado == 'activo' else 0

    @api.onchange('plan_id')
    def _onchange_plan(self):
        if self.plan_id:
            meses = {'mensual': 1, 'trimestral': 3, 'anual': 12}[self.plan_id.ciclo_facturacion]
            self.fecha_fin = self.fecha_inicio + timedelta(days=30 * meses)

    @api.model
    def generar_facturas_recurrentes(self):
        """
        Genera facturas recurrentes para contratos activos.
        """
        contratos_activos = self.search([('estado', '=', 'activo')])
        for contrato in contratos_activos:
            # Calcular el monto prorrateado si aplica
            if contrato.prorratear and contrato.fecha_inicio and contrato.fecha_fin:
                dias_totales = (contrato.fecha_fin - contrato.fecha_inicio).days
                dias_restantes = (contrato.fecha_fin - fields.Date.today()).days
                factor_prorrateo = dias_restantes / dias_totales
                monto_prorrateado = contrato.plan_id.precio * factor_prorrateo
            else:
                monto_prorrateado = contrato.plan_id.precio

            # Aplicar descuento por renovación automática
            if contrato.descuento_renovacion > 0:
                monto_descuento = monto_prorrateado * (contrato.descuento_renovacion / 100)
                monto_final = monto_prorrateado - monto_descuento
            else:
                monto_final = monto_prorrateado

            # Crear la factura
            factura_vals = {
                'partner_id': contrato.cliente_id.id,
                'invoice_date': fields.Date.today(),
                'move_type': 'out_invoice',
                'invoice_line_ids': [(0, 0, {
                    'name': contrato.plan_id.nombre,
                    'quantity': 1,
                    'price_unit': monto_final,
                })],
            }
            factura = self.env['account.move'].create(factura_vals)
            factura.action_post()  # Valida la factura automáticamente

            # Log de creación de factura
            contrato.message_post(body=f"Factura generada: {factura.name}")
