# Copyright (c) 2022, Rutwik Hiwalkar and contributors
# For license information, please see license.txt

import json
import frappe
from frappe import _
import requests
from datetime import datetime


def get_analytics_chart(chart_data):
	labels = chart_data["labels"]
	sent = chart_data["sent"]
	failed = chart_data["failed"]
	suspension = chart_data["suspension"]
	return {
		"data": {
			"labels": labels,
			"datasets": [
				{"name": "delivered", "values": sent},
				{"name": "failed", "values": failed},
				{"name": "suspended", "values": suspension},
			],
		},
		"fieldtype": "Int",
		"type": "bar",
		"axisOptions": {"xIsSeries": -1},
	}


def get_report_summary(sent, failed, suspension):
	return [
		{
			"value": sent,
			"indicator": "green",
			"label": "Total Emails Delivered",
			"datatype": "Int",
		},
		{
			"value": failed,
			"indicator": "red",
			"label": "Total Emails Failed",
			"datatype": "Int",
		},
		{
			"value": suspension,
			"indicator": "orange",
			"label": "Total Emails Suspended",
			"datatype": "Int",
		},
	]


def get_columns():
	columns = [
		{"fieldname": "date", "label": _("Date"), "fieldtype": "Data", "width": 100},
		{"fieldname": "status", "label": _("Status"), "fieldtype": "Data", "width": 100},
		{"fieldname": "sender", "label": _("Sender"), "fieldtype": "Long Text", "width": 200},
		{
			"fieldname": "recipient",
			"label": _("Recipient"),
			"fieldtype": "Data",
			"width": 300,
		},
		{"fieldname": "message", "label": _("Message"), "fieldtype": "Data", "width": 500},
	]

	return columns


def get_current_month(this_month):
	if type(this_month) == int:
		return this_month

	months = [
		"All",
		"January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
		"August",
		"September",
		"October",
		"November",
		"December",
	]

	return months.index(this_month)


def get_data_from_api(filters):
	cur_month = get_current_month(filters.get("month", datetime.now().month))
	data = {
		"key": frappe.get_site_config().get("sk_mail"),
		"site": frappe.local.site,
		"month": cur_month,
		"status": "" if filters["status"] == "all" else filters["status"],
	}
	resp = requests.post(
		"https://frappecloud.com/api/method/press.api.email.get_analytics", data=data
	)

	# prepare data based on status
	return json.loads(resp.text)["message"]


def execute(filters=None):
	response = get_data_from_api(filters)

	labels = []
	sent = []
	failed = []
	suspension = []

	for rec in response:
		if rec["date"] not in labels:  # make first entry
			labels.append(rec["date"])
			if rec["status"] == "delivered":
				sent.append(1)
				failed.append(0)
				suspension.append(0)
			elif rec["status"] == "failed":
				failed.append(1)
				sent.append(0)
				suspension.append(0)
			else:
				sent.append(0)
				failed.append(0)
				suspension.append(1)

		elif rec["date"] in labels:  # update existing entry
			ndx = labels.index(rec["date"])
			if rec["status"] == "delivered":
				sent[ndx] += 1
			elif rec["status"] == "failed":
				failed[ndx] += 1
			else:
				suspension[ndx] += 1

	chart_data = {
		"labels": labels,
		"sent": sent,
		"failed": failed,
		"suspension": suspension,
	}
	chart = get_analytics_chart(chart_data)
	report_summary = get_report_summary(sum(sent), sum(failed), sum(suspension))
	columns = get_columns()

	return columns, response, None, chart, report_summary
