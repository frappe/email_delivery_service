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

	if resp.status_code == 200:
		resp = json.loads(resp.text)
		update_queue_status(self, "Sending", commit=True)
	else:
		update_queue_status(self, "Error", resp.exc, commit=True)


@frappe.whitelist(allow_guest=True)
def update_status(**data):
	"""
	Update status of queued email via webhook
	"""
	secret_key = frappe.get_site_config().get("sk_email_delivery_service")
	event_secret_key = data.get("secret_key")
	if not event_secret_key:
		return

	if secret_key == event_secret_key:
		docname = frappe.db.get_value(
			"Email Queue", {"message_id": data["message_id"]}, "name"
		)

		doc = frappe.get_doc("Email Queue", docname)
		if data["status"] == "delivered":
			status = "Sent"
		elif data["status"] == "failed":
			status = "Error"

		update_queue_status(doc, status, commit=True)

	return


def update_queue_status(queue, status, error=None, commit=False):
	frappe.db.set_value("Email Queue", queue.name, "status", status)
	if error:
		frappe.db.set_value("Email Queue", queue.name, "error", error)
	if commit:
		frappe.db.commit()
	if queue.communication:
		communication_doc = frappe.get_doc("Communication", queue.communication)
		communication_doc.set_delivery_status(commit=commit)
