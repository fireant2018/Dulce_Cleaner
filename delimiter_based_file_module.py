import os
import datetime


def process_delimiter_based_file(county_name, file_name, file_fields):
    folder_base_path = "C:\\Users\\amy.stevens\\Documents\\Dulce\\Delinquent_Taxes\\"
    rej_file_name = "REJECTS__" + file_name
    my_del = "\t"
    dictionary_length = len(file_fields)
    field_counter = 0
    my_header = ""
    counter = 0
    my_data = ""
    jrs_line_number = 0
    with open(os.path.join(folder_base_path, county_name, "Input\\", file_name), 'r') as input_file:
        with open(os.path.join(folder_base_path, county_name, "Output\\", file_name), 'w') as output_file:
            for line in input_file:
                field_counter = 0
                if counter == 0:
                    # ====  header  =====
                    for field_name_size_pair in file_fields.items():
                        field_counter += 1
                        if field_counter < dictionary_length:
                            my_header += field_name_size_pair[0] + my_del
                        else:
                            my_header += field_name_size_pair[0] + my_del + "data_date" + "\n"
                    output_file.write(my_header)
                    counter += 1
                else:
                    # ====  data  =====
                    field_counter = 0
                    my_data = ""
                    split_line = line.split(',')
                    for field_name_size_pair in file_fields.items():
                        field_counter += 1
                        if field_counter < dictionary_length:
                            my_data += split_line[field_name_size_pair[1]] + my_del
                        else:
                            my_data += split_line[field_name_size_pair[1]] # + "\n"
                    report_date = datetime.datetime.now()
                    data_date = str(report_date.month) + "/" + str(report_date.day) + "/" + str(report_date.year)
                    output_file.write(my_data + my_del + data_date + '\n')
                    my_data = ""
                    counter += 1

                if jrs_line_number % 1000 == 0:
                    print(str(int(jrs_line_number / 1000)))
                jrs_line_number += 1
