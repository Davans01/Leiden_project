from api.model.measure_type import MeasureType
from flask import Blueprint, current_app

blueprint = Blueprint("meta", __name__)


@blueprint.route("/config")
def config():
    measure_types = MeasureType.query.all()

    return {
        "env": current_app.config["ENV"],
        "measureTypes": [mt.to_dict() for mt in measure_types],
    }
