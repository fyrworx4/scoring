import subprocess

def pollRDP(ip, port, user):
    username = user.split(":")[0]
    password = user.split(":")[1]
    #cmd = ['xfreerdp', '--ignore-certificate', '--authonly', '-u', username, '-p', password, ip]
    cmd = ['xfreerdp', '/cert-ignore', '/auth-only', f'/u:"{username}"', f'/p:"{password}"', f'/v:{ip}']

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = proc.stdout.read()

    print(output)
    #p = subprocess.Popen(cmd, stdout=subprocess.PIPE, close_fds=True)
    #output = p.stdout.read()
    #print(output)

    #output = subprocess.check_output(cmd)
    #print(output)
    #output = str(subprocess.Popen(cmd, stdout=subprocess.PIPE))
    #print(output)
    
pollRDP("10.100.10.145", "3389", "saulsolper:Orbitalweapons_1234") # True
#pollRDP("10.100.10.135", "3389", "saulsolper:Orbitalweapons_1234") # False