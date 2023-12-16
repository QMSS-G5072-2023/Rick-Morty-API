import pytest
import requests_mock
import sys

sys.path.append("Users/张语扬/poetry_project/Final/rmtrend")

from src.rmtrend.rmtrend import fetch_character_info, fetch_location_info, recent_reddit

# Mock data for tests
character_mock_response = {
    'results': [{
        # ... (character data as in your example)
    }]
}

location_mock_response = {
    'results': [{
        # ... (location data as in your example)
    }]
}

reddit_mock_response = {
    'data': {
        'children': [
            {'data': {'title': 'Post 1', 'score': 100, 'num_comments': 10}},
            # ... (more mock posts)
        ]
    }
}

# Tests for fetch_character_info
def test_fetch_character_info_success():
    with requests_mock.Mocker() as m:
        m.get("https://rickandmortyapi.com/api/character/?name=Rick Sanchez", json=character_mock_response)
        result = fetch_character_info("Rick Sanchez")
        assert result['Name'] == 'Rick Sanchez'
        assert result['Status'] == 'Alive'
        assert result['Species'] == 'Human'
        assert result['Gender'] == 'Male'
        assert result['Origin'] == 'Earth (C-137)'
        assert result['Episode Count'] == 3
        assert result['Image'] == 'https://rickandmortyapi.com/api/character/avatar/1.jpeg'
        assert result['URL'] == 'https://rickandmortyapi.com/api/character/1'

def test_fetch_character_info_not_found():
    with requests_mock.Mocker() as m:
        m.get("https://rickandmortyapi.com/api/character/?name=Audrey Zhang", json=character_mock_response)
        result = fetch_character_info("Rick Sanchez")
        assert result is None

# Tests for fetch_location_info
def test_fetch_location_info_success():
    with requests_mock.Mocker() as m:
        m.get("https://rickandmortyapi.com/api/location/?name=Citadel of Ricks", json=location_mock_response)
        result = fetch_location_info("Citadel of Ricks")
        # Add your assertions here, indented inside the function
        assert result is not None
        assert result['Name'] == 'Citadel of Ricks'

def test_fetch_location_info_not_found():
    with requests_mock.Mocker() as m:
        m.get("https://rickandmortyapi.com/api/location/?name=NYC for test", json=location_mock_response)
        result = fetch_location_info("NYC for test")
        assert result is None

# Tests for recent_reddit
def test_recent_reddit():
    # This requires mocking PRAW. One approach is to use unittest.mock to patch the PRAW methods used in your function.
    # Example (simplified):
    with mock.patch('praw.Reddit') as mock_reddit:
        mock_reddit.subreddit.return_value.search.return_value = [mock.MagicMock(title='Post 1', score=100, num_comments=10)]
        results = recent_reddit('Rick')
        assert len(results) == 1
        # More assertions based on your reddit_mock_response

# Run tests
if __name__ == '__main__':
    pytest.main()
