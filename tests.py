
import pytest

# Тест успешной авторизации
@pytest.mark.parametrize("email, password, expected", [
    ("valid@example.com", "CorrectPass1", True),
    ("invalid@example.com", "CorrectPass1", False),
    ("valid@example.com", "WrongPass", False),
])
def test_login(email, password, expected):
    def login(email, password):
        if email == "valid@example.com" and password == "CorrectPass1":
            return True
        return False
    result = login(email, password)
    assert result == expected


# Тест длины пароля
@pytest.mark.parametrize("password, expected", [
    ("1234567", False),
    ("12345678", True),
    ("LongPassword123", True),
])
def test_password_length(password, expected):
    def validate_password(password):
        return len(password) >= 8
    result = validate_password(password)
    assert result == expected


# Тест восстановления пароля
@pytest.mark.parametrize("contact, code_sent", [
    ("valid@example.com", True),
    ("invalid_email", False),
    ("+1234567890", True),
])
def test_password_recovery(contact, code_sent):
    def send_recovery_code(contact):
        if "@" in contact or contact.startswith("+"):
            return True
        return False
    result = send_recovery_code(contact)
    assert result == code_sent


# Тест уникальности email
@pytest.mark.parametrize("email, is_unique", [
    ("unique@example.com", True),
    ("existing@example.com", False),
])
def test_email_uniqueness(email, is_unique):
    existing_emails = ["existing@example.com"]
    def check_email_unique(email):
        return email not in existing_emails
    result = check_email_unique(email)
    assert result == is_unique


# Тест уникальности телефона
@pytest.mark.parametrize("phone, is_unique", [
    ("+1234567890", True),
    ("+9876543210", False),
])
def test_phone_uniqueness(phone, is_unique):
    existing_phones = ["+9876543210"]
    def check_phone_unique(phone):
        return phone not in existing_phones
    result = check_phone_unique(phone)
    assert result == is_unique


# Тест авторизации с временным кодом
@pytest.mark.parametrize("code, valid", [
    ("123456", True),
    ("654321", False),
])
def test_temp_code_authentication(code, valid):
    valid_code = "123456"
    def authenticate_with_code(code):
        return code == valid_code
    result = authenticate_with_code(code)
    assert result == valid


# Тест регистрации с некорректным email
@pytest.mark.parametrize("email, valid", [
    ("user@domain.com", True),
    ("userdomain.com", False),
    ("user@.com", False),
])
def test_registration_email(email, valid):
    def validate_email(email):
        return "@" in email and "." in email.split("@")[-1]
    result = validate_email(email)
    assert result == valid


# Тест проверки сложности пароля
@pytest.mark.parametrize("password, valid", [
    ("Password1", True),
    ("password", False),
    ("12345678", False),
    ("Pass1234", True),
])
def test_password_complexity(password, valid):
    def validate_password_complexity(password):
        return (
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password)
        )
    result = validate_password_complexity(password)
    assert result == valid


# Тест отображения ошибки при неверном коде восстановления
@pytest.mark.parametrize("input_code, expected_message", [
    ("000000", "Invalid code"),
    ("654321", "Invalid code"),
    ("123456", "Success"),
])
def test_recovery_code_error(input_code, expected_message):
    valid_code = "123456"
    def verify_code(input_code):
        if input_code == valid_code:
            return "Success"
        return "Invalid code"
    result = verify_code(input_code)
    assert result == expected_message


# Тест проверки пустых полей
@pytest.mark.parametrize("email, password, valid", [
    ("", "Password123", False),
    ("user@example.com", "", False),
    ("", "", False),
    ("user@example.com", "Password123", True),
])
def test_empty_fields(email, password, valid):
    def validate_fields(email, password):
        return bool(email and password)
    result = validate_fields(email, password)
    assert result == valid


# Тест для проверки подтверждения пароля при регистрации
@pytest.mark.parametrize("password, confirm_password, match", [
    ("Password123", "Password123", True),
    ("Password123", "password123", False),
    ("Password123", "Password", False),
])
def test_password_confirmation(password, confirm_password, match):
    def passwords_match(password, confirm_password):
        return password == confirm_password
    result = passwords_match(password, confirm_password)
    assert result == match

