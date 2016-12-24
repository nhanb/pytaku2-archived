## Dev setup

- Debian Jessie
- Ansible 2.2
- Vagrant 1.9
- Virtualbox 5.1
- Python 3.4

```bash
sudo apt-get install python3-venv libpq-dev
python3 -m venv ~/.venvs/pytaku
~/.venvs/pytaku/bin/activate
pip install -r backend/requirements-dev.txt

# https://github.com/mitchellh/vagrant/issues/6769#issuecomment-252151694
# TL;DR: installs Guest Additions automatically so vboxfs shared folder syncing works
vagrant plugin install vagrant-vbguest
vagrant up --provision

vagrant ssh
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
```
