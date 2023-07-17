

def main():
    code = copyBook()
    changeNames(code)    
    


def copyBook():
    codes = []
    inputfile = open("industryOptions.php","r")

    codes = inputfile.readlines()

    inputfile.close()
    return codes

def changeNames(mylist):
    file = mylist

    outputfile = open("industryOptions.php", 'w')


    for lines in file:
        lines = lines.replace("Accounting , Finance" or "jobsConnect" or "jobsconnect", "ToolBox")
        outputfile.write(lines)

    outputfile.close()       
 


main()
    