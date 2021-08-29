import dns.resolver

answers = dns.resolver.query.udp("telcolab.xyz", "10.100.10.1")

for rdata in answers:
    print('asdfasf', data.preference)