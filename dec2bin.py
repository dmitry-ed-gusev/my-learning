################################################################################
#
#	Utility from DECIMAL to BINARY.
#
#	Created:  Ishkinin Dmitrii, 13.02.2020
#	Modified: 
#
################################################################################

import sys  # импортируем библиотеку


def convert_dec2bin(decimal_number):
	return bin(decimal_number)


def main_function(cmd_line_arguments):

	if len(cmd_line_arguments) > 1:
		text = (sys.argv[1])  # беру значение переменной (первой)
		print(convert_dec2bin(int(text)))
	else:
		print("Please, provide a decimal number for conversion...")


# -- код скрипта / программы
main_function(sys.argv)
