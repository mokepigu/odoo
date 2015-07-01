# -*- coding: utf-8 -*- 
######################################################################
# 
# OpenERP, Open Source Management Solution 
# Copyright (C) 2011 OpenERP s.a. (<http://openerp.com>). 
# Copyright (C) 2013 INIT Tech Co., Ltd (http://init.vn). 
# This program is free software: you can redistribute it and/or modify 
# it under the terms of the GNU Affero General Public License as 
# published by the Free Software Foundation, either version 3 of the 
# License, or (at your option) any later version. 
# 
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU Affero General Public License for more details. 
# 
# You should have received a copy of the GNU Affero General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>. 
# 
######################################################################

{
    'name': 'Hide Databases Link',
    'version': '1.0',
    'category': 'INIT',
    'sequence': 12,
    'summary': 'Hide Manage Databases Link In Login Page',
    'description': """
This modules includes some utilities:
=====================================
* Hide Manage Databases link: go to Settings > General Settings
 > Tick on "Hide Manage Databases Link In Login Page" to hide and vice versa.
""",
    'author': 'dev@init.vn',
    'website': 'www.init.vn',
    'images': [],
    'depends':['base', 'base_setup', 'web'],
    'data': [
        'view/res_config_view.xml',
    ],
    'js': ['static/src/js/*.js'],
    'qweb': ['static/src/xml/*.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': True,
    'application': True,
}
