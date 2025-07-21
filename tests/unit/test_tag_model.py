from src.db.models.tag import Tag

def test_tag_model():
    tag = Tag(name="Test Tag", user_id=1)
    assert tag.name == "Test Tag"
    assert tag.user_id == 1
