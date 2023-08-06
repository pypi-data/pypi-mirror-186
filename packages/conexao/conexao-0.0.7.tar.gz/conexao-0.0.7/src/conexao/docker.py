from conexao.ssh import start_forward


def start_docker_forward(host):
    '''Creates an SSH forward to a Docker in a host and returns the path to its
    local socket.'''
    return start_forward(host, '{socket}:/var/run/docker.sock')
