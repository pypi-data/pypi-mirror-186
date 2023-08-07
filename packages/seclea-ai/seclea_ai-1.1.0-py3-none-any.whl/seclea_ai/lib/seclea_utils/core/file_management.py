# Original Credit https://stackoverflow.com/questions/23212435/permission-denied-to-write-to-my-temporary-file/63173312#63173312
# Extended by Roger Milroy

import os
import tempfile
from pathlib import PurePath


class CustomNamedTemporaryFile:
    """
    This custom implementation is needed because of the following limitation of tempfile.NamedTemporaryFile:

    > Whether the name can be used to open the file a second time, while the named temporary file is still open,
    > varies across platforms (it can be so used on Unix; it cannot on Windows NT or later).
    """

    def __init__(self, mode="w+b", delete=True):
        self._mode = mode
        self._delete = delete
        self.name = None

    def __enter__(self):
        # Generate a random temporary file name
        self.name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
        # Ensure the file is created
        open(self.name, "x").close()
        # Open the file in the given mode
        self._tempFile = open(self.name, self._mode)
        return self._tempFile

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._tempFile.close()
        if self._delete:
            os.remove(self.name)


FILE_START = b"-*-start-file-*-\n"
DIR_START = b"-*-start-dir-*-\n"
DIR_END = b"-*-end-dir-*-\n"


def encode_dir_to_file(dir_or_file: PurePath, file):
    """
    Encode a whole directory structure into a single structured file - a la tar.

    Recursively encode and return a useable/decodeable structure for us to turn back into a directory.

    NOTE - this is not designed for large files - it will overflow memory almost certainly.
    Will need a streaming version if we stick with this for any length of time.

    Also designed for use with decode_file_to_dir on the same system only. Not cross
    :param dir_or_file:t
    :param file: file handle to write to. opened with wb(+) as the mode.
    :return:
    """

    # encode dir
    if os.path.isdir(dir_or_file):
        # write start delim and filename
        file.write(DIR_START)
        file.write(dir_or_file.parts[-1].encode("utf-8") + b"\n")
        # encode each file recursively
        for name in os.listdir(dir_or_file):
            encode_dir_to_file(dir_or_file / name, file)
        # write end delim
        file.write(DIR_END)

    # encode file
    elif os.path.isfile(dir_or_file):
        # write start delim and filename
        file.write(FILE_START)
        file.write(dir_or_file.parts[-1].encode("utf-8") + b"\n")
        file.write(str(os.path.getsize(dir_or_file)).encode("utf-8") + b"\n")
        # write file
        with open(dir_or_file, "rb") as f:
            file.write(f.read())
    else:
        raise ValueError("Inputs can only be files or directories")


def decode_file_to_dir(file_handle) -> str:
    """
    Decode file to directory - placed in current directory unless otherwise specified.
    :param file_handle:
    :return:
    """

    # enter dir block create and enter directory
    # read line and pass to write func

    root = None

    while True:
        line = file_handle.readline()
        if line == b"":
            break
        elif line == FILE_START:
            line = file_handle.readline()
            file_name = line.decode("utf-8").rstrip("\n")
            line = file_handle.readline()
            size = int(line.decode("utf-8").rstrip("\n"))
            with open(file_name, "wb+") as write_f:
                write_f.write(file_handle.read(size))
        elif line == DIR_START:
            line = file_handle.readline()
            dir_name = line.decode("utf-8").rstrip("\n")
            os.mkdir(dir_name)
            if root is None:
                root = dir_name
            os.chdir(dir_name)
        elif line == DIR_END:
            os.chdir("..")  # todo make work on windows...
        else:
            raise ValueError("Something went wrong in decoding")

    if root is None:
        raise ValueError("Root name not defined - something went wrong encoding.")
    return root
