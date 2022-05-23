def test_get_all_users(test_client):
    response = test_client.get('/user')
    assert response.status_code == 200


def test_user_by_id(test_client):
    response = test_client.get('/user/17/')

    assert response.status_code == 404
    assert 'Could not find user with that id' in response.content.decode('utf-8')
