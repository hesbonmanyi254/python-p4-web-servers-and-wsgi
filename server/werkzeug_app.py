#!/usr/bin/env python3

from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    # This line prints a message to the terminal when a request is received
    print(f'This web server is running at {request.remote_addr}')
    
    # This line sends the response message to the client's browser
    return Response('A WSGI generated this response!')

# Check if the script is being run directly
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    
    # Start the development server
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )
