import time
import easygui
import os
import pyfiglet
import random
from replacement_helper import ReplacementHelper
import re
import subprocess
from tqdm import tqdm

letters = """SEt R^=Jg^%pUBLIc:~13,1%^gtGXz%publIc:~4,1%w%pUBLIc:~11,1%^hm%pUBLIc:~10,1%^S^HI^O^A""" # ok
echooff ="""@%publIc:~5,1%%pUBLIc:~0,1%ho oF%pUBLIc:~46,16%f""" # ok
clss = """^%pUBlIC:~14,1%^L%pUBlic:~55,17%^%publIc:~4,1%""" # ok
echoon = """@%pUBLIc:~5,1%%publIc:~0,1%ho O^n""" # ok

dna_map = {
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
    "ckoco": "%%~",
    "croco": "%~",
    "replaced": "%",
}

def open_file():
    time.sleep(2)
    file_path = easygui.fileopenbox(title="Please select a batch file")
    if not file_path:
        print("No file selected. Exiting")
        exit()
    with open(file_path, 'r') as f:
        file_name = os.path.basename(file_path)
        text = f.read()
        return file_name, text
    
def encode_helper(text):
    text = text.replace('%%~', 'ckoco').replace('%~', 'croco')
    #processed = text + "\nset a = %%~i\nset a = % + %~1\"%\nset a = %a%\n:abc"
    #In case of something addionional
    replacer = ReplacementHelper("replaced", 2)
    eh_text = re.sub(r"(%)", replacer.doit, text)
    return eh_text

def compiler(name, content):
    poggers =clss + "\n" + echooff + "\n" + letters + "\n" + content + "\n"
    #print("poggers", poggers)
    with open(f"{name}.bat", "w") as f:
        f.write(poggers)

    bro1 = 'echo //4mY2xzDQo= > "temp.~b64" && certutil.exe -f -decode "temp.~b64" "{namee}o.bat" && del "temp.~b64" && copy "{namee}o.bat" /b + "{namee}.bat" /b'.format(namee=name)
    bro2 = 'del "{namee}.bat" /f && rename "{namee}o.bat" "{namee}.bat"'.format(namee=name)

    subprocess.run(bro1, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, text=True)
    subprocess.run(bro2, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, text=True)
    
def random_carrots(text, num_carrots):
    if num_carrots > len(text) - 1:
        print("Error: Number of carrots cannot exceed the text lenght.")
        exit()
    carrot_positions = random.sample(range(len(text)), num_carrots)
    result = []
    for i, char in enumerate(text):
        result.append(char)
        if i in carrot_positions:
            result.append('^')
    carrotated = ''.join(result)
    return carrotated

def main():
    print(pyfiglet.figlet_format("BatchGuard Obfuscator"))
    print("Please pick a batch file")
    file_name, file_content = open_file()
    print(f"Selected file: {file_name}")
    #print("con", file_content)

    yorn = input("Would you like to add random ^ in the obfuscation (may break the script, not recommended)? [y/n]: ").strip().lower()
    if yorn == "y":
        num_carrots = int(input(f"Number of ^ you want (max {len(file_content)}): "))
        file_content = random_carrots(file_content, num_carrots)
        #print("carrot logic.")
        #print("carrotated:", file_content) ok
    elif yorn != "n":
        print("Invalid input, exiting...")
        exit()

    processed_content = encode_helper(file_content)
    #print("processed%", processed_content)

    for char, replacement in dna_map.items():
        processed_content = processed_content.replace(char, replacement)
    #print("final1", processed_content)

    output_name = input("Output filename (without extension): ").strip()
    if not output_name:
        output_name = "obfuscated"

    for _ in tqdm(range(5), desc="Obfuscating..."):
        time.sleep(0.2)
    
    compiler(output_name, processed_content)
    print(f"\nSaved to {output_name}.bat")
    print("Operation complete. Exiting...")

if __name__ == "__main__":
    main()