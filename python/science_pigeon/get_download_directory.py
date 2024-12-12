def get_download_directory(config_file_path):
    """Retrieve the download directory from the configuration file."""
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    return config.get("download_dir", None)