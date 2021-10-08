from flask_mail import Mail, Message
from flask import Blueprint, request
from flask.json import jsonify


bp = Blueprint('send', __name__)
mail = Mail(bp)

@bp.route('/send', methods=['POST'])
def Send():

    _title = request.json.get('title')
    _text = request.json.get('text')
    _email = request.json.get('email')

    msg = Message(_title, sender = 'confmail', recipients = [_email])
    msg.body = _text
    mail.send(msg)
    return jsonify("Sent")

if __name__ == '__main__':
   bp.run()