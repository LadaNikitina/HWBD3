# HWBD3

Выполнено Ледневой Дарьей Романовной

## Блок 1 (Flink checkpoint)

### 1. Развернуть локально flink+kafka через docker-compose

В репозитории расположен файл docker-compose.yml

### 2. Создать источник и потребителя сообщений из kafka (пример из семинара)

В репозитории расположены файлы producer_1.py, consumer_1.py, consumer_2.py

### 3. Настроить Flink checkpoint и сохранять в local dir `file:///opt/pyflink/tmp/checkpoints/logs`  для обеспечения recovery mechanism

Запуск:

```
docker-compose build 
docker-compose up -d 
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic itmo2023 --partitions 1 --replication-factor 1
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic itmo2023preprocessed --partitions 1 --replication-factor 1
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/checkpoint_device_job.py -d
python producer_1.py
python consumer_1.py
```

Код джобы находится в checkpoint_device_job.py

![image](https://github.com/LadaNikitina/HWBD3/assets/23546579/13021022-b01e-4d88-8b55-1cbb15149ec6)
![image](https://github.com/LadaNikitina/HWBD3/assets/23546579/90f1db6a-27e4-4132-8f3b-6675759f1dbe)
![image](https://github.com/LadaNikitina/HWBD3/assets/23546579/fafcfa20-b42a-4a12-aea1-c10b9fd81f79)


### 4. Настроить Flink checkpoint и сохранять в hdfs, предварительно поднять hdfs в docker-compose

```
docker-compose build 
docker-compose up -d 
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic itmo2023 --partitions 1 --replication-factor 1
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic itmo2023preprocessed --partitions 1 --replication-factor 1
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/checkpoint_hdfs_device_job.py -d
python producer_1.py
python consumer_1.py
```

Код джобы находится в checkpoint_hdfs_device_job.py. Flink не видит hdfs, не получилось выполнить задание.

![image](https://github.com/LadaNikitina/HWBD3/assets/23546579/96267192-a5bd-4530-b95d-c6c0e192a6d4)

## Блок 2 (Flink Window)

### 1. Развернуть локально flink+kafka через docker-compose

В репозитории расположен файл docker-compose.yml

### 2. Создать источник и потребителя сообщений из kafka (пример из семинара)

В репозитории расположены файлы producer_1.py, consumer_1.py, consumer_2.py

### 3. Использовать Tumbling Windows для подсчета максимальной температуры или или параметра на ваш выбор (интервал любой) (15)

```
docker-compose build 
docker-compose up -d 
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic itmo2023 --partitions 1 --replication-factor 1
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic itmo2023preprocessed --partitions 1 --replication-factor 1
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/tumbling_windows_device_job.py -d
python producer_1.py
python consumer_1.py
```

### 4. Использовать Sliding Windows для подсчета максимальной температуры или или параметра на ваш выбор (интервал любой) (15)

```
docker-compose build 
docker-compose up -d 
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic itmo2023 --partitions 1 --replication-factor 1
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic itmo2023preprocessed --partitions 1 --replication-factor 1
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/sliding_windows_device_job.py -d
python producer_1.py
python consumer_1.py
```

### 5. Использовать Session Windows  для подсчета максимальной температуры или или параметра на ваш выбор (интервал любой) (15)
```
docker-compose build 
docker-compose up -d 
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic itmo2023 --partitions 1 --replication-factor 1
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic itmo2023preprocessed --partitions 1 --replication-factor 1
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/session_windows_device_job.py -d
python producer_1.py
python consumer_1.py
```

