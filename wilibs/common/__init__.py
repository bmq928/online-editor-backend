def verifyAndReturn(r):
    if r['code'] == 200:
        return True, r['content']
    return False, r['reason']

def tokenHeader(token):
    return {'Authorization': token}