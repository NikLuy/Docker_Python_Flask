from flask import Flask, render_template
import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Disable template cachin

@app.route('/')
def index():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
