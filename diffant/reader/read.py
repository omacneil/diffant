def read_file(file_path: str, is_cloud_path: bool) -> str:
    """ "Read the file contents into a string."""
    if is_cloud_path:
        from .cloud import CloudReader

        contents = CloudReader().read_file(file_path)
    else:
        from .local import LocalReader

        contents = LocalReader().read_file(file_path)
    return contents