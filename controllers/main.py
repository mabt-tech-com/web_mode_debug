# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.web.controllers.main import Home


class Home(Home):

    @http.route()
    def web_login(self, redirect=None, **kw):
        res = super().web_login(redirect, **kw)
        uid = http.request.uid
        if uid:
            user = http.request.env['res.users'].sudo().browse(uid)
            if user._is_admin() or user._is_superuser():
                http.request.session['debug'] = 'assets'
        return res
