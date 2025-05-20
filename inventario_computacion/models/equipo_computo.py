from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EquipoComputo(models.Model):
    _name = 'inventario.equipo_computo'
    _description = 'Equipo de Computación'
    _rec_name = 'serial'  # Campo para mostrar como nombre del registro

    serial = fields.Char(string="Serial único", required=True, index=True, copy=False)
    tipo = fields.Selection([
        ('laptop', 'Laptop'),
        ('pc', 'PC'),
        ('componente', 'Componente')
    ], string="Tipo de Equipo", required=True)
    ubicacion = fields.Many2one('stock.location', string="Ubicación en Almacén")
    fecha_adquisicion = fields.Date(string="Fecha de Adquisición")
    marca = fields.Char(string="Marca")
    modelo = fields.Char(string="Modelo")
    procesador = fields.Char(string="Procesador")
    memoria_ram = fields.Char(string="Memoria RAM")
    disco_duro = fields.Char(string="Disco Duro")
    sistema_operativo = fields.Char(string="Sistema Operativo")
    descripcion = fields.Text(string="Descripción Adicional")

    _sql_constraints = [
        ('serial_unico', 'unique(serial)', 'El serial del equipo debe ser único.'),
    ]

    @api.constrains('serial')
    def _check_serial_unico(self):
        for record in self:
            if self.search_count([('serial', '=', record.serial)]) > 1:
                raise ValidationError("El serial '%s' ya existe en el inventario." % record.serial)

    @api.onchange('tipo')
    def _onchange_tipo(self):
        if self.tipo == 'componente':
            self.ubicacion = self.env.ref('stock.stock_location_components', raise_if_not_found=False)
        else:
            self.ubicacion = False