# This is our simple Python program

def get_greeting():
    return "Hello from my GitHub Action! 👋"

message = get_greeting()
print(message) # This will print the message

# Let's add a very simple "test"
# This checks if our message is what we expect.
if message == "Hello from my GitHub Action! 👋":
    print("Yay! The test passed. The message is correct!")
    # exit(0) tells the computer that everything went well (success)
else:
    print("Oh no! The test failed. The message is different.")
    # exit(1) tells the computer that something went wrong (failure)
