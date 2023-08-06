# -*- coding: utf-8 -*-

from odoo import models, api
from odoo.addons.sm_partago_db.models.models_smp_db_utils import smp_db_utils

class sm_db_wizard(models.TransientModel):
  _name = "smp.sm_db_wizard"

  @api.multi
  def create_request(self):
    app_db_utils = smp_db_utils.get_instance(self)
    app_db_utils.update_all_system_db_data_from_app_db(self)
    return True
