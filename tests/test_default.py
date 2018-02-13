import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_package(Package):
    assert Package("which").is_installed


def test_index(File):
    f = File("/var/www/localhost/html/index.html")
    assert f.exists
    assert f.is_file
