# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.web.controllers.main import Home


class CustomHome(Home):

    @http.route()
    def web_login(self, redirect=None, **kw):
        res = super(CustomHome, self).web_login(redirect, **kw)
        uid = http.request.session.uid
        if uid:
            user = http.request.env['res.users'].sudo().browse(uid)
            if user.has_group('base.group_system'):  # Checks if the user belongs to the Administrator group
                http.request.session['debug'] = 'assets'
        return res
