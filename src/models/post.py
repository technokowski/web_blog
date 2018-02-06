import uuid
import datetime
from src.common.database import Database

__author__ = "technokowski"

'''
This class initializes the Post object that will become a blog post. The json method
is converting the self. to a json format, and the save_to_mongo is inserting it into
the collections db using the insert method contained in Database.py. Pretty simple, actually.
'''

class Post(object):

    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'content': self.content,
            'author': self.author,
            'title': self.title,
            'created_date': self.created_date
        }
    @classmethod
    def from_mongo(cls, id):
        # Post.from_mongo('123')
        post_data = Database.find_one(collection='posts', query={'_id': id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]