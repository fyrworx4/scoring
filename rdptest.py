import subprocess

username = "saulsolper"
password = "Orbitalweapons_1234"
server = "10.100.10.145"
port = "3389"

cmd = ['xfreerdp', '/cert-ignore', '/auth-only', '/u:' + username, '/p:' + password, '/v:' + server]
#cmd.append('{}:{}'.format(server, port))

output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)