from fastapi.testclient import TestClient
from main import app
from main import Person

client = TestClient(app)

data= {
    id: 7,
    fname: "akanksha",
    lname: "kolte",
    ismale: True

}


def test_create():
    response = client.post("/addperson", json=data)
    assert response.status_code == 200
    assert response.json == data
