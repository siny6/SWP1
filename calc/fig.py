from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', ['-1'])[0]
    b = d.get('b', ['-1'])[0]
	plus = 0
	mult = 0
    if '' not in [a, b]:
        a, b = int(a), int(b)
        plus = a + b
		mult = a * b
    response_body = html % {'plus':plus, 'mult':mult}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
