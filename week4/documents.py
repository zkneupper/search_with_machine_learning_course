#
# A simple endpoint that can receive documents from an external source, mark them up and return them.  This can be useful
# for hooking in callback functions during indexing to do smarter things like classification
#
from flask import (
    Blueprint, redirect, render_template, request, url_for, jsonify, abort
)



bp = Blueprint('documents', __name__, url_prefix='/documents')


# Take in a JSON document and return a JSON document
@bp.route('/annotate', methods=['POST'])
def annotate():
    if request.mimetype == 'application/json':
        return request.get_json()
    abort(415)
