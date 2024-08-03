Four libraries used for the script (use via pip install):
- pymongo[tls]
- mongoengine
- redis
- python-dotenv

1. Create MongoDB account and a database cluster. Save your credentials.

2. Install mentioned above libraries.

3. Add your .env file to complete URI according to your credentials.
Necessary secrets:
- MONGO_USER
- MONGO_PASS
- MONGO_CLUSTER
- APP_NAME
- MY_DB_NAME

4. Create and fill in the MongoDB, for this purpose run the file "load_data_from_json.py".
The database is ready and filled in.

5. Run file "main.py" and perform search for quotation throughout the created database.
