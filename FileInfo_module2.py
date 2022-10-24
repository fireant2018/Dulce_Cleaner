def getFileDescription(inputFile):
    if inputFile == 'TXDallas_flat404.txt':
        extractedFields = {'Account': '1_34', 'Date Paid': '93_100', 'Due Date': '101_108', 'Suit': '122_122',
                           'Bankrupt No': '164_203', 'Category Code': '222_225', 'Owner': '226_265',
                           'Address2': '266_305', 'Address3': '306_345', 'Address4': '346_385', 'City': '386_425',
                           'State': '426_427', 'Zip': '428_439', 'RollCode': '440_440', 'Parcel No': '441_448',
                           'Parcel Name': '449_488', 'Tot Amt Due': '490_500'}

    elif inputFile == 'TXCollin_Master.DAT':
        # All_Fields: {'Account_Number':'1_30','SPTB_Code':'31_33','Roll_Code':'34_36','Legal_Description':'37_160','Acres':'161_173','Appraisal_District_Number':'174_203','Street_Name':'204_228','Street_Number':'229_238','Square_Feet':'239_244','Lot_Size':'245_250','Year_Built':'251_254','Loan_Number':'255_264','Map Number':'265_294','Mapsco_Number':'295_314','Appraisal_Map_Number':'315_334','Name1':'335_384','Name2':'385_434','Address1':'435_484','Address2':'485_534','City':'535_584','State':'585_604','Postal_Code':'605_622','Start_Deferral_Date':'623_632','End_Deferral_Date':'633_642','Volume':'643_648','Page':'649_654','Deed_Date':'655_664','Exemption_Codes':'665_679','Delinquency_Date':'680_689','Tax_Unit_Codes':'690_719','Non-Billed_Tax_Units':'720_769','Land_Value':'770_779','Improvement_Value':'780_790','Value':'791_801','Exemptions':'802_811','Levy':'812_823','Amount_Due':'824_835','Total_Amount_Due':'836_847'}
        extractedFields = {'Account_Number': '1_30', 'SPTB_Code': '31_33', 'Roll_Code': '34_36',
                           'Legal_Description': '37_160', 'Street_Name': '204_228', 'Street_Number': '229_238',
                           'Name1': '335_384', 'Name2': '385_434', 'Address1': '435_484', 'Address2': '485_534',
                           'City': '535_584', 'State': '585_604', 'Postal_Code': '605_622', 'Value': '791_801',
                           'Deed_Date': '655_664', 'Total_Amount_Due': '836_847'}
    elif inputFile == 'TXCollin_Receivables.DAT':
        # All_Fields: {'Account_Number':'1_30','Year':'31_34','Tax_Unit_Number':'35_37','Receivable_Type_Code':'38_40','Sequence_Number':'41_42','Value':'43_53','Exemptions':'54_64','Levy':'65_75','Amount_Due':'76_87','Delinquency_Date':'88_97','3307_Date':'98_107','Judgment_Date':'108_117','Suit_Number':'118_135','Suit_Date':'136_145','Bankruptcy_Number':'146_163','Bankruptcy_Date':'164_173','Status_Codes':'174_188','SequenceTypeCode':'189_190','Installment':'191_191','InstallmentType':'192_194','InstallmentStartDate':'195_204','InstallmentEndDate':'205_214','InstallmentPaidDate':'215_224'}
        extractedFields = {'Account_Number': '1_30', 'Amount_Due': '76_87', 'Delinquency_Date': '88_97'}

    return (extractedFields)

##def getFileDescription(county,inputFile):
##   if county == "TXDallas":
##      extractedFields = {'Account':'1_34','Date Paid':'93_100','Due Date':'101_108','Suit':'122_122','Bankrupt No':'164_203','Category Code':'222_225','Owner':'226_265','Address2':'266_305','Address3':'306_345','Address4':'346_385','City':'386_425','State':'426_427','Zip':'428_439','RollCode':'440_440','Parcel No':'441_448','Parcel Name':'449_488','Tot Amt Due':'490_500'}
##
##   elif county == "TXCollin":
##      if inputFile == 'TXCollin_Master.DAT':
##        # All_Fields: {'Account_Number':'1_30','SPTB_Code':'31_33','Roll_Code':'34_36','Legal_Description':'37_160','Acres':'161_173','Appraisal_District_Number':'174_203','Street_Name':'204_228','Street_Number':'229_238','Square_Feet':'239_244','Lot_Size':'245_250','Year_Built':'251_254','Loan_Number':'255_264','Map Number':'265_294','Mapsco_Number':'295_314','Appraisal_Map_Number':'315_334','Name1':'335_384','Name2':'385_434','Address1':'435_484','Address2':'485_534','City':'535_584','State':'585_604','Postal_Code':'605_622','Start_Deferral_Date':'623_632','End_Deferral_Date':'633_642','Volume':'643_648','Page':'649_654','Deed_Date':'655_664','Exemption_Codes':'665_679','Delinquency_Date':'680_689','Tax_Unit_Codes':'690_719','Non-Billed_Tax_Units':'720_769','Land_Value':'770_779','Improvement_Value':'780_790','Value':'791_801','Exemptions':'802_811','Levy':'812_823','Amount_Due':'824_835','Total_Amount_Due':'836_847'}
##        extractedFields = {'Account_Number':'1_30','SPTB_Code':'31_33','Roll_Code':'34_36','Legal_Description':'37_160','Street_Name':'204_228','Street_Number':'229_238','Name1':'335_384','Name2':'385_434','Address1':'435_484','Address2':'485_534','City':'535_584','State':'585_604','Postal_Code':'605_622','Value':'791_801','Deed_Date':'655_664','Total_Amount_Due':'836_847'}
##      elif inputFile == 'TXCollin_Receivables.DAT':
##        # All_Fields: {'Account_Number':'1_30','Year':'31_34','Tax_Unit_Number':'35_37','Receivable_Type_Code':'38_40','Sequence_Number':'41_42','Value':'43_53','Exemptions':'54_64','Levy':'65_75','Amount_Due':'76_87','Delinquency_Date':'88_97','3307_Date':'98_107','Judgment_Date':'108_117','Suit_Number':'118_135','Suit_Date':'136_145','Bankruptcy_Number':'146_163','Bankruptcy_Date':'164_173','Status_Codes':'174_188','SequenceTypeCode':'189_190','Installment':'191_191','InstallmentType':'192_194','InstallmentStartDate':'195_204','InstallmentEndDate':'205_214','InstallmentPaidDate':'215_224'}
##        extractedFields = {'Account_Number':'1_30','Amount_Due':'76_87','Delinquency_Date':'88_97'}
##
##   return(extractedFields)
