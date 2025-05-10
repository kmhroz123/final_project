from flask import Flask, render_template, session, redirect, url_for
from routes.auth_routes import auth
from routes.ai_routes import ai
from fastapi import FastAPI

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'

# Register routes
app.register_blueprint(auth)
app.register_blueprint(ai)

# Home route (redirect if not logged in)
@app.route("/")
def home():
    if 'user' in session:
        return render_template("home.html")
    return redirect(url_for("auth.login"))

if __name__ == "__main__":
    app.run(debug=True)
