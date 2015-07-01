openerp.init_hide_db_link = function(instance) {
    
    instance.web.Login.include({
        init: function(parent, action) {
            var self = this;
            console.log("THIS IS NEW COMME");
            self._super(parent, action);
            self.hide_db = false;
            // check to see hide db link or not
            var dbname = self.selected_db;
            if (dbname) {
                self.rpc("/init_utils/db/is_hide_db_link", {dbname: dbname}).then(function(result) {
                    console.log('hide db', result);
                    self.hide_db = result.hide_db;
                    if (self.hide_db) {
                        footer = '<a href="http://www.openerp.com" target="_blank">Powered by <span>OpenERP</span></a>'
                        $('.oe_login_footer').html(footer);
                    }
                });
            }
            
        },
        
    });
};
