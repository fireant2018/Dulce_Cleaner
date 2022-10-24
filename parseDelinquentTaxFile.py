#!/usr/bin/python

import datetime
import os

import FileInfo_module


# Define variables
inputFolderBasePath = "C:\\Users\\amy.stevens\\Documents\\Dulce\\Delinquent_Taxes\\"
folderName = 'TXDallas\\'
inputFileName = 'TXDallas_flat404.txt'  # The file name was changed to avoid problems with periods.

# folderName = "TXCollin"
# inputFileName = 'TXCollin_Master.DAT'    # Master does NOT contain the due date
# inputFileName = 'TXCollin_Receivables.DAT'

fileDescription = FileInfo_module.getFileDescription(inputFileName)

outputFolderBasePath = "C:\\Users\\amy.stevens\\Documents\\Dulce\\Delinquent_Taxes\\"
outputFileName = inputFileName

outputRejectFileName = "REJECTS__" + inputFileName

myDel = "\t"

filesWithYearsOverdue = ['TXDallas_flat404.txt', 'TXCollin_Receivables.DAT']

print(outputFolderBasePath + inputFileName)


# Open input and output files

with open(os.path.join(inputFolderBasePath, folderName, "Input\\", inputFileName), 'r') as inputFile:
    with open(os.path.join(outputFolderBasePath, folderName, "Output\\", outputFileName), 'w') as outputFile:
        with open(os.path.join(outputFolderBasePath, folderName, "Output\\", outputRejectFileName), 'w') as rejectFile:
            myHeader = ""
            myData = ""
            fieldCounter = 0

            # Build and print header

            dictionaryLength = len(fileDescription)

            for fieldNameSizePair in fileDescription.items():
                fieldCounter += 1

                if fieldCounter < dictionaryLength:
                    myHeader += fieldNameSizePair[0] + myDel
                else:
                    myHeader += fieldNameSizePair[0]
                    rejectFile.write(myHeader + myDel + "Reject_Reason\n")

                    if inputFileName in filesWithYearsOverdue:
                        outputFile.write(myHeader + myDel + "DataDate" + myDel + "Years_Overdue\n")
                    else:
                        outputFile.write(myHeader + myDel + "DataDate" + "\n")

            # Print data

            jrsLineNumber = 1
            reportDate = datetime.datetime.now()

            for line in inputFile:
                linePosition = 0
                printLine = True
                moreFields = True
                rejectLine = False
                fieldCounter = 0
                myData = ""
                fV = False
                yearsOverdue = -1
                # print(len(line))
                # if len(line) < 60:
                #     rejectLine = True
                #     print(line)
                # if rejectLine == False:
                for fieldNameSizePair in fileDescription.items():
                    k, v = fieldNameSizePair[1].split('_')
                    startPosition = int(k) - 1
                    endPosition = int(v)

                    if folderName == 'TXDallas\\':

                        if startPosition == 100 and moreFields == True:  # Create years overdue
                            fV = True
                            fieldValue = line[100:108].strip()
                            dueDate = fieldValue[4:6] + "/" + fieldValue[6:8] + "/" + fieldValue[0:4]

                            yearsOverdue = (reportDate - datetime.datetime(int(fieldValue[0:4]), int(fieldValue[4:6]),
                                                                           int(fieldValue[6:8]))).days / 365.00
                            fieldValue = dueDate

                        elif startPosition == 92 and moreFields == True:
                            fV = True
                            datePaid = line[92:100].strip()
                            if len(datePaid) > 0:
                                fieldValue = datePaid[4:6] + "/" + datePaid[6:8] + "/" + datePaid[0:4]
                            else:
                                fieldValue = ""


                        elif startPosition == 427 and moreFields == True:
                            fV = True
                            zip = line[427:439].strip()
                            fieldValue = zip[0:5]

                        else:
                            fV = False


                    elif folderName == "TXCollin":
                        print ("Collin County")

                    if fieldCounter < dictionaryLength - 1:
                        if fV == True:
                            myData += fieldValue + myDel
                        else:
                            myData += line[startPosition:endPosition].strip() + myDel
                    else:
                        if fV == True:
                            myData += fieldValue
                        else:
                            myData += line[startPosition:endPosition].strip()
                            moreFields = False
                    fieldCounter += 1




                    if moreFields == False:

                        if printLine:
                            dataDate = str(reportDate.month) + "/" + str(reportDate.day) + "/" + str(reportDate.year)

                            if inputFileName in filesWithYearsOverdue:
                                outputFile.write(myData + myDel + dataDate + myDel + str(yearsOverdue) + '\n')
                            else:
                                outputFile.write(myData + myDel + dataDate + '\n')

                        # else:
                        #     rejectFile.write(myData + "rejectReason" + '\n')

                        moreFields = True
                # else:
                #     rejectFile.write(line + '\n')

                if jrsLineNumber % 1000 == 0:
                    print(str(int(jrsLineNumber / 1000)))

                jrsLineNumber += 1

print('Done')
