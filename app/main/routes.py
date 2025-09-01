from flask import Blueprint, render_template, request
from ..services import OCRService

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def index():
    return render_template('index.html')

@pages_bp.route('/parse-image', methods=['POST'])
def parse_image():
    # This route would handle the image parsing logic
    data = request.json
    return data, 200