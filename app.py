print("APP STARTED")

from flask import Flask, request, jsonify
from file_analyzer import analyze_file

app = Flask(__name__)

def is_valid_filename(filename):
    if not filename.endswith(".txt"):
        return "INVALID_EXTENSION"
    if ".." in filename or "/" in filename or "\\" in filename:
        return "INVALID_PATH"
    
    return None

@app.route("/analyze", methods=["POST"])
def analyze():
    
    data = request.get_json()
    if data:
        filename = data.get("file")
    else:
        filename = None

    if not filename:
        return jsonify({
            "status": "error",
            "message": "file name is required"
        }), 400
    
    validation_error = is_valid_filename(filename)

    if validation_error == "INVALID_EXTENSION":
        return jsonify({
            "status": "error",
            "message": "only .txt files are allowed"
        }), 400
    
    if validation_error == "INVALID_PATH":
        return jsonify({
            "status": "error",
            "message": "file should be present in the same directory"
        }), 400
    
    output = analyze_file(filename)

    if output == "FILE_NOT_FOUND":
        return jsonify({
            "status": "error",
            "message": "file not found"
        }), 404
    
    if output is None:
        return jsonify({
            "status": "error",
            "message": "no valid numbers found"
        }), 400

    
    return jsonify({
        "count": output["count"],
        "average": output["average"],
        "minimum": output["min"],
        "maximum": output["max"],
        "product": output["product"]
    })

if __name__ == "__main__":
    app.run(debug=True)
