import gzip
import shutil


class ObjectS3:
    def __init__(self, path):
        self.__path = path

    @property
    def path(self):
        return self.__path

    def is_compressed(self):
        with gzip.open(self.__path, "r") as fh:
            try:
                # Try to read 1 byte of the file (Fails if not zipped)
                fh.read1()
                return True
            except Exception:
                return False

    def compress(self):
        with open(self.__path, "rb") as f_in:
            compressed_path = self.__path + ".gz"
            with gzip.open(compressed_path, "wb") as f_out:
                # Copying is done in chunks by default
                shutil.copyfileobj(f_in, f_out)
                self.__path = compressed_path
