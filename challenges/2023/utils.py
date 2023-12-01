import os


def get_input_file(file_name: str):
    """Get the absolute path for a given filename

    Args:
        file_name: the name of the file to find path for
    Returns:
        the filename with its absolute path preceding it
    """
    current_path = os.path.dirname(__file__)
    return current_path + '/inputs/' + file_name