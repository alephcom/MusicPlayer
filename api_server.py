# api server for control bot
# please make sure BOT TOKEN is set in configuration(.env file)

from core import app
from config import config
from pytgcalls import CustomApi
from pytgcalls import idle
from core.groups import all_groups, get_group

apiserver = CustomApi(config.API_SERVER_PORT)

@apiserver.on_update_custom_api()
async def handler(request: dict):
    """
        json request example:
            {
                "type"          : "command", ("command" or "streams")
                "chat_id"       : -1022459474630,
                "message"       : "!stream https://us-tx-dallas-1.listentochurch.com:8443/9235230.mp3"
            }
    """
    try:
        if request['type'] == "command":
            await app.send_message(int(request['chat_id']), request['message'])
        elif request['type'] == "streams":
            streams = []
            for group_id in all_groups():
                group = get_group(group_id)
                if group['is_playing']:
                    stream = group['now_playing'].to_dict()
                    stream['chat_id'] = group_id
                    streams.append(stream)
            
            return {'success' : True, 'streams' : streams}
        else:
            return {'success' : False, 'error' : 'unknown request type'}
    except:
        return {'success' : False}

    return {'success': True}

apiserver.start()