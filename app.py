import random
import string
from playwright.sync_api import sync_playwright
from flask import Flask, jsonify

#╔═══════════════════════════╗
#║                                            
#║    𝗖𝗼𝗽𝘆𝗿𝗶𝗴𝗵𝘁 © 𝟮𝟬𝟮𝟰 𝗬𝗨𝗩𝗥𝗔𝗝𝗠𝗢𝗗𝗭     
#║     𝗖𝗥𝗘𝗗𝗜𝗧: 𝐌𝐀𝐓𝐑𝐈𝐗 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑      
#║                                            
#╚═══════════════════════════╝

app = Flask(__name__)

def generate_name(length=6):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_number():
    return "86" + ''.join(random.choices(string.digits, k=8))

def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=6))
    return f"{username}@gmail.com"

def generate_username(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_password(length=12):
    password_characters = (
        string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()"
    )
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()"),
    ]
    password += random.choices(password_characters, k=length - 3)
    random.shuffle(password)
    return ''.join(password)

def fill_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        page.goto("https://dark-web.in/register.php")
        page.wait_for_timeout(2000)

        name = generate_name()
        number = generate_number()
        email = generate_email()
        username = generate_username()
        password = generate_password()

        page.fill("#NewName", name)
        page.fill("#NewNumber", number)
        page.fill("#NewEmail", email)
        page.fill("#NewUserName", username)
        page.fill("#dlab-password", password)

        page.click("#SubForm")
        page.wait_for_timeout(5000)

        browser.close()
        
        return {"email": email, "password": password}

@app.route('/start-action', methods=['GET'])
def start_action():
    result = fill_form()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5014)
