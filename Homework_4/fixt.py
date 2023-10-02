from ssh_help import ssh_checkout, upload_files
import yaml, pytest

with open('config.yml', 'r') as a:
    config = yaml.safe_load(a)

@pytest.fixture()
def prepare():
    upload_files(config['ssh_host'],
                 config['ssh_user'],
                 config['ssh_pass'],
                 "tests/p7zip-full.deb",
                 f"/home/{config['ssh_user']}/p7zip-full.deb"
                )
    
    ssh_checkout(config['ssh_host'],
                 config['ssh_user'],
                 config['ssh_pass'],
                 f"echo '{config['ssh_pass']}' | sudo -S dpkg -i /home/{config['ssh_user']}/p7zip-full.deb",
                 "Setting up"
                )

    yield
    
    ssh_checkout(config['ssh_host'],
                 config['ssh_user'],
                 config['ssh_pass'],
                 f"echo '{config['ssh_pass']}' | sudo -S dpkg -r p7zip-full",
                 "Status: install ok installed"
                )