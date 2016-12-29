# -*- coding: utf-8 -*-
"""
Image booru related models.
"""
from sibooru.model import DeclarativeBase, metadata, DBSession
from sqlalchemy import Integer, Column, String, Text, Boolean, DateTime


class Vote(DeclarativeBase):
    """Represents a users vote on an image, whether up or down"""
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)

    # true: upvote, false: downvote
    direction = Column(Boolean, nullable=False)

    # > user


class Favorite(DeclarativeBase):
    """Represents a favorite on an image"""
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)

    # > user


class Tag(DeclarativeBase):
    """Represents an image tag"""
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    short_description = Column(Text, nullable=False)
    # Spoiler image url
    # System
    # aliased to?


class Image(DeclarativeBase):
    """Represents an image on the site"""
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    source_url = Column(String(2000), nullable=False)
    image_format = Column(String(16), nullable=False)
    sha512 = Column(String(128), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    # < duplicate reports
    # > uploader
