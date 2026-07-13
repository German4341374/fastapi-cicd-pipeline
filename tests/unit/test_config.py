import pytest
from pydantic import ValidationError

from app.config import Settings


def test_default_settings_are_safe() -> None:
    settings = Settings()
    assert settings.environment == "production"
    assert settings.version == "0.1.0"


def test_unknown_environment_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Settings(environment="preview")
