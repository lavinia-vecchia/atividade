var produto = ['caneta', 'lápis', 'borracha', 'régua', 'caderno', 'lapiseira']
var preco = [5.25, 2.99, 3.99, 5.50, 15.90, 22.59]
var qtdEstoque = [27, 53, 60, 33, 28, 15]

function compras(qtdComprada, produtoComprado){
    indiceProduto = produto.indexOf(produtoComprado)
    qtdEstoque[indiceProduto] = qtdEstoque[indiceProduto] + qtdComprada
    console.log(qtdEstoque[indiceProduto])
}

function vendas(qtdVendida, produtoVendido){
    indiceProduto = produto.indexOf(produtoVendido)
    qtdEstoque[indiceProduto] = qtdEstoque[indiceProduto] - qtdVendida
    console.log(qtdEstoque[indiceProduto])
}

function novaMercadoria(nomeProduto, precoNovo, qtd){
    var posicao = produto.length
    produto[posicao] = nomeProduto
    preco[posicao] = precoNovo
    qtdEstoque[posicao] = qtd
}
