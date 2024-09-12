
import json
def decode_token(token_hex: str, full_key: bytes) -> str:
    try:
        token_bytes = bytes.fromhex(token_hex)
        decoded = ''
        for i, token_byte in enumerate(token_bytes):
            key_byte = full_key[i % len(full_key)]
            decoded += chr(token_byte ^ key_byte)
        print(f"Chuỗi đã giải mã: {decoded}")
        userinfo = json.loads(decoded)
        return userinfo
    except Exception as e:
        print(f"Error decoding token: {e}")
        return None


def encode_token(userinfo: dict, full_key: bytes) -> str:
    try:
        plaintext = json.dumps(userinfo).encode()
        out = b''
        for i, j in zip(plaintext, full_key):
            out += bytes([i ^ j])
        return out.hex()
    except Exception as e:
        print(f"Error encoding token: {e}")
        return None


if __name__ == "__main__":
    token_hex = "48674c3731025651282f614a4d54173609511c456e4141131e441918352b40515d194f1023261116534754783a19165a7b6e7b14"
    full_key = b'3E9DTp80EJCpmvvRd8rgBacww7itTR3sg9mqGKxxqktZOprxANJi'
    userinfo = decode_token(token_hex, full_key)

    if userinfo:
        print(f"Thông tin người dùng ban đầu: {userinfo}")
        userinfo['uid'] = 0
        print(f"Thông tin người dùng sau khi thay đổi uid: {userinfo}")
        new_token = encode_token(userinfo, full_key)
        print(f"Token mới sau khi thay đổi uid: {new_token}")
