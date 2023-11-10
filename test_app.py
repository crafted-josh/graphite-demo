from app import app, feature_flags

def test_index():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Welcome to the Flask App!" in response.data

def test_newpage_with_feature_flag():
    if feature_flags.get("new_page_flag"):
        with app.test_client() as client:
            response = client.get('/newpage')
            assert response.status_code == 200
            assert b"This is the New Page!" in response.data
    else:
        with app.test_client() as client:
            response = client.get('/newpage')
            assert response.status_code == 404
