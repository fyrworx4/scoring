import subprocess

def pollRDP(ip, port, users):
    for user in users:
        if ":" not in user:
            continue
        username = user.split(":")[0]
        password = user.split(":")[1]
    cmd = ['xfreerdp', '/cert-ignore', '/auth-only', '/u:"' + username, '" /p:"' + password, '" /v:' + ip]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        print(output)
        return True
    except:
        return False

print(pollRDP("10.100.10.145", "3389", "saulsolper:Orbitalweapons_1234")) # True
print(pollRDP("10.100.10.145", "3329", "saulsolper:Orbitalweapons_1234")) # False