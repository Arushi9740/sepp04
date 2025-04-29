from user import create_user

def test_case():
    assert create_user('"abc"',"abc@gmail.com","9036046474",5263965) == "User account created successfully"

def test_case_invalid():
    assert create_user("def","def@gmail.com","88840103",123) == "Password is too short"

print("Test passed")

