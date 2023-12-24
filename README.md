# HWBD3
## Блок 1 (Flink checkpoint )

### 1. Развернуть локально flink+kafka через docker-compose

В репозитории расположен файл docker-compose.yml

### 2. Создать источник и потребителя сообщений из kafka (пример из семинара)

В репозитории расположены файлы producer_1.py, consumer_1.py, consumer_2.py

### 3. Настроить Flink checkpoint и сохранять в local dir `file:///opt/pyflink/tmp/checkpoints/logs`  для обеспечения recovery mechanism

Код джобы находится в checkpoint_device_job.py

![image](https://github.com/LadaNikitina/HWBD3/assets/23546579/c3518db7-3dd0-400f-b375-f5d60c9641d4)
![image](https://github.com/LadaNikitina/HWBD3/assets/23546579/1820470c-10fb-4bfa-b5d9-2df3bb8db6da)
![image](https://github.com/LadaNikitina/HWBD3/assets/23546579/72fe1e9d-ecbd-4219-b939-384f4b54446d)
![image](https://github.com/LadaNikitina/HWBD3/assets/23546579/7dd8c790-3f2c-4f92-9f21-dc85ead79656)

### 4. Настроить Flink checkpoint и сохранять в hdfs, предварительно поднять hdfs в docker-compose

