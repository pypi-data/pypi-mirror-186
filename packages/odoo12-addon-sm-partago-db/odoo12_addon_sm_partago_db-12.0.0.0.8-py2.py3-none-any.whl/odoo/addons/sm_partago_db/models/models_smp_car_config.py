# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _


class smp_car_config(models.Model):
  _name = 'smp.sm_car_config'

  name = fields.Char(string=_("Name"), required=True)
  carconfig_name = fields.Char(string=_("Name (car config)"))
  home = fields.Char(string=_("Home"))
  description = fields.Char(string=_("Description"))
  type = fields.Char(string=_("Type"))
  group_index = fields.Char(string=_("Group Index"))
  group_id = fields.Many2one('smp.sm_group',string=_("Group"),compute="_get_group_id")
  owner_group_index = fields.Char(string=_("Owner Group Index"))
  owner_group_id = fields.Many2one('smp.sm_group',string=_("Owner Group"),compute="_get_owner_group_id")
  rel_car_index = fields.Char(string=_("Related car Index"))
  rel_car_id = fields.Many2one('smp.sm_car',string=_("Related car DB"),compute="_get_rel_car_id",store=False)
  rel_car_id_license_plate = fields.Char(string=_("Related car license plate"),compute="_get_rel_car_id_license_plate")

  _order = "name asc"

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

  @api.depends('rel_car_index')
  def _get_rel_car_id(self):
    for record in self:
      if record.rel_car_index:
        existing_car = self.env['smp.sm_car'].search([('name','=',record.rel_car_index)])
        if existing_car.exists():
          record.rel_car_id = existing_car[0].id

  @api.depends('rel_car_id')
  def _get_rel_car_id_license_plate(self):
    for record in self:
      if record.rel_car_id:
          record.rel_car_id_license_plate = record.rel_car_id.license_plate

  def fetch_db_data(self, config_data):
    car_config_update_data = {}
    
    if "name" in config_data:
      car_config_update_data['carconfig_name'] = config_data['name']
    else:
      car_config_update_data['carconfig_name'] = False
    
    if "description" in config_data:
      car_config_update_data['description'] = config_data['description']
    else:
      car_config_update_data['description'] = False
    
    if "type" in config_data:
      car_config_update_data['type'] = config_data['type']
    else:
      car_config_update_data['type'] = False
    
    if "home" in config_data:
      car_config_update_data['home'] = config_data['home']
    else:
      car_config_update_data['home'] = False
    
    if "group" in config_data:
      car_config_update_data['group_index'] = config_data['group']
    else:
      car_config_update_data['group_index'] = False
    
    if "ownerGroup" in config_data:
      car_config_update_data['owner_group_index'] = config_data['ownerGroup']
    else:
      car_config_update_data['owner_group_index'] = False
    
    if "car" in config_data:
      car_config_update_data['rel_car_index'] = config_data['car']
    else:
      car_config_update_data['rel_car_index'] = False

    self.write(car_config_update_data)

  def view_on_app_action(self):
    company = self.env.user.company_id
    return {
      'type': 'ir.actions.act_url',
      'url': '%s/admin/#/carConfigs/%s' % (company.sm_carsharing_api_credentials_cs_url,self.name),
      'target': 'blank'
    }
