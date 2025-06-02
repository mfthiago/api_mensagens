class MessageNotFoundException(Exception):
    def __init__(self, message="Mensagem não encontrada"):
        self.message = message
        super().__init__(self.message)
