# File Sorter
A robust Python utility designed to automatically organize cluttered directories by sorting files into categorized folders based on their extensions.

## 🚀 Features
- **Smart Categorization:** Automatically detects file types (Documents, Images, Videos, Music, Archives, Programs) and moves them to respective folders.
- **Collision Handling:** Never overwrites your data. If a file with the same name exists in the destination, the program intelligently renames the new file (e.g., image.jpg becomes image_1.jpg).
- **Performance Optimized:** Utilizes Python sets to cache directory verification, minimizing redundant system calls.
- **Portable & Cross-Platform:** Works seamlessly on Windows, Macintosh, Linux and Android (Pydroid 3, Termux, PyramIDE, etc.) thanks to robust path handling.
- **Input Validation:** Includes safety checks to ensure the provided path is valid and accessible.

## 🛠️ How It Works
The script follows a modular logic:
1. **Validation:** Confirms the source directory exists.
2. **Identification:** Uses `os.path.splitext` to determine file extensions.
3. **Lookup:** Maps extensions to categories using an efficient dictionary-based search.
4. **Relocation:** Moves files using `shutil.move` while ensuring unique naming in the target directory.

## 📋 Requirements
- Python 3.x
- No external libraries required (uses standard library `os` and `shutil`).

## 📖 Usage
1. Clone this repository or download file_sorter.py.
2. Run the script:
`python file_sorter.py`
3. Enter the full path of the directory you wish to organize when prompted.

## 📂 Default Mappings
| Folder    | Common Extensions                                                                                           |
| :-------- | :---------------------------------------------------------------------------------------------------------- |
| Documents | .pdf, .txt, .html, .css, .js, .py, .pbix, .csv, .epub, .docx, .xlsx, .ipynb, .json, .md, .yaml, .log, .pptx |
| Images    | .jpeg, .jpg, .png, .gif, .svg, .webp, .ico, .heic, .bmp                                                     |
| Videos    | .mp4, .mkv, .avi, .mov, .wmv, .3gp, .flv                                                                    |
| Music     | .mp3, .wav, .aac, .flac, .ogg, .m4a                                                                         |
| Archives  | .zip, .rar, .7z, .tar, .gz                                                                                  |
| Programs  | .exe, .msi, .bat, .apk, .sh, .whl                                                                           |


#### Files with unrecognized extensions are moved to an *Others* folder. 
Developed as a personal utility for cross-platform file management.

## 🤝 Contributing
Contributions are very welcome! If you'd like to add new extension mappings or features, feel free to submit a pull request. Please ensure changes align with the existing structure and include updates to this README if mappings are modified.

## 📄 License
This project is licensed under the [MIT License](http://choosealicense.com/licenses/mit/).