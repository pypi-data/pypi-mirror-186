# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.tools.translate import _


class smp_group_config(models.Model):
  _name = 'smp.sm_group_config'

  name = fields.Char(string=_("Name"), required=True)

  _order = "name asc"

  def fetch_db_data(self, config_data):
    pass
