def format_user_messages(messages: object) -> object:
    for msg in messages:
        return "From: {0} \n Content: {1}".format(msg['from'], msg['content'])


def get_welcome_message():
    return "Welcome, to access your messages use: msg/{user_id} \n" \
           "To send a message use post/{from_user_id} along with \n" \
           "{'content': <content_message>, \n " \
           "'to': <user_id> \n" \
           "}"
