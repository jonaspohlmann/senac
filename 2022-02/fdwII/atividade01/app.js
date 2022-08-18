var express = require('express');
var app = express();
const port = 3000

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
  })

//GET /produtos
app.get('/produtos', function (req, res) {
    res.send('GET /produtos');
});

//GET /produtos/:id
app.get('/produtos/:id', function (req, res) {
    res.send('GET /produtos/:id');
});

//POST /produtos
app.post('/produtos', function (req, res) {
    res.send('POST /produtos');
});

//PUT /produtos/:id
app.put('/produtos/:id', function (req, res) {
    res.send('PUT /produtos/:id');
});

//DELETE /produtos/:id
app.delete('/produtos/:id', function (req, res) {
    res.send('DELETE /produtos/:id');
});
  