from unittest.mock import patch

from agentforge.orchestrator import Orchestrator


def test_run_cog_executes():
    orch = Orchestrator({})
    with patch('agentforge.cog.Cog') as MockCog:
        instance = MockCog.return_value
        instance.run.return_value = 'ok'
        result = orch.run_cog('example_cog.yaml')
        assert result == 'ok'
        MockCog.assert_called_with('example_cog.yaml')
        instance.run.assert_called_once()
