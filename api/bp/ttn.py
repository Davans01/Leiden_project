from api.database import db
from api.model.device import Device
from api.model.measure_type import MeasureType
from api.model.measurement import Measurement
from api.model.measurement_row import MeasurementRow
from flask import Blueprint, abort, current_app, request

blueprint = Blueprint("tnn", __name__)


@blueprint.route("/ttn", methods=["POST"])
def tnn():
    if request.headers.get("Authorization") != current_app.config["TTN_AUTH_KEY"]:
        return abort(401)

    data = request.get_json()

    device = Device.query.get(data["hardware_serial"])
    if not device:
        return abort(500)

    measurement = Measurement()
    measurement.device = device
    db.session.add(measurement)

    for (k, v) in data["payload_fields"].items():
        type = MeasureType.query.get(int(k))
        if not type:
            continue

        row = MeasurementRow()
        row.measurement = measurement
        row.type = type
        row.value = float(v)
        db.session.add(row)

    db.session.commit()

    return "", 204
