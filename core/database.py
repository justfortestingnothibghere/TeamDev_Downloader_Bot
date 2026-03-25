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

import os
from datetime import datetime, date
from pymongo import MongoClient, DESCENDING
from pymongo.collection import Collection
from dotenv import load_dotenv

load_dotenv()

_MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://teamdevmail_db_user:CXVZnWuZgf55xVO8@cluster0.6xywr7u.mongodb.net/?appName=Cluster0")
_DB_NAME   = os.getenv("MONGO_DB",  "teamdev_downbot")

_client: MongoClient | None = None


def _get_client() -> MongoClient:
    global _client
    if _client is None:
        _client = MongoClient(_MONGO_URI, serverSelectionTimeoutMS=5000)
    return _client


def get_db():
    return _get_client()[_DB_NAME]


def _users()    -> Collection: return get_db()["users"]
def _logs()     -> Collection: return get_db()["download_logs"]
def _ads()      -> Collection: return get_db()["ads"]
def _settings() -> Collection: return get_db()["settings"]


def init_db():
    _users().create_index("telegram_id", unique=True)
    _logs().create_index("telegram_id")
    _logs().create_index("date")
    _ads().create_index("is_active")
    _settings().create_index("key", unique=True)

def get_or_create_user(telegram_id: int, first_name: str = "",
                       username: str = "") -> dict:
    col  = _users()
    user = col.find_one({"telegram_id": telegram_id})
    if not user:
        user = {
            "telegram_id":     telegram_id,
            "first_name":      first_name,
            "username":        username,
            "language":        "en",
            "is_premium":      False,
            "referral_points": 0,
            "referred_by":     None,
            "warn_count":      0,
            "is_banned":       False,
            "created_at":      datetime.utcnow(),
        }
        col.insert_one(user)
        user = col.find_one({"telegram_id": telegram_id})
    else:
        col.update_one(
            {"telegram_id": telegram_id},
            {"$set": {"first_name": first_name, "username": username}},
        )
        user = col.find_one({"telegram_id": telegram_id})
    return user


def get_user(telegram_id: int) -> dict | None:
    return _users().find_one({"telegram_id": telegram_id})


def update_user(telegram_id: int, **fields):
    _users().update_one({"telegram_id": telegram_id}, {"$set": fields})


def get_user_lang(telegram_id: int) -> str:
    u = _users().find_one({"telegram_id": telegram_id}, {"language": 1})
    return u.get("language", "en") if u else "en"


def count_all_users() -> int:
    return _users().count_documents({})


def count_premium_users() -> int:
    return _users().count_documents({"is_premium": True})


def get_all_users() -> list[dict]:
    return list(_users().find({}, {"telegram_id": 1, "language": 1}))

def log_download(telegram_id: int, platform: str, url: str):
    _logs().insert_one({
        "telegram_id": telegram_id,
        "platform":    platform,
        "url":         url,
        "date":        date.today().isoformat(),
        "created_at":  datetime.utcnow(),
    })


def count_downloads_today(telegram_id: int) -> int:
    today = date.today().isoformat()
    return _logs().count_documents({"telegram_id": telegram_id, "date": today})


def count_all_downloads() -> int:
    return _logs().count_documents({})


def count_downloads_since(since_date: str) -> int:
    return _logs().count_documents({"date": {"$gte": since_date}})


def count_downloads_today_all() -> int:
    return _logs().count_documents({"date": date.today().isoformat()})


def get_platform_stats() -> list[dict]:
    pipeline = [
        {"$group": {"_id": "$platform", "count": {"$sum": 1}}},
        {"$sort": {"count": DESCENDING}},
    ]
    return list(_logs().aggregate(pipeline))


def get_recent_logs(limit: int = 10) -> list[dict]:
    return list(_logs().find().sort("created_at", DESCENDING).limit(limit))


def create_ad(ad_type: str, content: str, photo_url: str | None,
              btn_text: str | None, btn_url: str | None) -> dict:
    doc = {
        "ad_type":     ad_type,
        "content":     content,
        "photo_url":   photo_url,
        "button_text": btn_text,
        "button_url":  btn_url,
        "is_active":   True,
        "created_at":  datetime.utcnow(),
    }
    result = _ads().insert_one(doc)
    return _ads().find_one({"_id": result.inserted_id})


def get_active_ad() -> dict | None:
    pipeline = [{"$match": {"is_active": True}}, {"$sample": {"size": 1}}]
    results  = list(_ads().aggregate(pipeline))
    return results[0] if results else None


def get_all_ads() -> list[dict]:
    return list(_ads().find().sort("created_at", DESCENDING))


def set_ad_active(ad_id, active: bool):
    from bson import ObjectId
    _ads().update_one({"_id": ObjectId(ad_id)}, {"$set": {"is_active": active}})


def delete_ad(ad_id):
    from bson import ObjectId
    _ads().delete_one({"_id": ObjectId(ad_id)})

def get_setting(key: str, default: str = "") -> str:
    doc = _settings().find_one({"key": key})
    return doc["value"] if doc else default


def set_setting(key: str, value: str):
    _settings().update_one(
        {"key": key},
        {"$set": {"key": key, "value": value}},
        upsert=True,
    )
