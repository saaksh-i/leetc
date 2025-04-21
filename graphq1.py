import requests
import json

# LeetCode's GraphQL endpoint
url = "https://leetcode.com/graphql/"

# Replace with your username
username = "__samz__"

# Prepare the GraphQL query for fetching the profile data
query = """
{
  userProfile(userSlug: "%s") {
    username
    userContestRanking {
      ranking
      rating
      globalRanking
    }
    solvedProblemsCount
    allSolvedProblems {
      difficulty
      problem {
        title
        titleSlug
      }
    }
    streak
  }
}
""" % username

# Set headers for the request
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/json",
}

# Send the request with the query
response = requests.post(url, json={'query': query}, headers=headers)

# Check for success
if response.status_code == 200:
    data = response.json()
    if data.get("data") and data["data"].get("userProfile"):
        user_data = data["data"]["userProfile"]
        print(f"Username: {user_data['username']}")
        print(f"Streak: {user_data['streak']}")
        print(f"Solved Problems: {user_data['solvedProblemsCount']}")
        print(f"Ranking: {user_data['userContestRanking']}")
    else:
        print({'error': 'User not found or LeetCode is blocking requests'})
else:
    print({'error': 'Failed to fetch data from LeetCode API'})
