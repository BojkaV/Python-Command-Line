import os
import time
import platform

OS = platform.system()
clearcom = ""
if OS == "Windows":
    os.system("cls")
    clearcom = "cls"
else:
    os.system("clear")
    clearcom = "clear"

print("PCL is made by Noay_dev and its their own intelectual property")
time.sleep(1)
os.system(clearcom)

print("Welcome to PCL | Type help to get started")
commands = ["help", "shutdown"]
inputcom = ""

while True:
    inputcom = input("$> ")
    if inputcom.lower() in commands:
        if inputcom.lower() == "help":
            print("Help - Lists all available commands")
            print("Shutdown - Shuts down the command line")
        if inputcom.lower() == "shutdown":
            os.system(clearcom)
            print("Shutting down...")
            time.sleep(3)
            os.system(clearcom)
            exit(0)
    else:
        print("Invalid command")