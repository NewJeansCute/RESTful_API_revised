from datetime import datetime, timedelta
from django.db import models
from mongoengine import *

# Create objects for MongoDB/collection connection
connect(host="mongodb://127.0.0.1:27017/LINE")


# Create model objects to save/query user messages with MongoDB
class User(DynamicDocument):
    user_id = StringField()
    display_name = StringField()
    language = StringField()
    picture_url = StringField()
    status_message = StringField()

    meta = {"collection": "user"}


class Message(DynamicDocument):
    user_id = StringField()
    display_name = StringField()
    message_id = StringField()
    send_time = FloatField()
    message_content = StringField()

    def to_dict(self):
        return {
            "message_sender": self.display_name,
            "message_id": self.message_id,
            "message_content": self.message_content,
            "send_time (UTC+8)": str(datetime.fromtimestamp(self.send_time/1000) + timedelta(hours=8)),
        }

    meta = {"collection": "message"}