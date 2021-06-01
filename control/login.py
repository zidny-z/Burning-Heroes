from ..model.get_data_user import get_user


class login(get_user):
    def __init__(self):
        get_user.__init__(self)
        get_user.get_stage("polisi")
