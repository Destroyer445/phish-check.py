# Phish-Check Tool - Created for DESTROYER445
# Educational Purpose Only - Learn to Detect Phishing!

import re
from urllib.parse import urlparse

def banner():
    print("""
╔════════════════════════════════════╗
║ DESTROYER445 - PHISH-AWARENESS ║
║ Stay Safe | Detect Phishing ║
╚════════════════════════════════════╝
    """)

def check_url(url):
    print(f"\n[>] Checking: {url}\n")
    parsed = urlparse(url)
    score = 0
    risks = []

    # 1. HTTPS check
    if parsed.scheme!= "https":
        risks.append("⚠️ HTTPS illa - http aanu, safe alla!")
        score += 2
    else:
        print("✅ HTTPS undu - good sign")

    # 2. IP address instead of domain
    if re.match(r"^\d+\.\d+\.\d+\.\d+$", parsed.netloc):
        risks.append("⚠️ Domain name illa, IP address aanu - 99% phish!")
        score += 3

    # 3. @ symbol
    if "@" in url:
        risks.append("⚠️ URL il @ undu - redirection trick!")
        score += 2

    # 4. Too long URL
    if len(url) > 75:
        risks.append("⚠️ URL valare long aanu - suspicious!")
        score += 1

    # 5. Misspelled popular domains
    suspicious = ["g00gle", "faceboook", "amaz0n", "paypaI", "micorsoft"]
    for s in suspicious:
        if s in url.lower():
            risks.append(f"⚠️ Fake spelling detected: {s}")
            score += 3

    print("\n--- RISKS FOUND ---")
    if not risks:
        print("✅ No obvious risks found! Still be careful machaa")
    else:
        for r in risks:
            print(r)

    print(f"\n[Risk Score: {score}/10]")
    if score >= 5:
        print("🔴 HIGH RISK - Click cheyyanda!")
    elif score >= 2:
        print("🟡 MEDIUM RISK - Sushichu nokku")
    else:
        print("🟢 LOW RISK - Paravayilla, but still alert aayirik")

    print("\n[Tip]: Real bank/company never asks OTP via link!")

if __name__ == "__main__":
    banner()
    url = input("URL enter cheyyu machaa: ").strip()
    if not url.startswith("http"):
        url = "http://" + url
    check_url(url)
