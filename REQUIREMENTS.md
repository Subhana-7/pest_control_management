# Pest Control Management — Business Requirements

## 1. Project Overview

Pest Control Management is a custom Frappe application built on ERPNext. It manages pest control service jobs, manpower allocation, technician schedules, and service completion reports.

The application aims to connect customer service requests with available employees and provide visibility into job progress.

## 2. User Roles

### 2.1 Manager

- Create pest control jobs for existing customers.
- Specify service location, service type, priority, planned date, and required manpower.
- Review job schedules and manpower allocations.
- Monitor the status of all service jobs.
- Review service reports and approve completion or request rework.

### 2.2 Supervisor

- View jobs requiring manpower allocation.
- Assign suitable technicians to jobs.
- Check technician availability and scheduling conflicts.
- Monitor assigned jobs and their progress.
- Review submitted service reports.
- Report operational issues and request additional manpower.

### 2.3 Technician

- View assigned jobs and schedules.
- View customer and service-location details required to perform the job.
- Update assignment status according to permitted workflow transitions.
- Record work performed, observations, and materials used where applicable.
- Submit a service report after completing the work.
- Report incomplete work or operational issues.

## 3. End-to-End Workflow

1. The manager creates a pest control job and selects an existing customer.
2. The manager provides service details, location, date, priority, and manpower requirements.
3. The supervisor reviews the job and assigns available technicians.
4. The system validates employee availability and prevents overlapping active assignments.
5. The technician views the assignment and performs the service.
6. The technician records the work performed and submits a service report.
7. The supervisor reviews the report and either approves it or requests rework.
8. Once the required reports are approved, the job can be marked Completed.
9. The manager monitors the final job status.

## 4. Functional Requirements

- Maintain pest control job records.
- Allocate one or more technicians to a job.
- Assign a supervisor to oversee the work.
- Track job and assignment statuses.
- Validate employee availability and schedule conflicts.
- Record service reports and review outcomes.
- Provide role-based access to jobs, assignments, and reports.
- Maintain traceability of job status changes.

## 5. Business Rules

- Each job must reference a valid customer.
- Each job must contain a service location, planned date, and service type.
- Each manpower assignment must reference a valid job and employee.
- An employee must not have overlapping active assignments.
- Only authorized users may allocate manpower or approve service reports.
- A job cannot be completed until its required service reports are approved.
- Cancelled jobs must not receive new active assignments.
- Rework must be recorded without losing the original service history.

## 6. Scope Assumptions

- ERPNext Customer and Employee records will be reused where suitable.
- HRMS and ONEFM availability must be confirmed before depending on their functionality.
- Attendance, inventory consumption, billing, GPS tracking, and customer signatures are optional extensions unless explicitly required.
- The first implementation focuses on job management, manpower allocation, and service reporting.

## 7. Acceptance Criteria

- A manager can create a pest control job.
- A supervisor can assign technicians to that job.
- Scheduling conflicts are rejected.
- A technician can submit a service report.
- A supervisor can approve a report or request rework.
- Job completion follows the defined validation rules.
- Each role can access only the records and actions permitted to it.