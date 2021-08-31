import subprocess

def pollRDP(ip, port, user):
    username = user.split(":")[0]
    password = user.split(":")[1]
    cmd = ['xfreerdp', '--ignore-certification', '--authonly', '-u', username, '-p', password, ip]
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    print(output)

pollRDP("10.100.10.145", "3389", "saulsolper:Orbitalweapons_1234") # True
pollRDP("10.100.10.145", "3329", "saulsolper:Orbitalweapons_1234") # False