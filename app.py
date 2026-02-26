import os
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Load model
MODEL_PATH = "Brain_Tumor2_model.h5"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
model = load_model(MODEL_PATH)

# Ensure uploads folder exists
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Class labels
CLASS_NAMES = ["Glioma", "Meningioma", "NoTumor", "Pituitary"]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    filename = None
    
    if request.method == "POST":
        # Check if file is uploaded
        if "file" not in request.files:
            return render_template("index.html", prediction="No file uploaded!", filename=None)
        
        file = request.files["file"]
        if file.filename == "":
            return render_template("index.html", prediction="No file selected!", filename=None)
        
        # Save uploaded file
        filename = file.filename
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # Preprocess image
        img = image.load_img(filepath, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Make prediction
        preds = model.predict(img_array)
        class_index = np.argmax(preds, axis=1)[0]
        prediction = CLASS_NAMES[class_index]

        # Path for displaying image in result.html
        img_path = os.path.join("uploads", filename)
        return render_template("result.html", prediction=prediction, img_path=img_path)

    return render_template("index.html", prediction=prediction, filename=filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
