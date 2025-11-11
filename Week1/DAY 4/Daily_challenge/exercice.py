
MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

rows = MATRIX_STR.strip().split('\n')
matrix = [list(row) for row in rows]
print(matrix)

num_rows = len(matrix)
num_cols = len(matrix[0])
decoded_message = ""

for col in range(num_cols):
    for row in range(num_rows):
        decoded_message += matrix[row][col]

print("Decoded message:", decoded_message)

# Step 3 & 4: Filter alpha and replace symbols with spaces
final_message = ""
in_word = False

for char in decoded_message:
    if char.isalpha():
        final_message += char
        in_word = True
    else:
        if in_word and (final_message[-1] != ' '):
            final_message += " "
        in_word = False

final_message = ' '.join(final_message.split())


print(f"final message :{final_message}")

 