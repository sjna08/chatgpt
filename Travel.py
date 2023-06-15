from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

@app.route('/user', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'new user created'})

@app.route('/trip', methods=['POST'])
def create_trip():
    destination = request.json['destination']
    start_date = request.json['start_date']
    end_date = request.json['end_date']
    user_id = request.json['user_id']
    new_trip = Trip(destination=destination, start_date=start_date, end_date=end_date, user_id=user_id)
    db.session.add(new_trip)
    db.session.commit()
    return jsonify({'message': 'new trip created'})

if __name__ == "__main__":
    app.run(debug=True)
