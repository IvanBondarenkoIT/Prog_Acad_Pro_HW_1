class User_Exception(Exception):
    def __init__(self, text):
        super(User_Exception, self).__init__()
        self.message = text

    def get_exception_message(self):
            return self.message
