## Подготовка к установке ##

Для начала работы, скачайте архив приложения и распакуйте в удобное мето

![скачать проект](https://github.com/kiselevvn/legal-service/blob/main/assets/img/download.PNG?raw=true)

Для работы приложения необходим python версии 3.7.3, для установки запустите установщик из папки 'assets' (в корне проекта)

Далее необходимио установить пакетный менеджер python poetry и windows choco

Для этого откройте PowerShell от имени администратора, и запустите в нем поочередно следующие команды:

![power shell](https://github.com/kiselevvn/legal-service/blob/main/assets/img/power-shell.PNG?raw=true)

Установка Poetry:

```cmd
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

Установка Choco:

```cmd
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

Далее из терминала windows введите следующую команду (win + r), впишите "cmd" и нажмите "ок"

![power shell](https://github.com/kiselevvn/legal-service/blob/main/assets/img/cmd.PNG?raw=true)

```cmd
choco install make
```

## Установка проекта ##

Откройте терминал windows, перейдите в корень проекта и запустите следующую команду:


```cmd
make install
```

После ее завершения проект готов к запуску:

```cmd
make run
```
