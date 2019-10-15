import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http


@channel_session_user_from_http
def ws_connect(message):

    print('message','-----ws_connect',message)
    Group('users').add(message.reply_channel)
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': True
        })
    })


@channel_session_user
def ws_disconnect(message):
    print('message', '-----ws_disconnect', message)
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })

    Group('users').discard(message.reply_channel)


# ''''''' mai try kr raha hu
@channel_session_user
def ws_receive(message):

    print(message.content.get('text'))
    print(json.loads(message.content.get('text'))) # This is how we take data in backend
    print(message,'message------->',ws_receive)

    # Group("users").add(message.reply_channel)

    # Group("users").send({
    #     "text":message.content.get('text')
    # })

    typing_person=json.loads(message.content.get('text'))

    if 'typing' in typing_person:

        Group('users').discard(message.reply_channel)

        Group("users").send({
            "text": message.content.get('text')
        })


    else:

        Group("users").add(message.reply_channel)
        Group("users").send({
            "text": message.content.get('text')
        })