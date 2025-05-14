from odoo import models, fields, api

class ReportEquipoComputo(models.AbstractModel):
    _name = 'report.inventario_computacion.report_equipos'
    _description = 'Reporte de Equipos de Computación'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['inventario.equipo_computo'].browse(docids)
        return {
            'doc_ids': docids,
            'docs': docs,
            'data': data,
            'company_logo': self._get_company_logo(),
        }

    def _get_company_logo(self):
        # Simulación de obtención del logo de la compañía
        # En una implementación real, podrías buscarlo en la configuración de la compañía.
        return '/logo.png' # Asume que tienes un archivo logo.png en la carpeta web estática de tu módulo o en la raíz.