class InstanceNotFound(Exception):
    def __init__(self):
        super().__init__("The specified instance url does not exist")


class IncorrectCredentials(Exception):
    def __init__(self):
        super().__init__("Incorrect email or password")
