function scriptTrabalho(){
    var senha = document.getElementById("senha");
    var confirmaSenha = document.getElementById("confirmaSenha");
    
    if (senha.value != confirmaSenha.value) {
        alert("Senhas diferentes!");
    } else {
        alert("SEGUE DADOS REESCRITOS: \n"
        +"Nome Completo: " + document.getElementById("nomeCompleto").value.toUpperCase() + "\n"
        +"Endereço: " + document.getElementById("endereco").value + "\n"
        +"Cidade: " + document.getElementById("cidade").value + "\n"
        +"Estado: " + document.getElementById("estado").value + "\n"
        +"Usuário: " + document.getElementById("nomeUsuario").value + "\n"
        +"Senha: " + document.getElementById("senha").value + "\n"
        +"Senha de confirmação: " + document.getElementById("confirmaSenha").value + "\n");
    }

}