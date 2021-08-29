import dns.query

answers = dns.query.udp("telcolab.xyz", "10.100.10.1")

for rdata in answers:
    print('asdfasf', rdata.preference)