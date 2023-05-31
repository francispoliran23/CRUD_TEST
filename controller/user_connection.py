from app import app
from model.model_connect import model_connect
from flask import request

object = model_connect()

@app.route("/user/getall")
def user_getall_controller():
    return object.user_getall()

@app.route("/user/creating", methods=["POST"])
def user_add_controller():
    return object.user_add_model(request.form)

@app.route("/user/updating", methods=["PUT"])
def user_update_controller():
    return object.user_update_model(request.form)

@app.route("/user/deleting/<id>", methods=["DELETE"])
def user_deleting_controller(id):
    return object.user_delete_model(id)




# lhfdkjhdsjfhkjshkfsh