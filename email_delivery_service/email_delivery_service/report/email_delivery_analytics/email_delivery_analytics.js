// Copyright (c) 2022, Rutwik Hiwalkar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Email Delivery Analytics"] = {
	"filters": [
        {
            "fieldname": "status",
            "label": __("Status"),
            "fieldtype": "Select",
            "options": "all\ndelivered\nfailed",
            "default": "all"
        },
        {
            "fieldname": "month",
            "label": __("Month"),
            "fieldtype": "Select",
            "options": "\nJanuary\nFebruary\nMarch\nApril\nMay\nJune\nJuly\nAugust\nSeptember\nOctober\nNovember\nDecember",
        }
	]
};
