# Form Test Cases

## Module Information

- **Module:** Form Input
- **Test Type:** Functional Testing
- **Automation Tool:** Selenium WebDriver
- **Language:** Python
- **Browser:** Google Chrome

---

# Test Scenario

**Scenario ID:** TS002

**Scenario Name:** Form Input Verification

**Description**

Verify that users can enter data into the Username and Password fields correctly.

---

# Test Case 1

## TC001 - Username Input

### Objective

Verify that the Username field accepts user input correctly.

### Preconditions

- Chrome browser is installed.
- Selenium WebDriver is configured.
- Login page is accessible.

### Test Data

| Field | Value |
|------|------|
| Username | 測試帳號 |

### Test Steps

1. Open the Login page.
2. Locate the Username input field.
3. Enter "測試帳號".
4. Read the value from the input field.

### Expected Result

The Username field should contain "測試帳號".

### Actual Result

The Username field contains "測試帳號".

### Status

✅ PASS

### Screenshot

screenshots/form_username.png

---

# Test Case 2

## TC002 - Password Input

### Objective

Verify that the Password field accepts user input correctly.

### Preconditions

Login page is opened.

### Test Data

| Field | Value |
|------|------|
| Password | 123456 |

### Test Steps

1. Locate the Password input field.
2. Enter "123456".
3. Read the value from the Password field.

### Expected Result

The Password field should contain "123456".

### Actual Result

The Password field contains "123456".

### Status

✅ PASS

### Screenshot

screenshots/form_password.png

---

# Test Case 3

## TC003 - Form Input Validation

### Objective

Verify that the entered Username and Password values match the expected values.

### Test Steps

1. Enter Username.
2. Enter Password.
3. Read both input values.
4. Compare the values using assertions.

### Expected Result

Both assertions pass successfully.

### Actual Result

Assertions passed.

### Status

✅ PASS

### Screenshot

screenshots/form_assertion.png

---

# Test Summary

| Test Case | Result |
|-----------|--------|
| TC001 | ✅ PASS |
| TC002 | ✅ PASS |
| TC003 | ✅ PASS |

---

# Conclusion

The Username and Password input fields accept data correctly. The entered values match the expected values, and all assertions passed successfully.