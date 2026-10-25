# Pest Control Management — DocType Inventory

## 1. Environment

- Framework: Frappe v15
- ERP system: ERPNext v15
- Custom app: pest_control_management
- Site: frappe.local

## 2. Installed Applications

Confirmed installed applications:

| Application | Version | Purpose |
|---|---|---|
| frappe | 15.122.0 | Framework |
| erpnext | 15.123.0 | ERP functionality |
| demo_app | 0.0.1 | Existing custom application |
| pest_control_management | 0.0.1 | New pest control application |

## 3. Existing DocTypes Inspected

### 3.1 CRM

| DocType | Finding | Proposed use |
|---|---|---|
| Lead | Found under CRM | Track potential customers where needed |
| Opportunity | Found under CRM | Track potential sales opportunities |
| CRM Settings | Found under CRM | Existing CRM configuration |
| CRM Note | Found under CRM | Existing CRM notes |
| Frappe CRM Allowed User | Found under CRM | Existing CRM access configuration |

The Lead and Opportunity records are not substitutes for an actual service job.

### 3.2 Customer Management

| DocType | Finding | Proposed use |
|---|---|---|
| Customer | Confirmed under Selling | Reuse for customer records |
| Customer Group | Found under Setup | Reuse for customer categorization |

The Customer form includes customer name, customer type, customer group, and references to Lead and Opportunity records.

### 3.3 Employee and Organization

| DocType | Finding | Proposed use |
|---|---|---|
| Employee | Confirmed under Setup | Reuse for technicians and supervisors |
| Department | Confirmed under Setup | Reuse for organizational grouping |
| Designation | Confirmed under Setup | Reuse for job titles and designations |

The existence of these DocTypes does not confirm that a separate HRMS application is installed.

### 3.4 Task Management

| DocType | Finding | Proposed use |
|---|---|---|
| Task | Found under Projects | Evaluate for general task tracking |

Task may be useful for internal work tracking, but pest control service jobs require domain-specific fields and validation.

## 4. ONEFM Investigation

Searches for DocTypes containing HR and ONEFM returned no matching results in the inspected list.

The installed application directories were:

- demo_app
- erpnext
- frappe
- pest_control_management

No separately named ONEFM app directory was visible in this output.

Conclusion: ONEFM functionality has not been identified in the current installation. Confirm the company's ONEFM requirements and whether a separate app will be provided before implementing integrations.

## 5. Reuse vs. Custom Development

| Requirement | Decision |
|---|---|
| Customer master | Reuse Customer |
| Employee master | Reuse Employee |
| Departments | Reuse Department |
| Employee designations | Reuse Designation |
| Potential customer tracking | Reuse Lead where relevant |
| Sales opportunity tracking | Reuse Opportunity where relevant |
| Pest control job | Create custom DocType |
| Manpower assignment | Create custom DocType |
| Service report | Create custom DocType |

## 6. Outstanding Checks

- Confirm whether the company provides an ONEFM application.
- Confirm whether HRMS-specific features are required.
- Inspect Employee fields needed for technician availability and eligibility.
- Check whether existing address and contact records meet service-location requirements.
- Confirm service report, material usage, attendance, and approval requirements with the interviewer.