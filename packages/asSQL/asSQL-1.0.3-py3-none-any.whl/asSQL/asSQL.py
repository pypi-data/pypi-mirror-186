import sqlite3, json
def jsonify(data):
    
    json_string = data
    return json_string

class Client:
    def __init__(self,username):
        self.username = username
        self.connection = sqlite3.connect('database.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        
    def __getitem__(self, key):
        return TableAPI(self.username, key, self.connection, self.cursor)
        
        
class TableAPI:
    def __init__(self,username,table_name, connection, cursor):
        self.username = username
        self.table_name = table_name
        self.connection = connection
        self.cursor = cursor
    def create_table(self):
        try:
            self.cursor.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name LIKE '{self.username}_%'")
            count = self.cursor.fetchone()[0]
            if count < 5:
                self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.username}_{self.table_name} (key TEXT PRIMARY KEY, value TEXT)")
                self.connection.commit()
                return jsonify(True)
            else:
                return jsonify("You have reached the maximum number of allowed tables (5)")
        except Exception as e:
            return jsonify(False)
  
            
    def set(self, key, value):
        self.cursor.execute(f"INSERT OR REPLACE INTO {self.username}_{self.table_name} (key, value) VALUES (?, ?)", (key, json.dumps(value)))
        self.connection.commit()
        return jsonify(True)

    def get(self,key):
        try:
            self.cursor.execute(f"SELECT value FROM {self.username}_{self.table_name} WHERE key=?", (key,))
            result = self.cursor.fetchone()
            if result:
                return jsonify(json.loads(result[0]))
            else:
                return jsonify(None)
        except sqlite3.OperationalError:
            return jsonify(None)

    def delete(self, key):
        try:
            self.cursor.execute(f"DELETE FROM {self.username}_{self.table_name} WHERE key = ?", (key,))
            self.connection.commit()
            return jsonify(True)
        except sqlite3.OperationalError:
            return jsonify(False)
            
    def get_all(self):
        try:
            self.cursor.execute(f"SELECT * FROM {self.username}_{self.table_name}")
            data = self.cursor.fetchall()
            if data:
                result = []
                for item in data:
                    key = item[0]
                    value = json.loads(item[1])
                    if type(value) is dict:
                        result.append(f"- {key}\n ├ {value}\n └ Dict.\n")
                    elif type(value) is str:
                        result.append(f"- {key}\n ├ {value}\n └ Str.\n")
                    elif type(value) is bool:
                        result.append(f"- {key}\n ├ {value}\n └ Bool.\n")
                    else:
                        result.append(f"- {key}\n ├ {value}\n └ {type(value)}.\n")
                return jsonify("".join(result))
            else:
                return jsonify(None)
        except Exception as e:
            return jsonify(str(e))
    def tables(self):
        try:
            self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '{self.username}_%'")
            tables = self.cursor.fetchall()
            self.connection.close()
            prefix = len(f"{self.username}_")
            user_tables = [table[0][prefix:] for table in tables]
            return user_tables
        except sqlite3.OperationalError:
            return None    
    def keys(self,pattern=None):
        try:
            self.cursor.execute(f"SELECT key FROM {self.username}_{self.table_name}")
            data = self.cursor.fetchall()
            if data:
                keys = []
                for item in data:
                    keys.append(item[0])
                return jsonify("\n".join(keys))
            else:
                return jsonify(None)
        except Exception as e:
            return jsonify(str(e))
    
    def key_exists(self, key):
            self.cursor.execute(f"SELECT 1 FROM {self.username}_{self.table_name} WHERE key=?", (key,))
            result = self.cursor.fetchone()
            if result:
                return 1
            else:
                return 0
    
    def push(self, key, value):
        try:
            self.cursor.execute(f"SELECT value FROM {self.username}_{self.table_name} WHERE key=?", (key,))
            data = self.cursor.fetchone()
            if data:
                json_data = json.loads(data[0])
                if isinstance(json_data, list):
                    json_data.append(value)
                    self.cursor.execute(f"UPDATE {self.username}_{self.table_name} SET value = ? WHERE key = ?", (json.dumps(json_data), key))
                    self.connection.commit()
                    return True
                else:
                    return "The value stored at this key is not a list"
            else:
                return "Key does not exist"
        except Exception as e:
            return str(e)
    
    def unpush(self, key, value):
        try:
            self.cursor.execute(f"SELECT value FROM {self.username}_{self.table_name} WHERE key=?", (key,))
            data = self.cursor.fetchone()
            if data:
                json_data = json.loads(data[0])
                if isinstance(json_data, list):
                    json_data.remove(value)
                    self.cursor.execute(f"UPDATE {self.username}_{self.table_name} SET value = ? WHERE key = ?", (json.dumps(json_data), key))
                    self.connection.commit()
                    return True
                else:
                    return "The value stored at this key is not a list"
            else:
                return "Key does not exist"
        except ValueError:
            return "Value is not in list"
