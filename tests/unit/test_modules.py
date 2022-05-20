def test_new_user(new_user):
    assert new_user.email == 'test@test.com'
    assert new_user.password != 'FastIsAwesome'
    assert new_user.fullname == 'fullname'
    assert new_user.username == 'username'
