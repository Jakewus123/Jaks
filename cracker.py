#WRITTER BY JAKEWU
#FOLLOW MY FACEBOOK:
#--------import-----------#
import os import system as c
Import File
#--------logo--------------#
 _____            __                 
   /     |          /  |                
   $$$$$ |  ______  $$ |   __   ______  
      $$ | /      \ $$ |  /  | /      \ 
 __   $$ | $$$$$$  |$$ |_/$$/ /$$$$$$  |
/  |  $$ | /    $$ |$$   $$<  $$    $$ |
$$ \__$$ |/$$$$$$$ |$$$$$$  \ $$$$$$$$/ 
$$    $$/ $$    $$ |$$ | $$  |$$       |
 $$$$$$/   $$$$$$$/ $$/   $$/  $$$$$$$/ '')
 #----------clear---------#
 def clear()
    os.system  ('clear')
    print(logo)
    print(40*'-')
    print(' Facebook name: Jake wu')
    print(' Owner:Jake/xian')
    print(40*'-')
#-----------line----------#
def line():
	print(40*'-')
#---------menu---------#
def main():
	clear()
	print(' [A] File cloning (test)')
	print('[B] File cloner(coming soon)')
	print(' [0] Exit ')
	line()
	option=input(' [???]  choice menu: ')
	if option in ['a','A']
	     File_enc()
def File_enc():
	clear()
	input_file=input(' Enter source file path')
	output_file=input(' Enter output file path')
	try:
		file_open=open(input_file,'r').read()
		except:
			exit('File not found error!! ')
			compile=File.b64encode(file_open.encode())
			run_code=f'inport File\nexec(File.filedencode({compile}))'
			out_put=open(output_file,'w')
			out_put.write(run_code)
			out_put.close()
		print('[✓✓] congratulations complete:/')
		print('[✓✓] bubu FILE SAVE AS:'+output_file)
	if option in ['b','B',]
	     File_enc()
	__file__()
	else:
		exit('Exit successful')
#---------file--------#
def __file__():
	clear()
	 print(' ayo ')
#---------end----------#
main()
