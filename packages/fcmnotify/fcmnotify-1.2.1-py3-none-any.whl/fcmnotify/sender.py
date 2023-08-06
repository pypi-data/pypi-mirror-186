"""notification > notification_sender.py"""
# PYTHON IMPORTS
import json
import requests
from django.shortcuts import get_object_or_404
from .models import FCMSettings, UserFcmToken  # , UserMobileFcmToken

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


try:
    fcm = get_object_or_404(FCMSettings, is_active=True)
    server_key = fcm.server_key
    action_domain = fcm.action_domain
    image_url = f"{fcm.icon_image.url}"
except Exception as e:
    server_key = None
    action_domain = None
    image_url = None
    print('error', e)


def fcm_notify(
        sender, recipient, message, title="DK", dataObject=None
):
    """Sends notification to user"""
    # Web Application notification
    try:
        user = UserFcmToken.objects.get(user=recipient)
        token = user.fcm_token
        url = "https://fcm.googleapis.com/fcm/send"
        body = {
            "notification": {
                "title": title,
                "body": message,
                "click_action": action_domain,
                "icon": image_url
            },
            "to": token,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": server_key
        }
        data = requests.post(url, data=json.dumps(body), headers=headers)
        logging.warning(f"Send {data.text}")
    except Exception as e:
        logging.warning(f"Unable to get TOKEN {e}")

    # Android Application notification
    # try:
    #     # See documentation on defining a message payload.
    #     user = UserMobileFcmToken.objects.get(user=recipient)
    #     token = user.fcm_token
    #     message = messaging.MulticastMessage(
    #         notification=messaging.Notification(
    #             title=title,
    #             body=message
    #         ),
    #         data=dataObject,
    #         tokens=token,
    #     )
    #     response = messaging.send_multicast(message)
    #     print('Successfully sent message:', response)
    # except Exception as e:
    #     logger.info(f"Unable to Successfully sent message {e}")
    return True