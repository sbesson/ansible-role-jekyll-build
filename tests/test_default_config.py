import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('jekyll-build-default')


def test_prefux(File):
    f = File("/var/www/localhost/html/index.html")
    assert f.exists
    assert "\"/www.openmicroscopy.org" in f.content_string
