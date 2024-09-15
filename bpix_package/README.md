# Bpix

Bpix aka BeautyPix is a Python package that provides functionality for taking screenshots of websites using Selenium WebDriver. This tool reads a list of domains from a file, captures screenshots of each domain, and saves them to a designated directory.

## Features

- Take screenshots of websites specified in a text file.
- Save screenshots in a specified directory.
- Handle different URL formats and provide error messages for invalid URLs.

## Installation

pip install beautypix



## USAGE

from bpix.bpix import Bpix

# Initialize Bpix with the path to the file containing domains and a timeout value
bpix = Bpix(file_path='path/to/domains.txt', time_out=5)

# Take screenshots of the domains listed in the file
bpix.s_shot()



## File format

The file_path specified should point to a text file containing one URL per line:
https://www.google.com
https://www.facebook.com
https://www.twitter.com

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions to Bpix are welcome! If you have suggestions, improvements, or bug fixes, please fork the repository and submit a pull request. Ensure your contributions adhere to the coding standards and include appropriate documentation.

## Contact
For any inquiries or feedback, please contact:

Author: Ankush Kumar Rajput (Mr.Horbio)
GitHub: https://github.com/MrHorbio
Youtube: https://www.youtube.com/@Mr-Horbio



Thank you for using Bpix!


### Key Sections

1. **Title and Description**: Clearly state the purpose and name of your package.
2. **Features**: Highlight what the package does.
3. **Installation**: Provide clear instructions for installation.
4. **Usage**: Offer examples of how to use the package.
5. **File Format**: Explain the format for input files.
6. **Directory Structure**: Show the expected project structure.
7. **Running Tests**: Include commands for testing.
8. **License**: State the license type and link to the license file.
9. **Contributing**: Encourage contributions and explain how.
10. **Contact**: Provide contact information for feedback or questions.


