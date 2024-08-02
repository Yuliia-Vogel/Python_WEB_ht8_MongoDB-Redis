import json
from mongoengine import connect, disconnect

from models import Author, Quote

URI = "mongodb+srv://melnychenkoyuliiav:CYOn54e4tDAWV8W8@cluster1.iva9h8j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
disconnect()
connect(host=URI, db="Homework8")


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
