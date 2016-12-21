# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1482334411.346364
_enable_loop = True
_template_filename = 'l:\\programming\\git\\sibooru\\sibooru\\sibooru\\templates\\master.mak'
_template_uri = '/programming/git/sibooru/sibooru/sibooru/templates/master.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['main_menu', 'body_class', 'meta', 'title', 'head_content', 'footer', 'content_wrapper']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    ')
        __M_writer(escape(self.meta()))
        __M_writer('\r\n    <title>')
        __M_writer(escape(self.title()))
        __M_writer('</title>\r\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/bootstrap.min.css')))
        __M_writer('" />\r\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/style.css')))
        __M_writer('" />\r\n    ')
        __M_writer(escape(self.head_content()))
        __M_writer('\r\n</head>\r\n<body class="')
        __M_writer(escape(self.body_class()))
        __M_writer('">\r\n    ')
        __M_writer(escape(self.main_menu()))
        __M_writer('\r\n  <div class="container">\r\n    ')
        __M_writer(escape(self.content_wrapper()))
        __M_writer('\r\n  </div>\r\n    ')
        __M_writer(escape(self.footer()))
        __M_writer('\r\n  <script src="http://code.jquery.com/jquery.js"></script>\r\n  <script src="')
        __M_writer(escape(tg.url('/javascript/bootstrap.min.js')))
        __M_writer('"></script>\r\n</body>\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <!-- Navbar -->\r\n  <nav class="navbar navbar-default">\r\n    <div class="navbar-header">\r\n      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-content">\r\n        <span class="sr-only">Toggle navigation</span>\r\n        <span class="icon-bar"></span>\r\n        <span class="icon-bar"></span>\r\n        <span class="icon-bar"></span>\r\n      </button>\r\n      <a class="navbar-brand" href="')
        __M_writer(escape(tg.url('/')))
        __M_writer('">\r\n        <img src="')
        __M_writer(escape(tg.url('/img/turbogears_logo.png')))
        __M_writer('" height="20" alt="TurboGears 2"/>\r\n        ')
        __M_writer(escape(getattr(tmpl_context, 'project_name', 'turbogears2')))
        __M_writer('\r\n      </a>\r\n    </div>\r\n\r\n    <div class="collapse navbar-collapse" id="navbar-content">\r\n      <ul class="nav navbar-nav">\r\n        <li class="')
        __M_writer(escape(('', 'active')[page=='index']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/')))
        __M_writer('">Welcome</a></li>\r\n        <li class="')
        __M_writer(escape(('', 'active')[page=='about']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/about')))
        __M_writer('">About</a></li>\r\n        <li class="')
        __M_writer(escape(('', 'active')[page=='data']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/data')))
        __M_writer('">Serving Data</a></li>\r\n        <li class="')
        __M_writer(escape(('', 'active')[page=='environ']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/environ')))
        __M_writer('">WSGI Environment</a></li>\r\n      </ul>\r\n\r\n')
        if tg.auth_stack_enabled:
            __M_writer('      <ul class="nav navbar-nav navbar-right">\r\n')
            if not request.identity:
                __M_writer('        <li><a href="')
                __M_writer(escape(tg.url('/login')))
                __M_writer('">Login</a></li>\r\n')
            else:
                __M_writer('        <li><a href="')
                __M_writer(escape(tg.url('/logout_handler')))
                __M_writer('">Logout</a></li>\r\n        <li><a href="')
                __M_writer(escape(tg.url('/admin')))
                __M_writer('">Admin</a></li>\r\n')
            __M_writer('      </ul>\r\n')
        __M_writer('    </div>\r\n  </nav>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        response = context.get('response', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <meta charset="')
        __M_writer(escape(response.charset))
        __M_writer('" />\r\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <footer class="footer hidden-xs hidden-sm">\r\n    <a class="pull-right" href="http://www.turbogears.org"><img style="vertical-align:middle;" src="')
        __M_writer(escape(tg.url('/img/under_the_hood_blue.png')))
        __M_writer('" alt="TurboGears 2" /></a>\r\n    <p>Copyright &copy; ')
        __M_writer(escape(getattr(tmpl_context, 'project_name', 'TurboGears2')))
        __M_writer(' ')
        __M_writer(escape(h.current_year()))
        __M_writer('</p>\r\n  </footer>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  ')

        flash=tg.flash_obj.render('flash', use_js=False)
          
        
        __M_writer('\r\n')
        if flash:
            __M_writer('      <div class="row">\r\n        <div class="col-md-8 col-md-offset-2">\r\n              ')
            __M_writer(flash )
            __M_writer('\r\n        </div>\r\n      </div>\r\n')
        __M_writer('  ')
        __M_writer(escape(self.body()))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"17": 0, "24": 1, "25": 4, "26": 4, "27": 5, "28": 5, "29": 6, "30": 6, "31": 7, "32": 7, "33": 8, "34": 8, "35": 10, "36": 10, "37": 11, "38": 11, "39": 13, "40": 13, "41": 15, "42": 15, "43": 17, "44": 17, "45": 32, "46": 34, "47": 38, "48": 39, "49": 41, "50": 48, "51": 86, "57": 50, "66": 50, "67": 60, "68": 60, "69": 61, "70": 61, "71": 62, "72": 62, "73": 68, "74": 68, "75": 68, "76": 68, "77": 69, "78": 69, "79": 69, "80": 69, "81": 70, "82": 70, "83": 70, "84": 70, "85": 71, "86": 71, "87": 71, "88": 71, "89": 74, "90": 75, "91": 76, "92": 77, "93": 77, "94": 77, "95": 78, "96": 79, "97": 79, "98": 79, "99": 80, "100": 80, "101": 82, "102": 84, "108": 34, "117": 35, "122": 35, "123": 36, "124": 36, "130": 41, "134": 41, "140": 39, "149": 43, "157": 43, "158": 45, "159": 45, "160": 46, "161": 46, "162": 46, "163": 46, "169": 20, "175": 20, "176": 21, "180": 23, "181": 24, "182": 25, "183": 27, "184": 27, "185": 31, "186": 31, "187": 31, "193": 187}, "filename": "l:\\programming\\git\\sibooru\\sibooru\\sibooru\\templates\\master.mak", "uri": "/programming/git/sibooru/sibooru/sibooru/templates/master.mak", "source_encoding": "utf-8"}
__M_END_METADATA
"""
