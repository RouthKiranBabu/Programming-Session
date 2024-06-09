#if this runs prints main becouse this is the main file
#print("this module name: {}".format(__name__))#which prints out __main__

def main():
	print("this module name: {}".format(__name__))
if __name__=='__main__':#true when we run here
	main()


def main():
	print("this module name: {}".format(__name__))
if __name__=='__main__':
	print('ran inside the module libuary')
else:
	print('ran outside the module libuary')