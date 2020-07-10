######################################
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#Author : Aalok Shah
#Version : 0.1
########################################

import os
import sys
import fileinput

#As the XLS is being used for configuration input, 'xlrd' and 'xlwt' packages needs to be downloaded through PIP
from xlrd import open_workbook
from xlwt import Utils

token = {}

#Procedure to Prepare Tokens for Packet Format Entries
def packet_entry_tokens(pkt_entry):
	token['<FILE_NAME>'] = 'ex_' + pkt_entry.lower()
	token['<FILE_DEF>'] = token['<FILE_NAME>'].upper() + '_H_'
	token['<FIELD_STRUCT>'] = pkt_entry.lower()
	token['<FIELD_STRUCT_ARG>'] = pkt_entry.lower() + ' *arg_' + pkt_entry.lower()

	cur_sheet = wb.sheet_by_name(pkt_entry);

	#<FIELD_STRUCT_DEF>
	temp = 'typedef struct __atribute__((packed)) ' + token['<FIELD_STRUCT>'] + '\n{\n'
	for rows in range(cur_sheet.nrows):
		temp += '\t' + str(cur_sheet.cell_value(rows, 0)) + ' ' + str(cur_sheet.cell_value(rows, 1)) + ';\n'
	temp += '};\n'	
	token['<FIELD_STRUCT_DEF>'] = temp

	#<FIELDS_PACK>
	token['<FIELDS_PACK>'] = 'memcpy((char*)buf, (char*)arg_' + pkt_entry.lower() + ', sizeof('+ token['<FIELD_STRUCT>'] + '));'

	#<FIELDS_UNPACK>
	token['<FIELDS_UNPACK>'] = 'memcpy((char*)arg_' + pkt_entry.lower() + ', (char*)buf, sizeof('+ token['<FIELD_STRUCT>'] + '));'

	#<FIELDS_PRINT>
	temp = ''
	for rows in range(cur_sheet.nrows):
		if str(cur_sheet.cell_value(rows, 0)) == 'int':
			temp += '\tprintf("Value of ' + str(cur_sheet.cell_value(rows, 1)).upper() + ' : %d \\n", arg_' + token['<FIELD_STRUCT>'] + '->' + str(cur_sheet.cell_value(rows, 1)) + ');\n'
		elif str(cur_sheet.cell_value(rows, 0)) == 'char':
			temp += '\tprintf("Value of ' + str(cur_sheet.cell_value(rows, 1)).upper() + ' : %c \\n", arg_' + token['<FIELD_STRUCT>'] + '->' + str(cur_sheet.cell_value(rows, 1)) + ');\n'
		elif str(cur_sheet.cell_value(rows, 0)) == 'long':
			temp += '\tprintf("Value of ' + str(cur_sheet.cell_value(rows, 1)).upper() + ' : %ld \\n", arg_' + token['<FIELD_STRUCT>'] + '->' + str(cur_sheet.cell_value(rows, 1)) + ');\n'
		elif str(cur_sheet.cell_value(rows, 0)) == 'float':
			temp += '\tprintf("Value of ' + str(cur_sheet.cell_value(rows, 1)).upper() + ' : %f \\n", arg_' + token['<FIELD_STRUCT>'] + '->' + str(cur_sheet.cell_value(rows, 1)) + ');\n'
	token['<FIELDS_PRINT>'] = temp;


#Procedure to Access Templates and Generate Output Files Using the Token Prepared
def generate_output(pkt_entry):
	src_tplt_file = open("source.template", "r")
        src_buf = src_tplt_file.read()
	hdr_tplt_file = open("header.template", "r")
	hdr_buf = hdr_tplt_file.read()

        #Source File Generation
	src_buf = src_buf.replace('<FIELDS_PRINT>', token['<FIELDS_PRINT>']);
	src_buf = src_buf.replace('<FIELDS_UNPACK>', token['<FIELDS_UNPACK>']);
	src_buf = src_buf.replace('<FIELDS_PACK>', token['<FIELDS_PACK>']);
	src_buf = src_buf.replace('<FIELD_STRUCT_ARG>', token['<FIELD_STRUCT_ARG>']);
	src_buf = src_buf.replace('<FIELD_STRUCT>', token['<FIELD_STRUCT>']);
	src_buf = src_buf.replace('<VERSION>', token['<VERSION>']);
	src_buf = src_buf.replace('<FILE_NAME>', token['<FILE_NAME>'] + '.h');
        
	out_file= 'output/' + token['<FILE_NAME>'] + '.c'
	src_out_file = open(out_file, "w")
	src_out_file.write(src_buf)
	src_out_file.close()
	src_tplt_file.close()

	#Header File Generation
	hdr_buf = hdr_buf.replace('<VERSION>', token['<VERSION>']);
	hdr_buf = hdr_buf.replace('<FILE_DEF>', token['<FILE_DEF>']);
	hdr_buf = hdr_buf.replace('<FIELD_STRUCT_DEF>', token['<FIELD_STRUCT_DEF>']);

	out_file= 'output/' + token['<FILE_NAME>'] + '.h'
	hdr_out_file = open(out_file, "w")
	hdr_out_file.write(hdr_buf);
	hdr_out_file.close()
	hdr_tplt_file.close()

#####################################################################

print "Code Generation Started!"

wb = open_workbook("input.xlsx");
config_sheet = wb.sheet_by_name("CONFIG");
os.mkdir("output")
	
#Parse Lines and Prepare Tokens
for rows in range(config_sheet.nrows):
	value = str(config_sheet.cell_value(rows, 0))
	if value == "VERSION":
		token['<VERSION>'] = str(config_sheet.cell_value(rows, 1))
	elif value == "ENTITIES":
		for cols in range(1, config_sheet.ncols):
			if config_sheet.cell_value(rows, cols):
				packet_entry_tokens(str(config_sheet.cell_value(rows, cols)))
				generate_output(str(config_sheet.cell_value(rows, cols)))


print "Code Generation Completed Successfully!"
