from flask import Blueprint, request, jsonify
from src.services.MessageService import MessageService

message_bp = Blueprint('message_bp', __name__)
service = MessageService()

@message_bp.route('/', methods=['GET'])
def get_all_messages():
    return jsonify(service.get_all())

@message_bp.route('/', methods=['POST'])
def create_message():
    data = request.json
    return jsonify(service.create(data)), 201
