# one doc
def DecodeBlog(doc) -> dict:
    return {
        "_id" : str(doc["_id"]) ,
        "title" : doc["title"] ,
        "sub_title" : doc["sub_title"] ,
        "content" : doc["content"] ,
        "author" : doc["author"] ,
        "date" : doc["date"] ,
        "tags" : doc["tags"] ,
        "likes" :doc["likes"] ,
        "dislikes" : doc["dislikes"] ,
        "comments" : doc.get("comments",[])
    }

# all blogs
def DecodeBlogs(docs) -> list:
    return [DecodeBlog(doc) for doc in docs]