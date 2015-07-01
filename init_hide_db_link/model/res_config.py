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

from openerp.osv import osv, fields


class base_config_settings(osv.TransientModel):
    _inherit = 'base.config.settings'

    _columns = {
        'init_hide_db_link_hide': fields.boolean('Hide Manage Databases Link In Login Page'),
    }
    
    def get_default_hide_db_link(self, cr, uid, fields, context=None):
        hide_db = self.pool.get("ir.config_parameter").get_param(cr, uid, "init.utils.hide_db") or ""
        return {'init_hide_db_link_hide': hide_db}
    
    def set_hide_db_link(self, cr, uid, ids, context=None):
        hide_db = self.browse(cr, uid, ids[0], context)['init_hide_db_link_hide'] or ''
        self.pool.get("ir.config_parameter").set_param(cr, uid, "init.utils.hide_db", hide_db)
        

