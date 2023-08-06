# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.tools.translate import _
from odoo.addons.sm_partago_db.models.models_smp_db_utils import smp_db_utils

class smp_group(models.Model):

  _rec_name = 'group_name'
  _name = 'smp.sm_group'
  _order = "name asc"

  name = fields.Char(string=_("Name"), required=True)
  group_name = fields.Char(string=_("Group name"))
  related_billingaccount_index = fields.Char(string=_("Billing Account Index"))
  related_billingaccount_id = fields.Many2one('smp.sm_billing_account',string=_("Billing Account"),
    compute="_get_related_billingaccount_id")
  related_billingaccount_minutesleft = fields.Float(string=_("Minutes left (Billing Account)"),
    compute="_get_related_billingaccount_minutesleft",store=False)
  related_config_index = fields.Char(string=_("Config Index"))
  related_config_id = fields.Many2one('smp.sm_group_config',string=_("Config"),compute="_get_related_config_id")
  owner_group_index = fields.Char(string=_("Owner Group Index"))
  owner_group_id = fields.Many2one("smp.sm_group", string=_("Owner Group"),compute="_get_owner_group_id")

  @api.depends('related_billingaccount_index')
  def _get_related_billingaccount_id(self):
    for record in self:
      if record.related_billingaccount_index:
        existing_ba = self.env['smp.sm_billing_account'].search([('name','=',record.related_billingaccount_index)])
        if existing_ba.exists():
          record.related_billingaccount_id = existing_ba[0].id

  @api.depends('related_billingaccount_id')
  def _get_related_billingaccount_minutesleft(self):
    for record in self:
      if record.related_billingaccount_id:
        record.related_billingaccount_minutesleft = record.related_billingaccount_id.minutesLeft

  @api.depends('related_config_index')
  def _get_related_config_id(self):
    for record in self:
      if record.related_config_index:
        existing_config = self.env['smp.sm_group_config'].search([('name','=',record.related_config_index)])
        if existing_config.exists():
          record.related_config_id = existing_config[0].id

  @api.depends('owner_group_index')
  def _get_owner_group_id(self):
    for record in self:
      if record.owner_group_index:
        existing_group = self.env['smp.sm_group'].search([('name','=',record.owner_group_index)])
        if existing_group.exists():
          record.owner_group_id = existing_group[0].id

  def fetch_db_data(self, config_data):
    app_db_utils = smp_db_utils.get_instance(self)
    update_data = {}

    if "name" in config_data:
      update_data['group_name'] = config_data['name']
    else:
      update_data['group_name'] = False

    if "billingAccount" in config_data:
      update_data['related_billingaccount_index'] = config_data['billingAccount']
    else:
      update_data['related_billingaccount_index'] = False

    if "config" in config_data:
      update_data['related_config_index'] = config_data['config']
    else:
      update_data['related_config_index'] = False

    if "ownerGroup" in config_data:
      update_data['owner_group_index'] = config_data['ownerGroup']
    else:
      update_data['owner_group_index'] = False

    self.write(update_data)

  def view_on_app_action(self):
    company = self.env.user.company_id
    return {
      'type': 'ir.actions.act_url',
      'url': '%s/admin/#/groups/%s' % (company.sm_carsharing_api_credentials_cs_url,self.name),
      'target': 'blank'
    }
