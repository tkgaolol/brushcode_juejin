def solution(rawStr, encodedStr):
    # Base32 index-character mapping
    index_to_char = "9876543210mnbvcxzasdfghjklpoiuyt"
    char_to_index = {char: index for index, char in enumerate(index_to_char)}

    def encode_base32(s):
        # Convert string to binary
        binary = ''.join(f'{ord(c):08b}' for c in s)
        # Pad binary to be a multiple of 5
        while len(binary) % 5 != 0:
            binary += '0'
        # Convert to Base32
        encoded = ''.join(index_to_char[int(binary[i:i+5], 2)]
                          for i in range(0, len(binary), 5))
        # Add padding based on the original bit length
        original_bit_length = len(s) * 8
        remainder = original_bit_length % 40
        if remainder == 8:
            encoded += '++++++'
        elif remainder == 16:
            encoded += '++++'
        elif remainder == 24:
            encoded += '+++'
        elif remainder == 32:
            encoded += '+'
        return encoded

    def decode_base32(s):
        # Remove padding
        s = s.rstrip('+')
        # Convert to binary
        binary = ''.join(f'{char_to_index[c]:05b}' for c in s)
        # Calculate the number of valid bits
        valid_bits = (len(s) * 5) - (len(s) % 8)
        # Convert binary to string using only valid bits
        decoded = ''.join(chr(int(binary[i:i+8], 2))
                          for i in range(0, valid_bits, 8))
        return decoded

    # Encode rawStr
    encoded_raw = encode_base32(rawStr)
    # Decode encodedStr
    decoded_encoded = ''.join(decode_base32(part)
                              for part in encodedStr.split('+++'))

    return f"{encoded_raw}:{decoded_encoded}"


if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("foo", "b0zj5+++") == "bljhy+++:bar")
    print(solution("The encoding process", "bljhy+++b0zj5+++")
          == "maf3m164vlahyl60vlds9i6svuahmiod:foobar")
    print(solution("Base32 encoding and decoding", "bvchz+++v4j21+++cals9+++")
          == "10zj3l0d31z3mod6vus3sod258zhil89bash3oo5v4j3c+++:c]hintts ")
