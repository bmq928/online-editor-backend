from .wilibs_obj import Wilib
from .authentication.auth import login as loginAPI

def login(username, password):
    err, user = loginAPI(username, password)
    if not err:
        return None
    return Wilib(user)