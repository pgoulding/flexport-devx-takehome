import json

from rock_paper_scissors.app import app


def test_health_endpoint():
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.data == b"OK"


def test_rps_endpoint_with_valid_input():
    with app.test_client() as client:
        data = {"move": "Rock"}
        response = client.post(
            "/rps", data=json.dumps(data), content_type="application/json"
        )
        # import pdb
        # pdb.set_trace()
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert "result" in response_data
        assert "game_result" in response_data
        assert "pc_choice" in response_data
        result = response_data["result"]
        game_result = response_data["game_result"]
        pc_choice = response_data["pc_choice"]

        if game_result == 0:
            assert result == "Tie"
            assert pc_choice == 0
        elif game_result == -1:
            assert result == "I win, Paper beats Rock"
            assert pc_choice == 1
        else:
            assert result == "You win, Rock beats Scissors"
            assert pc_choice == 2
