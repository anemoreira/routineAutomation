## Introdução
### Como funciona o cronJob:
O cronJob é um utilitário do sistema Unix/Linux que permite agendar tarefas para serem executadas em momentos específicos. Ele opera com base em um arquivo chamado "crontab", onde você pode configurar as tarefas a serem executadas e seus horários.

### Como pode ser usado:
O cronJob é amplamente utilizado para automatizar tarefas recorrentes, como backup de arquivos, limpeza de logs, execução de scripts de manutenção, entre outros. Ele permite agendar a execução de comandos em intervalos regulares, diariamente, semanalmente ou mensalmente, de acordo com a necessidade.

### Comandos iniciais normalmente utilizados pelos usuários:
<table border=\"1\"><tr><th align=\"right\">Comando</th><th align=\"left\">Função</th></tr><tr><td align=\"right\">`sudo service cron status`</td><td align=\"left\">Para verificar se o serviço está rodando</td></tr><tr><td align=\"right\">`sudo service cron start`</td><td align=\"left\">Para iniciar o serviço cron</td></tr></table><td align=\"right\">`sudo service cron start`</td><td align=\"left\">Para iniciar o serviço cron</td></tr></table><td align=\"right\">`sudo service cron start`</td><td align=\"left\">Para iniciar o serviço cron</td></tr></table><td align=\"right\">`sudo service cron start`</td><td align=\"left\">Para iniciar o serviço cron</td></tr></table>


## 🔎 Objetivo do script ? 
- Importa os módulos necessários: os, glob e datetime.
- Define uma função chamada cleanup_temp_files que recebe dois argumentos: o diretório de arquivos temporários (temp_dir) e o limite de dias (days_threshold).
- Obtém a data e hora atuais.
- Itera sobre todos os arquivos no diretório de arquivos temporários.
- Para cada arquivo, verifica se a última modificação foi há mais de days_threshold dias.
- Se sim, remove o arquivo.

## ⚙️ Como executar ?  
- Passo 1: Adicione o arquivo .py ao seu diretório
- Passo 2: Verifique o caminho do seu arquivo, ex: `temp_directory = "/caminho/do/diretorio/de/temporarios`
- Passo 3: Execute o comando *Automatizando tarefa* de acordo com as especificações de *Como pode ser usado*

## Automatizando tarefa
```
0 2 * * * python3 /caminho/para/o/script/backup.py

```
Todas as vezes que o relógio marcar 02:00h o comando vai ser executado


Ane Moreira😉✅
