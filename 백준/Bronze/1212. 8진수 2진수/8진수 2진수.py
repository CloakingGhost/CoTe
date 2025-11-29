import sys

input = sys.stdin.readline

OCTAL_MAP = {
    '0': '000', '1': '001', '2': '010', '3': '011',
    '4': '100', '5': '101', '6': '110', '7': '111'
}
octal_str = input().rstrip()
full_binary = ''.join(OCTAL_MAP[digit] for digit in octal_str)
first_index = full_binary.find('1')

if first_index == -1:
    print(0)
else:
    print(full_binary[first_index:])