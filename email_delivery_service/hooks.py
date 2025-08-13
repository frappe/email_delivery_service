from . import __version__ as app_version

app_name = "email_delivery_service"
app_title = "Email Delivery Service"
app_publisher = "Rutwik Hiwalkar"
app_description = "."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "rutwik@frappe.io"
app_license = "MIT"

override_email_send = ["email_delivery_service.controller.send"]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/email_delivery_service/css/email_delivery_service.css"
# app_include_js = "/assets/email_delivery_service/js/email_delivery_service.js"

# include js, css files in header of web template
# web_include_css = "/assets/email_delivery_service/css/email_delivery_service.css"
# web_include_js = "/assets/email_delivery_service/js/email_delivery_service.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "email_delivery_service/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "email_delivery_service.utils.jinja_methods",
# 	"filters": "email_delivery_service.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "email_delivery_service.install.before_install"
after_install = "email_delivery_service.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "email_delivery_service.uninstall.before_uninstall"
# after_uninstall = "email_delivery_service.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "email_delivery_service.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"email_delivery_service.tasks.all"
# 	],
# 	"daily": [
# 		"email_delivery_service.tasks.daily"
# 	],
# 	"hourly": [
# 		"email_delivery_service.tasks.hourly"
# 	],
# 	"weekly": [
# 		"email_delivery_service.tasks.weekly"
# 	],
# 	"monthly": [
# 		"email_delivery_service.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "email_delivery_service.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "email_delivery_service.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "email_delivery_service.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

fixtures = [
    "Client Script",
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"email_delivery_service.auth.validate"
# ]
