from webbrowser import get
import PyPDF2


def main_function():
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNo in range(0, pdfReader.numPages):
        lineCounter = 0
        if pageNo != 1:
            pageObj = pdfReader.getPage(pageNo)
            statementPageLines = pageObj.extract_text().split('\n')
            for item in statementPageLines:
                if pageNo == 0:
                    # print(item)
                    if "Statement Period" in item and pageNo == 0 and statementPageLines[lineCounter-8] == "SCENE":
                        # We can get statement period here
                        print(item)
                        print(statementPageLines[lineCounter+1])
                        print(statementPageLines[lineCounter+3])
                        print("\n")
                    if "Continued on page" in item:
                        # We can directly jump to page number
                        # print(item[-1])
                        pass
                    if "Transactions since your last statement" in item:
                        statementNum = statementPageLines[lineCounter+12]
                        # Found 
                        print("Transaction Number:",statementNum)
                        statementLineCounter = 1
                        for i in range(lineCounter+12,len(statementPageLines)):
                            if statementPageLines[i].isnumeric():
                                if int(statementPageLines[lineCounter+12])+statementLineCounter == int(statementPageLines[i]):
                                    print("\n")
                                    for j in range(0,8):
                                        if statementPageLines[i+j].isnumeric():
                                            if int(statementPageLines[lineCounter+12])+statementLineCounter +1 == int(statementPageLines[i+j]):
                                                # print(int(statementPageLines[lineCounter+12])+statementLineCounter +1)
                                                break
                                        print(statementPageLines[i+j])
                                      
                                    statementLineCounter+=1

                        # print(int(statementNum)+1)
                        
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
