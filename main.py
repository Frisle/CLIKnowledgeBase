import file_worker
import os

json_data_list_file = os.path.join(os.getcwd(), r"data.json")

# checking and creating json database
file_worker.check_create_data_base()


def conn_func():
    file_metadata = file_worker.read_file_list("artifacts", json_data_list_file)  # -> list of artifacts
    if not file_metadata:
        print("List is empty")
        user_input()
    try:
        file_number = input("Index of file: ")
        file_name = file_metadata[int(file_number)-1]
        file_worker.connected_db(file_name)
    except ValueError:
        print("Input valid symbols")


# invoke delete methods.
# can delete multiple items from dict. (for artifacts)
def delete_artifacts():
    file_metadata = file_worker.read_file_list("artifacts", json_data_list_file)
    position_indexes = input("Input indexes (\"ind... \"): ")
    file_worker.remove_notes(position_indexes, "Artifact", json_data_list_file)


# open appropriate app for redacting an artifact (now its notepad for .txt only)
def conn_edit_func():
    file_metadata = file_worker.read_file_list("artifacts", json_data_list_file)
    if not file_metadata:
        print("List is empty")

    try:
        file_number = input("Index of file: ")

        file_name = file_metadata[int(file_number) - 1]
        file_worker.write_db(file_name)
    except Exception as error:
        print(error)
        conn_edit_func()


# take file path as an input and copy it with importing_new_file
def import_func():
    path = input("Enter path: ").strip('"')

    if path:
        file_worker.importing_new_file(path)
    else:
        print("Path is probably empty")
        import_func()
    print("File successfully imported")


def help_func():
    print("Input \"-conn\" to view list of connected files\n"
          "Then you will be prompted to input index of file you need\n"
          "Text files will be printed directly in console\n"
          "Others will be opened by default application\n\n"
          "Input \"-conn edit\" to open text file for editing\n"
          "Similar to \"-conn\" except it can open Notepad.exe for text file to edit them\n\n"
          "Input \"-import\" to copy files to app directory\n"
          "Then input full path to new file.\n\n"
          "Input \"-del art\" to invoke delete sequence\n"
          )


def user_input():
    user_prompt = input("What to do: ")
    if user_prompt == "-conn":
        conn_func()
    elif user_prompt == "-import":
        import_func()
    elif user_prompt == "-del art":
        delete_artifacts()
    elif user_prompt == "-conn edit":
        conn_edit_func()
    elif user_prompt == "-help" or user_prompt == "--h":
        help_func()
    elif "-cls" in user_prompt:
        os.system("cls")
    user_input()


if __name__ == "__main__":
    user_input()


