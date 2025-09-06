# 📶 PLDT WiFi Wordlist

⚠️ **Disclaimer**  
This project is provided **strictly for educational and authorized security testing purposes only**.  
- It must **only** be used in environments where you have **explicit permission** (e.g., your own network, lab setups, or client networks with written consent).  
- Unauthorized access to computer systems, WiFi networks, or accounts is **illegal** under the [Cybercrime Prevention Act of 2012 (RA 10175)](https://www.officialgazette.gov.ph/2012/09/12/republic-act-no-10175/).
- The author does **not condone or take responsibility** for any misuse of this material.  
- By using this project, you agree that **you are solely responsible** for your actions.  

This wordlist is intended as a **pentesting and red team resource** to help:  
- Identify weak/default credentials on WiFi routers.  
- Raise awareness of insecure configurations.  
- Support research in improving security practices.

---

This repository provides a custom **PLDT WiFi wordlist**.  
You can either **generate it yourself with Python 3** or **download the pre-made `.7z` file**.  

---

## 🔹 Option 1 — Generate with Python 3

1. Make sure you have **Python 3** installed:  
   ```bash
   python3 --version
   ```

2. Run the generator script:  
   ```bash
   python3 wordlistgenerator.py
   ```

3. This will create a file:  
   ```
   pldt_wordlist.txt
   ```

4. (Optional) Compress it to save space:  
   ```bash
   7z a pldt_wordlist.7z pldt_wordlist.txt
   ```

---

## 🔹 Option 2 — Download the Pre-made Wordlist

If you don’t want to generate it yourself:  

- Download the ready-to-use **compressed file**:  
  ```
  pldt_wordlist.7z
  ```

- Extract it:  
  ```bash
  7z x pldt_wordlist.7z
  ```

---

## 👨‍💻 Author

Created by **PWIMAWY**  
For security research and penetration testing awareness.

---

## ✅ Ethical Use Reminder

Use this wordlist only in lawful scenarios, such as:  
- Security assessments of your own PLDT WiFi router.  
- Pentesting labs or Capture The Flag (CTF) competitions.  
- Authorized penetration testing engagements.  

🚫 **Never use this tool for unauthorized access or malicious purposes.**  
Doing so may result in criminal liability under Philippine law.
