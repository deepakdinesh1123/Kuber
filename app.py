from flask import Flask, jsonify, request

# Create a Flask app
app = Flask(__name__)


@app.route("/", methods=["POST"])
def echo_message():
    # Get the message from the POST request
    message = request.data.decode("utf-8")

    # Create a response JSON
    response = {"message": message}

    # Return the JSON response
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
