import frappe

import json
import requests

def get_exception_message(error: dict):
	srv_msgs = error.get("_server_messages")
	if srv_msgs:
		return '\n'.join(msg['message'] for msg in srv_msgs)
	return error['exception']

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
		update_queue_status(self, "Sending", commit=True)
	else:
		try:
			error = resp.json()
			exc_type = error["exc_type"]
			exception = get_exception_message(error)
			frappe.throw(exc=exc_type, msg=exception)
		except (json.decoder.JSONDecodeError, KeyError):
			error = resp.text
			frappe.throw(error, requests.HTTPError)


@frappe.whitelist(allow_guest=True)
def update_status(**data):
	"""
	Update status of queued email via webhook
	"""
	secret_key = frappe.get_site_config().get("sk_email_delivery_service")
	event_secret_key = data.get("secret_key")
	if not event_secret_key:
		return

	if secret_key != event_secret_key:
		return

	q_name = frappe.db.get_value("Email Queue", {"message_id": data["message_id"]}, "name")
	q = frappe.get_doc("Email Queue", q_name)

	error = ""
	status = "Sent"  # Default status by SendMailContext

	if data["status"] == "failed":
		status = "Error"
		error = data.get("delivery_message")

	update_queue_status(q, status, error, commit=True)


def update_queue_status(queue, status, error: str = "", commit=False):
	frappe.db.set_value("Email Queue", queue.name, "status", status)
	if error:
		frappe.db.set_value("Email Queue", queue.name, "error", error)
	if commit:
		frappe.db.commit()
	if queue.communication:
		communication_doc = frappe.get_doc("Communication", queue.communication)
		communication_doc.set_delivery_status(commit=commit)
