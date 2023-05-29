# deploys
import requests
print("Deployer by yazidears")
r = input("(f)ast mode or (d)etailed mode?")
if r == "f":
    print("Deploying now. Getting data from GitHub")
    url = "https://raw.githubusercontent.com/yazidears/persoployer/"
    print("Getting data-file.uwu")
    file = url + "data-file.uwu"
    response = requests.get(file)
    if response.status_code == 200:
        print("Download finished")
        text_file = response.text
    else:
        print("An error ocurred. Launching undeployer now.")
        os.system("python3 undeploy_urg.py")


