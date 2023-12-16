import pytest
import requests_mock
from rmtrend.rmtrend import fetch_character_info, fetch_location_info, recent_reddit
from unittest.mock import patch, MagicMock

# Mock data for the Rick & Morty API
character_mock_response = {
    'results': [
        {
            'name': 'Rick Sanchez',
            'status': 'Alive',
            'species': 'Human',
            'gender': 'Male',
            'origin': {'name': 'Earth (C-137)'},
            'episode': ['url1', 'url2'],
            'image': 'https://rickandmortyapi.com/api/character/avatar/1.jpeg',
            'url': 'https://rickandmortyapi.com/api/character/1'
        }
    ]
}

location_mock_response = {
    'results': [
        {
            'name': 'Citadel of Ricks',
            'type': 'Space station',
            'dimension': 'unknown',
            'residents': ['url1', 'url2', 'url3'],
            'url': 'https://rickandmortyapi.com/api/location/3'
        }
    ]
}

# Tests for fetch_character_info
def test_fetch_character_info_success():
    with requests_mock.Mocker() as m:
        m.get("https://rickandmortyapi.com/api/character/?name=Rick+Sanchez", json=character_mock_response)
        result = fetch_character_info("Rick Sanchez")
        assert result['Name'] == 'Rick Sanchez'
        assert result['Status'] == 'Alive'
        # ... more assertions

def test_fetch_character_info_not_found():
    with requests_mock.Mocker() as m:
        m.get("https://rickandmortyapi.com/api/character/?name=Unknown", json={'results': []})
        result = fetch_character_info("Unknown")
        assert result is None

# Tests for fetch_location_info
def test_fetch_location_info_success():
    with requests_mock.Mocker() as m:
        m.get("https://rickandmortyapi.com/api/location/?name=Citadel+of+Ricks", json=location_mock_response)
        result = fetch_location_info("Citadel of Ricks")
        assert result['Name'] == 'Citadel of Ricks'
        # ... more assertions

def test_fetch_location_info_not_found():
    with requests_mock.Mocker() as m:
        m.get("https://rickandmortyapi.com/api/location/?name=Unknown", json={'results': []})
        result = fetch_location_info("Unknown")
        assert result is None
