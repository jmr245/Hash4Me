import hashlib

stored_hash = " " #Already obtained hash goes here.  Feel free to add more stored hashes.

print("\n------------------------------------------------")
print(" |   |    \     ___|  |   |  |  |     \  | ____|")
print(" |   |   _ \  \___ \  |   |  |  |    |\/ | __|")
print(" ___ |  ___ \       | ___ | ___ __|  |   | |")
print("_|  _|_/    _\_____/ _|  _|    _|   _|  _|_____|")
print("------------------------------------------------")
print("\nWelcome to Hash4Me!")
print("\n1. Acquire the hash of a file\n2. Check the integrity of an existing file hash")
print("\n**If you have not already obtained a hash, please choose option 1 and store hash in the correct variable**")
new_hash = int(input("\nPlease choose option 1 or 2: "))

if (new_hash == 1):

    def hashes(file_path, algorithm='md5, sha1, sha256, sha512'):
        hash_func = hashlib.new(algorithm) #Constructor
        with open(file_path, "rb") as file: #Reads/opens file in binary mode.
            while chunk := file.read(8197): #Handle large files efficiently.
                hash_func.update(chunk) #Updates the hash object with each chunk of data.

        return hash_func.hexdigest() #Returns/outputs hash value in hexadecimal digits
    
    hash_again = "y"

    while hash_again == "y":

        file_path = input("\nPlease enter the path of the file to hash: ")
        print("\nAvailable Algorithms: md5, sha1, sha256, sha512")
        algorithm = input("\nPlease enter a hash algorithm: ")

        try:
            file_hash = hashes(file_path, algorithm)
            print(f"\nThe {algorithm} hash of the file is: {file_hash}\n")
        except FileNotFoundError: #Catches exception where file path is invalid/does not exist.
            print("File not found.  Please enter a valid file path.")
        except ValueError: #Catches exception where hash input value is invalid.
            print("Invalid hash algorithm.  Please enter an available algorithm.")

        hash_again = input("Would you like to hash another file (y/n): ")

elif (new_hash == 2):

    def hashes(file_path, algorithm='md5, sha1, sha256, sha512'):
        hash_func = hashlib.new(algorithm)
        with open(file_path, "rb") as file:
            while chunk := file.read(8197):
                hash_func.update(chunk)

        return hash_func.hexdigest()

    file_path = input("\nPlease input the path of the file to verify: ")
    print("\nAvailable Algorithms: md5, sha1, sha256, sha512")
    algorithm = input("\nEnter algorithm previously used: ")

    new_hash = hashes(file_path, algorithm)

    if new_hash == stored_hash:
        print("\nHash values are a match!  Data integrity has been maintained.\n")
    else:
        print("\nHashes do not match or hash not properly stored!  Data integrity may be compromised.\n")

else:
    print("\nOption not reconginized, please try again.")