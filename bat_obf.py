import time
import os
import random
import subprocess
from tkinter.filedialog import askopenfilename

banner = r'''
#############################################
______       _       _     _____                     _ 
| ___ \     | |     | |   |  __ \                   | |
| |_/ / __ _| |_ ___| |__ | |  \/_   _  __ _ _ __ __| |
| ___ \/ _` | __/ __| '_ \| | __| | | |/ _` | '__/ _` |
| |_/ / (_| | || (__| | | | |_\ \ |_| | (_| | | | (_| |
\____/ \__,_|\__\___|_| |_|\____/\__,_|\__,_|_|  \__,_|
                                                                                                            
#############################################
''' + '\n\n'


letters = """SEt R^=Jg^%pUBLIc:~13,1%^gtGXz%publIc:~4,1%w%pUBLIc:~11,1%^hm%pUBLIc:~10,1%^S^HI^O^A""" # ok
echooff ="""@%publIc:~5,1%%pUBLIc:~0,1%ho oF%pUBLIc:~46,16%f""" # ok
clss = """^%pUBlIC:~14,1%^L%pUBlic:~55,17%^%publIc:~4,1%""" # ok
echoon = """@%pUBLIc:~5,1%%publIc:~0,1%ho O^n""" # ok

encoding_map = {
    "J": "%r:~0,1%",
    "G": "%r:~5,1%",
    "g": "%r:~1,1%",
    "i": "%r:~2,1%",
    "I": "%r:~16,1%",
    "t": "%r:~4,1%",
    "X": "%r:~6,1%",
    "z": "%r:~7,1%",
    "S": "%r:~14,1%",
    "s": "%r:~8,1%",
    "w": "%r:~9,1%",
    "b": "%r:~10,1%",
    "h": "%r:~11,1%",
    "H": "%r:~15,1%",
    "m": "%r:~12,1%",
    "u": "%r:~13,1%",
    "O": "%r:~17,1%",
    "A": "%r:~18,1%",
}


def open_file():
    time.sleep(1)
    file_path = askopenfilename(
        title="Select your file",
        filetypes=[("BAT", "*.bat"), ("CMD", "*.cmd"), ("TXT", "*.txt"), ("All files", "*.*")]
    )
    if not file_path:
        print("\nNo file selected. Exiting...")
        exit()
    with open(file_path, 'r') as f:
            content = f.read()
    file_name = os.path.basename(file_path)
    return file_name, content


def add_random_carrots(text, num_carets):
    if num_carets > len(text) - 1:
        print("Error: Number of carets cannot exceed text length.")
        exit()
    
    positions = random.sample(range(len(text)), num_carets)
    result = []
    for i, char in enumerate(text):
        result.append(char)
        if i in positions:
            result.append('^')
    return ''.join(result)

def comments_cleaning(text):
    lines = text.split('\n')
    result = []
    for line in lines:
        stripped = line.lstrip() 
        if not (stripped.lower().startswith('::') or stripped.lower().startswith('rem ')):
            result.append(line)
    return '\n'.join(result)

# Additional replacemens can be added
# class ReplacementHelper:
#     def __init__(self, replace_with, every_nth):
#         self.counter = 0
#         self.replace_with = replace_with
#         self.every_nth = every_nth

#     def doit(self, match):
#         self.counter += 1
#         return match.group(1) if self.counter % self.every_nth else self.replace_with

# def encode_helper(text):
#     text = text.replace('%%~', 'ckoco').replace('%~', 'croco')
#     #processed = text + "\nset a = %%~i\nset a = % + %~1\"%\nset a = %a%\n:aaaaaaaaaaaaaaaaaaaaaaaaaaab"
#     #In case of something addionional
#     replacer = ReplacementHelper("replaced", 2)
#     return re.sub(r"(%)", replacer.doit, text)


def compile(name, content):
    poggers =clss + "\n" + echooff + "\n" + letters + "\n" + content
    with open(f"{name}.bat", "w") as f:
        f.write(poggers)

    step1 = 'echo //4mY2xzDQo= > "temp.~b64" && certutil.exe -f -decode "temp.~b64" "{name}o.bat" && del "temp.~b64" && copy "{name}o.bat" /b + "{name}.bat" /b'.format(name=name)
    step2 = 'del "{name}.bat" /f && rename "{name}o.bat" "{name}.bat"'.format(name=name)

    subprocess.run(step1, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, text=True)
    subprocess.run(step2, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, text=True)


def main():
    print(banner)
    print("Please pick a file")
    file_name, file_content = open_file()
    print(f"Selected file: {file_name}")

    clean_comments = input("Would you like to clean the comments (safe) [y/n]: ").strip().lower()
    if clean_comments == 'y':
        file_content = comments_cleaning(file_content)
    elif clean_comments != 'n':
        print("Invalid input, exiting...")
        exit()

    add_carets = input("Would you like to add random ∧ to the obfuscation (may break script, not recommended)? [y/n]: ").strip().lower()
    if add_carets == 'y':
        num_carets = int(input(f"Number of ^ you want (max {len(file_content)}): "))
        file_content = add_random_carrots(file_content, num_carets)
    elif add_carets != 'n':
        print("Invalid input, exiting...")
        exit()

    # processed_content = encode_helper(file_content)

    processed_content = file_content
    
    for char, replacement in encoding_map.items():
        processed_content = processed_content.replace(char, replacement)


    output_name = input("Output filename (without extension): ").strip()
    if not output_name:
        output_name = "obfuscated"
    
    compile(output_name, processed_content)
    print(f"\nSaved to {output_name}.bat")
    print("Operation complete. Exiting...")

if __name__ == "__main__":
    main()