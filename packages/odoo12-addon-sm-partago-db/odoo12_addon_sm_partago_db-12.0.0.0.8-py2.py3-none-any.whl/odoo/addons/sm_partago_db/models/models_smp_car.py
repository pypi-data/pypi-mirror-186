# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.tools.translate import _


class smp_car(models.Model):
  _name = 'smp.sm_car'

  name = fields.Char(string=_("Name"), required=True)
  home = fields.Char(string=_("Home"))
  car_name = fields.Char(string=_("name (car)"))
  license_plate = fields.Char(string=_("licensePlate"))
  invers_qnr = fields.Char(string=_("invers_qnr"))
  invers_type = fields.Char(string=_("invers_type"))
  invers_lomo_adapter = fields.Boolean(string=_("lomo_adapter"))
  swap_group = fields.Char(string=_("swapGroup"))
  owner_group_index = fields.Char(string=_("Owner Group Index"))
  owner_group_id = fields.Many2one('smp.sm_group', string=_("Owner Group"),compute="_get_owner_group_id")
  db_carconfigs_id = fields.One2many('smp.sm_car_config', string=_('Carconfigs'),inverse_name="rel_car_id")
  # TODO: Why this is not working?
  # db_carconfigs_id = fields.One2many('smp.sm_car_config', string=_('Carconfigs'),_compute="_get_carconfigs_id",store=False)

  _order = "name asc"

  @api.depends('name')
  def _get_carconfigs_id(self):
    for record in self:
      rel_carconfigs = self.env['smp.sm_car_config'].search([('rel_car_index','=',record.name)])
      cs_ccs = []
      if rel_carconfigs.exists():
        for rel_carconfig in rel_carconfigs:
          cs_ccs.append((4,rel_carconfig.id))
      record.db_carconfigs_id = cs_ccs

  @api.depends('owner_group_index')
  def _get_owner_group_id(self):
    for record in self:
      if record.owner_group_index:
        existing_group = self.env['smp.sm_group'].search([('name','=',record.owner_group_index)])
        if existing_group.exists():
          record.owner_group_id = existing_group[0].id

  def fetch_db_data(self, data):
    update_data = {}

    if "name" in data:
      update_data['car_name'] = data['name']
    else:
      update_data['car_name'] = False

    if "home" in data:
      update_data['home'] = data['home']
    else:
      update_data['home'] = False

    if "licensePlate" in data:
      update_data['license_plate'] = data['licensePlate']
    else:
      update_data['license_plate'] = False

    if "invers" in data:
      if "qnr" in data["invers"]:
        update_data['invers_qnr'] = data['invers']['qnr']
      else:
        update_data['invers_qnr'] = False
      if "type" in data["invers"]:
        update_data['invers_type'] = data['invers']['type']
      else:
        update_data['invers_type'] = False
      if "lomo_adapter" in data["invers"]:
        update_data['invers_lomo_adapter'] = data['invers']['lomo_adapter']
      else:
        update_data['invers_lomo_adapter'] = False
    else:
      update_data['invers_qnr'] = False
      update_data['invers_type'] = False
      update_data['invers_lomo_adapter'] = False

    if "swapGroup" in data:
      update_data['swap_group'] = data['swapGroup']
    else:
      update_data['swap_group'] = False

    if "ownerGroup" in data:
      update_data['owner_group_index'] = data['ownerGroup']
    else:
      update_data['owner_group_index'] = False

    self.write(update_data)

  def view_on_app_action(self):
    company = self.env.user.company_id
    return {
      'type': 'ir.actions.act_url',
      'url': '%s/admin/#/cars/%s' % (company.sm_carsharing_api_credentials_cs_url,self.name),
      'target': 'blank'
    }
