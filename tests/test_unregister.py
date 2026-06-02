def test_unregister_success(client):
    # Arrange
    email = "michael@mergington.edu"
    assert email in client.get("/activities").json()["Chess Club"]["participants"]

    # Act
    response = client.delete(f"/activities/Chess Club/unregister?email={email}")

    # Assert
    assert response.status_code == 200
    assert email not in client.get("/activities").json()["Chess Club"]["participants"]


def test_unregister_activity_not_found(client):
    # Act
    response = client.delete("/activities/NoSuch/unregister?email=a@b.com")

    # Assert
    assert response.status_code == 404


def test_unregister_not_signed_up(client):
    # Arrange
    email = "not-registered@mergington.edu"

    # Act
    response = client.delete(f"/activities/Chess Club/unregister?email={email}")

    # Assert
    assert response.status_code == 400
    assert "not signed up" in response.json().get("detail", "").lower()
