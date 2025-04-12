import sys
import io

#standart garalt
sys.stdout.write("This is standart out/n")

#standart aldaa
sys.stderr.write("This is error message")

#standart orolt
print("Write something and press Enter:")
user_input = sys.stdin.readline().strip()
print(f"You wrote: {user_input}")

#stout iig tur cigluleh
original_stout = sys.stdout
string.io = io.StringIO()
sys.stdout = string_io

print("This caught")
print("This one too")

sys.stdout = original_stout
captured_output = string_io.getvalue()
print(f"Caught: {captured_output}")