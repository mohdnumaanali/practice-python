import urllib.request
import bs4

# Use your own data URL from the assignment page
url = "http://py4e-data.dr-chuck.net/comments_2347368.html"

# Read the HTML
html = urllib.request.urlopen(url).read()

# Parse with BeautifulSoup
soup = bs4.BeautifulSoup(html, "html.parser")

# Find all <span> tags
tags = soup('span')

# Extract numbers and compute sum
total = 0
for tag in tags:
    total += int(tag.contents[0])

print("Count", len(tags))
print("Sum", total)
