"""Configuration and Settings Manager for Acupuncture Study App.

Handles persistent storage of API keys, model preferences, and app settings
in both data/settings.json and .env so keys survive app restarts and reboots.
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional

try:
    import dotenv
    HAS_DOTENV = True
except ImportError:
    HAS_DOTENV = False

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SETTINGS_FILE = DATA_DIR / "settings.json"
ENV_FILE = BASE_DIR / ".env"

# Ensure data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)


def init_settings():
    """Load settings from .env and settings.json at startup and populate os.environ."""
    # 1. Load .env if present
    if ENV_FILE.exists() and HAS_DOTENV:
        dotenv.load_dotenv(str(ENV_FILE), override=True)
        
    # 2. Load settings.json and ensure environment variables are synchronized
    settings = load_settings()
    for key in ["GEMINI_API_KEY", "OPENAI_API_KEY"]:
        if key in settings and settings[key]:
            os.environ[key] = settings[key]
            
    return settings


def load_settings() -> Dict[str, Any]:
    """Read all saved settings from settings.json."""
    if not SETTINGS_FILE.exists():
        # Check if .env has keys to migrate
        initial_data = {}
        if ENV_FILE.exists() and HAS_DOTENV:
            env_vals = dotenv.dotenv_values(str(ENV_FILE))
            for k, v in env_vals.items():
                if v:
                    initial_data[k] = v
        if initial_data:
            save_all_settings(initial_data)
            return initial_data
        return {}
        
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_all_settings(settings: Dict[str, Any]) -> bool:
    """Save settings dictionary to settings.json and update .env."""
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2)
            
        # Also persist sensitive API keys to .env
        if not ENV_FILE.exists():
            ENV_FILE.touch()
            
        if HAS_DOTENV:
            for k in ["GEMINI_API_KEY", "OPENAI_API_KEY"]:
                if k in settings and settings[k]:
                    dotenv.set_key(str(ENV_FILE), k, str(settings[k]))
                elif k in settings and not settings[k]:
                    try:
                        dotenv.unset_key(str(ENV_FILE), k)
                    except Exception:
                        pass
        return True
    except Exception as e:
        print(f"Error saving settings: {e}")
        return False


def get_setting(key: str, default: str = "") -> str:
    """Get setting value from Streamlit secrets, environment, or settings.json."""
    # 1. Streamlit secrets (useful for Cloud deployments)
    try:
        import streamlit as st
        if hasattr(st, "secrets") and key in st.secrets:
            return str(st.secrets[key])
    except Exception:
        pass

    # 2. Environment variable has priority
    env_val = os.getenv(key)
    if env_val:
        return env_val
        
    settings = load_settings()
    return settings.get(key, default)


def save_setting(key: str, value: str) -> bool:
    """Save a single setting to both settings.json and .env."""
    clean_val = value.strip()
    settings = load_settings()
    settings[key] = clean_val
    os.environ[key] = clean_val
    return save_all_settings(settings)


def remove_setting(key: str) -> bool:
    """Remove a setting completely."""
    settings = load_settings()
    if key in settings:
        del settings[key]
    if key in os.environ:
        del os.environ[key]
    return save_all_settings(settings)


# Auto-run initialization on module import
init_settings()
