def create_user(name,email,phone,password):
    if not name or not email or not phone or not password:
        return "All fields are required"
    if "@" not in email:
        return "Invalid Email"
    if password < 6:
        return "Password is too short"
    return "User account created successfully"