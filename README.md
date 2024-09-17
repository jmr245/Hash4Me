# Hash4Me
Welcome to my first Python project!  Hash4Me is a simple, ongoing, and security focused program built to allow users to obtain the hash of a specified file, save it, and later verify that the hash has remained the same.  This project appeals to the CIA triad, specifically within the scope of data integrity.  What are you waiting for?  Time to start hashing!
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Shoutout](#shoutout)
## Installation
*Hash4Me was written with Python3.9.7, so make sure you at least have Python3.9 installed on your device.*
1. Clone the repository:
   '''bash git clone https://github.com/jmr245/Hash4Me.git'''
2. Install dependencies:
   '''pip install hashlib'''
## Usage
To run Hash4Me, use the following command: '''python3 hash4me.py'''.  If this is your first time using the program, you will need to run option 1 to obtain the file hash, then add it to the global variable "stored_hash" to run option 2 and verify hash integrity.  Currently, only one hash can be stored in the global variable for verification (subject to change soon).
## Contributing
1. Fork the repository.
2. Create a new branch: 'git checkout -b feature-name'.
3. Make your changes.
4. Push your branch: 'git push origin feature-name'.
5. Create a pull request.
## License
This project is licensed under the [MIT License](LICENSE)
## Shoutout
Huge shoutout to www.geeksforgeeks.org for being an amazing resource and reference for this project and for learning Python in general.
