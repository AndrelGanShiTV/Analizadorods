from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from module.similitudes import calcular_similitud_archivo
from module.text_functions import extract_text_from_pdf

bp = Blueprint('ods', __name__)


@bp.route('/')
def index():
    return render_template('ods/index.html')


@bp.route('/analyze', methods=('GET', 'POST'))
def analyze():
    results = {'ODS': 0.0}
    archive_name = 'Nombre del Archivo'
    if request.method == 'POST':
        archive_path = request.files['archive_path']
        format_path = archive_path.filename.split('.')
        error = None
        if archive_path is None:
            error = 'No has elegido ningun archivo'
        else:
            archive_name = archive_path.filename
            if format_path[-1] == 'pdf':
                format_path = 'PDF'
            elif format_path[-1] == 'doc' or format_path[-1] == 'docx':
                format_path = 'DOCX'
            else:
                error = 'No se aceptan archivos distintos a .pdf o .docx'
            results = calcular_similitud_archivo(format_path, archive_path)

        print(format_path)

        print(results)

        flash(error)
    return render_template('ods/analyze.html', results=results, archive_name=archive_name)
