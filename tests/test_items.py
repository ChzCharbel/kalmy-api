def test_create_items(client):
    response = client.post("/items/", json={"name": "Laptop", "description": "Laptop Gamer", "price": 1500.00, "available": True})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["description"] == "Laptop Gamer"
    assert data["price"] == 1500.00
    assert data["available"] == True
    assert "id" in data

def test_get_items(client):
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_item_not_found(client):
    response = client.get("/items/9999")
    assert response.status_code == 404

def test_pagination(client):
    # Create multiple items
    for i in range(15):
        client.post("/items/", json={"name": f"Item {i}", "description": f"Description {i}", "price": 10.0 + i, "available": True})
    
    response = client.get("/items/?skip=5&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5