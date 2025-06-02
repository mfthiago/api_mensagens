from src.repositories.MessageRepository import MessageRepository

class MessageService:
    def __init__(self):
        self.repo = MessageRepository()

    def get_all(self):
        return self.repo.get_all()

    def create(self, data):
        return self.repo.create(data)
