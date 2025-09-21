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

def get_user(user_id):
    sql = "SELECT id, username FROM users WHERE id = ?"
    result = db.query(sql, [user_id])
    return result[0] if result else None

def check_companies(user_id):
    sql = "SELECT u.id, u.username, uc.company_id FROM users as u JOIN users_companies as uc on u.id = uc.user_id WHERE id = ?"
    result = db.query(sql, [user_id])
    if len(result) == 1:
        return result[0]["company_id"]
    elif len(result):
        pass
    else:
        return None
