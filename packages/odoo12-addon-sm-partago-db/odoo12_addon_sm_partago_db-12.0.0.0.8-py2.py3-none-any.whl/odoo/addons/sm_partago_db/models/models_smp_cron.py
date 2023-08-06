# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.addons.sm_partago_db.models.models_smp_db_utils import smp_db_utils

class smp_cron(models.Model):
  _name = 'smp.sm_fetch_carsharing_db_cron'

  @api.model
  def fetch_carsharing_db_cron_action(self):
    app_db_utils = smp_db_utils.get_instance(self)
    app_db_utils.update_all_system_db_data_from_app_db(self)
