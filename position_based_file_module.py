import os
import datetime
import fields_filetype_module


def process_position_based_file(county_name, file_name, file_fields):
    folder_base_path = "C:\\Users\\amy.stevens\\Documents\\Dulce\\Delinquent_Taxes\\"
    rej_file_name = "REJECTS__" + file_name
    my_del = "\t"
    dictionary_length = len(file_fields)
    field_counter = 0
    my_header = ""
    counter = 0
    my_data = ""
    jrs_line_number = 0
    report_date = datetime.datetime.now()

    with open(os.path.join(folder_base_path, county_name, "Input\\", file_name), 'r') as input_file:
        with open(os.path.join(folder_base_path, county_name, "Output\\", file_name), 'w') as output_file:
            with open(os.path.join(folder_base_path, county_name, "Output\\", rej_file_name), 'w') as reject_file:

                # Build and print header
                for field_name_size_pair in file_fields.items():
                    field_counter += 1

                    if field_counter < dictionary_length:
                        my_header += field_name_size_pair[0] + my_del
                    else:
                        my_header += field_name_size_pair[0]
                        #                       rejectFile.write(myHeader + myDel + "Reject_Reason\n")

                        if file_name in fields_filetype_module.files_with_years_overdue:
                            output_file.write(my_header + my_del + "DataDate" + my_del + "Years_Overdue\n")
                        else:
                            output_file.write(my_header + my_del + "DataDate" + "\n")

                # Print data

                jrs_line_number = 1

                for line in input_file:
                    line_position = 0
                    print_line = True
                    more_fields = True
                    reject_line = False
                    field_counter = 0
                    my_data = ""
                    f_v = False
                    years_overdue = -1
                    # print(len(line))
                    # if len(line) < 60:
                    #     reject_line = True
                    #     print(line)
                    # if reject_line == False:
                    for field_name_size_pair in file_fields.items():
                        k, v = field_name_size_pair[1].split('_')
                        start_position = int(k) - 1
                        end_position = int(v)

                        # County_Logic.county_specific_logic(fileName)
                        if county_name == 'TXDallas\\':

                            if start_position == 100 and more_fields is True:  # Create years overdue
                                f_v = True
                                field_value = line[100:108].strip()
                                due_date = field_value[4:6] + "/" + field_value[6:8] + "/" + field_value[0:4]

                                years_overdue = round((report_date - datetime.datetime(int(field_value[0:4]),
                                                                                int(field_value[4:6]),
                                                                                int(field_value[6:8]))).days / 365.00, 1)

                                field_value = due_date

                            elif start_position == 92 and more_fields is True:
                                f_v = True
                                date_paid = line[92:100].strip()
                                if len(date_paid) > 0:
                                    field_value = date_paid[4:6] + "/" + date_paid[6:8] + "/" + date_paid[0:4]
                                else:
                                    field_value = ""

                            elif start_position == 427 and more_fields is True:
                                f_v = True
                                zipcode = line[427:439].strip()
                                field_value = zipcode[0:5]

                            else:
                                f_v = False

                        elif county_name == "TXCollin":
                            print("Collin County")

                        if field_counter < dictionary_length - 1:
                            if f_v is True:
                                my_data += field_value + my_del
                            else:
                                my_data += line[start_position:end_position].strip() + my_del
                        else:
                            if f_v is True:
                                my_data += field_value
                            else:
                                my_data += line[start_position:end_position].strip()
                                more_fields = False
                        field_counter += 1

                        if more_fields is False:

                            if print_line:
                                data_date = str(report_date.month) + "/" + str(report_date.day) + "/" + str(
                                    report_date.year)

                                if file_name in fields_filetype_module.files_with_years_overdue:
                                    output_file.write(my_data + my_del + data_date + my_del + str(years_overdue) + '\n')
                                else:
                                    output_file.write(my_data + my_del + data_date + '\n')

                            # else:
                            #     rejectFile.write(myData + "rejectReason" + '\n')

                            more_fields = True
                    # else:
                    #     rejectFile.write(line + '\n')

                    if jrs_line_number % 1000 == 0:
                        print(str(int(jrs_line_number / 1000)))

                    jrs_line_number += 1
