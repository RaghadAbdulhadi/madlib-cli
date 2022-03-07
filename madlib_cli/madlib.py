import re

def welcome():
    """
    A function that prints a welcoming message to the user
    """
    print("""
    Welcome to Madlib Game!
    To start the game please type in your answers for the following to get the output of the Midlib Game
    """)

    
def get_user_inputs(path):
    """
    A function that returns a list of the users inputs.
    """
    try:
        with open(path, "r") as template:
            content = template.read().strip().replace("\n","\n")
    except FileNotFoundError:
       raise ValueError("path not found")

    input_placeholders= parse_template(content)[0]

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
            content = template.read()
            print(content)
    except FileNotFoundError:
        content = "Error: Sorry, file does not exist"
    finally:
        return content


def extract_contents(path):
    """
    A function that reads the content of the file that contains the template of the game.
    """
    try:
        with open(path, "r") as template:
            content = template.read().strip().replace("\n","\n")
    except FileNotFoundError:
        content = "Error: Sorry, file does not exist"
    else:
        return content


def parse_template(template_content):
    """
    A function that takes a string and returns a template without the language_parts and a list with the language parts
    Input: template_content
    Output: List and a template string without the language parts
    """
    language_parts = re.findall(r"\{(.*?)\}", template_content)
    for language_part in language_parts:
        template_content = template_content.replace(language_part, "")
    return [language_parts, template_content]


def merge(bare_template, users_inputs):
    """
    A function that takes the bare_template and the user_inputs as an input and return the final output which is a string with the language parts from the user included inside the bare_template
    Input: bare_template, users_inputs
    Output: String with the language parts from the user
    """
    for input in users_inputs:
        user_output = bare_template[1].replace("{}", f"{input}")
    print(user_output)
    

if __name__ == "__main__":
    welcome()
    user_input = get_user_inputs("assets/madlib_template.txt")
    read_template("assets/dark_and_stormy_night_template.txt")
    template_content = extract_contents("assets/madlib_template.txt")
    bare_template = parse_template(template_content)
    merge(bare_template, user_input)
