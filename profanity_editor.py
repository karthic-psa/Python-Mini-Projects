import urllib

def read_file():
    fo = open('FileLocation\\test_file.txt')
    content = fo.read()
    #print(content)
    fo.close()
    convert_text(content)

def convert_text(speech):
    connect = urllib.urlopen("http://www.wdyl.com/profanity?q="+speech)
    output = connect.read()
    print (output)
    connect.close()
    if "true" in output:
        print ("Profanity Alert!")
    elif "false" in output:
        print ("The document is safe")
    
read_file()
