using System;
namespace exercicios.desafioWhatsapp.Mensagem
{
    public abstract class Mensagem
    {
        public Contatinho Destinatrio;
        public string horaEnvio;
        public string conteudo;

        public Mensagem()
        {
        }

        public void toString() { }
    }
}

