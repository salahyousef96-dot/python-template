import os 

def main() :
	path_file = input ("Read a directory path: ")
	
	try: 
		result = thats_the_way(path_file)
		print(result)
	except (FileNotFoundError, NotADirectoryError) as error:
		print(f"Error: {error}")


def thats_the_way(path_file :str) -> list[str] :
	""" Find files whose names start with 'deep' in a given directory """

	final_lis = []
	files = os.listdir(path_file)
	
	for file in files:	
		if (file.startswith("deep") and os.path.isfile(os.path.join(path_file, file))):
				final_lis.append(file)


	return final_lis

if __name__ == "__main__" :

	main()
	
