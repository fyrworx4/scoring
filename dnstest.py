import dns.resolver

answers = dns.resolver.query('telcolab.xyz')

print(answers)