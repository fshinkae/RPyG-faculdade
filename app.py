from flask import Flask
from controllers.character_controller import set_character_controller

app = Flask(__name__)

app.add_url_rule('/character', 'character_route', set_character_controller, methods=['POST'])

if __name__ == '__main__':
    app.run()
