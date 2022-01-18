import os
from config import ROOT_DIR
from flask import Blueprint, render_template, request, redirect, url_for, flash
from generator.generate import generate

api_page = Blueprint('api', __name__, template_folder='templates')

@api_page.route('/generate', methods=['GET']    )
def gen():
    url = generate(ROOT_DIR)
    host = os.getenv("HOST")
    url = f"{host}{url}"
    dct = dict(
        url = url,
    )
    return dct