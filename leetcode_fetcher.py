import requests

def fetch_user_stats(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    data = response.json()

    print("Full API Response:", data)

    if data.get("status") != "success":
        return {"error": "Required data not found or API returned empty data"}

    total_solved = data.get("totalSolved", 0)
    easy = data.get("easySolved", 0)
    medium = data.get("mediumSolved", 0)
    hard = data.get("hardSolved", 0)
    submission_calendar = data.get("submissionCalendar", {})
    streak_days = len(submission_calendar)

    return {
        "username": username,
        "total_solved": total_solved,
        "easy": easy,
        "medium": medium,
        "hard": hard,
        "streak_days": streak_days
    }


