import subprocess

username = "saulsolper"
password = "Orbitalweapons_1234"
server = "10.100.10.145"
port = "3389"

cmd = ['xfreerdp', '--ignore-certificate', '--authonly', '-u', username, '-p', password]
cmd.append('{}:{}'.format(server, port))

output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)