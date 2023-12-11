# Nathan McGraw
# Introduction to Programming with Python
# Application 1: Screen Time App

print()

''' Intro: This application prompts the user for total minutes
spent on a social media site during the week. It then calculates how
minutes per day are spent on the site. '''

'''Change Log: 
* No specific welcome message with description provided.
* Created variable 'min_week' to denote user's input for weekly minutes.
* Created variable 'min_day' to denote calculated daily minutes spent on the site.
* Added rounding function to round min_day to hundredths place.
'''

# Print welcome message with app description
print("Welcome, this app will calculate your daily social media screen-time.")

# Print: "Submit weekly minute total to calculate daily screen-time."
print("\nPlease submit total weekly minutes spent online to calculate daily screen-time.")

# Prompt user to input weekly screen-time total in minutes (int)
min_week = float(input("\tTotal minutes spent on social media: "))

# Compute average daily minutes from int received
min_day = min_week / 7

# Display result as average daily minutes spent online
print("\nAverage daily minutes spent online: {} minutes".format(round(min_day, 2)))
