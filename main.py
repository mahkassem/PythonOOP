from requests import get

data = get('https://api.github.com/users/defunkt')

print(data.json()["avatar_url"])