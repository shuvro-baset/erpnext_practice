# Copyright (c) 2022, shuvro baset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class VehicleAvailability(Document):
	def before_save(self):
		self.chassis_number = f'{self.chassis_number}'

		