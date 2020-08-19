from librouteros import connect
from librouteros.login import plain

username = "bctm"
password = "EPsystems7"
hostname = "192.168.0.1"
api_port = 8001

DEVICE = connect(host=hostname, username=username, password=password, port=api_port, login_method=plain)
