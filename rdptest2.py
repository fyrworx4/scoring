import subprocess

def pollRDP(ip, port, user):
    username = user.split(":")[0]
    password = user.split(":")[1]
    cmd = ['xfreerdp', '/cert-ignore', '/auth-only', '/u:"' + username + '"',  '/p:"' + password + '"', '/v:' + ip]
    # xfreerdp /cert-ignore /auth-only /u:"saulsolper" /p:"Orbitalweapons_1234" /v:10.100.10.145
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    print(output)

pollRDP("10.100.10.145", "3389", "saulsolper:Orbitalweapons_1234") # True
pollRDP("10.100.10.145", "3329", "saulsolper:Orbitalweapons_1234") # False