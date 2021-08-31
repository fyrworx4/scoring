import subprocess

def pollRDP(ip, port, user):
    username = user.split(":")[0]
    password = user.split(":")[1]
    cmd = ['xfreerdp', '--ignore-certificate', '--authonly', '-u', username, '-p', password, ip]
    running = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    print(running.stdout.read())

pollRDP("10.100.10.145", "3389", "saulsolper:Orbitalweapons_1234") # True
#pollRDP("10.100.10.135", "3389", "saulsolper:Orbitalweapons_1234") # False