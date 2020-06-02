import os


def createFolder(customerName , platformName ,scriptPath):

    os.chdir(scriptPath+"/data")
    if not os.path.exists(customerName):
        os.makedirs(customerName)
        os.chdir(scriptPath+"/data/"+customerName)
    if not os.path.exists(platformName):
        os.makedirs(platformName)
        os.chdir(scriptPath+"/data/"+customerName+"/"+platformName)
    if not os.path.exists("zipfile"):
        os.makedirs("zipfile")
    if not os.path.exists("zipExtract"):
        os.makedirs("zipExtract")
    if not os.path.exists("jsonData"):
        os.makedirs("jsonData")