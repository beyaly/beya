from flask import Flask, jsonify, request

app = Flask(__name__)

aws_services = [
    {"id": 1, "service": "Lambda"},
    {"id": 2, "service": "Simple Storage Service(S3)"}
]

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, welcome to the AWS Services API!"})

@app.route('/aws_services/get_all', methods=['GET'])
def get_all():
    return jsonify({"aws_services": aws_services})

@app.route('/aws_services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = next((item for item in aws_services if item["id"] == service_id), None)
    if service:
        return jsonify(service)
    else:
        return jsonify({"message": "Service not found"}), 404

@app.route('/aws_services/add_service', methods=['POST'])
def add_service():
    new_service = {
        "id": len(aws_services) + 1,
        "service": request.json.get('service')
    }
    aws_services.append(new_service)
    return jsonify({"message": "Service added successfully"}), 201

@app.route('/aws_services/delete_service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    global aws_services
    aws_services = [item for item in aws_services if item["id"] != service_id]
    return jsonify({"message": "Service deleted successfully"})

@app.route('/aws_services/update_service/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    global aws_services
    service = next((item for item in aws_services if item["id"] == service_id), None)
    if service:
        service["service"] = request.json.get('service', service["service"])
        return jsonify({"message": "Service updated successfully"})
    else:
        return jsonify({"message": "Service not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)