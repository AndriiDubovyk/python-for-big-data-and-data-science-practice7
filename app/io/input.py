import pandas


def input_text_console():
    """
    Prompts the user to enter text via the console.

    Returns:
        str: The text entered by the user.
    """
    text = input("Enter text: ")
    return text


def read_file_builtin(file_path):
    """Reads content from a file using Python's built-in file reading capabilities.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content read from the file.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."


def read_file_pandas(file_path):
    """Reads data from a file using the pandas library.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
       DataFrame: The content read from the file.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
    """
    try:
        df = pandas.read_csv(file_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
