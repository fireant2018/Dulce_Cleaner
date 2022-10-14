#!/usr/bin/python

import sys

import fields_filetype_module
import delimiter_based_file_module
import position_based_file_module

# Define variables TEST

folder_name = 'TXDallas\\'
file_name = 'TXDallas_flat404.txt'  # The file name was changed to avoid problems with periods.
# file_name = 'account_apprl_year.csv'
# file_name = 'account_info.csv'

# folder_name = "TXCollin"
# file_name = 'TXCollin_Master.DAT'    # Master does NOT contain the due date
# file_name = 'TXCollin_Receivables.DAT'

file_fields = fields_filetype_module.get_fields(file_name)
file_type = fields_filetype_module.get_filetype(file_name)

files_with_years_overdue = ['TXDallas_flat404.txt', 'TXCollin_Receivables.DAT']

if file_type == 'position_based':
    position_based_file_module.process_position_based_file(folder_name, file_name, file_fields)
elif file_type == 'delimiter_based':
    delimiter_based_file_module.process_delimiter_based_file(folder_name, file_name, file_fields)
else:
    sys.exit('fileType is not defined. Add it to the delimited_file or position_based_file')

print('Done')
