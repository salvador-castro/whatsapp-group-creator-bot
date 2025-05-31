# WhatsApp Group Creator Bot 🤖📱

Automate the creation of WhatsApp groups using Selenium and a list of group names stored in a CSV file.
This script simulates human interaction in WhatsApp Web through Google Chrome to create groups at scale.

## 🚀 Features

* Creates multiple WhatsApp groups from a CSV file
* Adds a specific contact to each group (e.g. "Mio Uruguay")
* Works with Google Chrome for Testing
* Built with Selenium WebDriver and Python
* Compatible with macOS (tested on M1/M2)

## 📁 CSV Format

The script reads a file named `grupos_a_crear.csv` with the following structure:

```csv
group_name
AM1 - V1001
AM1 - V1002
AM1 - V1003
...
```

Each line creates a new group with the specified name and adds the contact **"Mio Uruguay"**.

## 🛠 Requirements

* Python 3.8+
* Google Chrome for Testing (ARM64 or x86)
* [ChromeDriver](https://sites.google.com/chromium.org/driver/) matching your Chrome version
* Selenium library

Install Selenium:

```bash
pip install selenium
```

## 💻 How to Use

1. Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/your-username/whatsapp-group-creator-bot.git
cd whatsapp-group-creator-bot
```

2. Edit the `grupos_a_crear.csv` file with your group names.

3. Update the script if needed:

   * Path to your `chromedriver`
   * Path to Chrome binary
   * Profile directory if different

4. Run the script:

```bash
python whatsapp.py
```

5. Scan the QR code with your phone when prompted.

6. Let the bot create the groups. Sit back and relax ☕.

## ⚠️ Warnings

* Do not abuse automation on WhatsApp. Creating too many groups too fast might flag your account.
* This script is intended for educational or internal organizational use.
* WhatsApp Web layout may change. If it breaks, update the XPATHs accordingly.

## 📷 Screenshot

![demo](docs/demo-screenshot.png)

## 📄 License

This project is licensed under the MIT License.
