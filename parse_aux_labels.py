"""
Creates a map from the labels in the aux file to the corresponding values 
and replaces the labels in the tex file with the corresponding values from the aux file. \\
The modified tex file is written to a new file.
"""
import re

def find_aux_labels(aux_file_path):
    # Open the file and read its contents
    with open(aux_file_path, 'r') as file:
        data = file.read()

    pattern = r"\\newlabel\{(\w+)\}\{\{.*?\}\{.*?\}\{.*?\}\{(.*?)\}\{\}\}"
    matches = re.findall(pattern, data)

    result = {key: value for key, value in matches}
    return result

def replace_labels(tex_file_path, labels_map):
    # Open the tex file and read its contents
    with open(tex_file_path, 'r') as file:
        data = file.read()

    # Find all the labels in the tex file and replace them with the corresponding values from the aux file

    for key, value in labels_map.items():
        pattern = r"\{" + key + r"\}"
        matches = re.findall(pattern, data)
        for _ in matches:
            data = re.sub(pattern, "{" + value + "}", data)

    return data


def write_modified_tex_file(modified_text_out_path, data):
    # Write the modified tex file to a new file
    with open(modified_text_out_path, 'w') as file:
        file.write(data)


# Specify the path to your file
file_name = "intro"
aux_file_path = f"./raw_data/{file_name}.aux"
tex_file_path = f"./raw_data/{file_name}.tex"
modified_text_out_path = f"./data/{file_name}.tex"

# Find the auxiliary labels in the aux file
labels_map = find_aux_labels(aux_file_path)

# Replace the labels in the tex file with the corresponding values from the aux file
modified_text = replace_labels(tex_file_path, labels_map)

# Write the modified tex file to a new file
write_modified_tex_file(modified_text_out_path, modified_text)

print("Modified tex file written to:", modified_text_out_path)
