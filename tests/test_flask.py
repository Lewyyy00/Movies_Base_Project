from main import app
from unittest.mock import Mock

def test_homepage(monkeypatch):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    avalible_list = ['popular', 'top_rated', 'upcoming', 'now_playing']
    with app.test_client() as client:
       
        for list in avalible_list:
            response = client.get(f'/?list_type={list}')
            assert response.status_code == 200
            api_mock.assert_called_once_with(f'movie/{list}')
            api_mock.assert_called_once_with('movie/popular')




