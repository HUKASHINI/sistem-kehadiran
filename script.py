import os

fail_html = "index.html"

if os.path.exists(fail_html):
    with open(fail_html, "r", encoding="utf-8") as f:
        kandungan = f.read()
        if "alert(" in kandungan:
            print("✅ Fail HTML wujud dan fungsi alert() dijumpai.")
        else:
            print("❌ Fungsi alert() tidak dijumpai dalam HTML.")
else:
    print("❌ Fail index.html tidak wujud.")
