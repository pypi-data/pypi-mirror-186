from odoo.addons.sm_maintenance.models.models_sm_utils import sm_utils
from odoo.addons.sm_connect.models.models_sm_carsharing_db_utils import sm_carsharing_db_utils
from odoo.addons.sm_connect.models.models_sm_carsharing_api_utils import sm_carsharing_api_utils

class smp_db_utils(object):
  __instance = None
  __cs_db_utils = None
  __cs_api_utils = None

  @staticmethod
  def get_instance(parent):
    if smp_db_utils.__instance is None:
      smp_db_utils(parent)
    return smp_db_utils.__instance

  def __init__(self, parent):
    if smp_db_utils.__instance is not None:
      raise Exception("This class is a singleton!")
    else:
      smp_db_utils.__instance = self
      smp_db_utils.__cs_db_utils = sm_carsharing_db_utils.get_instance(parent)
      smp_db_utils.__cs_api_utils = sm_carsharing_api_utils.get_instance(parent)

  def update_all_system_db_data_from_app_db(self,parent):
    self._update_system_db_data_from_app_db(parent,'smp.sm_group_config', 'config')
    self._update_system_db_data_from_app_db(parent,'smp.sm_group', 'groups')
    self._update_system_db_data_from_app_db(parent,'smp.sm_car', 'cars')
    self._update_system_db_data_from_app_db(parent,'smp.sm_car_config', 'carConfigs')
    # self._update_system_db_data_from_app_db(parent,'smp.sm_billing_account', 'billingAccounts')

  def update_system_config_from_app_config(self,parent,config_index=False):
    return self._update_system_db_data_from_app_db(parent,'smp.sm_group_config', 'config',config_index)

  def update_system_ba_from_app_ba(self,parent,ba_index=False):
    return self._update_system_db_data_from_app_db(parent,'smp.sm_billing_account', 'billingAccounts',ba_index)

  def update_system_group_from_app_group(self,parent,group_index=False):
    return self._update_system_db_data_from_app_db(parent,'smp.sm_group', 'groups',group_index)

  def get_app_reservations_by_group(self,parent,from_q=False,till_q=False):
    res_by_group = {}
    if from_q and till_q:
      groups = self.get_system_db_groups(parent)
      if groups:
        for group in groups:
          r = self.__cs_api_utils.get_reservations_by_group(from_q,till_q,group.name)
          r_json = self.__cs_api_utils.validate_response(r)
          if r_json:
            res_by_group[group.name] = r_json
    return res_by_group

  def get_app_person_details(self,cs_person_index = False):
    if cs_person_index:
      r = self.__cs_api_utils.get_persons(cs_person_index)
      return self.__cs_api_utils.validate_response(r)
    return False

  def get_app_person_groups(self,cs_person_index):
    if cs_person_index:
      cs_member_details = self.get_app_person_details(cs_person_index)
      if cs_member_details:
        if "groups" in cs_member_details.keys():
          if cs_member_details['groups'] is not None:
            return cs_member_details['groups']
    return False

  def get_system_db_group(self,parent,group_index):
    if group_index:
      system_group = parent.env['smp.sm_group'].search([("name","=",group_index)])
      if system_group.exists():
        return system_group[0]
    return False

  def get_system_db_groups(self,parent):
    system_groups = parent.env['smp.sm_group'].search([])
    if system_groups.exists():
      return system_groups
    return False

  def create_app_person(self,member_data = False):
    if member_data:
      r = self.__cs_api_utils.post_persons(member_data)
      return self.__cs_api_utils.validate_response(r)
    return False

  def create_app_ba_transaction(self,ba_id=False,ttype=False,description=False,credits=False):
    if ba_id and ttype and description and credits:
      r = self.__cs_api_utils.put_billingaccount_transactions(ba_id,ttype,description,credits)
      return self.__cs_api_utils.validate_response(r)
    return False

  def add_app_person_to_group(self,person_id=False,group_id=False,create_ba=False):
    if person_id and group_id and create_ba:
      r = self.__cs_api_utils.post_persons_groups(person_id,group_id,False,create_ba)
      return self.__cs_api_utils.validate_response(r)
    return False

  def add_app_person_to_group_with_defined_ba(self,person_id=False,group_id=False,ba_id=False):
    if person_id and group_id and ba_id:
      r = self.__cs_api_utils.post_persons_groups(person_id,group_id,ba_id,"false")
      return self.__cs_api_utils.validate_response(r)
    return False

  def delete_app_person_from_groups(self, person_id=False, group_id=False):
    if person_id and group_id:
      response = self.__cs_api_utils.delete_person_group(person_id, group_id)
      return self.__cs_api_utils.validate_response(response)
    return False

  def _update_system_db_data_from_app_db(self,parent, model_name, endpoint,record_index=False):
    if record_index is False:
      model_datas = self.__cs_db_utils.firebase_get(endpoint)
      if model_datas is not None:
        for model_index in model_datas:
          # search or create model base on unique name!
          self._update_create_system_db_entry(parent,model_name,model_index,model_datas[model_index])

        self._update_delete_system_db_entry(parent, model_name, model_datas)

        return True
    else:
      model_data = self.__cs_db_utils.firebase_get(endpoint,record_index)
      if model_data is not None:
        self._update_create_system_db_entry(parent,model_name,record_index,model_data)
        return True
    return False

  def _update_create_system_db_entry(self,parent,model_name,index,data):
    query = [('name', '=', index)]
    creation_data = {'name': index}
    model = sm_utils.get_create_existing_model(parent.env[model_name],query, creation_data)
    model.fetch_db_data(data)

  def _update_delete_system_db_entry(self, parent, model_name, data, index=False):
    if index:
      query = [('name', '=', index)]
    else:
      query = [('name', 'not in', list(data.keys()))]
    sm_utils.delete_existing_model(parent.env[model_name],query)

