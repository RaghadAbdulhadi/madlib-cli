import re

def welcome():
    """
    A function that prints a welcoming message to the user
    """
    print("""
    Welcome to Madlib Game!
    To start the game please type in your answers for the following to get the output of the Midlib Game
    """)


def extract_contents(path):
    """
    A function that reads the content of the file that contains the template of the game.
    """
    try:
        with open(path, "r") as template:
            content = template.read().strip().replace("\n","\n")
    except FileNotFoundError:
       raise FileNotFoundError("path not found")
    else:
        return content
        
    
def get_user_inputs(path):
    """
    A function that returns a list of the users inputs.
    """
    try:
        with open(path, "r") as template:
            content = template.read().strip().replace("\n","\n")
    except FileNotFoundError:
       raise FileNotFoundError("path not found")

    input_placeholders= parse_template(content)[1]
    user_inputs = []
    for placeholder in input_placeholders:
        add_language_part = input(f"type in {placeholder}:")
        user_inputs.append(add_language_part)

    return user_inputs


def read_template(path):
    """
    A function that takes in a path to text file and returns a stripped string of the file's contents.

    Input: path
    Output: 
        stripped string
        if the file is not found: raise error
    """
    try:
        with open(path, "r") as template:
            content = template.read().strip().replace("\n","\n")
            return content
    except FileNotFoundError:
        raise FileNotFoundError("File not found")


def parse_template(template_content):
    """
    A function that takes a string and returns a template without the language_parts and a list with the language parts
    Input: template_content
    Output: List and a template string without the language parts
    """
    language_parts = re.findall(r"\{(.*?)\}", template_content)
    for language_part in language_parts:
        template_content = template_content.replace(language_part, "")
    return [template_content, tuple(language_parts)]


def merge(bare_template, users_inputs):
    """
    A function that takes the bare_template and the user_inputs as an input and return the final output which is a string with the language parts from the user included inside the bare_template
    Input: bare_template, users_inputs
    Output: String with the language parts from the user
    """
    user_output = str(bare_template).format(*users_inputs)
    return user_output
    

def write_response(text):
    print(text)
    with open("../assets/fill_template", "w") as final_output:
        final_output.write(text)



if __name__ == "__main__":
    welcome()
    user_input = get_user_inputs("../assets/dark_and_stormy_night_template.txt")
    read_template("../assets/dark_and_stormy_night_template.txt")
    template_content = extract_contents("../assets/dark_and_stormy_night_template.txt")
    #template_content = extract_contents("../assets/dark_and_stormy_night_template.txt")
    bare_template = parse_template(template_content)[0]
    output = merge(bare_template, user_input)
    write_response(output)
   