try:
    with open("myfile.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
	print("Error: You do not have permission to read the file.")
except IsADirectoryError:
	print("Error: Expected a file but found a directory.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
