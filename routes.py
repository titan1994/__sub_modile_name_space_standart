from json import dumps as jsd
from functools import wraps
from starlette.responses import Response
import json
from uuid import UUID
from datetime import datetime

class EncoderHelper(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        if isinstance(obj, datetime):
            # if the obj is datetime - return str
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def standardize_response(func):
    """
    Декоратор стандартизации вывода.
    Предполагается что функции возвращают серриализуемый джсон и они асинхронные
    :param func:
    :return:
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        msg = ''
        status = True
        result = []
        try:
            result = await func(*args, **kwargs)
        except Exception as exp:
            status = False
            msg = str(exp)

        if isinstance(result, str):
            data_str = f'{{"status":{jsd(status)}, "errors":{jsd([msg])}, "response": {result}}}'
        else:
            data_out = {'status': status, 'errors': [msg], 'response': result}
            data_str = jsd(data_out, indent=4, ensure_ascii=False, cls=EncoderHelper)

        return Response(content=data_str, media_type='application/json')

    return wrapper
