#!/usr/bin/env python

import cgi
import os
import json

# stdout is sent over HTTP to the browser
print "Content-type: text/html"
print
print "<HTML><BODY><H1>Hello, world!</H1>"
print "<P>Query String: " + os.environ['QUERY_STRING'] + "</P>"
print "<P>Your browser is: " + os.environ['HTTP_USER_AGENT'] + "</P>"

# The webserver talks back to the CGI program with environment variables
print cgi.print_environ()

print json.dumps(dict(os.environ), indent=4)

print "</BODY></HTML>"
