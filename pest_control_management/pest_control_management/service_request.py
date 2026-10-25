
import frappe
from frappe.utils import getdate, today


DOCTYPE = "Pest Control Service Request"

ALLOWED_TRANSITIONS = {
    "Draft": {"Requested", "Cancelled"},
    "Requested": {"Scheduled", "Cancelled"},
    "Scheduled": {"In Progress", "Cancelled"},
    "In Progress": {"Completed", "Cancelled"},
    "Completed": set(),
    "Cancelled": set(),
}


def validate_service_request(doc, method=None):
    """Validate customer service requests on the server."""

    # Set a default status for new requests.
    if doc.is_new() and not doc.status:
        doc.status = "Draft"

    # Required-field checks.
    if not doc.customer:
        frappe.throw("Please select a Customer.")

    if not doc.pest_type:
        frappe.throw("Please select a Pest Type.")

    if not doc.urgency:
        frappe.throw("Please select an Urgency.")

    if not doc.requested_date:
        frappe.throw("Please enter the Requested Date.")

           # Validate the selected facility.
    if doc.facility:
        facility = frappe.get_doc(
            "Pest Control Facility",
            doc.facility
        )

        if facility.customer != doc.customer:
            frappe.throw(
                "The selected facility must belong to the selected customer."
            )

        if facility.status != "Active":
            frappe.throw(
                "You cannot create a service request for an inactive facility."
            )

        # Validate the Customer–Lead relationship.
    if doc.lead:
        lead = frappe.get_doc("Lead", doc.lead)

    # If the Lead is linked to a Customer, they must match.
    if lead.get("customer") and lead.customer != doc.customer:
        frappe.throw(
            "The selected Lead is linked to a different Customer."
        )

    # Prevent new requests from being scheduled in the past.
    if doc.is_new() and getdate(doc.requested_date) < getdate(today()):
        frappe.throw("Requested Date cannot be in the past.")

    # Check the initial status of a new request.
    if doc.is_new():
        if doc.status not in {"Draft", "Requested"}:
            frappe.throw(
                "A new request must start with Draft or Requested status."
            )
        return

    # Check status transitions for existing requests.
    old_doc = doc.get_doc_before_save()


    if not old_doc:
        return

    old_status = old_doc.status
    new_status = doc.status

    # Saving without changing the status is allowed.
    if old_status == new_status:
        return

    allowed = ALLOWED_TRANSITIONS.get(old_status, set())

    if new_status not in allowed:
        frappe.throw(
            f"Invalid status transition: {old_status} → {new_status}. "
            "Please follow the permitted workflow."
        )
