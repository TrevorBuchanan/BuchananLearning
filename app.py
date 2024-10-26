from flask import Flask, render_template, url_for

app = Flask(__name__)

lessons = [
    {"title": "Lesson 1: Something", "video_filename": "lesson1.mov"},
    {"title": "Lesson 2: Another Thing", "video_filename": "lesson2.mov"}
]

@app.route('/')
def index():
    return render_template('temp.html', lessons=lessons)

if __name__ == '__main__':
    app.run(debug=True)
