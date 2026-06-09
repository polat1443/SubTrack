import sqlite3

class Database:
    def __init__(self, db_name="subtrack.db"):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.conn.row_factory = sqlite3.Row  
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute_query(self, query, params=None):
        opened_here = False
        if not self.conn:
            self.connect()
            opened_here = True
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor.fetchall()
        finally:
            if opened_here:
                self.close()

    def init_db(self):
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                plan_type TEXT NOT NULL CHECK (plan_type IN ('Aylık', 'Yıllık', 'Haftalık')),
                price REAL NOT NULL,
                start_date DATE,
                status TEXT DEFAULT 'Aktif' CHECK (status IN ('Aktif', 'İptal Edildi')),
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            );
        """)
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS invoices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subscription_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                payment_date DATE NOT NULL,
                status TEXT DEFAULT 'Ödendi' CHECK (status IN ('Ödendi', 'Bekliyor', 'Gecikti')),
                FOREIGN KEY (subscription_id) REFERENCES subscriptions (id) ON DELETE CASCADE
            );
        """)

    def create_user(self, username, email):
        query = "INSERT INTO users (username, email) VALUES (?, ?)"
        self.execute_query(query, (username, email))

    def get_users(self):
        query = "SELECT * FROM users"
        return [dict(row) for row in self.execute_query(query)]

    def create_subscription(self, user_id, name, plan_type, price, start_date, status='Aktif'):
        query = "INSERT INTO subscriptions (user_id, name, plan_type, price, start_date, status) VALUES (?, ?, ?, ?, ?, ?)"
        self.execute_query(query, (user_id, name, plan_type, price, start_date, status))

    def get_subscriptions(self):
        query = """
            SELECT s.*, u.username 
            FROM subscriptions s
            LEFT JOIN users u ON s.user_id = u.id
        """
        return [dict(row) for row in self.execute_query(query)]

    # --- DÜZENLEME (UPDATE) İÇİN YENİ EKLENENLER ---
    
    # Sadece tek bir aboneliğin bilgilerini getirmek için (Formu doldururken lazım olacak)
    def get_subscription(self, sub_id):
        query = "SELECT * FROM subscriptions WHERE id = ?"
        rows = self.execute_query(query, (sub_id,))
        return dict(rows[0]) if rows else None

    # Veritabanında güncelleme (Update) komutunu çalıştıran fonksiyon
    def update_subscription(self, sub_id, name, plan_type, price, start_date):
        query = "UPDATE subscriptions SET name=?, plan_type=?, price=?, start_date=? WHERE id=?"
        self.execute_query(query, (name, plan_type, price, start_date, sub_id))

    def delete_subscription(self, subscription_id):
        query = "DELETE FROM subscriptions WHERE id = ?"
        self.execute_query(query, (subscription_id,))