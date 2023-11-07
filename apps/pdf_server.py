import os
from flask import Blueprint, render_template, send_from_directory

pdf_server = Blueprint('pdf_server', __name__)

# Get the absolute path to the directory containing the PDF resources
pdf_folder = os.path.join(os.getcwd(), 'pdf_resources')

@pdf_server.route('/download_pdf/<filename>', methods=['GET'])
def download_pdf(filename):
    # Use Flask's send_from_directory to send the file to the user
    return send_from_directory(pdf_folder, filename)

@pdf_server.route('/pdf_resources', methods=['GET'])
def pdf_resources_page():
    return render_template('pdf_resources.html')
