from flask import Flask
from flask import request
from flask import jsonify
import msgMock
import MessageDataBase
from Utils import payload_utils, message_formating_utils

app = Flask(__name__)

debug = False

if debug is False:
    dataBase = MessageDataBase.messages
else:
    dataBase = msgMock.mapMsgs


@app.route("/")
def hello():
    return message_formating_utils.get_welcome_message()


@app.route('/msg/<int:user_id>')
def get_msgs_by(user_id):
    user_msgs = dataBase.get(user_id)
    if not user_msgs:
        return 'No messages found for user ID: %d' % user_id
    return 'Hello user Id:{0}, your Messages are: \n {1}'\
        .format(user_id, message_formating_utils.format_user_messages(user_msgs))


@app.route('/post/<int:user_id>', methods=['POST'])
def post_msgs_by(user_id):
    payload = request.json
    if user_id is None:
        return "Must supply user_id in path param"
    error_from_payload = payload_utils.payload_check(payload)
    if error_from_payload['is_error']:
        return error_from_payload['err_message']
    else:
        result = {
            'from': user_id,
            'content': payload.get('content'),
        }
        to_index = int(payload.get('to'))
        if dataBase.get(to_index) is None:
            dataBase[to_index] = [result]
        else:
            messages_by_user = dataBase.get(to_index)
            messages_by_user.append(result)
            dataBase[to_index] = messages_by_user

    return jsonify({'to': payload.get('to'), **result})


# Uncomment when debug mode is necessary
# app.run(debug)
