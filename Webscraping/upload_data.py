import pymongo
import scrape_mars

# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.store_inventory
collection = db.produce
output = scrape_mars.scrape()
print(output)
for i in range(len(output)):
    db.collection.insert(output[i])

print("Data Uploaded!")
