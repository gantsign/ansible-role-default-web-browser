Ansible Role: Default Web Browser
=================================

[![Tests](https://github.com/gantsign/ansible-role-default-web-browser/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible-role-default-web-browser/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.default--web--browser-blue.svg)](https://galaxy.ansible.com/gantsign/default-web-browser)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-default-web-browser/master/LICENSE)

This role sets the default web browser for Ubuntu Unity and Xfce4.

Requirements
------------

* Ansible >= 2.8

* Ubuntu

    * Xenial (16.04)
    * Bionic (18.04)

* Supported desktop

    * Gnome

    * Ubuntu Unity

    * Xfce4 (i.e. the desktop on XUbuntu)

* Installed web browser

    * This role doesn't install the web browser; you need to have already
      installed your chosen web browser before using this role.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# The web browser to make the default (i.e. the name of the .desktop file without the extension)
default_web_browser: google-chrome
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.default-web-browser
      default_web_browser: google-chrome
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
