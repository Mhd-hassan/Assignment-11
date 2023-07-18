# Name: Muhammad Hassan Noorsumar
# Day: Tuesday
# Date: 18/07/2023
# Sub: Python
# Topic: Assignment-11
# Assignment-11: Q
# Q: Create a gui based form to take input from the user and then navigate to the particular site from where the user came to know about the content

# for example:
# create a form where the user is enquiring about the respective course
# and in the form there is an option for asking where the user came to know about it, for eg: instagram ads or YouTube ads

# and then when clicking the submit button
# take the user to the faq page of that site

import webbrowser
from tkinter import *

def submit_form(): # Function to handle form submission
    course = course_entry.get()
    source = source_variable.get()
    
    if source == "Instagram Ads": # Open the FAQ page based on the selected source
        faq_url = "https://www.example.com/faq/instagram"
    elif source == "YouTube Ads":
        faq_url = "https://www.example.com/faq/youtube"
    else:
        faq_url = "https://www.example.com/faq"

    webbrowser.open(faq_url)

window = Tk() # Create the main window
window.title("Course Enquiry Form")

course_label = Label(window, text="Course:") # Create form elements
course_label.pack()
course_entry = Entry(window)
course_entry.pack()

source_label = Label(window, text="Source:")
source_label.pack()
source_variable = StringVar(window)
source_variable.set("Instagram Ads")  # Default option
source_dropdown = OptionMenu(window, source_variable, "Instagram Ads", "YouTube Ads", "Other")
source_dropdown.pack()

submit_button = Button(window, text="Submit", command=submit_form)
submit_button.pack()

window.mainloop() # Start the main event loop
