from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/model-context', methods=['POST'])
def context():
    content = request.json
    # Dummy response for demo
    response = {
        "received_context": content,
        "status": "success"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
