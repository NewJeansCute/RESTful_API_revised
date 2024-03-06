import json
from django.views import View
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi
from .models import User, Message


class Line_User(View):
    def post(self, request):
        # user send message to LINE bot

        webhook_object = json.loads(request.body)
        line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

        # for LINE Developers Console webhook verify
        if not webhook_object["events"]:
            return HttpResponse()

        try:
            messages = []

            for event in webhook_object["events"]:
                if event["type"] == "message":
                    user_id = event["source"]["userId"]

                    # get the user's info
                    # if it's a new user, store the user's info into MongoDB
                    profile = line_bot_api.get_profile(user_id)
                    user_id = profile.user_id
                    display_name = profile.display_name
                    language = profile.language
                    picture_url = profile.picture_url
                    status_message = profile.status_message

                    exist = User.objects(user_id=user_id).count()

                    if not exist:
                        new_user = User(user_id=user_id, display_name=display_name, language=language, picture_url=picture_url, status_message=status_message)
                        new_user.save()

                    # get the message info
                    messages.append({"user_id": user_id, "display_name": display_name, "message_id": event["message"]["id"], "message_content": event["message"]["text"], "send_time": event["timestamp"]})
                else:
                    return HttpResponse()

            # store message info into MongoDB
            message_instances = [Message(**message) for message in messages]
            Message.objects.insert(message_instances)
            
            return HttpResponse()
        except:
            return HttpResponseBadRequest({"Something went wrong."})