# -*- coding: utf-8 -*-
######################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) 2011 OpenERP s.a. (<http://openerp.com>).
# Copyright (C) 2013 INIT Tech Co., Ltd (http://init.vn).
# DatabaseRestrict by Andrey Kolpakov 
#(https://www.odoo.com/forum/help-1/question/how-to-remove-manage-databases-2615)
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

import openerp
from openerp.modules.registry import RegistryManager
from openerp.addons.web.controllers.main import Database, db_list


class Controller(openerp.addons.web.http.Controller):
    _cp_path = '/init_utils/db'

    @openerp.addons.web.http.jsonrequest
    def is_hide_db_link(self, req, dbname):
        """Check to see whether hide Manage Databases link or not"""
        
        registry = RegistryManager.get(dbname)
        hide_db = False
        with registry.cursor() as cr:
            param_obj = registry.get('ir.config_parameter')
            hide_db = param_obj.get_param(cr, openerp.SUPERUSER_ID, 'init.utils.hide_db') == 'True'
        return {'hide_db': hide_db}


class DatabaseRestrict(Database):
    @openerpweb.jsonrequest
    def create(self, req, fields):
        # check if it is not first installation - restrict!
        dblist = db_list(req)
        if len(dblist) > 0:
            raise Exception('Not allowed')

        return super(Database_restrict, self).create(req, fields)

    @openerpweb.jsonrequest
    def duplicate(self, req, fields):
        raise Exception('Not allowed')

    @openerpweb.jsonrequest
    def drop(self, req, fields):
        raise Exception('Not allowed')

    @openerpweb.httprequest
    def backup(self, req, backup_db, backup_pwd, token):
        raise Exception('Not allowed')

    @openerpweb.httprequest
    def restore(self, req, db_file, restore_pwd, new_db):
        raise Exception('Not allowed')

    @openerpweb.jsonrequest
    def change_password(self, req, fields):
        raise Exception('Not allowed')
        
