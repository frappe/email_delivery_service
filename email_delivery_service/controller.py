import frappe

import json
import requests


def send(self, sender, recipient, msg):
	"""
	Send request to api
	"""
	data = {
		"sender": sender,
		"recipients": recipient,
		"sk_mail": frappe.get_site_config().get("sk_email_delivery_service"),
		"site": frappe.local.site,
	}
	files = {"mime": msg}

	resp = requests.post(
		"https://frappecloud.com/api/method/press.api.email.send_mime_mail",
		data={"data": json.dumps(data)},
		files=files,
	)

	resp = json.loads(resp.text)
	try:
		update_queue_status(self, resp["message"], commit=True)
	except Exception as e:
		frappe.throw(f"{resp['exc_type']}: {resp['exception']}")


@frappe.whitelist(allow_guest=True)
def update_status(**data):
	"""
	Update status of queued email via webhook
	"""
	docname = frappe.db.get_value(
		"Email Queue", {"message_id": data["message_id"]}, "name"
	)

	doc = frappe.get_doc("Email Queue", docname)
	if data["status"] == "delivered":
		status = "Sent"
	elif data["status"] == "failed":
		status = "Error"

	update_queue_status(doc, status, commit=True)


def update_queue_status(queue, status, commit=False):
	frappe.db.set_value("Email Queue", queue.name, "status", status)
	if commit:
		frappe.db.commit()
	if queue.communication:
		communication_doc = frappe.get_doc("Communication", queue.communication)
		communication_doc.set_delivery_status(commit=commit)
