import db

def add_company_doc(company_id, name, file):
    sql = "INSERT INTO documents (company_id, name, file) VALUES (?, ?, ?)"
    db.execute(sql, [company_id, name, file])

