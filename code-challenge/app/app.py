# app.py

from flask import Flask, jsonify, request
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes_powers.db'
db.init_app(app)

# Routes

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_data = [{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heroes]
    return jsonify(heroes_data)

# Implement other routes as described in the prompt...

# ... existing code ...

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
