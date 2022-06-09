import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="database",
   user="user",
   password="abc123"
)
#Lists all words
def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
#Give the user opportunity to add words to the dictionary
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
#Delete words from the dictionary
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
#Saves the dictionary
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()

#Welcome message with instructions 
print('''Hello and welcome to the dictionary, available commands:
  add    - add a word
  delete - delete a word
  list   - list all words
  quit   - quit the program
  help   - list all commands''')

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
        print(f" Added word {word}")
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
        print(f"Deleted word {word}")
    elif cmd == "quit":
        save_dict(conn)
        print(f"The end!")
        exit()
        

