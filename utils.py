import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAEwPqnukRwBANHoaLQOLVHX27cIGZAMvLrOozXVCjCT25RV9D4ZChGZCqgY6lLgoPpKSucfpDzgdTuCl6x3GCRQQgiDT7JaWsYUXTmvUHFzHx7viRRFQNkOcAa1n0vNbwdPZAnZAe9afUTCpJZAoCNIcNZCuqwyv5e0z2dGqsaMQZDZD"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_button_message(id,text,buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
               "attachment":{
                   "type":"template",
                   "payload":{
                       "template_type":"button",
                       "text":text,
                       "buttons":buttons
                    }
                }      
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_url_message(id,text,urls):
    url="{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
               "attachment":{
                   "type":"template",
                   "payload":{
                       "template_type":"button",
                       "text":text,
                       "buttons":urls
                    }
                }      
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_image_message(id,urls):
    url="{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
               "attachment":{
                   "type":"image",
                   "payload":{
                       "url":urls,
                       "is_reusable":True
                    }
                }      
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
