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
    'name' : 'Hide/Show Logs',
    'version': '1.0',
    'summary': 'Hide & Show Logs In Form View',
    'sequence': '19',
    'category': 'INIT',
    'complexity': 'easy',
    'author': 'dev@init.vn',
    'website': 'www.init.vn',
    'description': """
This modules includes feature:
=====================================
* Hide logs in form view, if you want to see these logs, click on 'Show all logs' link
""",
    'data': [
    ],
    'depends' : ['web', 'mail'],
    'js': [
        'static/src/js/*.js',
    ],
    'css': [],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
