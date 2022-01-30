from arango import ArangoClient

client=ArangoClient(hosts=["http://localhost:8529"])

sys_db=client.db("_system", username="root", password="lol")

if not sys_db.has_database("marketplace"):
    sys_db.create_database("marketplace")

db=client.db("marketplace", username="root", password="lol")

if db.has_collection("books"):
    books=db.collection("books")
else:
    books=db.create_collection("books")

books.add_hash_index(fields=["title"],unique=False)

books.truncate()


books.insert({'title':'The Lord of the Rings', 'author':'J.R.R. Tolkien', 'category':'Fantasy'})
books.insert({'title':'The Hobbit', 'author':'J.R.R. Tolkien', 'category':'Fantasy'})
books.insert({'title':'The Catcher in the Rye', 'author':'J.D. Salinger', 'category':'Fiction'})
books.insert({'title':'The Grapes of Wrath', 'author':'John Steinbeck', 'category':'Fiction'})
books.insert({'title':'The Great Gatsby', 'author':'F. Scott Fitzgerald', 'category':'Fiction'})
books.insert({'title':'The Scarlet Letter', 'author':'Nathaniel Hawthorne', 'category':'Fiction'})
books.insert({'title':'The Da Vinci Code', 'author':'Dan Brown', 'category':'Mystery'})
books.insert({'title':'The Lost Symbol', 'author':'Dan Brown', 'category':'Mystery'})
books.insert({'title':'The Alchemist', 'author':'Paulo Coelho', 'category':'Fiction'})
books.insert({'title':'The Count of Monte Cristo', 'author':'Alexandre Dumas', 'category':'Fiction'})
books.insert({'title':'The Godfather', 'author':'Mario Puzo', 'category':'Fiction'})

# Execute an AQL query. This returns a result cursor.
cursor = db.aql.execute('FOR doc IN books FILTER doc.category == "Mystery" RETURN doc ')

# Iterate through the cursor to retrieve the documents.

if __name__=='__main__':
    for document in cursor:
        print(document['title'],document['author'])
