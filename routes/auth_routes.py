from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth = Blueprint('auth', __name__)

# Dummy in-memory user store
users = {
    "user@example.com": "password123"
}

# ✅ Login Route
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if users.get(email) == password:
            session["user"] = email
            flash("Login successful!", "success")
            return redirect(url_for("ai.ai_model"))  # ✅ Redirects to AI page
        else:
            flash("Invalid credentials", "error")

    return render_template("login.html")


# ✅ Signup Route
@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        if email in users:
            flash("Email already registered.", "error")
        elif password != confirm_password:
            flash("Passwords do not match.", "error")
        else:
            users[email] = password
            flash("Signup successful! Please log in.", "success")
            return redirect(url_for("auth.login"))

    return render_template("signup.html")


# ✅ Logout Route
@auth.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully.", "info")
    return redirect(url_for("auth.login"))
