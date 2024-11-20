from flask import Flask, request, render_template, jsonify, send_from_directory
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

app = Flask(__name__)

# Path to the WebDriver
CHROME_DRIVER_PATH = r"C:\Users\Fabio\Desktop\WEBDRIVER\chromedriver-win64\chromedriver.exe"

# Path for static files
STATIC_IMAGE_PATH = r"C:\Users\Fabio\Desktop\crypto\static"

# Path to save the data.txt file
DATA_FILE_PATH = r"C:\Users\Fabio\Desktop\crypto\data.txt"

@app.route('/')
def index():
    return render_template('matrix.html')

@app.route('/static/<filename>')
def static_files(filename):
    return send_from_directory(STATIC_IMAGE_PATH, filename)

# Route to handle Wikipedia search
@app.route('/search', methods=['POST'])
def search():
    word = request.form['parola']
    wikipedia_url = f"https://it.wikipedia.org/wiki/{word}"

    # Configure Selenium in headless mode
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(wikipedia_url)
        content = driver.find_element(By.ID, 'mw-content-text').text
        letters = [char for char in content if char.isalnum()]
        driver.quit()
        truncated_letters = letters[:1024] + [''] * (1024 - len(letters[:1024]))
        return jsonify({'letters': truncated_letters})
    except Exception as e:
        driver.quit()
        return jsonify({'error': str(e)})

# Route to save matrix data into data.txt
@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.json.get('matrixData', [])
    try:
        with open(DATA_FILE_PATH, 'w') as file:
            for row in data:
                file.write(' '.join(row) + '\n')
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
