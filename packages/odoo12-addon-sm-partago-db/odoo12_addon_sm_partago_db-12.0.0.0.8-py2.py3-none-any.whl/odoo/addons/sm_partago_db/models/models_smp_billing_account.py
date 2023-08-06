# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.tools.translate import _


class smp_billing_account(models.Model):

  _name="smp.sm_billing_account"

  name = fields.Char(string=_("Name"), readonly=True)

  group_index = fields.Char(string=_("Group Index"),readonly=True)
  group_id = fields.Many2one('smp.sm_group',string=_("Group"),compute="_get_group_id")
  minutesLeft = fields.Float(string=_("Minutes Left"), readonly=True)
  owner_group_index = fields.Char(string=_("Owner Group Index"), readonly=True)
  owner_group_id = fields.Many2one("smp.sm_group", string=_("Owner Group"),compute="_get_owner_group_id")

  @api.depends('group_index')
  def _get_group_id(self):
    for record in self:
      if record.group_index:
        existing_group = self.env['smp.sm_group'].search([('name','=',record.group_index)])
        if existing_group.exists():
          record.group_id = existing_group[0].id

  @api.depends('owner_group_index')
  def _get_owner_group_id(self):
    for record in self:
      if record.owner_group_index:
        existing_group = self.env['smp.sm_group'].search([('name','=',record.owner_group_index)])
        if existing_group.exists():
          record.owner_group_id = existing_group[0].id

  def fetch_db_data(self, config_data):
    billing_account_update_data = {}

    if "group" in config_data:
      billing_account_update_data['group_index'] = config_data['group']
    else:
      billing_account_update_data['group_index'] = False

    if "minutesLeft" in config_data:
      mins_left_str = str(config_data['minutesLeft'])
      billing_account_update_data['minutesLeft'] = float(mins_left_str.replace(',','.'))
    else:
      billing_account_update_data['minutesLeft'] = 0

    if "ownerGroup" in config_data:
      billing_account_update_data['owner_group_index'] = config_data['ownerGroup']
    else:
      billing_account_update_data['owner_group_index'] = False

    self.write(billing_account_update_data)

  def view_on_app_action(self):
    company = self.env.user.company_id
    return {
      'type': 'ir.actions.act_url',
      'url': '%s/admin/#/billingAccounts/%s' % (company.sm_carsharing_api_credentials_cs_url,self.name),
      'target': 'blank'
    }
