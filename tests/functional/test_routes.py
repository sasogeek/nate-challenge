import json
from app import app


def test_index():
    """
    GIVEN the app object
    WHEN the '/' page is requested
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200


def test_health():
    """
    GIVEN the app object
    WHEN data is submitted to the '/health' endpoint
    THEN check that the response is valid, a json object, with a res key and a string value
    """
    with app.test_client() as test_client:
        response = test_client.post('/health', content_type='application/json', data=json.dumps({'text': "Tell the audience what you're going to say. Say it. Then tell them what you've said.", 'order': ''}))
        assert response.status_code == 200
        assert json.loads(response.data)
        assert 'res' in json.loads(response.data)
        assert type(json.loads(response.data)['res']) == str
