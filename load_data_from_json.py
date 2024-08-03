import os

import json
from mongoengine import connect, disconnect
from dotenv import load_dotenv

from models import Author, Quote


load_dotenv() # завантажуються дані з файлу .env 
# створюємо змінні для всіх сікретів у нашому файлі .env
mongo_user = os.getenv("MONGO_USER")
mongo_pass = os.getenv("MONGO_PASS")
cluster_name = os.getenv("MONGO_CLUSTER")
app_name = os.getenv("APP_NAME")
my_db_name = os.getenv("MY_DB_NAME")

URI = f"mongodb+srv://{mongo_user}:{mongo_pass}@{cluster_name}.iva9h8j.mongodb.net/?retryWrites=true&w=majority&appName={app_name}"

disconnect() # відключаємося на всяк випадок, щоб уникнути помилки, коли підключення вже існує і зробити нове неможливо
connect(host=URI, db=my_db_name)


# Функція для завантаження авторів
def load_authors(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            author = Author(**item)
            author.save()


# Функція для завантаження цитат
def load_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            author = Author.objects(fullname=item['author']).first()
            if author:
                quote = Quote(tags=item['tags'], author=author, quote=item['quote'])
                quote.save()


if __name__ == "__main__":
    load_authors('authors.json')
    load_quotes('quotes.json')
