from urllib.parse import quote

from src.app import activities


def test_unregister_success_removes_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    activity_path = quote(activity_name, safe="")
    assert email in activities[activity_name]["participants"]

    # Act
    response = client.delete(f"/activities/{activity_path}/unregister", params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert payload == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]


def test_unregister_rejects_student_not_signed_up(client):
    # Arrange
    activity_name = "Chess Club"
    email = "notenrolled@mergington.edu"
    activity_path = quote(activity_name, safe="")

    # Act
    response = client.delete(f"/activities/{activity_path}/unregister", params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload == {"detail": "Student is not signed up for this activity"}


def test_unregister_rejects_unknown_activity(client):
    # Arrange
    unknown_activity = "Unknown Activity"
    email = "student@mergington.edu"
    activity_path = quote(unknown_activity, safe="")

    # Act
    response = client.delete(f"/activities/{activity_path}/unregister", params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload == {"detail": "Activity not found"}
