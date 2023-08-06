import argparse

from conexao.docker import start_docker_forward
from conexao.ssh import list_forwards, kill_host


parser = argparse.ArgumentParser(prog='conexao')
subparsers = parser.add_subparsers(dest='command')

subparser = subparsers.add_parser('list')
subparser.set_defaults(func=lambda **kwargs: list_forwards())


subparser = subparsers.add_parser('kill')
subparser.add_argument('host')
subparser.set_defaults(func=lambda host, **kwargs: kill_host(host))


def docker(host, **_):
    local_sock = start_docker_forward(host)
    print(f'export DOCKER_HOST=unix://{local_sock}')


subparser = subparsers.add_parser('docker')
subparser.add_argument('host')
subparser.set_defaults(func=docker)


def run():
    args = parser.parse_args()
    if args.command:
        args.func(**vars(args))
    else:
        parser.print_help()
