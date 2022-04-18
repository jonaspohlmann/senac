using System;
namespace exercicios.desafioBancoMundial
{
    public abstract class Conta
    {
        public Pessoa Titular;
        public long Numero { get; set; }
        public int Agencia { get; set; }
        protected double Saldo;
        public double TaxaSaque { get; set; }

        public Conta()
        {
            this.Saldo = 0;
        }

        public abstract void Sacar(double valor);

        public abstract void Transferencia(Conta conta, double valor);


        public double ConsultarSaldo()
        {
            return this.Saldo;
        }

        public void setSaldo(double saldo)
        {
            this.Saldo += saldo;
        }
    }
}

