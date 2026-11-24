import os

os.makedirs("/output", exist_ok=True)
label = "WARNING: Human will lie to itself, then believe the lie so completely that it files a complaint against reality."
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(label)
