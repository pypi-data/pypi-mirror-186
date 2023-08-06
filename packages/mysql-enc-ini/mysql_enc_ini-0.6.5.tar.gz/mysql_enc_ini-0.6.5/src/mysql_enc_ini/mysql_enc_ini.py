#!/usr/bin/python3
# -*- coding: utf-8 -*-
# mysql_enc_ini.py


from cryptography.fernet import Fernet
from configparser import ConfigParser
from os.path import exists as file_exists
import getpass
import os

class Mysql_enc_ini():
  def __init__(self,**kvargs):
    self.kvargs = kvargs
    self.home = os.environ['HOME']
    self.key_file = self.home + '/.mclef'
    self.decrypted_file = self.home + '/decrypted_' + str(os.getpid()) + '.ini'

    if file_exists(self.key_file):
      with open(self.key_file, 'rb') as file:
        key = file.read()
        file.close
        self.key = key
    else:
      key = Fernet.generate_key()
      with open (self.key_file, 'wb') as file:
        file.write(key)
        os.chmod(self.key_file, 0o400)
        file.close
        self.key = key

  def decrypt(self,encrypted_inifile):
    fernet = Fernet(self.key)
    conn_data = {}
    filepath = os.path.split(encrypted_inifile)
    if filepath[1][:1] != ".":
      if filepath[0] != "":
        encrypted_inifile = filepath[0] + "/." + filepath[1]
      else:
        encrypted_inifile = "." + filepath[1]
    if file_exists(encrypted_inifile):
      with open(encrypted_inifile, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    else:
      self.encrypt(self.decrypted_file,encrypted_inifile)
      with open(encrypted_inifile, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    #decrypt the file
    decrypted = fernet.decrypt(encrypted)
    with open(self.decrypted_file, 'wb') as decrypted_file:
      decrypted_file.write(decrypted)
    config = ConfigParser()
    config.read(self.decrypted_file)
    os.remove(self.decrypted_file)
    conn_data["host"] = config.get('Connection', 'host')
    conn_data["user"] = config.get('Connection', 'user')
    conn_data["database"] = config.get('Connection', 'database')
    conn_data["passwd"] = config.get('Connection', 'passwd')
    conn_data["port"] = config.get('Connection','port')
    return conn_data

  def encrypt(self,init_file, encrypted_inifile):
    filepath = os.path.split(encrypted_inifile)
    if filepath[1][:1] != ".":
      if filepath[0] != "":
        encrypted_inifile = filepath[0] + "/." + filepath[1]
      else:
        encrypted_inifile = "." + filepath[1]
    print("Checking MySQL connection informations and gathering them if not given.")
    if self.kvargs:
      if self.kvargs["hostname"] == "localhost" or self.kvargs["hostname"] == "":
        self.kvargs["hostname"] = input("Give the Database server name: ")
      if self.kvargs["username"] == "":
        self.kvargs["username"] = input("Give the Database Username: ")
      if self.kvargs["database"] == "":
        self.kvargs["database"] = input("Give the Database Name: ")
      if self.kvargs["port"] == "":
        self.kvargs["port"] = input("Give the port number: ")
      password = getpass.getpass("Give the password for username: " + self.kvargs["username"] + " on server: " + self.kvargs["hostname"] + ": ")
      parser = ConfigParser()
      parser.add_section('Connection')
      parser.set('Connection', 'host', self.kvargs["hostname"])
      parser.set('Connection', 'user', self.kvargs["username"])
      parser.set('Connection', 'passwd', password)
      parser.set('Connection', 'port', self.kvargs["port"])
      parser.set('Connection', 'database', self.kvargs["database"])
    else:
      servername = input("Give the Database server name: ")
      username = input("Give the Database Username: ")
      db = input("Give the Database Name: ")
      port = input("Give the port number: ")
      password = getpass.getpass("Give the password for this Username: ")
      parser = ConfigParser()
      parser.add_section('Connection')
      parser.set('Connection', 'host', servername)
      parser.set('Connection', 'user', username)
      parser.set('Connection', 'passwd', password)
      parser.set('Connection', 'port', port)
      parser.set('Connection', 'database', db)
    fp=open(init_file,'w')
    parser.write(fp)
    fp.close()
    fernet = Fernet(self.key)
    with open(init_file, 'rb') as file:
      original = file.read()
    os.remove(init_file)
    encrypted = fernet.encrypt(original)
    with open (encrypted_inifile, 'wb') as file:
      file.write(encrypted)
      os.chmod(encrypted_inifile, 0o600)
