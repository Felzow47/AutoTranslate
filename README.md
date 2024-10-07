<h1 align="center" style="margin-top: 0px;">AutoTranslate</h1>

<div align="center">
    <img src="https://github.com/user-attachments/assets/dcb5bd42-ba4c-4153-abc2-b226570b8a43" width="400">
</div>


**AutoTranslate** is a Python script designed to automatically translate text files. It uses the Google Translate API to perform translations between multiple languages, facilitating content localization for different users.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributions](#contributions)
- [License](#license)

## Features

- Bulk text translation from text files.
- Support for multiple languages via Google Translate.
- Automatically ignore non-translatable content (identifiers, media files, etc.).
- Display progress status for the translation process.
- Handle special sequences to preserve formatting.

## Installation

You can clone this repository and install the necessary dependencies:

```bash
git clone https://github.com/Felzow47/Autotranslate.git
cd Autotranslate
pip install deep_translator
```

## Usage

### Make sure to include the directory containing the files to be translated:

```python
directory = 'path/to/folder'
```
### Changing the Source and Target Languages

To customize the translation language, modify the values of the `source_lang` and `target_lang` parameters in the `translate_text_in_code` function according to your needs.

### Available Languages

To know the languages supported by the Google API, consult the [list of available languages](https://cloud.google.com/translate/docs/languages?hl=en).

### Function Example

Here's how to define the source and target languages in the code:

```python
def translate_text_in_code(file_path, source_lang='en', target_lang='fr'):
```

## Examples

To translate Ren'Py games using `.rpy` files, simply modify the extension searched for in the script. For example, replace the following line:

```python
if filename.endswith('.rpy'):
```

## Contributions

Feel free to fork the project and contribute as you wish! Your ideas and improvements are welcome.

## License

This project is under free license, so feel free to use it
