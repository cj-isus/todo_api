from src.db.models.project import Project

def test_project_model():
    project = Project(title="Test Project", user_id=1)
    assert project.title == "Test Project"
    assert project.user_id == 1
