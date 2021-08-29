import dns.resolver

answers = dns.resolver.query('telcolab.xyz')
for rdata in answers:
    print('Host', rdata.exchange, 'has preference', rdata.preference)