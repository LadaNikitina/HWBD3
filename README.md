# HWBD3
## Блок 1 (Flink checkpoint )

### 1. Развернуть локально flink+kafka через docker-compose

В репозитории расположен файл docker-compose.yml

### 2. Создать источник и потребителя сообщений из kafka (пример из семинара)

В репозитории расположены файлы producer_1.py, consumer_1.py, consumer_2.py

### 3. Настроить Flink checkpoint и сохранять в local dir `file:///opt/pyflink/tmp/checkpoints/logs`  для обеспечения recovery mechanism

Код джобы находится в checkpoint_device_job.py

![image](https://github.com/LadaNikitina/HWBD3/assets/23546579/13021022-b01e-4d88-8b55-1cbb15149ec6)
![image](https://github.com/LadaNikitina/HWBD3/assets/23546579/90f1db6a-27e4-4132-8f3b-6675759f1dbe)
![image](https://github.com/LadaNikitina/HWBD3/assets/23546579/fafcfa20-b42a-4a12-aea1-c10b9fd81f79)


### 4. Настроить Flink checkpoint и сохранять в hdfs, предварительно поднять hdfs в docker-compose

