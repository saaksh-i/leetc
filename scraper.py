import requests
from bs4 import BeautifulSoup

# 🔁 Replace this with your actual LeetCode username
username = "saakshii11"

# 🌐 Profile URL
url = f"https://leetcode.com/u/saakshii11/"

# 🛡️ Add user-agent header to pretend we're a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36"
}

# 📥 Send the request
response = requests.get(url, headers=headers)

# 🧠 Parse and extract if successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Just for test: Print the page title to see if it worked
    title = soup.title.string if soup.title else "No title found"
    print(f"✅ Success! Page Title: {title}")
else:
    print({'error': 'User not found or LeetCode is blocking requests'})
