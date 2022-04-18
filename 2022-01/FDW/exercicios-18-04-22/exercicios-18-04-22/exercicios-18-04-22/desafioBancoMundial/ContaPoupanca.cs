using System;
namespace exercicios.desafioBancoMundial
{
    public class ContaPoupança : Conta
    {
        public ContaPoupança(Pessoa titular, long numero, int agencia)
        {
            this.Titular = titular;
            this.Numero = numero;
            this.Agencia = agencia;
            this.Saldo = 0;
            this.TaxaSaque = 5;
        }

        public override void Sacar(double valor)
        {
            if (this.Saldo >= (valor + this.TaxaSaque))
            {
                this.Saldo -= valor;
                Console.WriteLine("Você sacou " + valor);
            }
            else
            {
                Console.WriteLine("Não foi possivel realizar o saque");
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
                Console.WriteLine("Operação não realizada verifique seu saldo");
            }
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

    }
}

