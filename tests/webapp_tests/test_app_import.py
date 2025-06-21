from unittest.mock import patch

from webapp.app import create_app
from agentforge.config import Config
from agentforge.core.config_manager import ConfigManager
from agentforge.config_structs.agent_config_structs import AgentConfig


def _dummy_config() -> AgentConfig:
    manager = ConfigManager()
    raw = {
        "name": "SpecializedAgent",
        "params": {},
        "prompts": {"system": "hi", "user": "{msg}"},
        "model": object(),
        "settings": {"system": {"debug": {"mode": True}}},
        "simulated_response": "STUB",
    }
    return manager.build_agent_config(raw)


def test_app_creation():
    with patch.object(Config, "load_agent_data", return_value=_dummy_config()):
        app = create_app()
        assert app is not None
