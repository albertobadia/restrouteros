from librouteros import connect
from librouteros.login import plain
import os

username = os.environ.get("mtk_username")
password = os.environ.get("mtk_password")
hostname = os.environ.get("mtk_hostname")
api_port = os.environ.get("mtk_port")

print(username)

DEVICE = connect(host=hostname, username=username, password=password, port=api_port, login_method=plain)
