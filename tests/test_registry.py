import pytest


@pytest.fixture(scope='module')
def docker_registry():
    from pachypy.registry import DockerRegistry
    return DockerRegistry(registry_host='index.docker.io')


def test_docker_registry_get_image_digest(docker_registry):
    digest = docker_registry.get_image_digest('alpine', 'latest')
    assert digest.startswith('sha256:')


def test_docker_registry_get_image_digest_exception1(docker_registry):
    from pachypy.registry import RegistryImageNotFoundException
    with pytest.raises(RegistryImageNotFoundException):
        docker_registry.get_image_digest('repository/that_doesnt_exist', 'latest')


def test_docker_registry_get_image_digest_exception2():
    from pachypy.registry import DockerRegistry, RegistryAuthorizationException
    with pytest.raises(RegistryAuthorizationException):
        docker_registry = DockerRegistry(registry_host='index.docker.io', auth='Zm9vOmJhcg==')
        docker_registry.get_image_digest('repository/that_doesnt_exist', 'latest')