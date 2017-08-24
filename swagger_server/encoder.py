from connexion.apps import flask_app
from six import iteritems
from swagger_server.models.base_model_ import Model
from flask import json

class JSONEncoder(flask_app.FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Model):
            dikt = {}
            for attr, _ in iteritems(o.swagger_types):
                value = getattr(o, attr)
                if value is None and not self.include_nulls:
                    continue
                attr = o.attribute_map[attr]
                dikt[attr] = value
            return dikt
        return flask_app.FlaskJSONEncoder.default(self, o)
