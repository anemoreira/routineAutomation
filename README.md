## Introdução
### Como funciona o cronJob:
O cronJob é um utilitário do sistema Unix/Linux que permite agendar tarefas para serem executadas em momentos específicos. Ele opera com base em um arquivo chamado "crontab", onde você pode configurar as tarefas a serem executadas e seus horários. 

### Como pode ser usado:
O cronJob é amplamente utilizado para automatizar tarefas recorrentes, como backup de arquivos, limpeza de logs, execução de scripts de manutenção, entre outros. Ele permite agendar a execução de comandos em intervalos regulares, diariamente, semanalmente ou mensalmente, de acordo com a necessidade.
<table border=\"1\"><tr><th align=\"right\">Comando</th><th align=\"left\">Função</th></tr><tr><td align=\"right\">`sudo service cron status`</td><td align=\"left\">Para verificar se o serviço está rodando</td></tr><tr><td align=\"right\">`sudo service cron start`</td><td align=\"left\">Para iniciar o comando</td></tr></table>

[Link para instalar](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804-pt).

### Exemplo de execução:
Para executar o crontab basta executar o comando `crontab -e` que vai abrir o arquivo de texto do crontab, onde haverá dicas de configuração do crontab, porém são apenas comentários que podem ser apagados(opcional). Para definição do cronjob deve ser seguido o layout de definição:

![image](https://github.com/anemoreira/firstProjectSimple/assets/93550467/be3c8770-5457-470c-85d8-fc330ddb4235)

**Exemplo:**
- Executado em todos minutos de todas as horas `* * * * * py backup.py `
- Executado a cada 5 minutos em todas as horas `*/5 * * * * py backup.py`
- Executado a cada 2 horas nos minutos 10, 20 e 30 `10,20,30 */2 * * * * py backup.py`
- Executado a cada segunda-feira às 09:37H  `37 9 * * 1 py backup.py`

**Exemplo para criar uma automações simples para imprimir a data e hora atual**
`*/2 * * * * echo $(date) >> /home/caminho/do/arquivoquedesejacriareaindanaoexiste/dois-minuto.txt` Assim quando rodar a primeira vez irá criar o arquivo, aperte ^X para salvar **S**, em seguida digite o comando `crontab -l` para verificar se o arquivo foi salvo. Caso deseje abra o arquivo em seu editor de código e verifique a execução. Desejando apagar o arquivo digite `crontab -r`. 


## 🔎 Objetivo do script deste repositório? 
- Definir uma função chamada cleanup_temp_files que recebe dois argumentos: o diretório de arquivos temporários (temp_dir) e o limite de dias (days_threshold), para obter a data e hora atual, iterando sobre todos os arquivos no diretório de arquivos temporários que verifica se a última modificação foi há mais de days_threshold dias para remover o arquivo.

## Comando para automatizar
```
0 2 * * * python3 /caminho/para/o/script/backup.py

```
Todas as vezes que o relógio marcar 02:00h o comando vai ser executado 😉✅
____________________________________________________________________________________
