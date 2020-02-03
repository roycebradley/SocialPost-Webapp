from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts

app = Flask(__name__)

#security measure against SQL injection or javascript insert to allow users to see info in db
CORS(app)

@app.route('/', methods=['GET', 'POST'])

def index():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    #calling get_posts() function is models.py
    posts = get_posts()

    #create a variable posts and setting it to posts so it reflects new posts
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)