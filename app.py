from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    profile_image = "https://koshka.top/uploads/posts/2021-11/thumbs/1637819640_69-koshka-top-p-britanets-koshka-okras-70.jpg"
    user_name = "Ириска"
    return render_template('index.html', profile_image=profile_image, user_name=user_name)


app.run()
