#!/usr/bin/python3
""" init for base models"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
