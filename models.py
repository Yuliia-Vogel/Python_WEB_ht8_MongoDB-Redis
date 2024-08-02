from mongoengine import Document, StringField, ReferenceField, ListField, connect
import mongoengine

# Підключаємося до бази даних
URI = "mongodb+srv://melnychenkoyuliiav:CYOn54e4tDAWV8W8@cluster1.iva9h8j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
connect(host=URI, db='Homework8')


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
