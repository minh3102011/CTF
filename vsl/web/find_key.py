def find_key(token_hex: str, known_plaintext: str, partial_key: bytes) -> bytes:
    token_bytes = bytes.fromhex(token_hex)
    key_guess = bytearray(partial_key)
    for i in range(len(partial_key), len(token_bytes)):
        token_byte = token_bytes[i]
        known_char = ord(known_plaintext[i % len(known_plaintext)])
        key_byte = token_byte ^ known_char
        key_guess.append(key_byte)

    return bytes(key_guess)


known_plaintext = '{"username": "admin", "displays": "admin", "uid": 1}'
token_hex = "48674c3731025651282f614a4d54173609511c456e4141131e441918352b40515d194f1023261116534754783a19165a7b6e7b14"
partial_key = b'3E9DTp80EJCp'
full_key = find_key(token_hex, known_plaintext, partial_key)
print(full_key)
