from flask import redirect
from flask_login import logout_user

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("/l"))