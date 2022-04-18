using System;
namespace exercicios.desafioBancoMundial
{
    public abstract class Pessoa
    {
        public static int NumeroDePessoas;
        public int id;
        public string Endereco { get; set; }
        public string tel { get; set; }
        public string email { get; set; }

        public Pessoa()
        {
            Pessoa.NumeroDePessoas++;
            this.id = NumeroDePessoas + 1;
        }

        public abstract double CalculaRendimento();

    }
}

