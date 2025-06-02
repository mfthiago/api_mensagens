class ValidationException(Exception):
    def __init__(self, message="Dados inválidos"):
        self.message = message
        super().__init__(self.message)
