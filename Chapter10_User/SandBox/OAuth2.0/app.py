from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
app.secret_key = "supersekrit"  # Replace this with your own secret!
blueprint = make_github_blueprint(
    client_id="dcf6aff069d1f9ff29a2",
    client_secret="e98c2aeef0df17ada6d4ff6808b2129a4b49e92b",
)
app.register_blueprint(blueprint, url_prefix="/login")


@app.route("/")
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    return "You are @{login} on GitHub".format(login=resp.json()["login"])


if __name__ == "__main__":
    app.run(debug=True, ssl_context='adhoc')
