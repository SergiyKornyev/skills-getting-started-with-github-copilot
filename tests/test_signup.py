def test_signup_success(client):
    # Arrange
    email = "testuser@example.com"
    before = client.get("/activities").json()["Chess Club"]["participants"]
    assert email not in before

    # Act
    response = client.post(f"/activities/Chess Club/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json().get("message", "")
    after = client.get("/activities").json()["Chess Club"]["participants"]
    assert email in after


def test_signup_activity_not_found(client):
    # Act
    response = client.post("/activities/NoSuch/signup?email=a@b.com")

    # Assert
    assert response.status_code == 404


def test_signup_duplicate(client):
    # Arrange: michael@mergington.edu already signed up in seed data
    email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/Chess Club/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json().get("detail", "").lower()
