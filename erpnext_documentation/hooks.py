# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_documentation"
app_title = "ERPNext Documentation"
app_publisher = "Frappe Technologies Pvt Ltd"
app_description = "To manage erpnext user manual"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@erpnext.com"
app_license = "MIT"


website_context = {
	"repo": "frappe/erpnext_documentation",
	"hide_login": 1,
	"favicon": "/assets/erpnext_documentation/img/erpnext-logo-blue.png"
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_documentation/css/erpnext_documentation.css"
# app_include_js = "/assets/erpnext_documentation/js/erpnext_documentation.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_documentation/css/erpnext_documentation.css"
# web_include_js = "/assets/erpnext_documentation/js/erpnext_documentation.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "index"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_documentation.utils.get_home_page"

base_template_map = {
	r'docs/v\d{1,3}/user/manual.*': 'templates/erpnext_docs.html'
}

website_redirects = [
	{"source": r"/docs/user(.*)", "target": r"/docs/v13/user\1"},
]

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_documentation.install.before_install"
# after_install = "erpnext_documentation.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_documentation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_documentation.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_documentation.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_documentation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_documentation.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_documentation.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_documentation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_documentation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "erpnext_documentation.task.get_dashboard_data"
# }

