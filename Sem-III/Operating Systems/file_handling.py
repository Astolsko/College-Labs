def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            file.write(data)
        print("File written successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except IOError:
        print(f"Error: An IO error occurred while writing to '{file_name}'.")


def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print("File read successfully.")
        return content
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except IOError:
        print(f"Error: An IO error occurred while reading from '{file_name}'.")
    return None

file_name = 'example.txt'
data = "Hello, World!"

write_to_file(file_name, data)

file_content = read_from_file(file_name)
if file_content is not None:
    print("File content:")
    print(file_content)
