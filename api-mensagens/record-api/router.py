from src.controllers.MessageController import message_bp

def register_routes(app):
    app.register_blueprint(message_bp, url_prefix='/messages')
