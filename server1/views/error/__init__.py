"""Provides error handlers
"""
from .client import handle404

handlers = [
    (404, handle404)
]
