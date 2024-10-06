from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from datetime import datetime

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages')
def messages():
    messages = Message.query.all()
    return jsonify([message.to_dict() for message in messages]), 200

@app.route('/messages/<int:id>', methods=['GET'])
def messages_by_id(id):
    message = Message.query.filter_by(id=id).first()
    return make_response(message, 200)


@app.route('/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    new_message = Message(
        body=data.get('body', ''),
        username=data.get('username'),
        created_at = datetime.utcnow()
    )
    db.session.add(new_message)
    db.session.commit()

    return jsonify(new_message.to_dict()), 201

@app.route('/messages/<int:id>', methods=['PATCH'])
def update_message(id):
    message = Message.query.filter_by(id=id).first()
    data = request.get_json()
    if 'body' in data:
        message.body = data['body']

    db.session.commit()

    return jsonify(message.to_dict()), 200

    

@app.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    message= Message.query.filter_by(id=id).first()

    db.session.delete(message)
    db.session.commit()

    return jsonify({'message': 'Message deleted'}), 204


    

if __name__ == '__main__':
    app.run(port=5555)
