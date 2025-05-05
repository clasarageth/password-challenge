# password-challenge


## Overview

This project is designed to automatically find a 3-digit PIN by sending a series of POST requests to a local server. The process starts by identifying the correct server port, then building and sending requests with different PIN combinations. It checks the server's responses to see if a guess is correct, and carefully spaces out each attempt to avoid being blocked or rate-limited. The main logic is handled through a simple brute-force function that tries every possible PIN until it finds the right one.

## Flow of the Solution

### 1. Finding the Server Port

- Used `tasklist | findstr (file name)`
- Used `netstat -ano | findstr LISTENING`
- Match the PID found in the first command to the result in second command


### 2. Storing the Current PIN Guess

- Added a variable `pin_guess` to represent the current 3-digit PIN being tested.
- The PIN is formatted as a string with leading zeros using `f"{pin:03d}"`.


### 3. Creating Form Data for POST Request

- Built a `form_data` to send with each POST request to the server.


### 4. Decoding and Processing the Response

- After sending a request, the response is decoded 
- The content is scanned for success indicators like "Access Granted" or "Correct".
- If the PIN is correct, the process stops; otherwise, it continues to the next guess

### 5. Implemented `brute_force_pins()` Function

- Loop from 000 to 999
- For each PIN:
  - Send POST request with the PIN
  - Wait 1.1 seconds between attempts to avoid rate limiting
  - Stop if the correct PIN is found

```python
def brute_force_pins():
    for pin in range(1000):
        pin_guess = f"{pin:03d}"
        if send_post_request(pin_guess):
            print(f"Found correct PIN: {pin_guess}")
            break
        time.sleep(1.1)
```


