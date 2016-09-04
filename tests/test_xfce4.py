import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_helpers_file_permissions(File):
    config = File('/etc/xdg/ansible-default-web-browser/xfce4/helpers.rc')

    assert config.exists
    assert config.is_file
    assert config.user == 'root'
    assert config.group == 'root'
    assert oct(config.mode) == '0644'
    assert config.contains('WebBrowser=google-chrome')

def test_desktop_file_permissions(File):
    desktop = File('/etc/xdg/ansible-default-web-browser/xfce4/helpers/google-chrome.desktop')

    assert desktop.exists
    assert desktop.is_file
    assert desktop.user == 'root'
    assert desktop.group == 'root'
    assert oct(desktop.mode) == '0644'

@pytest.mark.parametrize('expected', [
    ('Type=X-XFCE-Helper'),
    ('X-XFCE-Category=WebBrowser'),
    ('X-XFCE-Commands=/usr/bin/google-chrome-stable'),
    ('X-XFCE-CommandsWithParameter=/usr/bin/google-chrome-stable "%s"')
])
def test_desktop_file(File, expected):
    desktop = File('/etc/xdg/ansible-default-web-browser/xfce4/helpers/google-chrome.desktop')

    assert desktop.exists
    assert desktop.is_file
    assert desktop.contains(expected)
