# -*- coding: utf-8 -*-
{
  'name': "sm_partago_db",

  'summary': """
    Module showing some carsharing app models into odoo
  """,

  'author': "Som Mobilitat",
  'website': "https://www.sommobilitat.coop",

  # Categories can be used to filter modules in modules listing
  # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
  # for the full list
  'category': 'vertical-carsharing',
  'version': '12.0.0.0.8',

  # any module necessary for this one to work correctly
  'depends': ['base','vertical_carsharing'],

  # always loaded
  'data': [
    'security/ir.model.access.csv',
    'views/views.xml',
    'views/views_car.xml',
    'views/views_car_config.xml',
    'views/views_group_config.xml',
    'views/views_group.xml',
    'views/views_billing_account.xml',
    'views/views_wizards.xml',
    'views/views_cron.xml'
  ],
  # only loaded in demonstration mode
  'demo': [],
}
