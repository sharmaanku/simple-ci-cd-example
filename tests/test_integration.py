from app import add, external_api_data

def test_add_and_external_api():
    result = add(2, 3)
    data = external_api_data()
    assert result == 5
    assert "title" in data
