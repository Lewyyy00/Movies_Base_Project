import tmdb_client
from unittest.mock import Mock
import pytest

def test_get_poster_url_uses_default_size():
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   assert expected_default_size in poster_url

def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None

def test_get_movies_list(monkeypatch):
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list

   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
   mock_movie_data = {'title': 'Test Movie', 'id': 123}

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie_data

   monkeypatch.setattr("your_module.requests.get", requests_mock)
   movie_data = tmdb_client.get_single_movie(123)
   assert movie_data == mock_movie_data

def test_get_image(monkeypatch):
   mock_images_data = {'backdrops': ['image1.jpg', 'image2.jpg']}

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_images_data

   monkeypatch.setattr("your_module.requests.get", requests_mock)

   images_data = tmdb_client.get_image(123)
   assert images_data == mock_images_data

def test_get_single_movie_cast_success(monkeypatch):
    mock_cast_data = {'cast': [{'name': 'Actor 1', 'character': 'Character 1'},
                               {'name': 'Actor 2', 'character': 'Character 2'}]}

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_cast_data

    monkeypatch.setattr("your_module.requests.get", requests_mock)

    cast_data = tmdb_client.get_single_movie_cast(123)

    assert cast_data == mock_cast_data['cast']