from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)
urls = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.form['url']
    if url in urls:
        short_url = urls[url]
    else:
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choices(characters, k=6))
        urls[url] = short_url
    return render_template('shorten.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    for url, code in urls.items():
        if code == short_url:
            return redirect(url)
    return f'<h1>404 Not Found</h1><p>The requested URL was not found on this server.</p>'

if __name__ == '__main__':
    app.run(debug=True)
