# Pest Control Management — Data Design

## 1. Design Goals

- Reuse existing ERPNext master records.
- Avoid duplicate customer and employee data.
- Separate service jobs from individual employee assignments.
- Track work performed and service approval.
- Enforce scheduling, status, and permission rules on the server.

## 2. Proposed Custom DocTypes

### 2.1 Pest Control Job

Purpose: Represents a pest control service request.

Proposed fields:

| Field | Type | Required | Description |
|---|---|---|---|
| job_title | Data | Yes | Short job description |
| customer | Link: Customer | Yes | Customer requesting service |
| service_location | Small Text | Yes | Address where service is performed |
| service_type | Select | Yes | Type of pest control service |
| priority | Select | Yes | Low, Medium, High, Urgent |
| planned_date | Date | Yes | Planned service date |
| required_technicians | Int | Yes | Number of technicians required |
| supervisor | Link: Employee | No | Responsible supervisor |
| status | Select | Yes | Current job status |
| description | Text Editor | No | Detailed requirements |
| completion_notes | Small Text | No | Summary of completion |

Proposed status values:

Draft, Open, Scheduled, In Progress, Completed, Cancelled.

### 2.2 Manpower Assignment

Purpose: Represents one employee's assignment to one pest control job.

Proposed fields:

| Field | Type | Required | Description |
|---|---|---|---|
| pest_control_job | Link: Pest Control Job | Yes | Job being staffed |
| technician | Link: Employee | Yes | Assigned employee |
| supervisor | Link: Employee | No | Supervisor overseeing assignment |
| start_datetime | Datetime | Yes | Planned start |
| end_datetime | Datetime | Yes | Planned end |
| status | Select | Yes | Assignment status |
| assignment_notes | Small Text | No | Notes for the assignment |

Proposed status values:

Assigned, Accepted, In Progress, Completed, Cancelled.

### 2.3 Service Report

Purpose: Records the work performed for a service job.

Proposed fields:

| Field | Type | Required | Description |
|---|---|---|---|
| pest_control_job | Link: Pest Control Job | Yes | Related service job |
| manpower_assignment | Link: Manpower Assignment | Yes | Related assignment |
| work_performed | Text Editor | Yes | Description of work |
| observations | Small Text | No | Findings at the site |
| materials_used | Small Text | No | Materials or chemicals used |
| report_status | Select | Yes | Review status |
| reviewer | Link: Employee | No | Person reviewing report |
| review_comments | Small Text | No | Approval or rework notes |

Proposed report statuses:

Draft, Submitted, Approved, Rework Required.

## 3. Relationships

- One Customer can have many Pest Control Jobs.
- One Pest Control Job can have many Manpower Assignments.
- One Employee can have many Manpower Assignments over time.
- One Pest Control Job can have multiple Service Reports.
- Each Service Report references the relevant job and assignment.

## 4. Status Transition Rules

### Pest Control Job

- Draft → Open
- Open → Scheduled
- Scheduled → In Progress
- In Progress → Completed
- In Progress → Scheduled when rework or rescheduling is required
- Draft, Open, or Scheduled → Cancelled, subject to authorization

A job can become Completed only when the required reports have been approved and all required work is complete.

### Manpower Assignment

- Assigned → Accepted
- Accepted → In Progress
- In Progress → Completed
- Assigned or Accepted → Cancelled, subject to authorization

If the business requires technician acceptance, the transition must be enforced before work starts.

### Service Report

- Draft → Submitted
- Submitted → Approved
- Submitted → Rework Required
- Rework Required → Submitted

The reviewer must be authorized to approve reports.

## 5. Validation Rules

1. Customer must reference an existing Customer record.
2. Required dates and service details must be supplied before a job is submitted.
3. required_technicians must be greater than zero.
4. Assignment start_datetime must be earlier than end_datetime.
5. The technician and supervisor must reference valid Employee records.
6. A technician must not have overlapping active assignments.
7. A cancelled job must not receive new active assignments.
8. A completed job must have all required reports approved.
9. A report must reference an assignment belonging to the same job.
10. Invalid status transitions must be rejected by server-side validation.

## 6. Permission Design

### Manager

- Create and view service jobs.
- Define job requirements and priority.
- View manpower allocation and progress.
- Approve completion, subject to workflow permissions.

### Supervisor

- View jobs assigned to their operational scope.
- Create or update manpower assignments.
- Monitor technician progress.
- Review service reports and request rework or approve them.

### Technician

- View their own assignments and the necessary job details.
- Update permitted assignment statuses.
- Create and submit service reports for their assignments.
- Cannot allocate other technicians or approve their own reports.

### System Enforcement

- Define roles and DocType permissions.
- Apply document-level access restrictions where necessary.
- Validate operations on the server.
- Do not rely on hidden buttons or client-side restrictions as the sole security control.

## 7. Implementation Notes

- Create the custom DocTypes inside the pest_control_management app.
- Use Link fields to reference existing Customer and Employee records.
- Implement overlap detection and cross-document validation in Python.
- Use a Frappe Workflow or explicit server-side transition rules for status management.
- Test each role using separate user accounts.
- Confirm the final fields and statuses against the interview requirements before implementation.