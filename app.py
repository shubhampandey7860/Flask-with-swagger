from flask import Flask, jsonify,request
from flask_swagger_ui import get_swaggerui_blueprint
from swagger_spec import swagger_spec

app = Flask(__name__)


items = []

# Route to add an item
@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.get_json()
    items.append(data)
    print(data)
    print(items)
    return jsonify({'message': 'Item added successfully'}),201

# Route to get all items
@app.route('/get_items', methods=['GET'])
def get_items():
    return jsonify(items)

# Route to serve Swagger JSON documentation
@app.route('/api/swagger.json')
def serve_swagger_json():
    return jsonify(swagger_spec)

# Swagger UI blueprint configuration
SWAGGER_URL = '/api/docs/'  # URL for accessing Swagger UI (not a part of API)
API_URL = '/api/swagger.json'   # URL to the API documentation JSON

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask Swagger API"
    }
)

# Register the Swagger UI blueprint with the Flask application
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
