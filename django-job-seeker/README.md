# Job Seeker

This is an open-source application focused on the tools needed by a programmer to find a job like tracking job offers, selection processes, companies, and recruiters.

## Apps

This project is composed of several Django applications:

* Companies
* Workers
* Technologies
* Jobs
* Quizzes

## Models

Each one of the applications is composed of models and relationships. Next, we have descriptions for each one of the models.

### Companies

* Job Type
    * Name

* Company
    * Company type: Job Type
    * Company URL
    * LinkedIn ID
    * Country

* Headhunter Company
    * Parent: Company

* Software Company
    * Parent Company
    * Sofwtare company type: Startup | Factory | Enterprise
    * Industry: Energy | Marketing | Cybersecurity

### Technologies

* Stack
    * Name
    * Technologies

* Technology
    * Name

* Course
    * Name
    * Technologies

### Workers

* Worker
    * First name
    * Second name
    * LinkedIn ID
    * Position
    * Company

* Recruiter
    * Parent: Worker

* Programmer
    * Parent: Worker

### Jobs

* Message
    * Channel
    * Language
    * Sender
    * Receiver
    * Timestamp
    * Email
    * Phone
    * Text

* Job Description
    * Title
    * Minimum salary
    * Maximum salary
    * URL
    * Schema: Payroll | Contractor
    * Location: Remote | Hybrid | On-site
    * Status
    * Description
    * Technologies
    * Software Company

* Selection Process
    * Job Description
    * Headhunting Firm
    * Status

* Question
    * Text
    * Answer

* Stage
    * Selection Process
    * Number
    * Channel
    * Platform
    * Date
    * Questions

### Quizzes

* Quizz
    * Technology
    * Questions

* Question
    * Technology

## Relationships

...