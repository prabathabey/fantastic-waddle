from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# location of the gif displayed.
image_url = "/static/images/hello-world.gif"

@app.route("/")
def index():
    return render_template("index.html", url=image_url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
