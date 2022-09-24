# Lab Attendance Checker :heavy_check_mark:
## What does it do?

### 1) Checks which students skipped the lab
Compares a csv file of participants to 
the csv file of students in enrolled in the lab section. 
Students in the lab section that are not listed in the
participants did not attend the lab.

### 2) Matches Zoom user names to students' real names
Some students forget to change their zoom name to their full name.
This program tries to match ambiguous students to their
real names.

## How do I use this?

1) Download the participants list csv file from zoom 
([instructions](https://support.zoom.us/hc/en-us/articles/360039017432-Dashboard-for-meetings-and-webinars))
(see formatting guidelines). 

2) Add that csv file to the `student_files/participants` directory. Ensure that this file is the 
*only* file in that directory. Participant files from previous labs can be kept in the 
`student_files/participants/previous` directory.  

3) Obtain a csv file that lists all the students in the lab section 
(see formatting guidelines). 

4) Put the csv file (see formatting guidelines) of all students in the lab section in the `student_files/all_students`
directory. Ensure that this file is the *only* file in that directory.

5) Run `app.py`!

### CSV File Formatting Guidelines
#### Both files
No blank lines unless it's a single blank line at the beginning or end of the file.
#### Participants file  
First line: `Name (Original Name),User Email,Total Duration (Minutes),Guest`  
Next lines: comma-separated values with each comma-separated value corresponding to a column 
(Zoom should take care of this formatting)  
#### All students file  
Students' full names column: first non digit column, values are in the form
`"<last_name>,<first_name>"` or `"<last_name>,<first_name> <middle_name>"` 
TODO