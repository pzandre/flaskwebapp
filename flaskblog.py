from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Gabriella',
        'title': 'meular112 post 1',
        'content': 'Primeiro post',
        'date_posted': '10 de setembro de 2020'
    },
    {
        'author': 'Andre',
        'title': 'Flask post 1',
        'content': 'Primeiro post de Flask',
        'date_posted': '10 de setembro de 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
