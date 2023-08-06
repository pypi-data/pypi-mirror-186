from pathlib import Path
import shelve
import subprocess
import os
import signal


sockets_folder = Path('/tmp/conexao')
sockets_folder.mkdir(exist_ok=True)
db_path = str(sockets_folder / 'pids')


def list_forwards():
    with shelve.open(db_path) as db:
        for host, pid in db.items():
            print(host, pid)


def get_pid(host: str) -> int:
    with shelve.open(db_path) as db:
        return db.get(host)  # type: ignore


def kill_host(host: str):
    pid = get_pid(host)
    os.kill(pid, signal.SIGTERM)
    with shelve.open(db_path) as db:
        del db[host]


def is_alive(pid: int) -> bool:
    '''Returns True if a proccess exists and isn't a zombie.'''
    proc_dir = Path(f'/proc/{pid}')
    if not proc_dir.exists():
        return False
    if 'State:	Z' in (proc_dir / 'status').read_text():
        return False
    return True


def start_forward(host: str, forwards: list[str]) -> str:
    '''Inicia um forward usando SSH e salva o pid do SSH num BD.'''
    if isinstance(forwards, str):
        forwards = [forwards]

    # TODO: Host may not be unique...
    # TODO: Only works for 1 socket...
    socket = str(sockets_folder / f'{host}.sock')

    if (pid := get_pid(host)) and is_alive(pid):
        return socket

    cmd = f'ssh {host} -o StreamLocalBindUnlink=yes -nTN'
    for forward in forwards:
        # socket = sockets_folder / f'{host}{i}.sock'
        # TODO: Only works for 1 socket...
        cmd += f' -L {forward.format(socket=socket)}'

    proc = subprocess.Popen(cmd.split())

    with shelve.open(db_path) as db:
        db[host] = proc.pid

    return socket
