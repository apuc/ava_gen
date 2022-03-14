import os
from Auth import auth_required
from config import ROOT_DIR
from flask import Blueprint, request
from generator.generate import generate

api_page = Blueprint('api', __name__, template_folder='templates')

@api_page.route('/generate', methods=['GET'])
@auth_required()
def gen():
    url = generate(ROOT_DIR)
    host = os.getenv("HOST")
    url = f"{host}{url}"
    dct = dict(
        url = url,
    )
    return dct