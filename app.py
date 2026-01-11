print("APP STARTED")

from flask import Flask, request, jsonify
from file_analyzer import analyze_file

app = Flask(__name__)

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
