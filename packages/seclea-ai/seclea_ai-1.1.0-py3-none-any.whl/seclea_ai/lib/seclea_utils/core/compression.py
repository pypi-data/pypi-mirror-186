import os
import subprocess  # nosec
from abc import abstractmethod
from pathlib import Path
from sys import platform

from .exceptions import DecompressionError
from ..object_management.utils import ensure_path_exists


# TODO: Safety review of using subprocess for compression/decompression


class CompressionException(Exception):
    pass


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pigz_binary_unix = os.path.join(base_dir, "clib", "compiled", "pigz", "pigz")
pigz_binary_win32 = os.path.join(base_dir, "clib", "pigz.exe")


class Compressor:
    @abstractmethod
    def compress(self, path, name, out_dir: str = None) -> (str, str):
        """
        e.g.
        with a sample directory structure:
        - project
            - test_data
                - datasets
                    - flowers
                        - img1.jpg
                        ...
                        - dset.csv

        compress (test_data/datasets, flowers)
        generates file:
        test_data/dataset/flowers.tar.gz
        returns (test_data/datasets, flowers.gz)
        @param path: working dir
        @param name: file or dir to compress
        @param out_dir: directory to save file to (defaults to path if None)
        @return:
        """
        raise NotImplementedError

    @abstractmethod
    def decompress(self, path, name) -> (str, str):
        raise NotImplementedError


def get_compressor() -> Compressor:
    compressors = {
        "linux": UnixCompressor,
        "linux2": UnixCompressor,
        "darwin": MacOSCompressor,
        "win32": Win32Compressor,
    }
    return compressors[platform]()


class UnixCompressor(Compressor):
    _ext = ".tar.gz"

    def compress(self, path, name, out_dir: str = None) -> (str, str):
        if not os.path.exists(os.path.join(path, name)):
            raise FileExistsError(os.path.join(path, name))
        write_dir = out_dir if out_dir is not None else path
        ensure_path_exists(write_dir)
        new_name = f"{name}{self._ext}"
        curr_dir = os.getcwd()
        command = f'cd "{path}" && tar -cf - "{name}" | {pigz_binary_unix} > "{os.path.join(write_dir, new_name)}" && cd {curr_dir}'

        with subprocess.Popen(  # nosec
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT  # nosec
        ) as proc:  # nosec
            cmd_out = []
            while proc.poll() is None:
                cmd_out.append(
                    proc.stdout.readline().decode()
                )  # give output from your execution/your own message
            proc.stdout.close()
            exit_code = proc.wait()
        if exit_code != 0:
            cmd_out = "\n".join(cmd_out)
            raise CompressionException(
                f"Compression error code:{exit_code}, Error Log: {cmd_out} - Please ensure pigz is installed via brew or apt"
            )  # catch return code
        return write_dir, new_name

    def decompress(self, path: str, name) -> (str, str):
        path_in = os.path.join(path, name)
        if not os.path.exists(path_in):
            raise FileExistsError(path_in)
        if not name.endswith(self._ext):
            raise DecompressionError(
                f"file name: {name} must end with {self._ext} otherwise we cannot guarantee safe decompression"
            )
        new_name = name[: -len(self._ext)]
        if not os.path.exists(path):
            Path(path).mkdir(parents=True, exist_ok=True)
        os.system(  # nosec
            f'tar --use-compress-program={pigz_binary_unix} -xf "{path_in}" -C "{path}"'  # nosec
        )  # nosec
        return path, new_name


class Win32Compressor(Compressor):
    _ext = ".tar.gz"

    def compress(self, path, name, out_dir: str = None) -> (str, str):
        if not os.path.exists(os.path.join(path, name)):
            raise FileExistsError(os.path.join(path, name))
        write_dir = out_dir if out_dir is not None else path
        ensure_path_exists(write_dir)
        new_name = f"{name}{self._ext}"
        curr_dir = os.getcwd()
        command = f'chdir "{path}" && tar -cf - "{name}" | {pigz_binary_win32} > "{os.path.join(write_dir, new_name)}" && chdir {curr_dir}'
        with subprocess.Popen(  # nosec
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT  # nosec
        ) as proc:  # nosec
            cmd_out = []
            while proc.poll() is None:
                cmd_out.append(
                    proc.stdout.readline().decode()
                )  # give output from your execution/your own message
            proc.stdout.close()
            exit_code = proc.wait()

        if exit_code != 0:
            cmd_out = "\n".join(cmd_out)
            raise CompressionException(
                f"Compression error code:{exit_code}, Error Log: {cmd_out} - Please ensure pigz is installed via brew or apt"
            )  # catch return code
        return write_dir, new_name

    def decompress(self, path: str, name) -> (str, str):
        path_in = os.path.join(path, name)
        if not os.path.exists(path_in):
            raise FileExistsError(path_in)
        if not name.endswith(self._ext):
            raise DecompressionError(
                f"file name: {name} must end with {self._ext} otherwise we cannot guarantee safe decompression"
            )
        new_name = name[: -len(self._ext)]
        if not os.path.exists(path):
            Path(path).mkdir(parents=True, exist_ok=True)
        os.system(  # nosec
            f'tar --use-compress-program={pigz_binary_win32} -xf "{path_in}" -C "{path}"'  # nosec
        )  # nosec
        return path, new_name


class MacOSCompressor(Compressor):
    _ext = ".tar.gz"

    def compress(self, path, name, out_dir: str = None) -> (str, str):
        if not os.path.exists(os.path.join(path, name)):
            raise FileExistsError(os.path.join(path, name))
        write_dir = out_dir if out_dir is not None else path
        ensure_path_exists(write_dir)
        new_name = f"{name}{self._ext}"
        curr_dir = os.getcwd()
        command = f'cd "{path}" && tar -cf - "{name}" | {pigz_binary_unix} > "{os.path.join(write_dir, new_name)}" && cd {curr_dir}'

        with subprocess.Popen(  # nosec
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT  # nosec
        ) as proc:  # nosec
            cmd_out = []
            while proc.poll() is None:
                cmd_out.append(
                    proc.stdout.readline().decode()
                )  # give output from your execution/your own message
            proc.stdout.close()
            exit_code = proc.wait()
        if exit_code != 0:
            cmd_out = "\n".join(cmd_out)
            raise CompressionException(
                f"Compression error code:{exit_code}, Error Log: {cmd_out} - Please ensure pigz is installed via brew or apt"
            )  # catch return code
        return write_dir, new_name

    def decompress(self, path: str, name) -> (str, str):
        path_in = os.path.join(path, name)
        if not os.path.exists(path_in):
            raise FileExistsError(path_in)
        if not name.endswith(self._ext):
            raise DecompressionError(
                f"file name: {name} must end with {self._ext} otherwise we cannot guarantee safe decompression"
            )
        new_name = name[: -len(self._ext)]
        if not os.path.exists(path):
            Path(path).mkdir(parents=True, exist_ok=True)
        os.system(f'tar -xf "{path_in}" -C "{path}"')  # nosec
        return path, new_name
