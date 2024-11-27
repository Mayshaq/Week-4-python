def read_and_write_file():
    try:
        # Prompt the user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Attempt to open the file for reading
        with open(input_filename, 'r') as infile:
            # Read the contents of the file
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Prompt the user for the output filename
        output_filename = input("Enter the name of the file to write the modified content to: ")

        # Attempt to write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to {output_filename}.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You may not have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()
