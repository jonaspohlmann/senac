var express = require('express');
var app = express();
const port = 3000

let listaProdutos = [];
let geradorId = 1;

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
  })

app.use(express.json())

//GET /produtos
app.get('/produtos', function (req, res) {
    res.send(listaProdutos);
});

//GET /produtos/:id
app.get('/produtos/:id', function (req, res) {
    res.send('Buscando o produto '+req.params.id);
});

//POST /produtos
app.post('/produtos', function (req, res) {
    let nome = req.body.nome;
    let preco = req.body.preco;

    listaProdutos.push(geradorId, nome, preco);
    res.send('Cadastrando produto '+ nome);

    geradorId++;
});

//PUT /produtos/:id
app.put('/produtos/:id', function (req, res) {
    res.send('Atualizando o produto '+req.params.id)
});

//DELETE /produtos/:id
app.delete('/produtos/:id', function (req, res) {
    res.send('Removendo o produto '+req.params.id)
});