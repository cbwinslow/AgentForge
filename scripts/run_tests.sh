#!/bin/bash
set -euo pipefail
pip install -r requirements.lock
pytest -q
