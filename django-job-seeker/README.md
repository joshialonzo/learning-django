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
    * type: Startup | Factory | Enterprise
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
    * type: Recruiter | Programmer | Leader
* Recruiter
    * Parent: Worker
* Programmer
    * Parent: Worker

### Jobs

* Message
    * Channel
    * From
    * To
    * Date
* Job Description
    * Title
    * Description
    * Minimum salary
    * maximum salary
    * url
* Selection Process
    * Recruitment Firm
    * Software Company
    * Technologies
    * Stages
    * Messages
* Stage
    * Selection Process
* Interview
    * Selection Process
    * Channel
    * Stage
    * Date
* Question
    * Interview

### Quizzes

* Quizz
    * Technology
    * Questions
* Question
    * Technology

## Relationships

...