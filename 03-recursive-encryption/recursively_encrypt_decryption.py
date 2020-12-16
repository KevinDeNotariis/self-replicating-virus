import encrypt_decryption

number_of_encryption = 1
original_filename = ""

def level_of_encryption():
  global number_of_encryption
  print("Number of encryption: ")
  number_of_encryption = input()


def ask_for_filename():
  global original_filename
  encrypt_decryption.ask_for_filename()
  original_filename = encrypt_decryption.file_name[:-3]


def encrypt_loop():
  to_encrypt_filename = original_filename
  encrypted_filename = to_encrypt_filename + "_e1"

  for i in range(1, int(number_of_encryption)+1):
    print(i)
    encrypt_decryption.compute_payloads()
    encrypt_decryption.write_virus(encrypted_filename + ".py")

    encrypt_decryption.file_name = encrypted_filename + ".py"
    encrypted_filename = original_filename + "_e" + str(i+1)

    encrypt_decryption.payload.clear()
    encrypt_decryption.encode.clear()
    encrypt_decryption.previous_payload.clear()


if __name__ == '__main__':
  level_of_encryption()
  ask_for_filename()
  encrypt_loop()