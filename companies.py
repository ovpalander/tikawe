import db

def create_company(user_id, company_name, business_id, city, address, postal_code, apartment_count, registration_date, completion_year):
    sql = "INSERT INTO companies (company_name, business_id, city, address, postal_code, apartment_count, registration_date, completion_year) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    db.execute(sql, [company_name, business_id, city, address, postal_code, apartment_count, registration_date, completion_year])
    company_id = db.last_insert_id()

    sql2 = "INSERT INTO users_companies (user_id, company_id) VALUES (?, ?)"
    db.execute(sql2, [user_id, company_id])

    return company_id

def get_company(company_id):
    sql = "SELECT company_name, business_id, city, address, postal_code, apartment_count, registration_date, completion_year FROM companies WHERE id = ?"
    result = db.query(sql, [company_id])
    return result[0]
