#
#   Secure Passwords
#
#   A script to create passwords
#
#   @niklaswendt, @TheMorpheus407

import secrets
import string

print("")
print("Safe Password creator")
print("")
print("Run multiple times for new passwords")
print("")
chars = string.digits + string.ascii_letters + string.punctuation
print("Number of used chars: " + str(len(chars))) # Entropie: 6,555, Min: 100 Bit geg. BruteForce (BSI)
print("")
print("BSI Safety Standard: ")
print("")
print(''.join(secrets.choice(chars) for _ in range(16)))
print("")
print("Cryptographical Safety Standard: ")
print("")
print(''.join(secrets.choice(chars) for _ in range(40)))
print("")
print("Creation complete")