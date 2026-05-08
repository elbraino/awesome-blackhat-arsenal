"""
Scraper for Black Hat Asia 2026 Arsenal schedule.

The 2026 page is rendered behind Cloudflare and populated by JS after a delay.
The `data-container` in the page source includes a Handlebars template plus
real entries — `find_elements` only returns the real (DOM) ones.
"""
import json
import os
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.blackhat.com/asia-26/arsenal/schedule/index.html"
EVENT_TAG = "BH-ASIA-26"
OUT = "Data/Asia/asia-26_arsenal_schedule_index.html.json"

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")


def make_driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument(f"--user-agent={UA}")
    opts.add_argument("--window-size=1400,2200")
    return webdriver.Chrome(options=opts)


def text_or_none(el, css):
    try:
        return el.find_element(By.CSS_SELECTOR, css).text.strip()
    except Exception:
        return None


def parse_track(container):
    """Tracks are rendered as: '<strong>Track(s)</strong>: <icon> Name1[, <icon> Name2]'.
    Track names themselves can contain commas (e.g. 'AI, ML & Data Science'), so we
    split on the icon-div boundary, not on commas."""
    try:
        block = container.find_element(By.CSS_SELECTOR, ".arsenal-session-track")
    except Exception:
        return None
    inner = block.get_attribute("innerHTML")
    # Drop the "Track:" / "Tracks:" prefix
    inner = re.sub(r"<strong>Tracks?</strong>\s*:\s*", "", inner)
    # Each track is preceded by an icon div; segments after icons are track names.
    parts = re.split(r'<div\s+class="track_type_iconlist[^"]*"\s*[^>]*>\s*</div>', inner)
    names = []
    for p in parts:
        # Strip remaining HTML tags and decode &amp;
        text = re.sub(r"<[^>]+>", "", p).replace("&amp;", "&").strip().rstrip(",").strip()
        if text:
            names.append(text)
    return names or None


def parse_room(container):
    try:
        block = container.find_element(By.CSS_SELECTOR, ".arsenal-session-room")
    except Exception:
        return None
    return re.sub(r"^Location:\s*", "", block.text).strip() or None


def extract_basic(driver):
    containers = driver.find_elements(By.CSS_SELECTOR, "div.data-container")
    tools = []
    for c in containers:
        try:
            link = c.find_element(By.CSS_SELECTOR, "a.sd_link")
        except Exception:
            continue
        name = link.text.strip()
        tool_id = link.get_attribute("data-id")
        if not name or not tool_id or "{{" in name or "{{" in (tool_id or ""):
            continue  # skip Handlebars template node
        speakers = [s.text.strip() for s in c.find_elements(By.CSS_SELECTOR, "a.speaker_link") if s.text.strip()]
        tools.append({
            "tool_name": name,
            "tool_id": tool_id,
            "speakers": speakers or None,
            "tracks": parse_track(c),
            "skill_level": "All",
            "event": EVENT_TAG,
            "session_type": parse_room(c),
            "github_url": None,
            "description": None,
        })
    return tools


def enrich_descriptions(driver, tools):
    for tool in tools:
        tid = tool["tool_id"]
        try:
            link = driver.find_element(By.CSS_SELECTOR, f'a.sd_link[data-id="{tid}"]')
            driver.execute_script("arguments[0].scrollIntoView({block:'center'}); arguments[0].click();", link)
            desc_id = f"session_desc_{tid}"
            WebDriverWait(driver, 6).until(
                EC.presence_of_element_located((By.ID, desc_id))
            )
            try:
                el = driver.find_element(By.CSS_SELECTOR, f"#{desc_id} .description")
                tool["description"] = el.get_attribute("innerText").strip() or None
            except Exception:
                el = driver.find_element(By.ID, desc_id)
                tool["description"] = el.get_attribute("innerText").strip() or None
            # Close modal if any visible close button — otherwise next click handles
            try:
                close = driver.find_element(By.CSS_SELECTOR, ".session-view-wrapper .close, .session-view-wrapper button[aria-label='Close']")
                driver.execute_script("arguments[0].click();", close)
            except Exception:
                pass
        except Exception as e:
            print(f"  ⚠️  desc fail [{tid} / {tool['tool_name']}]: {e.__class__.__name__}")


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    driver = make_driver()
    try:
        driver.get(URL)
        # Wait for tools to actually appear
        for i in range(40):
            time.sleep(1)
            tools = extract_basic(driver)
            if tools:
                print(f"✅ Found {len(tools)} tools after {i+1}s")
                break
        else:
            print("❌ No tools found after 40s")
            return

        print("📝 Enriching descriptions...")
        enrich_descriptions(driver, tools)

        with open(OUT, "w", encoding="utf-8") as f:
            json.dump(tools, f, indent=2, ensure_ascii=False)
        print(f"💾 Saved {len(tools)} tools to {OUT}")
        # Quick stats
        with_desc = sum(1 for t in tools if t.get("description"))
        print(f"   Descriptions captured: {with_desc}/{len(tools)}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
