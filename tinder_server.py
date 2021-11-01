from flask import Flask, jsonify, request
import estrutura_interesses as i
from flask import render_template

database = i.database
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/pessoas", methods=['GET', 'POST'])
def pessoas(database):
    return render_template('pessoas.html', pessoas=database["pessoas"])


if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
