# -*- coding: utf-8 -*-
"""
Auth* related model.

This is where the models used by the authentication stack are defined.

It's perfectly fine to re-use this definition in the sibooru application,
though.

"""
import os
from datetime import datetime
from hashlib import sha512

from sqlalchemy import Table, ForeignKey, Column, Unicode, Integer, DateTime, String, UnicodeText
from sqlalchemy.orm import relation, synonym

from sibooru.model import DeclarativeBase, metadata, DBSession

"""Association table for the many-to-many relationship between users and groups"""
auth_users_groups_table = Table('auth_users_groups', metadata,
                                Column('user_id', Integer,
                                       ForeignKey('auth_users.user_id',
                                                  onupdate='CASCADE',
                                                  ondelete='CASCADE'),
                                       primary_key=True),
                                Column('group_id', Integer,
                                       ForeignKey('auth_groups.group_id',
                                                  onupdate='CASCADE',
                                                  ondelete='CASCADE'),
                                       primary_key=True))

"""Association table for the many-to-many relationship between groups and permissions"""
auth_groups_permissions_table = Table('auth_groups_permissions', metadata,
                                      Column('group_id', Integer,
                                             ForeignKey('auth_groups.group_id',
                                                        onupdate='CASCADE',
                                                        ondelete='CASCADE'),
                                             primary_key=True),
                                      Column('permission_id', Integer,
                                             ForeignKey('auth_permissions.permission_id',
                                                        onupdate='CASCADE',
                                                        ondelete='CASCADE'),
                                             primary_key=True))


class AuthUser(DeclarativeBase):
    """
    Defines a user on the site
    """
    __tablename__ = 'auth_users'

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(Unicode(64), unique=True, nullable=False)
    email = Column(Unicode(254), unique=True, nullable=False)
    # Display name?
    _password = Column('password', String(256))
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return '<User: name={}, email={}>'.format(self.username, self.email)

    @property
    def permissions(self):
        """Return a set with all of the user's permissions"""
        perms = set()
        for group in self.groups:
            perms |= set(group.permissions)
        return perms

    @classmethod
    def with_email(cls, email):
        """Return the user whose email address is ``email``."""
        return DBSession.query(cls).filter_by(email=email).first()

    @classmethod
    def with_username(cls, username):
        """Return the user whose username is ``username``"""
        return DBSession.query(cls).filter_by(username=username).first()

    @classmethod
    def _hash_password(cls, password):
        """
        Take a provided plaintext password and hash it with a random salt.

        :param password: the plaintext password provided by the user.
        :type password: unicode object.
        :return: the hashed password concatenated after the salt that was used.
            Salt and pass will both be 128 bytes long, 256 bytes total.
        """
        salt = sha512()
        salt.update(os.urandom(60))  # Magic number?
        salt = salt.hexdigest()

        pass_hash = sha512()
        # Make sure password is a str because we cannot hash unicode objects
        pass_hash.update((password + salt).encode('utf-8'))
        pass_hash = pass_hash.hexdigest()

        # Store final password hash after the salt, and return them
        return salt + pass_hash

    def _set_password(self, password):
        """
        Hash ``password`` and store its hashed value.
        Used when a user first creates an account or changes their password
        """
        self._password = self._hash_password(password)

    def _get_password(self):
        """Return the hashed version of the password"""
        return self._password

    password = synonym('_password', descriptor=property(_get_password, _set_password))

    def validate_password(self, password):
        """
        Check the provided plaintext password against the stored hashed version.

        :param password: the plaintext password provided by the user
        :type password: unicode object.
        :return: Whether the password is valid.
        :rtype: bool
        """
        pass_hash = sha512()
        pass_hash.update((password + self.password[:128]).encode('utf-8'))
        return self.password[128:] == pass_hash.hexdigest()


class AuthGroup(DeclarativeBase):
    """
    Defines a user group that can store permissions
    """
    __tablename__ = 'auth_groups'

    group_id = Column(Integer, autoincrement=True, primary_key=True)
    group_name = Column(Unicode(64), unique=True, nullable=False)
    group_description = Column(UnicodeText, nullable=False, default='')
    # Display name?
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    users = relation(AuthUser, secondary=auth_users_groups_table, backref='groups')

    def __repr__(self):
        return '<Group: name={}>'.format(self.group_name)


class AuthPermission(DeclarativeBase):
    """
    Defines a permission that can be applied to groups
    """

    __tablename__ = 'auth_permissions'

    permission_id = Column(Integer, autoincrement=True, primary_key=True)
    permission_name = Column(Unicode(64), unique=True, nullable=False)
    permission_description = Column(UnicodeText, nullable=False, default='')
    created_at = Column(DateTime, nullable=False, default=datetime.now)

    groups = relation(AuthGroup, secondary=auth_groups_permissions_table, backref='permissions')

    def __repr__(self):
        return '<Permission: name={}>'.format(self.permission_name)
