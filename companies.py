import db

def create_company(user_id, company_name, business_id, address, postal_code, apartment_count, registration_date, completion_year):
    sql = "INSERT INTO companies (company_name, business_id, address, postal_code, apartment_count, registration_date, completion_year) VALUES (?, ?, ?, ?, ?, ?, ?)"
    db.execute(sql, [company_name, business_id, address, postal_code, apartment_count, registration_date, completion_year])
    company_id = db.last_insert_id()

    sql2 = "INSERT INTO users_companies (user_id, company_id) VALUES (?, ?)"
    db.execute(sql2, [user_id, company_id])

