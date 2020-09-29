#! /usr/bin/python3

import cgi
import subprocess
import webbrowser as wb

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

var = mydata.getvalue("z")

if("docker" in var):
        wb.open("http://13.233.92.195/cgi-bin/Doc.py")

output = subprocess.getoutput("sudo " + var)

print("\n Hello User Welcome to output Console")
print("<br />")
print("<br />")

print("*****************************************************************************************************************************************************************************************************")
print("<br />")
print("<br />")

print("Command : ",var)
print("<br />")
print("<br />")


print("output :",output)
