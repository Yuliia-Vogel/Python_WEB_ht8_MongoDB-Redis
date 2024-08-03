import os

from mongoengine import Document, StringField, ReferenceField, ListField, connect, disconnect
import mongoengine
from dotenv import load_dotenv

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


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

    def __str__(self):
        return f"Author(fullname={self.fullname})"

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True, reverse_delete_rule=mongoengine.CASCADE)
    quote = StringField(required=True)
