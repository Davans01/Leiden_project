from api.database import db
from api.model.test import Test
from flask import Blueprint, request

blueprint = Blueprint("test", __name__)


@blueprint.route("/test/")
def list_tests():
    tests = Test.query.all()

    return {"tests": [test.serialize() for test in tests]}


@blueprint.route("/test/<int:test>/")
def get_test(test):
    test = Test.query.get_or_404(test)

    return test.serialize()


@blueprint.route("/test/", methods=["POST"])
def create_test():
    data = request.get_json()

    test = Test()
    test.name = data["name"]

    db.session.add(test)
    db.session.commit()

    return test.serialize()


@blueprint.route("/test/<int:test>/", methods=["PUT"])
def update_test():
    data = request.get_json()

    test = Test.query.get_or_404(test)
    test.name = data["name"]

    db.session.add(test)
    db.session.commit()

    return test.serialize()


@blueprint.route("/test/<int:test>/", methods=["DELETE"])
def delete_test(test):
    test = Test.query.get_or_404(test)

    db.session.delete(test)
    db.session.commit()

    return "", 204
