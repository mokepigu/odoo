
openerp.init_hide_log = function(instance) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

	var module = instance.mail;

	module.ThreadComposeMessage = module.ThreadComposeMessage.extend({
		template: 'mail.compose_message',

		init: function (parent, datasets, options) {
			this.parent = parent;
			this._super(parent, datasets, options);
		},

		bind_events: function () {
			var self = this;
			this.$('.show_all_logs').on('click', self.on_show_all_logs);
			this._super.apply(this, arguments);
		},

		on_show_all_logs: function () {
			this.parent.message_fetch(null, null, this.parent.widget.action.params.message_ids);
		}
	});

	module.Thread = module.Thread.extend({
		init: function (parent, datasets, options) {
			this.widget = parent;
			this._super(parent, datasets, options);
		}
	});

	module.Widget = module.Widget.extend({

		message_render: function (search) {
			this.thread = new module.Thread(this, {}, {
                'domain' : this.domain,
                'context' : this.context,
                'options': this.action.params,
            });

            this.thread.appendTo( this.$el );

            if (this.action.params.show_compose_message) {
                this.thread.instantiate_compose_message();
                this.thread.compose_message.do_show_compact();
            }
		}
	});
}
