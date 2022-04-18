using System;
namespace exercicios.desafioWhatsapp.Mensagem
{
    public class MsgTexto : Mensagem
    {
        public int numChar;

        public MsgTexto(int numChar, Contatinho Contato, string horaEnvio, string conteudo)
        {
            this.numChar = numChar;
            this.Destinatrio = Contato;
            this.horaEnvio = horaEnvio;
            this.conteudo = conteudo;
        }
    }
}

