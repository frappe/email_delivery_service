import frappe
import json
import requests


def after_install():
	"""Setup Email Delivery Service with Frappe Cloud"""
	key = frappe.get_site_config().get("sk_mail", "fcmailsetupkey")
	data = {"key": key, "site": frappe.local.site}

	requests.post("https://frappecloud.com/api/method/press.api.email.setup", data=data)
