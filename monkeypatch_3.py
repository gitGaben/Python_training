# data_fetcher.py

#def fetch_data():
#    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
#    return response.json()["title"]

# test_data_fetcher.py
import pytest
from data_fetcher import fetch_data

def test_fetch_data_with_monkeypatch(monkeypatch):
    # Mock the requests.get function
    def mock_get(*args, **kwargs):
        class MockResponse:
            @staticmethod
            def json():
                return {"title": "Mocked data"}

        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    # Call the fetch_data function, which will now use the mocked requests.get
    result = fetch_data()

    # Verify that the function returned the expected result based on the mock
    assert result == "Mocked data"

    # Reset or undo the monkeypatch modifications
    monkeypatch.undo()

if __name__ == '__main__':
    # Run the tests using pytest
    pytest.main([__file__])