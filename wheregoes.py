import sys
import requests as r
from bs4 import BeautifulSoup
from colorama import Fore, Back ,Style

class usage:

	def help(self):
	        print('WHEREGOES v1.0')
	        about = '''Have you ever wondered: Where does this link go? 
	The Wheregoes it allows you to see the complete path a redirected URL goes through. 
	It will show you the full redirection path of URLs, shortened links, or tiny URLs.'''
	        print(about)
	        print('\nRequirements: Python 3, requests and colorama libraries')
	        print('To install the requirements run these commands')
	        print('\tUpdate: apt-get update')
	        print('\tPython 3: apt-get install python3')
	        print('\tRequests: pip install requests')
	        print('\tcolorama: pip install colorama')
	        print('\tcolorama: pip install BeautifulSoup ')
	        print('Commands')
	        print('--help or -h  -> To display helpline how to use this tool & about tool. ')
	        print('\nCoded by: VARMAN FROM ETHICALHACK&TECH')
	        print('Subscribe YouTube : https://www.youtube.com/channel/UCKryPE2Lb5eu8-79-4hCYZg')
	def banner(self):
		print("\\\ ********||| BE SAFE WITH UNKNOWN LINKS |||********//")
		col = Fore.BLUE
		print(col + "          _                                         ")
		print(col + "__      _| |__   ___ _ __ ___  __ _  ___   ___  ___ ") 
		print(col + "\ \ /\ / / '_ \ / _ \ '__/ _ \/ _` |/ _ \ / _ \/ __|")
		print(col + " \ V  V /| | | |  __/ | |  __/ (_| | (_) |  __/\__ \ ")
		print(col + "  \_/\_/ |_| |_|\___|_|  \___|\__, |\___/ \___||___/")
		print(col + "                              |___/                 ") 		

		print(col + "\\\****||| TRACKING THE END FACE OF URLs |||****// \n")
		print('WHEREGOES v1.0')
		about = '''Have you ever wondered: Where does this link go? 
		The Wheregoes it allows you to see the complete path a redirected URL goes through. 
		It will show you the full redirection path of URLs, shortened links, or tiny URLs.'''
		print(about)
		print('\n')



class tracker:
	def trackit(self):

		Source_link = input ("Target url: ")
		url = "https://wheregoes.com/trace/"
		data = {'url': Source_link , 'ua' : 'Wheregoes.com Redirect Checker/1.0'}

		post_data = r.post(url,data = data).text
		l = post_data	

		soup = BeautifulSoup( l , 'lxml')	

		Redirected_URL = soup.find_all('div' , class_='cell url')
		page_URL = soup.find_all('div' , class_="share-trace icon-files")
		total_redirects = soup.find_all('li' , class_='total-redirects')
		try:
			error = soup.find('div' , class_='errtext')
			error = error.text
		except:
			print("")	

		for tag in total_redirects:
			s = tag.text.split(" ")
			s = s[1]
			print("Redirect:",s,"\n")
			

		for tag in Redirected_URL[2:]:
			i = tag.text
			if 'Complete' in i:
				i = i.split()
				i = i[1]
				print(Fore.GREEN + i[:-5],"\n\nRedirects Completed\n")	

			elif 'Error' in tag.text:
				i = i.split()
				i = i[0]
				i = i[:-6]
				print(Fore.RED +f' {error} ==> {i}\n ')	

			else:
				i = i.split()
				length= len(i)
				z = i[length-1]
				i = i[length-2]
				status_code = i[-3:]
				i = i[:-3]
				print(Fore.WHITE + f'{i} ==> Status code {status_code} {z}\n')
		
			

		for tag in page_URL:
			print(Fore.BLUE + tag.text.replace("Click to Copy URL of This Trace" , "URL for This Trace ==> "))


if __name__=='__main__':

    intro = usage()

    if len(sys.argv) == 2:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            intro.help()
    else:
        intro.banner()
        track=tracker()
        track.trackit()

