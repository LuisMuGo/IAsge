import requests

html = requests.get("https://respontodo.com/como-crear-y-ejecutar-scripts-de-bash-shell-en-windows-10/")
print(html.text)