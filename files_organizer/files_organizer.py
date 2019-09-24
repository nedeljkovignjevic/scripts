import os
from pathlib import Path


DIRECTORY_EXTENSIONS = {
    'Audio': ['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.wpl', '.m3u'],
    'Text': ['.txt', '.doc', '.docx', '.odt ', '.pdf', '.rtf', '.tex', '.wks ', '.wps', '.wpd'],
    'Video': ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv'],
    'Images': ['.ai', '.bmp', '.gif', '.ico', '.jpg', '.jpeg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff', '.CR2'],
    'Compressed': ['.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip'],
    'Disc': ['.bin', '.dmg', '.iso', '.toast', '.vcd'],
    'Programming': ['.c', '.class', '.dart', '.py', '.sh', '.swift', '.html', '.h', '.java', '.kt']
}

# '.aif': 'Audio',
# '.cda': 'Audio',
# ...
EXTENSIONS = {file_format: directory
              for directory, file_formats in DIRECTORY_EXTENSIONS.items()
              for file_format in file_formats}


def organize():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        path = Path(entry)
        extension = path.suffix.lower()
        if extension in EXTENSIONS:
            directory_path = Path(EXTENSIONS[extension])
            if not os.path.exists(EXTENSIONS[extension]):
                directory_path.mkdir()
        else:
            directory_path = Path('Other')
            if not os.path.exists('Other'):
                directory_path.mkdir()
        path.rename(directory_path.joinpath(path))


if __name__ == '__main__':
    organize()

