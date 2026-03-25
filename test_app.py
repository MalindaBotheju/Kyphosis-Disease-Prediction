import pytest
from app import app # This imports your Flask app
import os

@pytest.fixture
def client():
    # This creates a fake web browser to test your app without actually starting a server
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage_loads(client):
    """Test if the homepage loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Patient Screening" in response.data # Checks if your UI text is there!

def test_model_exists():
    """Test if the SVM model file is actually in the folder"""
    assert os.path.exists("kyphosis_svm_model.pkl") == True