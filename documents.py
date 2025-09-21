import db

def add_company_doc(company_id, name, filename, file):
    sql = "INSERT INTO documents (company_id, name, file_name, file) VALUES (?, ?, ?, ?)"
    db.execute(sql, [company_id, name, filename, file])

def get_company_doc(company_id, doc_id):
    sql = "SELECT * FROM documents WHERE company_id = ? AND id = ?"
    return db.query(sql, [company_id, doc_id])[0]

def find_company_docs(company_id, query):
    sql = "SELECT id, name, file_name FROM documents WHERE company_id = ? AND LOWER(name) LIKE ? OR LOWER(file_name) LIKE ? ORDER BY name DESC"
    like = "%" + query + "%"
    return db.query(sql, [company_id, like, like])

def delete_company_doc(company_id, doc_id):
    sql = "DELETE FROM documents WHERE company_id = ? AND id = ?"
    db.execute(sql, [company_id, doc_id])
