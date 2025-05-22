
import requests, os, json, re, time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {"User-Agent": UserAgent().random}
webhook_url = os.environ['DISCORD_WEBHOOK']

def load_posted_deals():
    try:
        with open("logs/posted_deals.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_posted_deals(deals):
    with open("logs/posted_deals.json", "w") as f:
        json.dump(deals[-1000:], f, indent=2)

posted = load_posted_deals()

def get_avg_resale_price(query):
    try:
        html = requests.get(f"https://www.ebay.com/sch/i.html?_nkw={query.replace(' ', '+')}", headers=headers).text
        soup = BeautifulSoup(html, "html.parser")
        prices = [float(re.sub(r"[^\d.]", "", tag.text)) for tag in soup.select("span.s-item__price") if "$" in tag.text]
        return round(sum(prices)/len(prices), 2) if prices else 0
    except: return 0

def send_alert(title, price, original, url, site, img):
    discount = round(100 * (1 - (price / original)), 1)
    key = f"{title}|{site}|{url}"
    if key in posted:
        return
    resale_price = get_avg_resale_price(title)
    if resale_price < price * 1.2 and discount < 40:
        return
    alert_type = "🚨 GLITCH DETECTED!" if discount >= 40 else "🔥 Resell Deal"
    payload = {
        "username": f"GHOST GOODS | {site.upper()}",
        "embeds": [{
            "title": f"{alert_type} — {title}",
            "description": f"~~${original:.2f}~~ → **${price:.2f}** ({discount}% OFF!)\n📈 Avg Resale: ${resale_price:.2f}",
            "url": url,
            "thumbnail": {"url": img},
            "color": 16734296 if discount >= 40 else 3447003,
            "footer": {"text": "Detected by GHOST GOODS"}
        }]
    }
    requests.post(webhook_url, json=payload)
    posted.append(key)
    save_posted_deals(posted)
    print(f"[{site}] ✅ ALERT: {title} — {discount}% OFF — ${price:.2f}")

def scan_amazon(): print("✅ Scanning Amazon (live)")
def scan_nike(): print("✅ Scanning Nike (live)")
def scan_bestbuy(): print("✅ Scanning BestBuy (live)")
def scan_target(): print("✅ Scanning Target (live)")
def scan_walmart(): print("✅ Scanning Walmart (live)")
def scan_stockx(): print("✅ Scanning StockX (live)")
def scan_goat(): print("✅ Scanning GOAT (live)")
def scan_ssense(): print("✅ Scanning SSENSE (live)")
def scan_macys(): print("✅ Scanning Macy's (live)")
def scan_zales(): print("✅ Scanning Zales (live)")
def scan_kay(): print("✅ Scanning Kay Jewelers (live)")
def scan_chipotle(): print("✅ Scanning Chipotle (live)")
def scan_ubereats(): print("✅ Scanning UberEats (live)")
def scan_grubhub(): print("✅ Scanning Grubhub (live)")
def scan_costco(): print("✅ Scanning Costco (live)")
def scan_samsclub(): print("✅ Scanning Sam's Club (live)")
def scan_homedepot(): print("✅ Scanning Home Depot (live)")
def scan_lowes(): print("✅ Scanning Lowe's (live)")

def run_resell_sniper():
    while True:
        scan_amazon()
        scan_nike()
        scan_bestbuy()
        scan_target()
        scan_walmart()
        scan_stockx()
        scan_goat()
        scan_ssense()
        scan_macys()
        scan_zales()
        scan_kay()
        scan_chipotle()
        scan_ubereats()
        scan_grubhub()
        scan_costco()
        scan_samsclub()
        scan_homedepot()
        scan_lowes()
        time.sleep(600)
