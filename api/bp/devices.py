from datetime import datetime, timedelta
from random import randint

from api.database import db
from api.model.device import Device
from api.model.measure_type import MeasureType
from api.model.measurement import Measurement
from api.model.measurement_row import MeasurementRow
from flask import Blueprint, request
from flask_login import current_user, login_required

blueprint = Blueprint("devices", __name__)


@blueprint.route("/devices")
@login_required
def list_devices():
    devices = Device.query.filter_by(user=current_user).all()

    return {"devices": [device.to_dict() for device in devices]}


@blueprint.route("/devices/<device_serial>")
@login_required
def get_device(device_serial):
    device = Device.query.get(device_serial)
    if not device or device.user_id != current_user.id:
        return {"error": "DEVICE_NOT_FOUND"}, 404

    return device.to_dict()


@blueprint.route("/devices", methods=["POST"])
@login_required
def register_device():
    data = request.get_json()

    device = Device.query.get(data["serial"])
    if not device or device.pairing_code != data["pairing_code"]:
        return {"error": "DEVICE_NOT_FOUND"}, 404

    device.user = current_user

    db.session.add(device)
    db.session.commit()

    return device.to_dict()


@blueprint.route("/devices/<device_serial>/measurements")
@login_required
def get_measurements_for_device(device_serial):
    device = Device.query.get(device_serial)
    if not device or device.user_id != current_user.id:
        return {"error": "DEVICE_NOT_FOUND"}, 404

    measurements = (
        Measurement.query.filter_by(device_id=device_serial)
        .filter(Measurement.timestamp > datetime.now() - timedelta(days=7))
        .all()
    )

    return {"measurements": [measurement.to_dict() for measurement in measurements]}
