# Project Overview

`science_pigeon` is a Python module designed to manage and retrieve download directories based on user-defined configurations. This project provides a simple interface for users to specify where files should be downloaded, making it easier to manage file storage.

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

To use the `science_pigeon` module, you can import it in your Python scripts as follows:

```python
from science_pigeon import get_download_directory

download_dir = get_download_directory()
print(f"Download directory: {download_dir}")
```

Make sure to configure your `pigeon_config.json` file to specify the desired download directory.

## Configuration

Create a configuration file named `pigeon_config.json` in the specified config directory. The file should contain the following structure:

```json
{
    "download_dir": "/path/to/your/download/directory"
}
```

## Running Tests

To ensure everything is working correctly, you can run the tests using:

```
pytest
```

This will execute the unit tests defined in the `tests/test_science_pigeon.py` file.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.