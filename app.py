from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory, abort
from flask_babel import Babel
import datetime
import os

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

# Create a directory for PDFs if it doesn't exist
os.makedirs('static/pdfs', exist_ok=True)

# Create a directory for artwork if it doesn't exist
os.makedirs('static/images/artwork', exist_ok=True)

def get_locale():
    if 'language' in session:
        return session['language']
    return request.accept_languages.best_match(['en', 'zh'])

babel = Babel(app, locale_selector=get_locale)

@app.context_processor
def inject_now():
    return {
        'current_year': datetime.datetime.now().year,
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/climate_tech')
def climate_tech():
    return render_template('climate_tech.html')

@app.route('/thoughts')
def thoughts():
    return render_template('thoughts.html')

@app.route('/thoughts/<thought_id>')
def thought_detail(thought_id):
    try:
        # Validate thought_id to prevent directory traversal
        if not thought_id.isalnum() and not thought_id.replace('-', '').isalnum():
            abort(404)
        template_path = f'thoughts/{thought_id}.html'
        return render_template(template_path)
    except:
        abort(404)

@app.route('/dont_click')
def dont_click():
    return redirect('https://waitbutwhy.com/2015/01/artificial-intelligence-revolution-1.html')

@app.route('/set_language/<language>')
def set_language(language):
    if language not in ['en', 'zh']:
        abort(400)  # Bad request
    session['language'] = language
    return redirect(request.referrer or url_for('index'))

@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        # Security check to prevent directory traversal
        if '..' in filename or filename.startswith('/'):
            abort(404)
        # Use send_from_directory with safe handling of filenames with spaces
        return send_from_directory('static/pdfs', filename, as_attachment=True)
    except Exception as e:
        abort(404)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, port=5004) 