import random
from flask import Flask, render_template

app = Flask(__name__, static_folder='static')
app.config['TEMPLATES_FOLDER'] = 'templates'

@app.route('/')
def index():
    table_size = 6
    true_fields = [
        random.choice([True, False]) for _ in range(table_size**2)
    ]
    return render_template('index.html', true_fields=true_fields, table_size=table_size)



if __name__ == '__main__':
    app.run(debug=True)
