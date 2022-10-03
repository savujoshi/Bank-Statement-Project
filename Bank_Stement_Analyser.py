from webbrowser import get
import PyPDF2


def main_function():

    filePathScotia = 'Scotia_September_statement.pdf'
    parse_Scotia_Pdf(filePathScotia)


def parse_Scotia_Pdf(filePath):
    pdfFileObj = open(filePath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNo in range(0, pdfReader.numPages):
        lineCounter = 0
        if pageNo != 1:
            pageObj = pdfReader.getPage(pageNo)
            statementPageLines = pageObj.extract_text().split('\n')
            for item in statementPageLines:

                if "Statement Period" in item and pageNo == 0 and statementPageLines[lineCounter-8] == "SCENE":
                    # We can get statement period here
                    print(item)
                    print(statementPageLines[lineCounter+1])
                    print(statementPageLines[lineCounter+3])
                    print("\n")
                if "Continued on page" in item:
                    # We can directly jump to page number
                    print(item[-1])
                lineCounter += 1

            print("\n \n")
    pdfFileObj.close()


def parse_Neo_Pdf(filePath):
    pdfFileObj = open(filePath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNo in range(0, pdfReader.numPages):
        if pageNo != 1:
            pageObj = pdfReader.getPage(pageNo)

    pdfFileObj.close()


if __name__ == '__main__':

    main_function()
