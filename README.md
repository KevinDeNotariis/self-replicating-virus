# Self Replicating Virus

## ** Disclaimer **

The information and code provided here, are inteded to be used for educational and research purposes only. Do not use the information for illegal activities, any actions and or activities related to the material contained within this repository is solely your responsibility. The author will not be held responsibile in the event of any criminal charges against any individual misusing the information provided here.

## Content

This repository contains various versions of the same virus, a virus whose only purpose is to infect other python scripts with itself and propagating in this way. Nothing neither too fancy nor dangerous, but in the process, lots of so called _shadowing techniques_ will be presented. The ideal path to take for inspecting these different versions is given by the progressive initial number at the beginning of each directory.

Let me briefly summarize the peculiarities of each version:

1. `01-no-encryption`: base version of the virus.

2. `02-encryption`: this folder will contain the virus and an encryption script, which - from the plain virus file - will generate an encrypted version of the virus, with a decryption method appended.

3. `03-recursive-encryption`: this comes with 2 versions:

   - The first will encrypt the whole encrypted virus (namely the encrypted payload + the decryption method) and generate e new decryption method;
   - The second will encrypt only the decryption method and append this new payload to the original payload and it will add a decryption method to decrypt the encrypted decryption method (lol).

4. `04-polymorphic`: this version will rely on the polymorphic _shadowing technique_, which embrace various methods to hide the virus from detection (other than encryption).
