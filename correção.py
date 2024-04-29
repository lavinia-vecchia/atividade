import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Função para criar tabela de produtos (se não existir)
def criar_tabela_produtos():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )
    """)

# Função para cadastrar novo produto
def cadastrar_produto(nome, preco, estoque):
    criar_tabela_produtos()
    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", (nome, preco, estoque))
    conexao.commit()
    print(f"Produto cadastrado com sucesso: {nome}")

# Função para buscar produto por ID
def buscar_produto_por_id(produto_id):
    criar_tabela_produtos()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()
    return produto

# Função para atualizar estoque de um produto
def atualizar_estoque_produto(produto_id, nova_quantidade):
    produto = buscar_produto_por_id(produto_id)
    if produto:
        if nova_quantidade >= 0:
            cursor.execute("UPDATE produtos SET estoque = ? WHERE id = ?", (nova_quantidade, produto_id))
            conexao.commit()
            print(f"Estoque atualizado: {produto['nome']} - Nova quantidade: {nova_quantidade}")
        else:
            print("Erro: Quantidade nova deve ser maior ou igual a zero.")
    else:
        print(f"Produto não encontrado: {produto_id}")

# Exemplo de uso das funções
cadastrar_produto("Caneta", 2.50, 30)
atualizar_estoque_produto(1, 25)  # Venda de 5 canetas
atualizar_estoque_produto(1, 40)  # Erro: Quantidade nova deve ser maior ou igual a zero.
