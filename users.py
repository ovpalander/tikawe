from werkzeug.security import check_password_hash, generate_password_hash
import db

def create_user(username, password):
    pwd_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, pwd_hash) VALUES (?, ?)"
    db.execute(sql, [username, pwd_hash])

def check_login(username, password):
    sql = "SELECT id, pwd_hash FROM users where username = ?"
    result = db.query(sql, [username])
    if not result:
        return None

    user_id = result[0]["id"]
    pwd_hash = result[0]["pwd_hash"]
    if check_password_hash(pwd_hash, password):
        return user_id

    else:
        return None
