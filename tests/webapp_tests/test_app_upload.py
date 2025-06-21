from io import BytesIO
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


def test_upload_route_handles_files():
    with patch.object(Config, "load_agent_data", return_value=_dummy_config()):
        app = create_app()
        with app.test_client() as client, \
             patch('agentforge.orchestrator.Orchestrator.execute', return_value={'a': 'b'}):
            data = {
                'instructions': 'ping',
                'documents': (BytesIO(b'hi'), 'test.txt')
            }
            resp = client.post('/', data=data, content_type='multipart/form-data')
            assert resp.status_code == 200
            assert resp.get_json()['results'] == {'a': 'b'}
