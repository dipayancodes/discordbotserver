from flask import Flask, request, render_template, jsonify
import subprocess
import os

app = Flask(__name__)

# Ensure uploads directory exists
os.makedirs('uploads', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        filename = file.filename
        file_path = os.path.join('uploads', filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully'})
    return jsonify({'message': 'No file part'})

@app.route('/execute', methods=['POST'])
def execute_script():
    filename = request.form.get('filename')
    if filename:
        python_executable = '/usr/bin/python3'  # Replace this with the actual path to your Python executable
        try:
            output = subprocess.check_output([python_executable, os.path.join('uploads', filename)], stderr=subprocess.STDOUT, universal_newlines=True)
            return jsonify({'output': output})
        except subprocess.CalledProcessError as e:
            return jsonify({'error': str(e.output)})
    return jsonify({'message': 'No filename provided'})

if __name__ == '__main__':
    app.run(debug=True)
