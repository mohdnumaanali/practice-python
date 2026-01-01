# # # import urllib.request
# # # import json

# # # # Prompt for the URL
# # # url = "http://py4e-data.dr-chuck.net/comments_2347371.json"

# # # print("Retrieving", url)
# # # data = urllib.request.urlopen(url).read().decode()

# # # # Parse JSON
# # # info = json.loads(data)

# # # # Extract counts and compute sum
# # # counts = [item['count'] for item in info['comments']]
# # # print("Count:", len(counts))
# # # print("Sum:", sum(counts))

# # import urllib.request, urllib.parse, urllib.error
# # from bs4 import BeautifulSoup

# # # Starting URL
# # url = 'http://py4e-data.dr-chuck.net/known_by_Fraser.html'

# # # Parameters
# # count = 7
# # position = 18  # 1-based index

# # for i in range(count):
# #     # Open and read HTML
# #     html = urllib.request.urlopen(url).read()
# #     soup = BeautifulSoup(html, 'html.parser')

# #     # Retrieve all anchor tags
# #     tags = soup('a')
    
# #     # Select the link at the given position
# #     url = tags[position - 1].get('href', None)
# #     print("Retrieving:", url)

# # # Extract the last name from the final URL
# # last_name = url.split('_')[-1].split('.')[0]
# # print("The answer to the assignment is:", last_name)

# import urllib.request, urllib.parse, json

# serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

# address = input("Enter location: ")
# url = serviceurl + urllib.parse.urlencode({'q': address})

# print("Retrieving", url)
# uh = urllib.request.urlopen(url)
# data = uh.read().decode()
# print("Retrieved", len(data), "characters")

# js = json.loads(data)
# print(js)  # Debug: see full JSON

# if 'plus_code' in js:
#     print("Plus code", js['plus_code'])
# else:
#     print("No plus_code found. Check spelling or URL.")


import urllib.request, urllib.parse, json

serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

address = input("Enter location: ")
url = serviceurl + urllib.parse.urlencode({'q': address})

print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

js = json.loads(data)

# Extract plus_code from first feature
try:
    plus_code = js['features'][0]['properties']['plus_code']
    print("Plus code", plus_code)
except:
    print("No plus_code found. Check spelling or URL.")
