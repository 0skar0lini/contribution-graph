import calendar
import datetime
import os

# Define the message to spell out
message = "Unleash"

# Define the starting date for the contributions
start_date = datetime.date(2023, 1, 1)

# Define the number of weeks and days in a week
weeks = 52
days_in_week = 7

# Create a dictionary to map characters to their binary representation
char_map = {
    'U': [
        "10001",
        "10001",
        "10001",
        "10001",
        "01110"
    ],
    'n': [
        "00000",
        "11110",
        "10001",
        "10001",
        "10001"
    ],
    'l': [
        "00000",
        "10000",
        "10000",
        "10000",
        "11110"
    ],
    'e': [
        "00000",
        "01110",
        "10001",
        "11111",
        "01110"
    ],
    'a': [
        "00000",
        "01110",
        "10001",
        "11111",
        "11111"
    ],
    's': [
        "00000",
        "01111",
        "10000",
        "01110",
        "11110"
    ],
    'h': [
        "00000",
        "10001",
        "10001",
        "11111",
        "10001"
    ]
}

# Create a function to generate the commit dates
def generate_commit_dates(start_date, message):
    commit_dates = []
    current_date = start_date
    for char in message:
        if char in char_map:
            for row in char_map[char]:
                for col in row:
                    if col == "1":
                        commit_dates.append(current_date)
                    current_date += datetime.timedelta(days=1)
                current_date += datetime.timedelta(days=(days_in_week - len(row)))
        current_date += datetime.timedelta(days=days_in_week)
    return commit_dates

# Generate the commit dates
commit_dates = generate_commit_dates(start_date, message)

# Create a function to make commits
def make_commits(commit_dates):
    for commit_date in commit_dates:
        os.system(f'echo "{commit_date}" > commit.txt')
        os.system('git add commit.txt')
        os.system(f'git commit --date="{commit_date}T12:00:00" -m "Commit on {commit_date}"')

# Make the commits
make_commits(commit_dates)
