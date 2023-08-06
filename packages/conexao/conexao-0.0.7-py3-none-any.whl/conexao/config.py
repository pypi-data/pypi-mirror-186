import json
from pathlib import Path


config_fp = Path('~/.config/conexao/config.json').expanduser()
config = json.loads(config_fp.read_text(encoding='utf8'))
