Job Finder Script
A Python script that scrapes job listings from TimesJobs and filters them based on the skills provided by the user. It also includes functionality to extract specific data from an HTML file (e.g., course details from a local file).

Features
Scrapes job listings using BeautifulSoup and Requests.
Filters jobs based on skills you are unfamiliar with.
Extracts details like:
Company Name
Skills Required
Job Link
Repeats job searching every 10 minutes (configurable).
Bonus functionality to extract and print <h5> tags and course card information from an HTML file.
Prerequisites
Before running this script, make sure you have the following:

Python 3.x installed
The required Python libraries installed:
bash
Copy code
pip install requests beautifulsoup4
Usage
Job Finder
Run the script:
bash
Copy code
python script_name.py
Enter the skills you are unfamiliar with (separated by spaces). For example:
sql
Copy code
put some skill that you are not familiar with:
>java php
The script will filter out job listings containing these skills.
The script will display job details such as company name, skills, and a link for more information.
HTML File Processing
Place the home.html file in the same directory as the script.
The script will:
Find all <h5> tags and print their content.
Extract course details (name and price) from <div> tags with the class card.
Code Explanation
Main Functions
find_jobs()
Fetches job listings from TimesJobs.
Filters jobs posted in the last 3 days.
Filters out jobs requiring skills the user is unfamiliar with.
Displays the job details.
HTML File Processing
Opens and reads a local HTML file.
Extracts and prints all <h5> tags.
Extracts course names and prices from <div> elements with the class card.
Configuration
Time Interval: Change the job searching interval by modifying the time_wait variable:
python
Copy code
time_wait = 10  # Set to the desired number of minutes
Technologies Used
Python: Programming language.
BeautifulSoup: For HTML parsing.
Requests: For making HTTP requests.
Notes
Ensure that the website structure matches the parsing logic in the script. If the website changes, the script may need updates.
The course extraction functionality is designed for a specific HTML structure (home.html).
