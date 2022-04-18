using System;
namespace exercicios.desafioBancoMundial
{
    public class ContaSalario : Conta
    {

        public ContaSalario(Pessoa titular, long numero, int agencia)
        {
            this.Titular = titular;
            this.Numero = numero;
            this.Agencia = agencia;
            this.Saldo = 0;
        }

        public override void Sacar(double valor)
        {
            if (this.Saldo >= valor)
            {
                this.Saldo -= valor;
            }
            else
            {
                Console.WriteLine("Saldo insuficiente");
            }
        }

        public override void Transferencia(Conta conta, double valor)
        {
            if (this.Titular.id == conta.Titular.id)
            {
                if (this.Saldo < valor)
                {
                    Console.WriteLine("Saldo insuficiente");
                }
                else
                {
                    this.Saldo -= valor;
                    conta.setSaldo(valor);
                }
            }
            else
            {
                Console.WriteLine("Conta salario não pode realizar esse procedimento");
            }
        }


    }
}

