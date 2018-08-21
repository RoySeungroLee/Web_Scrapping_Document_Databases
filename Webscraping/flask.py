from flask import Flask, render_template
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
import scrape_mars
# Create an instance of our Flask app.
app = Flask(__name__)
# Create connection variable
conn = 'mongodb://localhost:27017'
# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
# Connect to a database. Will create one if not already available.
db = client.team_db
# Drops collection if available to remove duplicates
db.team.drop()

from flask import Flask, render_template


# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
# Create an instance of our Flask app.
app = Flask(__name__)
# Create connection variable
conn = 'mongodb://localhost:27017'
# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
# Connect to a database. Will create one if not already available.
db = client.team_db
# Drops collection if available to remove duplicates
db.team.drop()
output = scrape_mars.scrape()
for i in range(len(output)):
    db.team.insert(output[i])



if __name__ == '__main__':
    app.run(debug= True)

@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    inventory = list(db.collection.find())
    print(inventory)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", inventory=inventory)

@app.route("/home")
def home():
    return render_template('home.html')
