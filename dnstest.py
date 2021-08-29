import dns.query as dns

answers = dns.query('telcolab.xyz', 'A')
for rdata in answers:
    print('Host', rdata.exchange, 'has preference', rdata.preference)