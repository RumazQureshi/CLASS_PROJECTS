import streamlit as st
import random
import string
# import pyperclip
# page setting
st.set_page_config(page_icon="🔐",page_title="Password Strength Meter",layout="centered")
st.title("🔐🔑Passwrod Strength Meter")
# title 
password=st.text_input("Enter Your Password: ",placeholder="Enter Your Password",type="password")

# function to check password strength
def Strength_parameters(password):
# initial score
    score = 0
    # to not show anything until not write anything
    messages =[]

    # length
    if len(password)>=8:
        score += 1
        st.markdown(":green[✔ Your Password is of 8 characters]")
    else:
        st.markdown(":red[❌The Length Of Your Password Is Less Than **8** Digits]")

    # for characters in lower
    if any(char.islower() for char in password):
        score +=1
        st.markdown(":green[✔ Your Password has at least one lowercase letter]")
    else:
        st.markdown(":red[❌Your Password Should Have At Least **One Lowercase Letter**]")
        
    # for characters in upper
    if any(char.isupper() for char in password):
        score+=1
        st.markdown(":green[✔ Your Password has at least one uppercase letter]")
    else:
        st.markdown(":red[❌Your Password Should Have At Least **One Uppercase Letter**]")
        
    # for digit
    if any(char.isdigit() for char in password):
        score += 1
        st.markdown(":green[✔ Your Password has at least one digit]")
    else:
        st.markdown(":red[❌Your Password Should Have At Least **One Digit**]")
        
    # for special characters
    if any(char in "!@#$%^&*()_+-={}:<>?/" for char in password):
        score += 1
        st.markdown(":green[✔ Your Password has at least one special character]")
    else:
        st.markdown(":red[❌Your Password Should Have At Least **One Special Character**]")
        
# additonal chellanges

    Blacklisted_Passwords={"password123","admin","qwerty","12345678","welcome","admin123","asdf",'11111111', "00000000","0000","1234"}
    if password.lower() in Blacklisted_Passwords:
        st.error("🚨 This password is **too common!** Choose a stronger one.")
        return
    #  error and success upon score
    if score == 5:
        st.success("✅🔐Your Password Is Strong")
    elif score ==3 or score==4:
        st.warning("⚠ Moderate password - Improve It Using The Suggestions Above🔼")
    else:
        st.error("🚨Weak Password - Change It ASAP ")

# function call
if st.button("Check Password Strength"):
    Strength_parameters(password)

# Function to generate strong password
def generate_password(length=12):
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()_+-={}:<>?/")
    
    remaining_chars = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+-={}:<>?/", k=length - 4))

    password = list(upper + lower + digit + special + remaining_chars)
    random.shuffle(password)
    return ''.join(password)

# Button to generate password
if st.button("Generate Password"):
    st.session_state["generated_password"] = generate_password()  # Store in session state

# Display password if generated
if "generated_password" in st.session_state:
    password = st.session_state["generated_password"]
    # st.text_input("Generated Password:", password, disabled=True)
    st.code(password, language='text')

    # Copy Password Button
    # if st.button("📋 Copy Password"):
    #     pyperclip.copy(password)  # this will Copy password to clipboard
    #     st.success("✅ Password copied to clipboard!")

# my footer using html to center
st.markdown("---")
st.markdown(
    "<h4 style='text-align: center;'> Developed by <b>💻👨‍💻Rumaz Naveed Qureshi</b></h4>",
    unsafe_allow_html=True)