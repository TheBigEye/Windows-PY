import base64

__author__ = 'TheBigEye'
__version__ = '1.2'

# TODO Add encoders (in addition to decoders) and make Base64.py independent of the Python module

def read_32_sl(File, line):

# Documentation ---------------------------------------------------------------------------------------------------------------

    """
    Decode Base32 information to ASCII Text (just decode a single line).

    Parameters
    ----------
    `File` : string
        The address that the function will use to read the file that has information in Base32, example: `Disk/Disk32.txt`.

    `line` : string
        The line of the file to be read to decode the information.

    Then the function prints the information in the console along with the file name
        
    """

# Decode Base32 ---------------------------------------------------------------------------------------------------------------

    File_get_data = open(File, "r")
    File_read_data = File_get_data.readlines()[line]
    File_bytes = File_read_data.encode("ascii")
    Data_bytes = base64.b32decode(File_bytes)
    Data = Data_bytes.decode("ascii")

    print(File)
    print(Data)



def read_64_sl(File, line):

# Documentation ---------------------------------------------------------------------------------------------------------------

    """
    Decode Base64 information to ASCII Text (just decode a single line).

    Parameters
    ----------
    `File` : string
        The address that the function will use to read the file that has information in Base64, example: `Disk/Disk64.txt`.

    `line` : string
        The line of the file to be read to decode the information.

    Then the function prints the information in the console along with the file name
        
    """

# Decode Base64 ---------------------------------------------------------------------------------------------------------------

    File_get_data = open(File, "r")
    File_read_data = File_get_data.readlines()[line]
    File_bytes = File_read_data.encode("ascii")
    Data_bytes = base64.b64decode(File_bytes)
    Data = Data_bytes.decode("ascii")

    print(File)
    print(Data)


# Print the module info
#print("Author: " + str(__author__))
#print("Module version: " + str(__version__))
#print("Cropped version of Python Base64 module :)")
