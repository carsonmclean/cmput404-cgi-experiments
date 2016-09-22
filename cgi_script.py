#!/usr/bin/env python

import cgi

# stdout is sent over HTTP to the browser
print "Content-type: text/html"
print
print "<HTML><BODY><H1>Hello, world!</H1>"

# The webserver talks back to the CGI program with environment variables
print cgi.print_environ()

print "</BODY></HTML>"
