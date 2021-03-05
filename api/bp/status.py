from flask import Blueprint, current_app

blueprint = Blueprint("status", __name__)


@blueprint.route("/status")
def status():
    return {
        "env": current_app.config["ENV"],
    }
