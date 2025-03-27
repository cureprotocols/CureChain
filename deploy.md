# 🚀 CureChain Deployment Guide

This guide walks contributors through deploying the CureChain protocol library app using **Streamlit Cloud**.

---

## 🧱 Requirements

- GitHub account  
- Streamlit Cloud account (free)  
- Basic knowledge of Python and Git

---

## 📁 Project Structure (Quick Overview)

```
CureChain/
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
├── deploy.md
├── curechain_manifesto.md
├── protocols/
│   └── influx_core.json
├── pages/
│   ├── protocol_viewer.py
│   └── submit_protocol.py
└── .streamlit/
    └── config.toml
```

---

## 🌐 Deployment Steps (Streamlit Cloud)

1. **Push to GitHub**
   - Ensure all files are committed

2. **Go to:** [https://share.streamlit.io](https://share.streamlit.io)

3. **Click “New app”**
   - Choose your GitHub repo
   - Set the main file to: `app.py`
   - Click **Deploy**

4. ✅ Your CureChain instance will go live at:
```
https://<your-username>-<repo-name>.streamlit.app
```

---

## 🔧 Contributor Notes

- Protocols live in `/protocols` as `.json` files  
- New protocols can be added via UI or GitHub  
- Follow CureChain schema: `meta`, `methods`, `results`, etc.

---

## 🧬 License & Ethos

This project follows the **CureCommons Ethic** —  
No patents. No gatekeeping. Full cultural respect.

Please read `curechain_manifesto.md` and `README.md` before contributing.

---

🧬 *Built by sovereign minds. For humanity.*
```

---
