from dns import resolver
from dns.resolver import *

res = resolver.Resolver()

answers = res.query('pfsense.telcolab.xyz', 'A')

for ipval in answers:
    print('asdfasf', ipval.to_text())