# Тест авторизации с неправильными данными
@pytest.mark.parametrize("email, password, expected", [
    ("notexist@example.com", "WrongPass", False),
    ("", "SomePass", False),
    ("valid@example.com", "", False),
])
def test_invalid_login(email, password, expected):
    def login(email, password):
        if email == "valid@example.com" and password == "CorrectPass1":
            return True
        return False
    result = login(email, password)
    assert result == expected


# Тест авторизации с невалидным email
@pytest.mark.parametrize("email, expected", [
    ("invalidemail", False),
    ("user@domain", False),
    ("valid@example.com", True),
])
def test_email_format(email, expected):
    def validate_email(email):
        return "@" in email and "." in email.split("@")[-1]
    result = validate_email(email)
    assert result == expected


# Тест ограничения длины пароля
@pytest.mark.parametrize("password, valid", [
    ("short", False),  # Меньше 8 символов
    ("exactly8", True),  # Ровно 8 символов
    ("thisisaverylongpassword", True),  # Длинный пароль
])
def test_password_length_validation(password, valid):
    def validate_password_length(password):
        return len(password) >= 8
    result = validate_password_length(password)
    assert result == valid


# Тест регистрации с пустыми полями
@pytest.mark.parametrize("email, password, confirm_password, valid", [
    ("", "Password123", "Password123", False),
    ("user@example.com", "", "Password123", False),
    ("user@example.com", "Password123", "", False),
    ("user@example.com", "Password123", "Password123", True),
])
def test_registration_empty_fields(email, password, confirm_password, valid):
    def validate_registration(email, password, confirm_password):
        return email and password and confirm_password and password == confirm_password
    result = validate_registration(email, password, confirm_password)
    assert result == valid


# Тест успешного редиректа после авторизации
def test_redirect_after_login():
    def login_and_redirect():
        # Эмуляция успешной авторизации
        return "/dashboard"
    result = login_and_redirect()
    assert result == "/dashboard"


# Тест восстановления пароля с неверным телефоном
@pytest.mark.parametrize("phone, valid", [
    ("+1234567890", True),
    ("+0000000000", False),
    ("123456", False),
])
def test_password_recovery_phone(phone, valid):
    def validate_phone(phone):
        return phone.startswith("+") and len(phone) == 12
    result = validate_phone(phone)
    assert result == valid


# Тест авторизации через разные учетные данные
@pytest.mark.parametrize("credential_type, value, valid", [
    ("email", "valid@example.com", True),
    ("email", "invalidemail", False),
    ("phone", "+1234567890", True),
    ("phone", "123456", False),
])
def test_login_with_various_credentials(credential_type, value, valid):
    def validate_credential(credential_type, value):
        if credential_type == "email":
            return "@" in value and "." in value.split("@")[-1]
        elif credential_type == "phone":
            return value.startswith("+") and len(value) == 12
        return False
    result = validate_credential(credential_type, value)
    assert result == valid


# Тест проверки блокировки после 3 неправильных попыток авторизации
def test_account_lock_after_failed_attempts():
    def simulate_login_attempts(attempts):
        max_attempts = 3
        if attempts > max_attempts:
            return "Locked"
        return "Allowed"
    result = simulate_login_attempts(4)
    assert result == "Locked"


# Тест для проверки поля "Регион" при регистрации
@pytest.mark.parametrize("region, valid", [
    ("Москва", True),
    ("", False),
    ("UnknownRegion", False),
])
def test_region_field_validation(region, valid):
    def validate_region(region):
        allowed_regions = ["Москва", "Санкт-Петербург", "Новосибирск"]
        return region in allowed_regions
    result = validate_region(region)
    assert result == valid


# Тест отображения ошибки при совпадении пароля с тремя предыдущими
@pytest.mark.parametrize("password, previous_passwords, valid", [
    ("Password1", ["Password2", "Password3", "Password4"], True),
    ("Password1", ["Password1", "Password2", "Password3"], False),
])
def test_password_reuse(password, previous_passwords, valid):
    def check_password_reuse(password, previous_passwords):
        return password not in previous_passwords
    result = check_password_reuse(password, previous_passwords)
    assert result == valid
