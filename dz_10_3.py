class MyError(Exception):
    def __init__(self, message, nomber):
        self.message = message
        self.nomber = nomber

raise MyError('We have a problem', 404)