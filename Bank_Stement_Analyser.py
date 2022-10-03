from webbrowser import get
import PyPDF2


def main_function():

    filePathScotia = 'Scotia_September_statement.pdf'
    parse_Scotia_Pdf(filePathScotia)


def parse_Scotia_Pdf(filePath):
    transactionDict = {}
    pdfFileObj = open(filePath, 'rb')
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
                        # print("\n")
                    if "Continued on page" in item:
                        # We can directly jump to page number
                        # print(item[-1])
                        pass
                    if "Transactions since your last statement" in item:
                        statementNum = statementPageLines[lineCounter+12]
                        # Found
                        # print("Transaction Number:", statementNum)
                        statementLineCounter = 0
                        for i in range(lineCounter+12, len(statementPageLines)):
                            if statementPageLines[i].isnumeric():
                                if int(statementPageLines[lineCounter+12])+statementLineCounter == int(statementPageLines[i]):
                                    # print("\n")
                                    # print(statementPageLines[i])
                                    transactionElements = []
                                    for j in range(0, 8):
                                        if statementPageLines[i+j].isnumeric():
                                            if int(statementPageLines[lineCounter+12])+statementLineCounter + 1 == int(statementPageLines[i+j]):
                                                # print(int(statementPageLines[lineCounter+12])+statementLineCounter +1)
                                                break
                                        if j != 0:
                                            transactionElements.append(
                                                statementPageLines[i+j])
                                        # print(statementPageLines[i+j])
                                    # print(int(statementPageLines[i]))
                                    transactionDict.update(
                                        {int(statementPageLines[i]): transactionElements})
                                    # print(transactionDict)
                                    statementLineCounter += 1

                        # print(int(statementNum)+1)

                    lineCounter += 1
                else:
                    # print(item)
                    if "Transactions - continued" in item:
                        # print(statementNum)
                        statementLineCounter = 0
                        for i in range(lineCounter+8, len(statementPageLines)):
                            if statementPageLines[i].isnumeric():
                                if int(statementPageLines[lineCounter+8])+statementLineCounter == int(statementPageLines[i]):
                                    # print("\n")
                                    # print(statementPageLines[i])
                                    transactionElements = []
                                    for j in range(0, 8):
                                        if statementPageLines[i+j].isnumeric():
                                            if int(statementPageLines[lineCounter+8])+statementLineCounter + 1 == int(statementPageLines[i+j]):
                                                # print(int(statementPageLines[lineCounter+12])+statementLineCounter +1)
                                                break
                                        if j != 0:
                                            transactionElements.append(
                                                statementPageLines[i+j])
                                        # print(statementPageLines[i+j])
                                    # print(int(statementPageLines[i]))
                                    transactionDict.update(
                                        {int(statementPageLines[i]): transactionElements})
                                    # print(transactionDict)
                                    statementLineCounter += 1
                    lineCounter += 1

    print("\n")
    pdfFileObj.close()
    print(transactionDict)


def parse_Neo_Pdf(filePath):
    pdfFileObj = open(filePath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNo in range(0, pdfReader.numPages):
        if pageNo != 1:
            pageObj = pdfReader.getPage(pageNo)

    pdfFileObj.close()


if __name__ == '__main__':

    main_function()
