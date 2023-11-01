#--------------------------------------------------------------------------------
# INF452 Midterm
# University of Toronto, Faculty of Information, Bachelor of Information Program
#--------------------------------------------------------------------------------
# Author: Sebastian Rodriguez
# Prepared For: Dr. Maher Elshakankiri
# GitHub: https://github.com/seb646/uoft-ischool-course-navigator
# License: BSD 3-Clause License – Copyright (c) 2023, Sebastian Rodriguez
# Date Created: October 18, 2023
# Last Modified: November 1, 2023
#--------------------------------------------------------------------------------
# PROGRAM DESCRIPTION
# This program scrapes data on courses within the University of Toronto's
# Faculty of Information. It captures data directly from the faculty's website,
# including course title, description, and available syllabi and makes that data
# available to the user through a command-line interface. Users can browse the
# faculty's course catalogue using course codes (ex: INF452).
#--------------------------------------------------------------------------------

# Import the BeautifulSoup library to handle HTML parsing
from bs4 import BeautifulSoup

# Import the requests library to handle the HTTP GET requests
import requests

# Print introduction message to user
print('-' * 80)
print("UNIVERSITY OF TORONTO FACULTY OF INFORMATION COURSE NAVIGATOR")
print('-' * 80)
print("This tool allows you to browse information on all available iSchool courses.\n")
print("• Undergraduate courses format: INF000\n• Graduate courses format: INF0000\n")
print("Please be patient! We fetch data live from the iSchool's website so it may \ntake some time to load. We'll let you know when it's ready!")
print('-' * 80)

# Define initial search URL
url = "https://ischool.utoronto.ca/current-students/programs-courses/courses/course-list/"

# Set up HTTP GET request to URL
page = requests.get(url, timeout=5)

# Use BeautifulSoup to parse the page's content
content = BeautifulSoup(page.content, 'html.parser')

# Find rows for undergraduate courses
undergrad_courses_text = content.find("div", id="undergrad_courses") # Find the div
undergrad_courses_table = undergrad_courses_text.find("table") # Find the table
undergrad_courses_rows = undergrad_courses_table.find_all("tr") # Find the rows

# Find rows for graduate courses
grad_courses_text = content.find("div", id="grad_courses") # Find the div
grad_courses_table = grad_courses_text.find("table") # Find the table
grad_courses_rows = grad_courses_table.find_all("tr") # Find the rows

# Combine undergraduate and graduate courses
courses_rows = undergrad_courses_rows + grad_courses_rows

# Set empty dictionary for all courses
courses = {}

# Iterate through all course rows
for row in courses_rows:

    # Find all columns in the row
    course_cols = row.find_all("td")

    # Create empty array for course data
    course_data = []

    # Iterate through the columns
    for i, cell in enumerate(course_cols):

        # Add the course title to the course data array
        course_data.append(cell.text)

        # Check if it's the second column
        if i == 1:

            # Find the link in the column
            link = cell.find("a")['href']

            #Append the link to course data
            course_data.append(link)

    # Check if there's any content in the course data array
    if course_data:
        # Remove the H/H1 formatting from the course title
        title = course_data[0].replace("H1", "")
        title = title.replace("H", "")

        # Add course data to the global courses dictionary
        courses[title] = {
            'title': course_data[1],
            'link': course_data[2]
        }

# Iterate through all of the courses found on the previous link
for code, data in courses.items():

    # Define the individual course URL
    url = data['link']

    # Establish a new HTTP GET request for course URL
    page = requests.get(url, timeout=5)

    # Use BeautifulSoup to parse the page's content
    content = BeautifulSoup(page.content, 'html.parser')

    # Find the course description text
    course_description = content.find("div", {"class": "post_content"}).find("p")

    # Add course description to the global courses dictionary
    courses[code]['description'] = course_description.text

    # Find the course syllabi information
    course_syllabi = content.find("div", {"class": "syllabi"})

    # Check if the course has any available syllabi
    if course_syllabi is not None:

        # Define an empty dictionary for course syllabi
        syllabi_store = {}

        # Find all course syllabi links
        course_syllabi = course_syllabi.find_all("a")

        # Iterate through course syllabi links
        for syllabus in course_syllabi:

            # Store course syllabi in local dictionary
            syllabi_store[syllabus.text] = syllabus['href']

        # Add local course syllabi dictionary to global courses dictionary
        courses[code]['syllabi'] = syllabi_store

# Inform the user that the courses have been loaded
print("Courses loaded! HINT: You can leave at any time by typing \"exit\".")
print('-' * 80)

# Ask the user to input a course code
code = input("To learn about a course, enter a course code: ")

# Loop through while the user has entered a code
while code is not None:

    # Transform user inputted code to uppercase
    code = code.upper()

    # If the user says exit, exit the loop
    if code == "EXIT":
        print('-' * 80)
        break

    # Check if the user inputted code is in the global courses dictionary
    elif code in courses:

        # Print course data to user
        print('-' * 80)
        print("Course Code:", code, "\n")
        print("Course Title:", courses[code]['title'], "\n")
        print("Course Link:", courses[code]['link'], "\n")
        print("Course Description:")
        print(courses[code]['description'])

        # Check if the course has any syllabi
        if 'syllabi' in courses[code]:
            print("\nCourse Syllabi:")

            # Iterate through the course syllabi
            for syllabus in courses[code]['syllabi']:
                print("    ", syllabus, ":", courses[code]['syllabi'][syllabus])

        # Ask the user to input another course code
        print('-' * 80)
        code = input("Enter another course code to continue browsing, or type \"exit\" to leave: ")

    # Run if the user entered a course code that is not found in the global courses dictionary
    else:

        # Ask the user to input a new course code
        print('-' * 80)
        code = input("The course code you entered is not valid. Enter a different code or type \"exit\" to leave: ")
