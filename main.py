from mongoengine import connect, disconnect

import redis

from models import Author, Quote


URI = "mongodb+srv://melnychenkoyuliiav:CYOn54e4tDAWV8W8@cluster1.iva9h8j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
disconnect()
connect(host=URI, db="Homework8")


def search_quotes():
    while True:
        user_input = input("Enter command (name: значення, tag: значення, tags: значення, exit): ").strip()
        if user_input.startswith("name:"):
            name = user_input[len("name:"):].strip()
            print(f"Searching the author by the name: {name}")
            
            # mongoengine
            author = Author.objects(fullname=name).first()
            if author:
                quotes = Quote.objects(author=author)
                for quote in quotes:
                    print(quote.quote)
            else:
                print("Author not found.")
        elif user_input.startswith("tag:"):
            tag = user_input[len("tag:"):].strip()
            quotes = Quote.objects(tags=tag)
            if not quotes:
                print(f"Tag '{tag}' not found.")
            else:
                for quote in quotes:
                    print(quote.quote)
        elif user_input.startswith("tags:"):
            tags = user_input[len("tags:"):].strip().split(',')
            quotes = Quote.objects(tags__in=[tag.strip() for tag in tags])
            if not quotes:
                print(f"Tags '{', '.join(tags)}' not found.")
            else:
                for quote in quotes:
                    print(quote.quote)
        elif user_input == "exit":
            print("Bye!!!")
            break
        else:
            print("Unknown command.")



if __name__ == "__main__":
    search_quotes()
