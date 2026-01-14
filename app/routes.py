from flask import Blueprint, request, jsonify
from app.services import analyze_file
from app.db import save_report

routes = Blueprint("routes", __name__)

def is_valid_filename(filename):
    if not filename.endswith(".txt"):
        return "INVALID_EXTENSION"
    if ".." in filename or "/" in filename or "\\" in filename:
        return "INVALID_PATH"
    
    return None

def error_response(code, message, status_code):
    return jsonify({
        "status": "error",
        "error": {
            "code": code,
            "message": message
        }
    }), status_code

@routes.route("/analyze", methods=["POST"])
def analyze():
    
    data = request.get_json()
    if data:
        filename = data.get("file")
    else:
        filename = None

    if not filename:
        return error_response(
            "MISSING_FILE_NAME",
            "filename is required",
            400
        )

    
    validation_error = is_valid_filename(filename)

    if validation_error == "INVALID_EXTENSION":
        return error_response(
            "INVALID_EXTENSION",
            "only .txt files are allowed",
            400
        )
    
    if validation_error == "INVALID_PATH":
        return error_response(
            "INVALID_PATH",
            "file should be present in the same directory",
            400
        )
    
    output = analyze_file(filename)

    if output == "FILE_NOT_FOUND":
        return error_response(
            "FILE_NOT_FOUND",
            "file not found",
            404
        )
    
    if output is None:
        return error_response(
            "NO_VALID_NUMBERS",
            "no valid numbers found",
            400
        )

    save_report(filename, output)
    print(f"\nSaved the Result in a SQL Database report.db\n")
    
    return jsonify({
        "count": output["count"],
        "average": output["average"],
        "minimum": output["min"],
        "maximum": output["max"],
        "product": output["product"]
    })