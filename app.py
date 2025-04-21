from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from leetcode_fetcher import fetch_user_stats  # Make sure your scraper file is named correctly

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# DB Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    total_solved = db.Column(db.Integer)
    easy = db.Column(db.Integer)
    medium = db.Column(db.Integer)
    hard = db.Column(db.Integer)
    streak_days = db.Column(db.Integer)

    def to_dict(self):
        return {
            "username": self.username,
            "total_solved": self.total_solved,
            "easy": self.easy,
            "medium": self.medium,
            "hard": self.hard,
            "streak_days": self.streak_days
        }

# Create DB tables
with app.app_context():
    db.create_all()

# Route to fetch + store LeetCode stats
@app.route('/api/stats/<username>', methods=['GET'])
@app.route('/api/user/<username>', methods=['GET'])
def get_saved_stats(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'error': 'User not found in database'}), 404

    stats = {
        "username": user.username,
        "total_solved": user.total_solved,
        "easy": user.easy,
        "medium": user.medium,
        "hard": user.hard,
        "streak_days": user.streak_days
    }

    return jsonify({"data": stats, "message": "Fetched from database"})

def get_stats(username):
    stats = fetch_user_stats(username)
    if stats is None:
        return jsonify({'error': 'User not found'}), 404

    stats.pop("username", None)

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        existing_user.total_solved = stats['total_solved']
        existing_user.easy = stats['easy']
        existing_user.medium = stats['medium']
        existing_user.hard = stats['hard']
        existing_user.streak_days = stats['streak_days']
        message = "Stats updated"
    else:
        new_user = User(username=username, **stats)
        db.session.add(new_user)
        message = "Stats saved"

    db.session.commit()
    return jsonify({"message": message, "data": stats})

if __name__ == '__main__':
    app.run(debug=True)
