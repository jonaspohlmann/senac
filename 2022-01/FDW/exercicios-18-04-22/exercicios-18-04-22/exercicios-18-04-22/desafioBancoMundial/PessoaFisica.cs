using System;
namespace exercicios.desafioBancoMundial
{
    public class PessoaFisica : Pessoa
    {
        public string Nome { get; set; }
        public string Sobrenome { get; set; }
        public string Rg { get; set; }
        public string Cpf { get; set; }
        public DateTime DataNascimento { get; set; }
        public int Idade { get; }
        public string FaixaEtaria { get; }
        public double Renda { get; set; }

        public PessoaFisica(string endereco, string tel, string email, string nome, string sobrenome, string rg, string cpf, DateTime dataNascimento, double renda)
        {
            this.Endereco = endereco;
            this.tel = tel;
            this.email = email;
            this.Nome = nome;
            this.Sobrenome = sobrenome;
            this.Rg = rg;
            this.DataNascimento = dataNascimento;
            this.Idade = Auxiliar.CalcularIdade(this.DataNascimento);
            this.FaixaEtaria = Auxiliar.FaixaEtaria(this.Idade);
            this.Renda = renda;

        }

        public override double CalculaRendimento()
        {
            return this.Renda;
        }
    }
}

