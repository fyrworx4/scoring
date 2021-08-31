def pollRDP(ip, port, users):
    try:
        for user in users:
            if ":" not in user:
                continue
            username = user.split(":")[0]
            password = user.split(":")[1]
        cmd = ['xfreerdp', '/cert-ignore', '/auth-only', '/u:"' + username, '" /p:"' + password, '" /v:' + ip]
        return True
    except:
        return False

print(pollRDP("10.100.10.145", "3389", "saulsolper:Orbitalweapons_1234"))