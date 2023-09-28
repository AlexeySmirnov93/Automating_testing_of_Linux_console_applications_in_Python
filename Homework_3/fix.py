from check_skript import checkout
import pytest
import yaml
from datetime import datetime
import os

with open("config.yaml") as a:
    data = yaml.safe_load(a.read())
    

@pytest.fixture()
def make_folders():
    checkout(f"mkdir -p {data['folderin']} {data['folderout']} {data['folderext']}" , '')
    yield
    # checkout(f"rm -rf {data['folderin']} {data['folderout']} {data['folderext']}", '')
    

@pytest.fixture()
def make_files():
    checkout(f"cd {data['folderin']}; touch file1 file2", '')
    
    
@pytest.fixture()
def make_string():
    files = {}
    for file in os.listdir(data['folderin']):
        files[file] = os.path.getsize(f"{data['folderin']}/{file}")
    
    checkout(f"cd {data['folderin']}; echo 'time info: {datetime.now().strftime('%H:%M:%S')} files: {len(files)}\n{files}' >> stat.txt; cat /proc/loadavg >> stat.txt; echo '' >> stat.txt", '')