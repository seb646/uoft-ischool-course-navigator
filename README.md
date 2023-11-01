# University of Toronto iSchool Course Navigator
This program helps users navigate the Univeristy of Toronto's Faculty of Information (iSchool)'s course catalogue. It scrapes data directly from the Faculty's website, and makes it available to users through a command-line interface. Users can search for an undergraduate or graduate course using the course's code (ex: `INF452`) and view information such as the course title, official course description, and any available syllabi from previous sessions. 

## Getting Started

### Requirements
This script was developed in Python and requires at least Python 3 to run (tested using Python version 3.11.5). The program is also dependant on the [Requests](https://requests.readthedocs.io/en/latest/) HTTP client library for Python and the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) HTML and XML document parsing library for Python. 

### Execution Instructions
Navigate to the directory housing the `course_navigator.py` script. Once your terminal is in the same location as the script (which you can confirm by typing `ls` to view all files in your working directory), use the following command to run the script:

```bash
python3 course_navigator.py
```
> **Note**<br>
> Your command to initiate Python may vary depending on your computer's configuration. For my computer, the command for running a Python 3 script is `python3` but your computer may use `python`, for example.

### Sample Output
Once the script executes, you will be greeted with the program's startup message:

```
--------------------------------------------------------------------------------
UNIVERSITY OF TORONTO FACULTY OF INFORMATION COURSE NAVIGATOR
--------------------------------------------------------------------------------
This tool allows you to browse information on all available iSchool courses.

• Undergraduate courses format: INF000
• Graduate courses format: INF0000

Please be patient! We fetch data live from the iSchool's website so it may
take some time to load. We'll let you know when it's ready!
```
Seeing this message indicates that the script is running and is in the process of scraping data live from the Faculty of Information's website. Once the scraped data is stored in your Python session, you will be alerted with the following message:

```
--------------------------------------------------------------------------------
Courses loaded! HINT: You can leave at any time by typing "exit".
--------------------------------------------------------------------------------
To learn about a course, enter a course code: 
```
At this point, you may enter in a valid code of a course offered by the Faculty. Courses are coded in the following format: 

* Undergraduate courses are styled `INF000`, with 3 digits. (Ex: `INF452`)
* Graduate courses are styled `INF0000`, with 4 digits. (Ex: `INF1330`)

Course codes are not case sensitive, but they must match a couse code listed on [this page](https://ischool.utoronto.ca/current-students/programs-courses/courses/course-list).

#### Exiting the program
Once the data is loaded, you may safely exit the program at any time by typing `exit` instead of a course code. 

## How It Works

The program begins by requesting data from this page of the Faculty's website: [https://ischool.utoronto.ca/current-students/programs-courses/courses/course-list](https://ischool.utoronto.ca/current-students/programs-courses/courses/course-list). It parses the page, turning the text into a Python-readable format and finds each row of the two tables (representing both undergraduate and graduate courses). It then loads the course code, course title, and course link into a Python dictionary.

Next, the program iterates through the new Python dictonary and uses the links found in the previous step to request data from individual course pages from the Faculty's website. It parses the individual course page, loading the course description and any available syllabi into the Python dictionary. 

To find a course, the program matches the user's input against all available course codes listed in the dictionary. If the user's input is found within the dictionary, it returns the collected course information. If the user's input does not match any course within the dictionary, it returns a notification to the user and a prompt to enter a different course code. If the user enters the `exit` command, the program will end and the user will lose all scraped data.

Each time the script runs, the program will fetch data live from the Faculty's website at the aforementioned URL. While this provides the most up-to-date information, if the HTML structure of the page changes this program may not function as expected. 

## Acknowledgments 
Created by [Sebastian Rodriguez](https://srod.ca), licensed under the [BSD 3-Clause License](https://github.com/seb646/uoft-ischool-course-navigator/blob/main/LICENSE). Built using Python 3, the [Requests](https://requests.readthedocs.io/en/latest/) HTTP client library for Python, and the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) HTML and XML document parsing library for Python. 

Prepared for [Dr. Maher Elshakankiri](https://ischool.utoronto.ca/profile/maher-elshakankiri), instructor of [INF452: Information Design Studio V: Coding](https://ischool.utoronto.ca/course/information-design-studio-v-coding) and Assistant Professor, Teaching Stream at the Univeristy of Toronto's Faculty of Information. 