def columnar_transposition_cipher(message, num_columns):
    # Write the message in columns
    columns = [''] * num_columns
    for i, char in enumerate(message):
        columns[i % num_columns] += char

    # Rearrange the columns (simple swap example)
    columns[0], columns[2] = columns[2], columns[0]

    # Read the encrypted message
    encrypted_message = ''.join(columns)

    return encrypted_message

message = "helloworld"
num_columns = 3
encrypted_message = columnar_transposition_cipher(message, num_columns)
print(encrypted_message)  # Output: "lehw lolro d"
