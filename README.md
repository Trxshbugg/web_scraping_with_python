Job Finder Script

A Python-based project to automate the process of finding and filtering job listings from online sources. This script focuses on simplifying the job search by excluding positions requiring specific skills that the user is not familiar with.

Features

Automated Job Search: Scrapes job listings from TimesJobs and filters them based on the user’s input.
Customizable Skill Filtering: Users can specify skills they are unfamiliar with to exclude irrelevant job postings.
Periodic Execution: The script runs periodically to fetch the latest job postings, ensuring you stay updated.
Detailed Job Information: Displays company name, required skills, and links to the full job description.

How It Works

The user specifies a list of skills they want to filter out.
The script retrieves job listings posted within the last three days from TimesJobs.
Jobs matching the user's criteria are displayed with relevant details.
The process repeats at regular intervals, ensuring fresh job listings.
Prerequisites
Before using this script, ensure you have the following:

Python 3.x installed on your system.
Required Python libraries:
requests for making web requests.
beautifulsoup4 for parsing HTML content.
Application Scenarios
Job Seekers: Automate your job search and focus only on positions that match your expertise.
Skill-Specific Searches: Identify jobs based on specific skill requirements and avoid irrelevant listings.
Recruitment Assistance: Useful for recruiters or agencies to filter job postings for their clients.
Additional Functionality
The script also includes features for processing local HTML files. It can extract specific elements, such as course names and prices, from structured data.

Repository Goals

This repository aims to:
Simplify the job search process using Python automation.
Provide an example of web scraping with BeautifulSoup and Requests.
Offer a base script that can be further customized for various job portals and criteria.
