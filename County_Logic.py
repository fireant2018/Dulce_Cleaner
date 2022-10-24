def county_specific_logic(folder_name):
    if folder_name == 'TXDallas\\':

        if startPosition == 100 and moreFields is True:  # Create years overdue
            fV = True
            fieldValue = line[100:108].strip()
            dueDate = fieldValue[4:6] + "/" + fieldValue[6:8] + "/" + fieldValue[0:4]

            yearsOverdue = (reportDate - datetime.datetime(int(fieldValue[0:4]), int(fieldValue[4:6]),
                                                           int(fieldValue[6:8]))).days / 365.00
            fieldValue = dueDate

        elif startPosition == 92 and moreFields is True:
            fV = True
            datePaid = line[92:100].strip()
            if len(datePaid) > 0:
                fieldValue = datePaid[4:6] + "/" + datePaid[6:8] + "/" + datePaid[0:4]
            else:
                fieldValue = ""

        elif startPosition == 427 and moreFields is True:
            fV = True
            zipcode = line[427:439].strip()
            fieldValue = zipcode[0:5]

        else:
            fV = False

    elif folder_name == "TXCollin":
        print("Collin County")


