import paq

# Custom Base 255 encoding function
def custom_base255_encode(data):
    encoded_data = bytes((x + 1 if x < 255 else 255 for x in data))
    return encoded_data

# Custom Base 255 decoding function
def custom_base255_decode(data):
    decoded_data = bytes((x - 1 if x > 0 else 0 for x in data))
    return decoded_data

# Compression
def compress_file(file_name, output_file_name):
    with open(file_name, "rb") as file:
        file_content = file.read()

    compressed_content = file_content
    encoded_content = custom_base255_encode(paq.compress(compressed_content))

    with open(output_file_name, "wb") as output_file:
        output_file.write(encoded_content)

    print(f"File '{file_name}' compressed and saved as '{output_file_name}'.")

# Extraction
def extract_file(file_name, extracted_file_name):
    with open(file_name, "rb") as file:
        file_content = file.read()

    decoded_content = custom_base255_decode(paq. decompress(file_content))
    decompressed_content = decoded_content

    with open(extracted_file_name, "wb") as extracted_file:
        extracted_file.write(decompressed_content)

    print(f"File '{file_name}' extracted and saved as '{extracted_file_name}'.")

# Ask the user for an option
choice = input("Choose an option:\n1. Compress a file\n2. Extract a file\nEnter 1 or 2: ")

if choice == "1":
    # Compression
    file_name = input("Enter the name of the file you want to compress: ")
    output_file_name = input("Enter the name of the output file for the compressed data: ")
    compress_file(file_name, output_file_name)

elif choice == "2":
    # Extraction
    file_name = input("Enter the name of the file you want to extract: ")
    extracted_file_name = input("Enter the name of the output file for the extracted data: ")
    extract_file(file_name, extracted_file_name)

else:
    print("Invalid option. Please choose 1 or 2.")