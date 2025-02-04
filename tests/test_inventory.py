
def test_create_inventory_item(client):
    """Test creating an inventory item"""
    response = client.post(
        "/api/v1/inventory/",
        json={"name": "Test Item", "description": "Test Desc", "quantity": 10, "price": 100.0, "is_active": True},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

def test_get_inventory(client):
    """Test retrieving all inventory items"""
    response = client.get("/api/v1/inventory/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_inventory_item(client):
    """Ensure an item exists before updating it"""
    create_response = client.post(
        "/api/v1/inventory/",
        json={"name": "Test Item", "description": "Test Desc", "quantity": 10, "price": 100.0, "is_active": True},
    )
    assert create_response.status_code == 200
    created_item = create_response.json()
    item_id = created_item["id"]

    response = client.put(
        f"/api/v1/inventory/{item_id}",
        json={"name": "Updated Item", "description": "Updated Desc", "quantity": 5, "price": 99.99, "is_active": True},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Item"

def test_delete_inventory_item(client):
    """Ensure an item exists before deleting it"""
    create_response = client.post(
        "/api/v1/inventory/",
        json={"name": "Delete Item", "description": "To be deleted", "quantity": 1, "price": 50.0, "is_active": True},
    )
    assert create_response.status_code == 200
    created_item = create_response.json()
    item_id = created_item["id"]

    response = client.delete(f"/api/v1/inventory/{item_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted successfully"
