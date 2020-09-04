import os


class Motherboard:
    manufacturer = ""
    serialNumber = ""

#Defining DRAM class
class DRAM:
    manufacturer = ""
    serialNumber = ""
    size = ""
    locator = ""

################################################################
#getDramInfo()
#arguments: none
#returns: nothing
#Redirects output of dmidecode -t17 command to file
#then parses that file and extracts relevant DRAM information. 
#DRAM object is created for each DRAM present in the system and 
#the DRAM object's member variables are initalized with the 
#extract DRAM information. Finally the member variables of each 
#DRAM object is printed.
################################################################
def getDramInfo():
    numDrams = 0
    dramList = []

    #redirect stdout of dmidecode command to file
    os.system("sudo dmidecode -t 17 > dram.txt")
    #open file to read
    dramFp = open("dram.txt", "r")

    #count the number of drams in system
    for line in dramFp:
        if 'type 17' in line:
            numDrams = numDrams + 1

    #go back to beginning of file
    dramFp.seek(0)

    for drams in range(0, numDrams):
        #Flags letting us know that a Dram's information has been read
        manufacturer = False
        serialNumber = False
        size = False
        locator = False
        #creating DRAM object for each DRAM in system
        dram = DRAM()

        #extract DMI information from file
        for line in dramFp:
            #if all of a Dram's information has been read, break
            if(manufacturer and serialNumber and size and locator):
                break

            if 'Manufacturer' in line:
                dram.manufacturer = line.split("Manufacturer:",1)[1].strip()
                manufacturer = True
            if 'Serial Number' in line:
                dram.serialNumber = line.split("Serial Number:",1)[1].strip()
                serialNumber = True
            if 'Size' in line:
                dram.size = line.split("Size:",1)[1].strip()
                size = True
            if 'Locator' in line:
                dram.locator = line.split("Locator:",1)[1].strip()
                locator = True

        #add dram object to dram list
        dramList.append(dram)

    print("DRAM Information")
    for dramObj in dramList:
        print(dramObj.__dict__)

    dramFp.close()

############################################################################
#getMBInfo()
#arguments: none
#returns: nothing
#Redirects output of dmidecode -t 2 to file.
#Then parses this file extracts relevant motherboard information.
#Motherboard object is created and member variables are set to the extracted
#information and printed.
############################################################################

def getMBInfo():
    os.system("sudo dmidecode -t 2 > mb.txt")
    
    motherboardFp = open("mb.txt", "r")
    
    mb = Motherboard()
    
    for line in motherboardFp:
        if 'Manufacturer' in line:
            mb.manufacturer = line.split("Manufacturer:",1)[1].strip()
        if 'Serial Number' in line:
            mb.serialNumber = line.split("Serial Number:",1)[1].strip()

    print("Motherboard Information")
    print(mb.__dict__)

    motherboardFp.close()



def main():
    #call functions to get system information
    getDramInfo()
    getMBInfo()



main()
