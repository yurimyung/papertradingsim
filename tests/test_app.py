from papertradingsim import create_app


def test_health_endpoint():
    app = create_app({"TESTING": True})

    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "service": "papertradingsim",
        "status": "ok",
    }


def test_factory_accepts_configuration_overrides():
    app = create_app({"TESTING": True})

    assert app.config["TESTING"] is True
