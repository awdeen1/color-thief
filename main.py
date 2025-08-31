from tools import *
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from flask_bootstrap import Bootstrap5
from werkzeug.utils import secure_filename
import os
from colorthief import ColorThief

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
#file
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def clear_uploads():
    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        clear_uploads()
        # check if the post request has the file part
        if 'image' not in request.files:
            flash('No image part')
            return redirect(url_for('home'))
        image = request.files['image']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if image.filename == '':
            flash('No selected file')
            return redirect(url_for('home'))
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            colorthief = ColorThief(f"uploads/{filename}")
            palette = [rgb_to_hex(rbg) for rbg in colorthief.get_palette(color_count=10)]
            return render_template('home.html', filename=filename, palette=palette)

    return render_template('home.html')

@app.route('/uploads/<path:filename>')
def uploads(filename):
    return send_from_directory('uploads', filename)

if __name__ == "__main__":
    app.run(debug=True)

