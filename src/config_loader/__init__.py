# src/config_loader/__init__.py
"""Configuration loader package."""

__version__ = "0.1.0"

from config_loader.core.loader import load_config, ConfigurationError

__all__ = ["load_config", "ConfigurationError"]