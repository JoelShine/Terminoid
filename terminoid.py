#The print in the below code is always "print_formatted_text as print". Not normal print.

from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as print
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style
import getpass
import sys
import os
import time
import datetime

os.system('cls')
os.system('title TERMINOID V1.0')

# Style of input taken
style = Style.from_dict({
    # red colour:
    '':          '#ff0066',
})


user = getpass.getuser()

print(HTML('''<blue>

████████ ███████ ██████  ███    ███ ██ ███    ██  ██████  ██ ██████      ██    ██  ██     ██████  
   ██    ██      ██   ██ ████  ████ ██ ████   ██ ██    ██ ██ ██   ██     ██    ██ ███    ██  ████ 
   ██    █████   ██████  ██ ████ ██ ██ ██ ██  ██ ██    ██ ██ ██   ██     ██    ██  ██    ██ ██ ██ 
   ██    ██      ██   ██ ██  ██  ██ ██ ██  ██ ██ ██    ██ ██ ██   ██      ██  ██   ██    ████  ██ 
   ██    ███████ ██   ██ ██      ██ ██ ██   ████  ██████  ██ ██████        ████    ██ ██  ██████  
                                                                                                                                                                   
</blue>'''))

while True:

	try:
		choice = prompt(HTML(f'<white>{os.getcwd()} - Terminoid> </white>'), style=style)
		print("")

		if choice == "exit":
			print(HTML('Thanks for using <blue>T</blue><red>E</red><green>R</green><yellow>M</yellow><orange>I</orange><red>N</red><blue>O</blue><yellow>I</yellow><green>D</green>'))
			time.sleep(2)
			os.system('cls')
			sys.exit()

		elif 'echo ' in choice:
			word_to_replace = "echo "
			text = choice.replace(word_to_replace, "")
			print(text)

		elif choice == "dir":
			for items in os.listdir(os.getcwd()):
				print(items)

		elif choice == "cls":
			os.system('cls')

		elif 'cd ' in choice:
			try:
				word_to_replace = "cd "
				text = choice.replace(word_to_replace, "")
				os.chdir(text)
			except:
				print(f"FileNotFoundError: [WinError 2] The system cannot find the file specified: \"{text}\"")

		elif 'start ' in choice:
			try:
				word_to_replace = "start "
				text = choice.replace(word_to_replace, "")
				os.system(text)
			except:
				print(f"FileNotFoundError: [WinError 2] The system cannot find the file specified: \"{text}\"")

		elif 'title ' in choice:
			try:
				os.system(choice)
			except:
				print(f"'{choice}' is not recognized as an internal or external command,\noperable program or batch file.")

		elif 'prompt ' in choice:
			try:
				os.system(choice)
			except:
				print(f"\'{choice}\' is not recognized as an internal or external command,\noperable program or batch file.")

		elif choice == "date" or choice == "time" or choice == "year" or choice == "month" or choice == "day" or choice == "clock":
			print("")
			print(datetime.datetime.now().strftime("%d %a, %B %Y - %I:%M:%S %p"), end="\r")
			print("")

		elif choice == "battery" or choice == "battery remaining":
			import psutil

			battery = psutil.sensors_battery()
			percent = battery.percent
			percentinletters = str(percent)
			print("There is "+percentinletters+" % remaining.")
			print("")

		else:
			try:
				os.system(choice)
			except:
				print(HTML(f"\'{choice}\' is not recognized as an internal or external command,\noperable program or batch file."))
	
	except KeyboardInterrupt:
		print(HTML('Thanks for using <blue>T</blue><red>E</red><green>R</green><yellow>M</yellow><orange>I</orange><red>N</red><blue>O</blue><yellow>I</yellow><green>D</green>'))
		time.sleep(2)
		os.system('cls')
		sys.exit()
