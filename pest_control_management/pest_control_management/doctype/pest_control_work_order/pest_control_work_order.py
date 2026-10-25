import frappe
from frappe.utils import get_datetime, time_diff_in_hours


def validate_work_order(doc, method=None):
    # 1. Validate the linked service request
    if not doc.service_request:
        frappe.throw("Please select a Service Request.")

    request = frappe.get_doc(
        "Pest Control Service Request",
        doc.service_request,
    )

    # 2. Populate customer and facility when missing
    if request.customer and not doc.customer:
        doc.customer = request.customer

    if request.facility and not doc.facility:
        doc.facility = request.facility

    # 3. Validate customer
    if request.customer != doc.customer:
        frappe.throw(
            "The work order customer must match "
            "the service request customer."
        )

    # 4. Validate facility
    if request.facility and doc.facility != request.facility:
        frappe.throw(
            "The work order facility must match "
            "the service request facility."
        )

    # 5. Validate assigned technician
    if doc.assigned_technician:
        employee = frappe.get_doc(
            "Employee",
            doc.assigned_technician,
        )

        if employee.status != "Active":
            frappe.throw(
                "Only active employees can be assigned "
                "to a work order."
            )

    # 6. Validate planned schedule and calculate duration
    if doc.planned_start and doc.planned_end:
        start = get_datetime(doc.planned_start)
        end = get_datetime(doc.planned_end)

        if end <= start:
            frappe.throw(
                "Planned End must be later than Planned Start."
            )

        doc.duration_hours = time_diff_in_hours(end, start)

    # 7. Validate work order status
    allowed_statuses = [
        "Scheduled",
        "In Progress",
        "Completed",
        "Cancelled",
    ]

    if doc.work_order_status not in allowed_statuses:
        frappe.throw(
            "Please select a valid Work Order Status."
        )