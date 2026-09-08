import os

from flask import Flask, render_template, request

from services.food_analyzer import analyze_food_label


app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "food-image" not in request.files:
        return "No image uploaded."

    image = request.files["food-image"]

    if image.filename == "":
        return "No image selected."

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        image.filename
    )

    image.save(file_path)

    # Run complete food label analysis
    result = analyze_food_label(file_path)

    # Store uploaded image filename for display
    result["image_filename"] = image.filename

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)