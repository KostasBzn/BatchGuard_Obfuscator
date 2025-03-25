import time
import easygui
import os




letters = """SEt R^=Jg^%pUBLIc:~13,1%^gtGXz%publIc:~4,1%w%pUBLIc:~11,1%^hm%pUBLIc:~10,1%^S^HI^O^A""" # ok
echooff ="""@%publIc:~5,1%%pUBLIc:~0,1%ho oF%pUBLIc:~46,16%f""" # ok
clss = """^%pUBlIC:~14,1%^L%pUBlic:~55,17%^%publIc:~4,1%""" # ok
echoon = """@%pUBLIc:~5,1%%publIc:~0,1%ho O^n""" # ok

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

def main():
    file_name, file_content = open_file()
    print(f"Selected file: {file_name}")
    #print("con", file_content)

if __name__ == "__main__":
    main()