# Conexao

A connection helper. Current features:

- Management of multiple remote MongoDB connection profiles.
- Faster permanent remote Docker connections.
- SSH port forward proxies.

## MongoDB

Add a JSON file to `~/.config/conexao/config.json`.

Example:

```json
{
  "profiles": {
    "simpleMongo": {
      "mongo": {
        "host": "simple-mongo.example.com"
      },
    },
    "mongoInsideDockerVPS": {
      "mongo": {
        "host": "127.0.0.1"
      },
      "ssh": {
        "host": "my-vps.example.com",
        "forwards": ["127.0.0.1:27017:123.docker.container.ip.456:27017"]
      }
    },
  }
}
```

Then use:

```python
from conexao.mongodb import create_client

client1 = create_client('simpleMongo')
client2 = create_client('mongoInsideDockerVPS')
```


## Docker

Opens a permanent SSH forward for faster remote Docker command execution.
Based on:
https://forums.docker.com/t/setting-docker-host-to-ssh-results-in-slow-workflow-can-ssh-connection-be-reused/98754

    conexao docker <host>

This feature doesn't use the `config.json` file.


## Limitations

This program uses a Python Shelve to store SSH PIDs of all running forwards. Shelve isn't concurrent safe, so avoid calling this program multiple times in parallel. Once the program returns it should be safe to call it again to add more connections.


## Development

Install locally using symlinks:

    pip install -e .

Build:

    python -m build

Publish ([need auth](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives)):

    twine upload dist/*