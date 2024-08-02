from pymongo import MongoClient


URI = "mongodb+srv://melnychenkoyuliiav:CYOn54e4tDAWV8W8@cluster1.iva9h8j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
client = MongoClient(URI)

# try: #один раз підключилися - і все, цей код вже приєднаний, тепер цей трай-ексепт можна видалити чи закоментувати, і працювати звідси з базою
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

# client.close()