from odoo import models, fields
import json

class SpreadsheetDashboard(models.Model):
    _inherit = 'spreadsheet.dashboard'  # use _inherit to extend, not _name

    def get_readonly_dashboard(self):
        # Fallback to empty JSON if field is empty or null
        data = self.spreadsheet_data or '{}'
        snapshot = json.loads(self.spreadsheet_data or '{}')

        widgets = snapshot.get('widgets', [])
        filters = snapshot.get('filters', {})

        return {
            'widget_count': len(widgets),
            'has_filters': bool(filters)
        }


