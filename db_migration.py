import sqlite3
import json

conn = sqlite3.connect("test.db")

conn.execute("""CREATE TABLE IF NOT EXISTS quotes
        (
            ID INT PRIMARY KEY NOT NULL,
            quote TEXT NOT NULL,
            author CHAR(50),
            tags CHAR(100)
        );""")

data = json.load(open("css-scraper-results.json"))

for index in range(len(data)):
    ID = index + 1
    quote = data[index]["text"].encode("utf-8")
    author = data[index]["author"]
    tags = ""
    tags_concate = ",".join(data[index]["tags"]).strip()
    if tags_concate != "":
        tags = tags_concate
    query = """INSERT INTO quotes (ID,quote,author,tags) VALUES (?, ?, ?, ?);"""
    conn.execute(query, (ID, quote, author, tags))


cursor = conn.execute("SELECT * FROM quotes")

for row in cursor:
    print("ID \t Text \t\t Author \t Tags")
    print("{} \t {} \t\t {} \t {}".format(row[0],row[1],row[2],row[3]))