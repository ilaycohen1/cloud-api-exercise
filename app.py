from flask import Flask, request, render_template
import test_app
import json


app = Flask(__name__)

@app.route('/api/services', methods=['GET'])
def get_services():
    data = [{'serviceName':'service1'}]
    return json.dumps({
        "services": data,
        "length": len(data),
        "last_updated":"2024-03-17"
    })

@app.route('/api/services', methods=['POST'])
def add_services():
    data=json.loads(request.json["services"])
    return json.dumps({
        "status":"ok",
        "length":len(data)
    })

if __name__ == '__main__':
    app.run(debug=True)
 