# Yours Robotics - Follow & Unlock Robot 82

Interactive mobile landing page for **Yours Robotics**, featuring official social media channels:
- 📸 **Instagram**: [@yours_robotics](https://www.instagram.com/yours_robotics)
- 🎥 **YouTube**: [@YoursRobotics-q3I](https://www.youtube.com/@YoursRobotics-q3I)
- 💼 **LinkedIn**: [Yours Robotics](https://www.linkedin.com/company/105981796/)

---

## 🌐 Live Website (GitHub Pages)

👉 **[https://stafford-yours.github.io/Yours-Robotics-Link-Tree/](https://stafford-yours.github.io/Yours-Robotics-Link-Tree/)**

---

## 🤖 How the Lid Unlock Works

When a visitor scans the QR code on Robot 82 and taps any of the 3 social channels:
1. The webpage fires an asynchronous HTTPS request to the Yours cloud actuation gateway:
   ```http
   POST https://jp.yours.xyz/index.php/api/v1/merchant/robot/openGrid
   Content-Type: application/x-www-form-urlencoded

   robotid=4c5f6921115ae44a0f5c64cc952deba3&str=0&is_all=0
   ```
2. Robot 82's onboard service receives the MQTT signal and releases the compartment lock (`/yours_base/locks_ctrl`).
3. The page plays a sci-fi audio chime, vibrates the phone (haptics), displays an animated unlock confirmation modal, and opens the social profile.
4. An *"Already following? Open Robot Lid Now"* quick-action button is also provided.

---

## 📱 QR Code Assets

- **`robot82_qr_code.png`**: High-resolution print-ready display card with branding, robot ID (A0082), and scanning instructions.
- **`robot82_qr_code_raw.png`**: High-DPI clean square QR code for direct sticker printing or screen display.

### Re-generating QR Codes
```bash
python3 generate_qr.py --url "https://stafford-yours.github.io/Yours-Robotics-Link-Tree/"
```
