import re

# Define the regex pattern
pattern = re.compile(r'\s+|[()+\-*/=<>{};]|[a-zA-Z_]\w*|\d+\.\d*|\.\d+|\d+(\.\d*)?[eE][+\-]?\d+|\.')

# Input code
input_code = """
void main ()
{
int sum = 0;
for(int j=0; j < 10; j=j+1)
{
sum = sum + j + 10.43 + 34E4 + 45.34E-4 + E43 + .34;
}
}
"""

# Find all matches
matches = pattern.findall(input_code)

# Print tokens
print("Class : Lexeme")
for match in matches:
    print(f"{match}")

