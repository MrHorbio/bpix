# Bpix (Beautypix)

Bpix aka BeautyPix is a Python package that provides functionality for taking screenshots of websites using Selenium WebDriver. This tool reads a list of domains from a file, captures screenshots of each domain, and saves them to a designated directory.

## Features

- Take screenshots of websites specified in a text file.
- Save screenshots in a specified directory.
- Handle different URL formats and provide error messages for invalid URLs.

## Installation

` pip install beautypix `



## USAGE

```
from BPix.bpix import Bpix

#Initialize Bpix with the path to the file containing domains and a timeout value 
bpix = Bpix(file_path='path/to/domains.txt', time_out=5) 

#Take screenshots of the domains listed in the file 
bpix.s_shot()
``` 



## File format

The file_path specified should point to a text file containing one URL per line:
* https://www.google.com
* https://www.facebook.com
* https://www.twitter.com

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions to Bpix are welcome! If you have suggestions, improvements, or bug fixes, please fork the repository and submit a pull request. Ensure your contributions adhere to the coding standards and include appropriate documentation.

## Contact
For any inquiries or feedback, please contact:

* Author: Mr.Horbio 
* GitHub: https://github.com/MrHorbio/bpix/blob/main/bpix_package/README.md
* Youtube: https://www.youtube.com/@Mr-Horbio



## Thank you for using Bpix!





