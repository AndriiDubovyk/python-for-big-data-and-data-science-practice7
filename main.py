from app.io.input import input_text_console, read_file_builtin, read_file_pandas
from app.io.output import output_text_console, write_file_builtin, write_file_pandas


def main():
    text_console = input_text_console()
    text_builtin = read_file_builtin("data/read_builtin.txt")
    text_pandas = read_file_pandas("data/read_pandas.csv")

    output_text_console(text_console)
    write_file_builtin("data/write_builtin.txt", text_builtin)
    write_file_pandas("data/write_pandas.csv", text_pandas)


if __name__ == "__main__":
    main()
