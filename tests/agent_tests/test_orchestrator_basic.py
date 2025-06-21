from unittest.mock import patch

import pytest

from agentforge.orchestrator import Orchestrator, SpecializedAgent
from agentforge.config import Config
from agentforge.core.config_manager import ConfigManager
from agentforge.config_structs.agent_config_structs import AgentConfig


@pytest.fixture()
def dummy_agent_config(isolated_config: Config) -> AgentConfig:
    config_manager = ConfigManager()
    raw_agent_data = {
        "name": "SpecializedAgent",
        "params": {},
        "prompts": {"system": "hi", "user": "{msg}"},
        "model": object(),
        "settings": isolated_config.data["settings"].copy(),
        "simulated_response": "STUB",
    }
    raw_agent_data["settings"]["system"]["debug"]["mode"] = True
    return config_manager.build_agent_config(raw_agent_data)


def test_orchestrator_executes(dummy_agent_config):
    with patch.object(Config, "load_agent_data", return_value=dummy_agent_config):
        orch = Orchestrator({"test": SpecializedAgent("demo")})
        result = orch.execute("ping")
        assert "test" in result
