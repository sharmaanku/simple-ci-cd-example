from app import external_api_data

def test_external_api_data(monkeypatch):
    # Mocking the external API response
    class MockResponse:
        @staticmethod
        def json():
            return {"id": 1, "title": "Test Title"}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    data = external_api_data()
    assert data["title"] == "Test Title"
