import subprocess

def pollRDP(ip, port, user):
    username = user.split(":")[0]
    password = user.split(":")[1]
    #cmd = ['xfreerdp', '--ignore-certificate', '--authonly', '-u', username, '-p', password, f'{ip}:{port}']
    cmd = ['xfreerdp', '/cert-ignore', '/auth-only', f'/u:"{username}"', f'/p:"{password}"', f'/v:{ip}:{port}']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = proc.communicate()

    if (str(output)[-5]) == "0":
        print(True)
        return True
    else:
        print(False)
        return False

    #cmd = ['xfreerdp', '/cert-ignore', '/auth-only', f'/u:"{username}"', f'/p:"{password}"', f'/v:{ip}']
    #p = subprocess.Popen(cmd, stdout=subprocess.PIPE, close_fds=True)
    #output = p.stdout.read()
    #print(output)
    #output = subprocess.check_output(cmd)
    #print(output)
    #output = str(subprocess.Popen(cmd, stdout=subprocess.PIPE))
    #print(output)
    
pollRDP("10.100.10.145", "3389", "saulsolper:Orbitalweapons_1234") # True
pollRDP("10.100.10.135", "3389", "saulsolper:Orbitalweapons_1234") # False
pollRDP("10.100.10.145", "1337", "saulsolper:Orbitalweapons_1234") # False