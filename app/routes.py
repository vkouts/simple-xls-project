import io
import xlwt
from app import app, db
from flask import render_template, url_for, redirect, request, abort, send_file
from app.models import Record


@app.route('/', methods=['GET', 'POST'])
def index():
    q = Record.query.all()
    return render_template('index.html', title='XLS Example', records=q)


@app.route('/xls')
def get_xls():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('FB')
    records = Record.query.all()
    row = 0
    for im in records:
        ws.write(row, 0, im.name)
        ws.write(row, 1, im.email)
        ws.write(row, 2, im.profile)
        ws.write(row, 3, im.photo)
        row += 1 
    myio = io.BytesIO()
    wb.save(myio)
    myio.seek(0)
    return send_file(myio, attachment_filename="file.xls", as_attachment=True)
