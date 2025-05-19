# This is our simple Python program

def get_greeting():
    return "GitHub Actions is super cool! ✨"

# This part below means: "If this app.py file is run directly,
# then do the following." It won't run if another file (like our test file)
# just imports functions from here.

if __name__ == "__main__":
    message = get_greeting()
    print(f"Message from app.py: {message}")


'''
message = get_greeting()
print(message) # This will print the message

# Let's add a very simple "test"
# This checks if our message is what we expect.
if message == "GitHub Actions is super cool! ✨":
    print("Yay! The test passed. The message is correct!")
    # exit(0) tells the computer that everything went well (success)
else:
    print("Oh no! The test failed. The message is different.")
    # exit(1) tells the computer that something went wrong (failure)
'''
