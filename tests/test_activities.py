def test_get_activities_returns_expected_shape(client):
    # Arrange
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload

    for activity_name, activity_details in payload.items():
        assert required_keys.issubset(activity_details.keys()), activity_name
        assert isinstance(activity_details["participants"], list)
