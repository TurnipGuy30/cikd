from msvcrt import getch
from os import system

def cls(cls_command: str='cls') -> int: system(cls_command)

ciks = 0
player_exit = False
in_char = quit_char = ''

def printx(out: str=''):
	cls()
	print(f'\nciks: {ciks}\n\n{out}')

while not player_exit:
	printx('press space to *cik*')
	in_char = getch()

	if in_char == b' ':
		ciks += 1

	elif in_char == b'q':
		printx('do you want to quit? (there no save function lol) y/n')
		while quit_char not in [b'y', b'n']:
			quit_char = getch()
		if quit_char == b'y':
			player_exit = True
		quit_char = ''
