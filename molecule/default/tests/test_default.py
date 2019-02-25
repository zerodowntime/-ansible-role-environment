import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_environment_file(host):
    f = host.file('/etc/environment')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o0644
    assert not f.contains('WHOAMI')
    assert f.contains('EDITOR=vim')
