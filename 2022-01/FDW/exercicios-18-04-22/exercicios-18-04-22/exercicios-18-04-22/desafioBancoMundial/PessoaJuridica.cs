using System;
using System.Collections.Generic;

namespace exercicios.desafioBancoMundial
{
    public class PessoaJuridica : Pessoa
    {
        public List<PessoaFisica> Socio = new List<PessoaFisica>();
        public string RazaoSocial { get; set; }
        public string NomeFantasia { get; set; }
        public int IncricaoEstadual { get; set; }
        public DateTime DataAbertura { get; set; }
        public int Idade { get; }
        public double Faturamento { get; set; }

        public PessoaJuridica(string endereco, string tel, string email, string razaoSocial,
            string nomeFantasia, int inscricao, DateTime abertura, double faturamento)
        {
            this.Endereco = endereco;
            this.tel = tel;
            this.email = email;
            this.RazaoSocial = razaoSocial;
            this.NomeFantasia = nomeFantasia;
            this.IncricaoEstadual = inscricao;
            this.DataAbertura = abertura;
            this.Idade = Auxiliar.CalcularIdade(this.DataAbertura);
            this.Faturamento = faturamento;

        }

        public override double CalculaRendimento()
        {
            return this.Faturamento;
        }

    }
}

