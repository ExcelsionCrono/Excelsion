# Lost Ark PvP Mobility Calculator

This Python tool compares the **mobility potential of different classes in Lost Ark PvP**, specifically focused on 10–15 second skirmishes. It's designed for high-level players who want to understand who can outmaneuver whom.

## ⚙️ Formula
Each skill:
Mobility Score = (Uses/sec) × Distance × Flexibility
Class Score:
Weighted Score = Base Score × √(Number of Skills)

## 💡 Features
- Per-skill and per-class scoring
- Normalized 0–100 mobility ratings
- Based on 150 ms reaction time

## 📥 Example Usage

```bash
python mobility_calculator.py

📜 License
MIT License – Free to use, modify, and share.
