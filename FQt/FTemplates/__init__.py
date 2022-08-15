from F import OS

FILE_PATH_AND_NAME: str = __file__
FILE_PATH: str = OS.get_path(FILE_PATH_AND_NAME)
FILES = OS.get_files_in_directory()

DEFAULT_TEMPLATE = f"{FILE_PATH}/default.ui"
