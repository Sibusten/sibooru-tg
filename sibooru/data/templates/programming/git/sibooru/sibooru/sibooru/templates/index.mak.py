# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1482340131.269525
_enable_loop = True
_template_filename = 'l:\\programming\\git\\sibooru\\sibooru\\sibooru\\templates\\index.mak'
_template_uri = '/programming/git/sibooru/sibooru/sibooru/templates/index.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'local:templates.master', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n<div class="row">\r\n  <div class="col-md-8">\r\n    <div class="jumbotron">\r\n      <h1>Welcome to TurboGears 2.3</h1>\r\n      <p>If you see this page it means your installation was successful!</p>\r\n      <p>TurboGears 2 is rapid web application development toolkit designed to make your life easier.</p>\r\n      <p>\r\n        <a class="btn btn-primary btn-lg" href="http://www.turbogears.org" target="_blank">\r\n          ')
        __M_writer(escape(h.icon('book')))
        __M_writer(' Learn more\r\n        </a>\r\n      </p>\r\n    </div>\r\n  </div>\r\n  <div class="col-md-4 hidden-xs hidden-sm">\r\n    <a class="btn btn-info btn-sm active" href="http://turbogears.readthedocs.io/en/latest">')
        __M_writer(escape(h.icon('book')))
        __M_writer(' TG2\r\n      Documentation</a> <span class="label label-success">new</span><em> Get Started</em><br/>\r\n    <br/>\r\n    <a class="btn btn-info btn-sm active" href="http://turbogears.readthedocs.io/en/latest/cookbook/cookbook.html">')
        __M_writer(escape(h.icon('book')))
        __M_writer('\r\n      TG2 CookBook</a><em> Read the Cookbook</em> <br/>\r\n    <br/>\r\n    <a class="btn btn-info btn-sm active" href="http://groups.google.com/group/turbogears">')
        __M_writer(escape(h.icon('comment')))
        __M_writer(' Join the\r\n      Mail List</a> <em>for help/discussion</em><br/>\r\n    <br/>\r\n    <a class="btn btn-info btn-sm active" href="http://runnable.com/TurboGears">')
        __M_writer(escape(h.icon('play')))
        __M_writer(' Play on Runnable</a>\r\n    <em>for basic examples</em><br/>\r\n    <br/>\r\n    <a class="btn btn-info btn-sm active" href="http://stackoverflow.com/questions/tagged/turbogears2">')
        __M_writer(escape(h.icon('search')))
        __M_writer('\r\n      Search Stackoverflow</a> <em>for questions</em>\r\n  </div>\r\n</div>\r\n\r\n<div class="row">\r\n  <div class="col-md-4">\r\n    <h3>Code your data model</h3>\r\n    <p> Design your data <code>model</code>, Create the database, and Add some bootstrap data.</p>\r\n  </div>\r\n\r\n  <div class="col-md-4">\r\n    <h3>Design your URL architecture</h3>\r\n    <p> Decide your URLs, Program your <code>controller</code> methods, Design your\r\n      <code>templates</code>, and place some static files (CSS and/or Javascript). </p>\r\n  </div>\r\n\r\n  <div class="col-md-4">\r\n    <h3>Distribute your app</h3>\r\n    <p> Test your source, Generate project documents, Build a distribution.</p>\r\n  </div>\r\n</div>\r\n\r\n<em class="pull-right small"> Thank you for choosing TurboGears.</em>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\r\nWelcome to TurboGears 2.3, standing on the shoulders of giants, since 2007\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"34": 1, "35": 5, "36": 14, "37": 14, "38": 20, "39": 20, "40": 23, "41": 23, "42": 26, "43": 26, "44": 29, "45": 29, "46": 32, "47": 32, "53": 3, "57": 3, "28": 0, "63": 57}, "filename": "l:\\programming\\git\\sibooru\\sibooru\\sibooru\\templates\\index.mak", "uri": "/programming/git/sibooru/sibooru/sibooru/templates/index.mak", "source_encoding": "utf-8"}
__M_END_METADATA
"""
