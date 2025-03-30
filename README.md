## BatchGuard Batch Obfuscator v2

**Updated version from my old obfuscator**

**BatchGuard** is a simple batch file obfuscator written in Python that transforms your batch scripts into an unreadable format, enhancing their security and hiding their original logic. By encoding, adding random characters, and using encoding techniques, BatchGuard makes reverse-engineering your batch files a challenging task.

### Features
- **Obfuscation**: Transforms the content of a batch file into a more complex and difficult-to-understand format.
- **Random Carets**: Add random `^` symbols to confuse and break the logic flow (use cautiously as it may break scripts).
- **Comments Cleaning**: Removes all comments from the batch file for cleaner and more secure obfuscation.
- **Encoding**: Uses custom encoding scheme to replace characters and hide the actual logic.
- **Easy-to-use GUI**: Simple file picker to choose the batch file to obfuscate.
- **Operating System**: Windows. It may not work as expected on other operating systems such as Linux or macOS.

### How It Works
BatchGuard works by reading the contents of your batch script, applying various encoding techniques, and optionally deletes the comments and adds random carets (`^`) to obfuscate the file further. The final result is a new batch file that can still be executed but is unreadable. The logic of the tool can be edited for different types of obuscations.

### Encoding Example
In the repository there is an `example.txt` file with simple commands that you can experiment by obfuscating and executing them.

### Usage
1. Clone the repository or download the files.
2. Navigate to the folder containing the App.
3. Run the `bat_obf.py` script: `python bat_obf.py`

## Ethical Disclaimer
This tool is intended for educational purposes and to help improve your understanding of obfuscation, programming, and cybersecurity. **Misuse is prohibited**.


