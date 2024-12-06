def modify_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        modified_content = content.upper()
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"File successfully written to {output_filename}.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: Could not read or write to the file.")
def main():
    input_filename = input("Enter the filename to read from: ")
    output_filename = input("Enter the filename to write to: ")
    modify_and_write_file(input_filename, output_filename)
main()
