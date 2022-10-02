from webbrowser import get
import PyPDF2
  

def main_function():
    # creating a pdf file object
    pdfFileObj = open('statement-32.pdf', 'rb')
    
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    # printing number of pages in pdf file
    print("Number of pages:"+str(pdfReader.numPages))
    
    # creating a page object
    for pageNo in range(0, pdfReader.numPages):
        print(pageNo)
        pageObj = pdfReader.getPage(pageNo)
        print("\n")
        print(len(pageObj.extractText().splitlines()))

    print("Object Type:" + str(type(pageObj)))
    
    # extracting text from page
    # print(pageObj.extractText())
    
    # closing the pdf file object
    pdfFileObj.close()



if __name__=='__main__':

    main_function()