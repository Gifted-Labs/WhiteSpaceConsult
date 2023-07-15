

def main():
    code = copyBook()
    changeNames(code)    
    


def copyBook():
    codes = []
    inputfile = open("index.php","r")

    codes = inputfile.readlines()

    inputfile.close()
    return codes

def changeNames(mylist):
    file = mylist

    outputfile = open("index.php", 'w')


    for lines in file:
        lines = lines.replace("JobsConnect" or "jobsConnect" or "jobsconnect", "ToolBox")
        outputfile.write(lines)

    outputfile.close()       
 


main()
    