using System;
namespace exercicios.desafioBancoMundial
{
    public class ContaCorrente : Conta
    {
        public string Tipo { get; }
        public double Limite { get; }
        public double TaxaDoLimite { get; }

        public ContaCorrente(Pessoa titular, long numero, int agencia)
        {
            this.Titular = titular;
            this.Numero = numero;
            this.Agencia = agencia;
            this.Tipo = this.TipoConta();
            this.Limite = this.CalculaLimite();
            this.TaxaDoLimite = this.CalculaTaxaLimite();
        }

        public override void Sacar(double valor)
        {
            if (this.Saldo < valor)
            {
                if (((valor * (this.TaxaDoLimite / 100)) + valor) <= this.Limite)
                {
                    this.Saldo -= ((valor * (this.TaxaDoLimite / 100)) + valor);
                }
                else
                {
                    Console.WriteLine("Não foi possivel realizar essa operação");
                }
            }
            else
            {
                this.Saldo -= valor;
            }

        }

        public override void Transferencia(Conta conta, double valor)
        {
            if (this.Saldo >= valor)
            {
                this.Saldo -= valor;
                conta.setSaldo(valor);
                Console.WriteLine("Você transferiu " + valor);
                Console.WriteLine("Para " + conta.Agencia);
                Console.WriteLine("Você transferiu " + conta.Numero);
            }
            else
            {
                Console.WriteLine("Transação não realizada verifique seu saldo");
            }
        }

        public string TipoConta()
        {
            bool isRendimento = this.Titular.CalculaRendimento() >= 5000;

            return isRendimento ? "Especial" : "Simples";
        }


        public double CalculaLimite()
        {
            bool isSimples = this.Tipo == "Simples";
            double rendimento = this.Titular.CalculaRendimento();

            return isSimples ? (rendimento * 150) / 100 : (rendimento * 250) / 100;
        }


        public int CalculaTaxaLimite()
        {
            bool isSimples = this.Tipo == "Simples";

            return isSimples ? 2 : 5;
        }

        public void Depositar(double valor)
        {
            if (valor > 0)
            {
                this.Saldo += valor;
            }
            else
            {
                Console.WriteLine("Não foi possivel depositar");
            }
        }

        public void Pagar(string CodigoBarras)
        {
            CodigoBarras = "3000";
            Double.Parse(CodigoBarras);

            if (this.Saldo > Double.Parse(CodigoBarras))
            {
                Console.WriteLine("Conta paga");
                this.Saldo -= Double.Parse(CodigoBarras);
            }
            else
            {
                Console.WriteLine("Saldo insuficiente");
            }
        }

        public void Emprestimo(double valor)
        {
            this.Saldo += valor;
        }


    }
}

