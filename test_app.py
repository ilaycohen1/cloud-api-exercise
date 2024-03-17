from app import get_services
import json
import requests

def test_get_services():
    services_data = json.loads(get_services())["services"]
    length = json.loads(get_services())["length"]
    assert len(services_data)==length and length is not None


def test_add_services():
    status = requests.post(url="http://127.0.0.1:5000/api/services",json=json.dumps({"services":[]})).json()["status"]

    length = requests.post(url="http://127.0.0.1:5000/api/services", json=json.dumps({"services":[]})).json()["length"]
    assert length == 0 and status == "ok"