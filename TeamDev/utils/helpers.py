"""
           ───── ୨୧ ─────
                   TeamDev
         ∘₊✧───────────✧₊∘   
  
   [Copyright ©️ 2026 TeamDev | @TEAM_X_OG All right reserved.]

Project Name: All In One Downloader
Project Discription: Download From Multiple Platforms Video Such As Terabox, Youtube, instagram, and much more!
Project Number: 38
Project By: @MR_ARMAN_08 | @TEAM_X_OG

                   Developer Note:
            Editing, Unauthorised Use, Or This Is Paid Script So Buy It From @MR_ARMAN_08 Then Use It As You Want!
"""

import re
from datetime import timedelta


def format_duration(seconds: int) -> str:
    td    = timedelta(seconds=seconds)
    total = int(td.total_seconds())
    h, remainder = divmod(total, 3600)
    m, s = divmod(remainder, 60)
    if h:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def is_youtube_url(url: str) -> bool:
    patterns = [
        r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/",
        r"(https?://)?music\.youtube\.com/",
    ]
    return any(re.search(p, url) for p in patterns)


def is_instagram_url(url: str) -> bool:
    return bool(re.search(r"(https?://)?(www\.)?instagram\.com/", url))


def is_facebook_url(url: str) -> bool:
    return bool(re.search(r"(https?://)?(www\.)?(facebook\.com|fb\.watch)/", url))


def is_pinterest_url(url: str) -> bool:
    return bool(re.search(r"(https?://)?(www\.)?pinterest\.[a-z.]+/|pin\.it/", url))


def is_terabox_url(url: str) -> bool:
    _TB = (
        "terabox.com", "1024terabox.com", "teraboxapp.com",
        "terasharefile.com", "4funbox.com", "mirrobox.com",
        "nephobox.com", "freeterabox.com", "momerybox.com",
        "tibibox.com", "terabox.fun", "terabox.club",
        "terabox.link", "terabox.ws",
    )
    return any(d in url for d in _TB)


def is_spotify_url(url: str) -> bool:
    return bool(re.search(r"(https?://)?open\.spotify\.com/", url))


def is_twitter_url(url: str) -> bool:
    return bool(re.search(r"(https?://)?(www\.)?(twitter\.com|x\.com)/", url))


def is_tiktok_url(url: str) -> bool:
    return bool(re.search(r"(https?://)?(www\.|vm\.|vt\.)?tiktok\.com/", url))


def is_soundcloud_url(url: str) -> bool:
    return bool(re.search(r"(https?://)?(www\.)?soundcloud\.com/", url))


def is_vimeo_url(url: str) -> bool:
    return bool(re.search(r"(https?://)?(www\.)?(vimeo\.com|player\.vimeo\.com)/", url))

PLATFORM_META = {
    "youtube":    {"emoji": "•",  "label": "YouTube"},
    "instagram":  {"emoji": "🅾",  "label": "Instagram"},
    "facebook":   {"emoji": "ⓕ",  "label": "Facebook"},
    "pinterest":  {"emoji": "⚝",  "label": "Pinterest"},
    "twitter":    {"emoji": "𝕏",  "label": "Twitter / X"},
    "tiktok":     {"emoji": "【ꚠ】",  "label": "TikTok"},
    "soundcloud": {"emoji": "☁",  "label": "SoundCloud"},
    "terabox":    {"emoji": "•",  "label": "Terabox"},
    "vimeo":      {"emoji": "•",  "label": "Vimeo"},
    "spotify":    {"emoji": "(ᯤ)",  "label": "Spotify"},
}


def detect_platform(url: str) -> str | None:
    if is_youtube_url(url):     return "youtube"
    if is_instagram_url(url):   return "instagram"
    if is_facebook_url(url):    return "facebook"
    if is_pinterest_url(url):   return "pinterest"
    if is_twitter_url(url):     return "twitter"
    if is_tiktok_url(url):      return "tiktok"
    if is_soundcloud_url(url):  return "soundcloud"
    if is_terabox_url(url):     return "terabox"
    if is_vimeo_url(url):       return "vimeo"
    if is_spotify_url(url):     return "spotify"
    return None


def build_referral_link(bot_username: str, telegram_id: int) -> str:
    return f"https://t.me/{bot_username}?start=ref_{telegram_id}"
