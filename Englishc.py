while True:
    colom =""
    web = ""
    filename = ""
    def say(text):
        print(text)
    def get(web, filename):
        import bs4 as bs
        import urllib.request as request
        import requests
        response = requests.get(web)
        if response.status_code == 200:
                with open(filename, "wb") as file:
                    file.write(response.content)
        else:
            print("Errno1: Bad request", web)
        def Update_Toolchain():
               
    code = input("Englishc@windows:~$")
    if code == "About":
        print("Englishc is a programming language created by some contributors. Visit our github page to be a contributor")
    if code == say(colom):
        print(colom)
    if code == "Stop everything":
        exit()
    if code == get(web, filename):
        get(web, filename)
    if code == "Version":
        print("Toolchain version(compiler): 0.0.1")
        print("Shell version: 1.0")
    if code == Update:
        r