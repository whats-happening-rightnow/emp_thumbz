import sys

import rtconfig as cf

def print_(out_string = "", topic = None, log = False):

	message = out_string
	if topic is not None:
		message = topic.strip().ljust(10) + ": " + out_string.strip()

	if str(out_string).endswith('\n') or str(out_string).endswith('\r'):
		sys.stdout.write(message)
	else:
		sys.stdout.write(message + '\n')

	if log:
		cf.out_message.append(message)

def print_progress(part, of):

	prog_char = "#"
	total_prog_chars = 50

	progress_percent = int(round(((part * 1.0) / of) * 100))
	progress_percent = str(progress_percent).rjust(3, " ")

	progress = int(round(total_prog_chars * ((part * 1.0) / of)))

	prog_bar = "".rjust(progress, prog_char).ljust(total_prog_chars, " ")
	out_string = "|{0}|{1}%{2}".format(prog_bar, progress_percent, "\r" if part < of else "\n")

	print_(out_string)
