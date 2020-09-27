#! /usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

var = mydata.getvalue("z")


output = subprocess.getoutput("sudo " + var)

print("\n Hello User Welcome to output Console")
print("<br />")
print("<br />")



print("Command : ",var)
print("<br />")
print("<br />")


print("output :",output)
