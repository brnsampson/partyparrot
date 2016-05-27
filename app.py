import partyparrot
import os
from flask import Flask, request, jsonify
app = Flask(__name__)

slack_team_tokens = os.environ.get('SLACK_TEAM_TOKENS').split(':')


@app.route('/', methods=['GET'])
def index():
    return 'OK'


@app.route('/', methods=['POST'])
def slack():
    if slack_team_token and request.form.get('token') not in slack_team_tokens:
        return 'Unauthorized', 401

    text = request.form.get('text')
    if not text:
        return 'I need some text.', 200

    out = partyparrot.convert_str_to_emoji(text, space='        ')
    return jsonify(
        response_type='in_channel',
        text=out
    )

if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', 5000))
