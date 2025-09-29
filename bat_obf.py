import time
import os
from tkinter.filedialog import askopenfilename

banner = r'''
#######################################################
______       _       _     _____                     _ 
| ___ \     | |     | |   |  __ \                   | |
| |_/ / __ _| |_ ___| |__ | |  \/_   _  __ _ _ __ __| |
| ___ \/ _` | __/ __| '_ \| | __| | | |/ _` | '__/ _` |
| |_/ / (_| | || (__| | | | |_\ \ |_| | (_| | | | (_| |
\____/ \__,_|\__\___|_| |_|\____/\__,_|\__,_|_|  \__,_|
                                                                                                            
#######################################################
''' + '\n\n'

def open_file():
    time.sleep(1)
    file_path = askopenfilename(
        title="Select your file",
        filetypes=[("BAT", "*.bat"), ("CMD", "*.cmd"), ("TXT", "*.txt"), ("All files", "*.*")]
    )
    if not file_path:
        print("\n[!] No file selected. Exiting...")
        exit()
    with open(file_path, 'rb') as f:
            content = f.read()
    file_name = os.path.basename(file_path)
    return file_name, content

def hex_encode(content):
    hex_header = ["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"]
    hex_content = ['{:02X}'.format(b) for b in content]
    encoded = hex_header + hex_content
    return encoded

def main():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        print(banner)
        print(f"[+] Please pick a file")
        file_name, file_content = open_file()
        print(f"[+] Selected file: {file_name}")

        output_name = input("[>] Output filename (without extension): ").strip()
        if not output_name:
            output_name = f"{file_name}_obfuscated"

        hex_enc = hex_encode(file_content)
    
        output_file = f'{output_name}.bat'
        with open(output_file, 'wb') as f:
            for hex_byte in hex_enc:
                f.write(bytes.fromhex(hex_byte))
    
        print(f"[+] Saved to {output_name}.bat")

    except Exception as e:
        print(f"Error: {e}")
        print("Exiting...")
        exit(1)

if __name__ == "__main__":
    main()