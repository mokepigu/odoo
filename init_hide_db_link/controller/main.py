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

import openerp
from openerp.modules.registry import RegistryManager


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
        print 'HIDE DB:' * 10, hide_db
        return {'hide_db': hide_db}

