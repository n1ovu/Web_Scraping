import requests


response = requests.get('https://www.google.com/')
webpage = response.content

print(webpage)
