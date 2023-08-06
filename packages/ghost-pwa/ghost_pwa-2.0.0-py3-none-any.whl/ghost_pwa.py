from os import path, remove
from pathlib import Path
import requests
import shutil
from subprocess import run
from tempfile import TemporaryDirectory

try:
    from updateable_zip_file import UpdateableZipFile as ZipFile, ZipInfo
except ModuleNotFoundError:
    from ghost_pwa.updateable_zip_file import (
        UpdateableZipFile as ZipFile,
        ZipInfo
    )

header_insert = """
    {{!-- PWA --}}
    <link rel="manifest" href="/manifest.webmanifest">
    <meta name="theme-color" content="#0075FF">
    <link rel="apple-touch-icon" href="/assets/icons/ghost-4.png">
"""

footer_insert = """
{{!-- Service Worker for PWA --}}
<script>
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js');
    });
}
</script>
"""

MODULE_DIR = path.dirname(path.realpath(__file__))

def get_position_for_insert(tag, text):
    start_position = 0
    end_position = text.index("{{" + tag + "}}")
    input_position = text.rfind("\n\n", start_position, end_position) + 1
    return input_position

def insert_before_tag(tag, insert, original):
    input_position = get_position_for_insert(tag, original)

    return "".join([
        original[:input_position],
        insert,
        original[input_position:]
    ])

def insert_pwa_scripts(original_markup):
    with_header = insert_before_tag(
        "ghost_head", header_insert, original_markup
    )
    with_header_and_footer = insert_before_tag(
        "ghost_foot", footer_insert, with_header
    )
    return with_header_and_footer

def get_file(url, out_file):
    r = requests.get(url, allow_redirects=True)
    open(out_file, 'wb').write(r.content)

def dir_exists(directory):
    return path.isdir(directory)

def unpack_example():
    """
    >>> unpack_example()
    """
    with TemporaryDirectory() as temp_dir:
        get_file(
            "https://codeload.github.com/TryGhost/Casper/zip/refs/tags/3.1.3",
            f"{temp_dir}/Casper-3.1.3.zip"
        )
        unpack(f"{temp_dir}/Casper-3.1.3.zip", target_dir=temp_dir)
        assert dir_exists(f"{temp_dir}/Casper-3.1.3")

    assert dir_exists(temp_dir) is False

def unpack(archive, target_dir="."):
    shutil.unpack_archive(archive, target_dir)

def get_root_dir(archive_file):
    """
    Returns the root directory of the theme ZIP file.

    Examples:

    >>> with ExampleArchiveWithOneSubdir("test.zip") as test_archive:
    ...     get_root_dir(test_archive)
    'Casper-3.1.3'

    >>> with EmptyExampleArchive("test.zip") as test_archive:
    ...     get_root_dir(test_archive)
    '.'

    >>> with ExampleArchiveWithTwoSubdirs("test.zip") as test_archive:
    ...     get_root_dir(test_archive)
    '.'
    """
    with ZipFile(archive_file) as zip_file:
        paths = [
            file[:-1] for file in zip_file.namelist()
            if file.count("/") == 1 and file[-1] == '/'
        ]

        return paths[0] if len(paths) == 1 else '.'

def get_new_file_path(original_file_path):
    """
    >>> path = Path("Casper.zip")
    >>> new_path_obj = get_new_file_path(path)
    >>> str(new_path_obj)
    'Casper-PWA.zip'
    """
    return Path(original_file_path.stem + "-PWA" + original_file_path.suffix)

def get_processed_zip(archive_file):
    original_file = Path(archive_file)
    new_file = get_new_file_path(original_file)

    shutil.copy(original_file, new_file)

    with ZipFile(new_file) as out_zip:
        root_dir = get_root_dir(new_file)
        default_hbs_path = f"{root_dir}/default.hbs"
        assert default_hbs_path in out_zip.namelist()

        default_hbs = out_zip.read(default_hbs_path).decode()

    with_header_and_footer = insert_pwa_scripts(default_hbs)

    with ZipFile(new_file, 'a') as out_zip:
        out_zip.writestr(default_hbs_path, with_header_and_footer)

        out_zip.write(
            f"{MODULE_DIR}/manifest.webmanifest",
            f"{root_dir}/manifest.webmanifest"
        )

        out_zip.write(
            f"{MODULE_DIR}/sw.js",
            f"{root_dir}/sw.js"
        )

        out_zip.write(
            f"{MODULE_DIR}/icons/ghost-2.png",
            f"{root_dir}/assets/icons/ghost-2.png"
        )
        out_zip.write(
            f"{MODULE_DIR}/icons/ghost-4.png",
            f"{root_dir}/assets/icons/ghost-4.png"
        )

    return new_file

class ExampleArchive:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self._create_archive(self.name)
        return self.name

    def __exit__(self, type, value, traceback):
        remove(self.name)

    def _create_archive(self, name):
        with ZipFile(name, 'w') as out_zip:
            pass

def mkdir(zip_file, folder):
    zfi = ZipInfo(folder + '/')
    zip_file.writestr(zfi, '')

class EmptyExampleArchive(ExampleArchive):
    pass

class ExampleArchiveWithOneSubdir(ExampleArchive):
    def _create_archive(self, name):
        with ZipFile(name, 'w') as out_zip:
            mkdir(out_zip, "Casper-3.1.3")

class ExampleArchiveWithTwoSubdirs(ExampleArchive):
    def _create_archive(self, name):
        with ZipFile(name, 'w') as out_zip:
            mkdir(out_zip, "assets")
            mkdir(out_zip, "doc")

def make_pwa(file_name):
    new_file = get_processed_zip(file_name)
    return new_file

def example_make_casper_pwa():
    """
    Example:
    >>> example_make_casper_pwa()
    PosixPath('Casper-3.1.3-PWA.zip')

    Clean up:
    >>> remove("Casper-3.1.3.zip")
    >>> remove("Casper-3.1.3-PWA.zip")
    """
    get_file(
        "https://codeload.github.com/TryGhost/Casper/zip/refs/tags/3.1.3",
        "Casper-3.1.3.zip"
    )
    return make_pwa("Casper-3.1.3.zip")
