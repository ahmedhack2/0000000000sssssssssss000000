from flask_restx import fields

from .extensions import api

bot_conversion_model = api.model("Chat", {
        "message": fields.String,
        "response": fields.String
    })