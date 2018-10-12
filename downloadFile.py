import requests

def downloadFile(downloadUrl):
	resp = requests.get(downloadUrl)
	output = open('C:/Users/Jake/OneDrive/4th Year/project/dataFiles/tests.xlsx', 'wb')
	output.write(resp.content)
	print(downloadUrl + " downloaded")
	output.close()

downloadFile("https://www.hia.ie/sites/default/files/Vhi%20price%20template%2001.07.2018.xlsx")
