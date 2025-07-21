from src.db.models.user import User

def test_user_model():
    user = User(username="testuser", email="test@example.com", password_hash="hashedpassword")
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.password_hash == "hashedpassword"
