#Script for dividing pdf in two
from pyPdf import PdfFileWriter, PdfFileReader
import copy, sys


def split(file_name):

    input1 = PdfFileReader(file(file_name, "rb"))
    output = PdfFileWriter()
    
    numPages = input1.getNumPages()
    print "document has %s pages." % numPages
    
    for i in range(numPages):
        page1 = input1.getPage(i)
        page2 = copy.copy(page1)
        w = page1.mediaBox.getUpperRight_y()
        h = page1.mediaBox.getUpperRight_x()
        #The width and height are weird
        page1.cropBox.lowerLeft = (0, 0)
        page1.cropBox.upperRight = (h, w/2)
        
        page2.cropBox.lowerLeft = ( 0,w/2)
        page2.cropBox.upperRight = (h, w)
        
        output.addPage(page1)
        output.addPage(page2)
        
        
        
    
    
    outputStream = file("out.pdf", "wb")
    output.write(outputStream)
    outputStream.close()    
    
    print 'Finished'   
    

if __name__ == "__main__":
    
    split(sys.argv[1])            
            
            