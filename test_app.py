# test_app.py
# This is our script for testing app.py

# 'import app' allows us to use the get_greeting function from app.py
import app

def test_greeting_output():
    print("--- Starting Test: Greeting Message ---")
    # What message do we expect from app.py's get_greeting function?
    # Make sure this matches exactly what's in app.py!
    expected_message = "GitHub Actions is super cool! ✨"

    actual_message = app.get_greeting()
    print(f"Expected: '{expected_message}'")
    print(f"Got: '{actual_message}'")

    # 'assert' is a Python keyword that checks if something is True.
    # If it's False, it will raise an error and stop the script,
    # which tells GitHub Actions that the test failed!
    assert actual_message == expected_message, f"Test Failed! Expected '{expected_message}', but got '{actual_message}'"

    print("Test Passed! The greeting message is correct.")
    print("--------------------------------------")

# You could add more test functions here later if you want, like:
# def test_another_thing():
#     assert 1 + 1 == 2
#     print("Test Passed! 1+1 is 2")

# This part runs our test function(s) when we execute "python test_app.py"
if __name__ == "__main__":
    test_greeting_output()
    # If you add more test functions, call them here too:
    # test_another_thing()

    print("\nAll tests in test_app.py have finished.")
