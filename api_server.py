# api server for control bot
# please make sure BOT TOKEN is set in configuration(.env file)

from core import app
from pytgcalls import CustomApi
from pytgcalls import idle

apiserver = CustomApi()

@apiserver.on_update_custom_api()
async def handler(request: dict):
    """
        json request example:
            {
                "chat_id" : -1022459474630,
                "message" : "!stream https://us-tx-dallas-1.listentochurch.com:8443/9235230.mp3"
            }
    """
    try:
        await app.send_message(int(request['chat_id']), request['message'])
    except:
        return {'success' : False}

    return {'success': True}

apiserver.start()