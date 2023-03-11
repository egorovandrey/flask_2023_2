from requests import delete, get

print(get('http://localhost:5000/api/v2/news/999'))
# новости с id = 999 нет в базе

print(get('http://localhost:5000/api/v2/news/2').json())
