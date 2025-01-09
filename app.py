from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///asep.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Define the database models
class Component(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False)

@app.route("/")
def home_page():
    # components = Component.query.all()  # Fetch all components from the database
    return render_template("index.html")

@app.route("/engine")
def engine_page():
    return render_template("engine.html")

@app.route("/brake")
def brake_page():
    return render_template("brake.html")

@app.route("/trans")
def transmission_page():
    return render_template("trans.html")

@app.route("/query")
def query_page():
    return render_template("query.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)

