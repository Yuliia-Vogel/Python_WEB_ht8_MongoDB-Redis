import os

from mongoengine import connect, disconnect
import redis
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

# підключення до Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


def search_quotes():
    while True:
        user_input = input("Enter command (name: <fullname>, tag: <tag>, tags: <tags>, exit): ").strip()
        if ":" not in user_input:
            if user_input == "exit":
                print("Bye!!!")
                break
            else:
                print("Unknown command.")
                continue

        command, value = user_input.split(":", 1)
        value = value.strip()

        if command == "name":
            cache_key = f"name:{value}"
            cached_result = redis_client.get(cache_key)
            if cached_result:
                print("From cache:")
                print(cached_result)
            else:
                print(f"Searching the author by the name: {value}")
                authors = Author.objects(fullname__icontains=value)  # mongoengine
                if authors:
                    quotes = []
                    for author in authors:
                        author_quotes = Quote.objects(author=author)
                        for quote in author_quotes:
                            quotes.append(quote.quote)
                            print(quote.quote)
                    redis_client.set(cache_key, "\n".join(quotes))
                else:
                    print("Author not found.")
        elif command == "tag":
            cache_key = f"tag:{value}"
            cached_result = redis_client.get(cache_key)
            if cached_result:
                print("From cache:")
                print(cached_result)
            else:
                print(f"Searching quotes with tag: {value}")
                quotes = Quote.objects(tags__icontains=value)
                if quotes:
                    quote_texts = [quote.quote for quote in quotes]
                    for quote_text in quote_texts:
                        print(quote_text)
                    redis_client.set(cache_key, "\n".join(quote_texts))
                else:
                    print(f"Tag '{value}' not found.")
        elif command == "tags":
            tags = [tag.strip() for tag in value.split(",")]
            cache_key = f"tags:{','.join(tags)}"
            cached_result = redis_client.get(cache_key)
            if cached_result:
                print("From cache:")
                print(cached_result)
            else:
                print(f"Searching quotes with tags: {', '.join(tags)}")
                quotes = Quote.objects(tags__in=tags)
                if quotes:
                    quote_texts = [quote.quote for quote in quotes]
                    for quote_text in quote_texts:
                        print(quote_text)
                    redis_client.set(cache_key, "\n".join(quote_texts))
                else:
                    print(f"No quotes found with tags: {', '.join(tags)}")


if __name__ == "__main__":
    search_quotes()
