from flask import Blueprint, abort, current_app, request

blueprint = Blueprint("tnn", __name__)


@blueprint.route("/tnn", methods=["POST"])
def tnn():
    if request.headers.get("Authorization") != current_app.config["TNN_AUTH_KEY"]:
        return abort(401)

    data = request.get_json()
    print(data)
