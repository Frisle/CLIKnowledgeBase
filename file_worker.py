from columnar import columnar
from shutil import copyfile
import json
import os

json_data_list_file = os.path.join(os.getcwd(), r"data.json")


def check_create_data_base():

    try:
        with open(json_data_list_file, "r") as file_list:
            file_list.readlines()
    except FileNotFoundError:
        create_null_list_json()

    try:
        os.listdir("connected")
    except FileNotFoundError:
        os.mkdir("connected")


def create_null_list_json():
    with open(json_data_list_file, "w", encoding="utf-8") as json_file:
        data = {
            "artifacts": []

        }
        json_object = json.dumps(data, indent=4)
        json_file.write(json_object)


# display notes in a fancy looking tables
def pretty_print(line, doc_type):
    if line:
        table = columnar(line, headers=['Order', 'Extension', 'File name', 'Size', 'Type', 'Description'],
                         no_borders=True,
                         max_column_width=None, wrap_max=5, terminal_width=None)
        return table


#  function to view available artifacts
def read_file_list(position, file_name):
    names_list = []
    with open(file_name, "r") as json_file:
        file_data = json.load(json_file)
        data_pull = file_data[position]

        print(pretty_print(file_data[position], "artifacts"))
        for item in data_pull:
            names_list.append(item[2]+item[1])
        return names_list


# function form record with artifact data and write in data.json
def update_artifact_list(position, file_name, name, extension, size, key, description):

    """
    :param position:
    :param file_name:
    :param name:
    :param extension: file extension from an os.path.splitext(file_name)
    :param size: size in bytes
    :param key:
    :param description:
    :return:
    """

    with open(file_name, "r") as json_file:
        file_data = json.load(json_file)
        data_pull = file_data[position]
        order = len(data_pull)

        data = [f"{order+1}", extension, name, f"{size} kb", key, description]

    file_data[position].append(data)

    with open(file_name, "w") as json_file:
        json.dump(file_data, json_file, ensure_ascii=False, indent=4)


def importing_new_file(path):
    file_name = os.path.basename(path)  # extract only name.ext of file from path string
    name, extension = os.path.splitext(file_name)  # separate file name and extension
    size = os.path.getsize(path) / 1024  # get file size in bytes
    description = input("Input short description: ")
    content_category = input("Input category: ")
    size_in_bt = '{0:.2f}'.format(size)
    update_artifact_list("artifacts", json_data_list_file, name, extension, size_in_bt, content_category, description)
    parent_dir = os.getcwd()
    target_dir = os.path.join(parent_dir, "connected/"+str(file_name))

    copyfile(path, target_dir)


# function used to get list of files from a directory: "connected/"
# and open notepad to edit it.
def write_db(file_name):
    list_of_file = os.listdir("connected/")
    index = list_of_file.index(file_name)
    file_name = list_of_file[index]
    full_path = os.path.abspath("connected/"+str(file_name))
    os.startfile(full_path)


# function used to get list of files from a directory: "connected/"
# and print its content in the cmd.
def connected_db(file_name):
    list_of_file = os.listdir("connected/")
    index = list_of_file.index(file_name)
    connected_file = list_of_file[index]
    full_path = os.path.abspath("connected/" + str(connected_file))
    file = open("connected/" + str(connected_file), "r")
    try:
        content = file.read()
        print(content)
    except UnicodeDecodeError:
        os.startfile(full_path)

    file.close()


def delete_note(list_data, index_list):
    for index in index_list:
        list_data.pop(index)
    return list_data


# deletes notes from dictionary
def remove_notes(user_input, elem, file_name):
    position = ""
    lines_indexes = ""
    if elem == "Artifact":
        position = "artifacts"
        lines_indexes = user_input.split()
    with open(file_name, "r") as json_file:
        file_data = json.load(json_file)
        index_list = []
        try:
            len(file_data[position])
        except KeyError:
            print("This date is not exist")
            return
        for order in file_data[position]:
            try:
                note_index = order[0].strip("#")
            except Exception:
                note_index = order[0]
            for number in lines_indexes:
                if int(number) == int(note_index):

                    if elem == "Artifact":
                        file = f"connected/{order[2]}{order[1]}"
                        if os.path.exists(file):
                            os.remove(file)
                        else:
                            print("The file does not exist")
                    index_list.append(file_data[position].index(order))
                    index_list.sort(reverse=True)
                    print(elem + " " + str(note_index) + " deleted")
        val = delete_note(file_data[position], index_list)

        file_data[position] = val

    with open(file_name, "w") as json_file:
        json.dump(file_data, json_file, ensure_ascii=False, indent=4)


def file_updater():
    file_list = os.listdir("connected")
    for index, item in enumerate(file_list):
        if item != ".placeholder":
            name, extension = os.path.splitext(item)
            size = os.path.getsize(path) / 1024
            size_in_bt = '{0:.2f}'.format(size)
            update_artifact_list("artifacts", json_data_list_file, item, "", "", "", "")

def edit_db():
    with open(json_data_list_file, "r") as json_file:
        file_data = json.load(json_file)
        index_list = []
        print(file_data)
edit_db()