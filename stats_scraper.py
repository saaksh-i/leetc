import requests

# Replace with your LeetCode username
username = "saakshii11"

# LeetCode Stats API URL
url = f"https://leetcode-stats-api.herokuapp.com/saakshii11"

# Send the GET request to the API
response = requests.get(url)

# Check for success
if response.status_code == 200:
    data = response.json()
    
    # Log the full response to see what we're getting
    print("Full API Response:", data)
    
    # Extract the relevant fields
    if data and 'totalSolved' in data and 'easySolved' in data and 'mediumSolved' in data:
        total_solved = data['totalSolved']
        easy_solved = data['easySolved']
        medium_solved = data['mediumSolved']
        hard_solved = data['hardSolved']
        streak = len(data.get("submissionCalendar", {}))  # Count days in submissionCalendar

        print(f"Username: {username}")
        print(f"Total Problems Solved: {total_solved}")
        print(f"Easy Problems Solved: {easy_solved}")
        print(f"Medium Problems Solved: {medium_solved}")
        print(f"Hard Problems Solved: {hard_solved}")
        print(f"Streak Days: {streak} days")
    else:
        print({'error': 'Required data not found or API returned empty data'})
else:
    print({'error': 'Failed to fetch data from LeetCode Stats API'})
