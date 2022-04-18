from flask import render_template, request, jsonify

from utils import *

app = Flask(__name__)
DATABASE = './db.db'


@app.route("/blog", methods=['POST'])
def blog():
    post_in_blog(request.form['author'], request.form['text'])
    queryset = get_all_blogs()
    return jsonify(queryset)


if __name__ == "__main__":
    app.run()
