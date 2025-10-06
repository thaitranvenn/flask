from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/add", methods=["GET"])
def add_numbers():
    # Lấy tham số từ query string
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    if a is None or b is None:
        return jsonify({"error": "Not enough argument"}), 400

    result = a + b
    return jsonify({"a": a, "b": b, "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
