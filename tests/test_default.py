import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')
FILEPATH = '/var/www/localhost/html/index.html'
PREFIX = '\"/www.openmicroscopy.org'


def test_package(Package):
    assert Package("rubygems").is_installed


def test_prefix(File, TestinfraBackend):
    host = TestinfraBackend.get_hostname()
    f = File(FILEPATH)
    assert f.exists
    if host == 'jekyll-build-dual-config':
        assert PREFIX not in f.content_string
    else:
        assert PREFIX not in f.content_string
