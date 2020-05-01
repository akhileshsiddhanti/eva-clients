from flask import Flask, Blueprint, request, Response, jsonify, url_for,\
    redirect, render_template, abort, session

# import json

from db import ImageInfoRepo

image_info_bp = Blueprint('image_info_blueprint', __name__)


@image_info_bp.route('/')
def all_images():
    # abort(401)  # Unauthorized
    result = ImageInfoRepo.find_all_from_db(True)
    return jsonify(result)

    # resp = Response(json.dumps(result), mimetype='application/json')
    # resp.headers.add('Server', 'python flask')
    # return resp


