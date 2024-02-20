from flask import Flask, render_template, request, redirect
import conn
import traceback
print("Erro ao inserir dados:")
traceback.print_exc()
app = Flask(__name__, template_folder='templates')

def get_db_connection():
    conn_obj = conn.create_connection()
    return conn_obj
@app.route("/", methods=["GET"])
def home():
    print("---------------------------------------------------------")
    try:
        conn_obj = get_db_connection()
        conn.create_table(conn_obj)
        cursor = conn_obj.cursor()
        print("test")
        cursor.execute("select * from Tbs where concluidos = ?", (0,))
        print("test")
        dados = cursor.fetchall()
        
        conn_obj.close()
    except:
        print("erro ao ler a tabela")


    return render_template("index.html", dados=dados)

@app.route("/", methods=['POST'])
def home1():
    print("")
    
@app.route("/cadastro", methods=['GET'])
def cadastro1():
    
    return render_template("cadastro.html")
@app.route("/cadastro", methods=['POST'])
def cadastro():
    
    quantidade = request.form['quantidade']
    nome = request.form['nome']
    telefone = request.form ['telefone']
    concluidos = 0
    try:
        conn_obj = get_db_connection()
        
        cursor = conn_obj.cursor()
        cursor.execute('insert into Tbs ( quantidade, nome, telefone, concluidos) values (?, ?, ?, ?) ', (quantidade, nome, telefone, concluidos))
        conn_obj.commit()
        print("Dados inseridos com sucesso.")
        conn_obj.close()
    except(KeyError):
        print(f"Erro ao inserir dados", KeyError)
    return render_template("cadastro.html")

@app.route('/delete_entry/<int:id>', methods=['POST'])
def delete_entry(id):
    # Lógica para excluir a entrada correspondente do banco de dados
    # Substitua isso com a sua lógica de exclusão real
    try:
        # Aqui você executaria a lógica para excluir a entrada do banco de dados
        conn_obj = get_db_connection()
        
        cursor = conn_obj.cursor()
        # Por exemplo:
        print((id))
        cursor.execute('update Tbs set concluidos = (?) where id = (?)', (1, id ))
        conn_obj.commit()
        print(f"Entrada com ID {id} excluída com sucesso.")
        conn_obj.close()
        return redirect("/")
    except Exception as e:
        print(f"Erro ao excluir entrada do banco de dados: {e}")
        return '', 500  # Resposta vazia com código de status 500 (Internal Server Error)

@app.route("/concluidos", methods=["GET"])
def concluidos():
    print("---------------------------------------------------------")
    try:
        conn_obj = get_db_connection()
        conn.create_table(conn_obj)
        cursor = conn_obj.cursor()
        print("test")
        cursor.execute("select * from Tbs where concluidos = ?", (1,))
        print("test")
        dados2 = cursor.fetchall()
        
        conn_obj.close()
    except:
        print("erro ao ler a tabela")


    return render_template("concluidos.html", dados2=dados2)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
