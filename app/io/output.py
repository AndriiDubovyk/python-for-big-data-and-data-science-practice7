def output_text_console(text):
    """Outputs text to the console.

    Args:
        text (str): The text to be displayed in the console.
    """
    print(text)


def write_file_builtin(file_path, content):
    """Writes content to a file using Python's built-in file writing capabilities.

    Args:
        file_path (str): The path to the file to be written.
        content (str): The content to be written to the file.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print("File not found.")


def write_file_pandas(file_path, content):
    """Writes content to a file using the pandas library.

    Args:
        file_path (str): The path to the file to be written.
        content (DataFrame): The content to be written to the file.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
    """
    try:
        content.to_csv(file_path, index=False)
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
