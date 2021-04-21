# 비밀번호 암호화방법
from passlib.hash import sha256_crypt

password = sha256_crypt.encrypt("password")

print(password)