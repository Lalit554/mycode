#!/usr/bin/python3
"""
Making use of HTTP non-200 type responses.
https://tools.ietf.org/html/rfc2616 # rfc spec describing HTTP
1xx - informational
2xx - success / ok
3xx - redirection
4xx - errors
5xx - server errors
"""

from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort
from flask import make_response

app = Flask(__name__)

header = ["Host Name","IP Address","Domain Name"]

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

# set the cookie and redirect to "showtbl"
@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    # if user generates a POST to our API
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assigned via the POST
        #if request.form["nm"] <-- this also works, but returns ERROR if no nm
            user = request.form.get("nm") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            user = "defaultuser"

        print("in setcookie.......")
        # instantiate a response object
        #resp = make_response(render_template("readcookie.html"))
        #resp = make_response(render_template('login.html'))
        resp = make_response(render_template('redirect.html'))
        #resp = make_response()

        # add a cookie to our response object
                        #cookievar #value
        print("here2")
        #resp.set_cookie("userID", name)
        resp.set_cookie("userID", user)

        return resp
        #return redirect(url_for("showtbl")) # redirect to display groups table

    if request.method == "GET": # if the user sends a GET
        return redirect(url_for("index")) # redirect to index


# if user sends GET to / (root)
@app.route("/")
def index():
    return render_template("login.html")   # found in templates/


# if user sends GET or POST to /login
@app.route("/login", methods = ["POST", "GET"])
def login():
    # if user sent a POST
    if request.method == "POST":
        # if the POST contains 'admin' as the value for 'username'
        #if request.form["username"] == "admin" :
        print("here1")
        if request.cookies.get["user"] == "admin":
            return redirect(url_for("showtbl")) # return a 302 redirect to /showtbl
        else:
            abort(401)  # if they didn't supply the username 'admin' send back a 401
    elif request.method == "GET":
        return redirect(url_for("index")) # if they sent a GET to /login send 302 redirect to /


# check users cookie for their name
@app.route("/getcookie")
def getcookie():
    print("in getcookie() ....................")
    # attempt to read the value of userID from user cookie
    name = request.cookies.get("userID") # preferred method
    
    # name = request.cookies["userID"] # <-- this works but returns error
                                       # if value userID is not in cookie
    
    # return HTML embedded with name (value of userID read from cookie) 
    return f'<h1>Welcome {name}</h1>'


# if user sends POST to /addgrp
@app.route("/addgrp", methods = ["GET", "POST"])
def addgrp():
    return render_template("addgroups.html",headings=header,data=groups)   # found in templates/

# if user sends POST to /noaction
@app.route("/noaction", methods = ["POST"])
def noaction():
    return redirect(url_for("showtbl")) # redirect to display groups table

# if user sends POST to /appendgrp
@app.route("/appendgrp", methods = ["POST"])
def appendgrp():
    Hnm = request.form.get("Hostnm")
    ip  = request.form.get("IPAddr")
    Dnm = request.form.get("DName")
    #print(f"Hnm = {Hnm} | ip = {ip} | Dnm = {Dnm}")
    #newgrp = {"hostname": f"{Hnm}","ip": f"{ip}", "fqdn": f"{Dnm}"}
    #print(newgrp)
    if Hnm and ip and Dnm:
       newgrp = {"hostname": f"{Hnm}","ip": f"{ip}", "fqdn": f"{Dnm}"}
       #print(newgrp)
       groups.append(newgrp)
       #print(groups)

    return redirect(url_for("showtbl")) # redirect to display groups table

# if user sends POST to /logout
@app.route("/logout", methods = ["GET"])
def logout():
      #resp = make_response(view_function())
      resp.set_cookie("userID", "")    
      #request.cookies.set_cookie("userID","")
      return redirect(url_for("index")) # redirect to login after logout action

@app.route("/showtbl")
def showtbl():
    name = request.cookies.get("userID") # preferred method

    if name == "admin":
       return render_template("showtbladm.html",headings=header,data=groups)   # found in templates/
    else:
       return render_template("showtbloth.html",headings=header,data=groups)   # found in templates/


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

