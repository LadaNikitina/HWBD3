from pyflink.common import SimpleStringSchema
from pyflink.common.typeinfo import Types, RowTypeInfo
from pyflink.common.watermark_strategy import WatermarkStrategy
from pyflink.datastream import StreamExecutionEnvironment, TimeCharacteristic, CheckpointingMode, CheckpointStorage
from pyflink.datastream.connectors import DeliveryGuarantee
from pyflink.datastream.connectors.kafka import KafkaSource, \
    KafkaOffsetsInitializer, KafkaSink, KafkaRecordSerializationSchema
from pyflink.datastream.formats.json import JsonRowDeserializationSchema
from pyflink.datastream.functions import MapFunction, KeyedProcessFunction, ReduceFunction
from pyflink.datastream.window import TumblingProcessingTimeWindows, SessionWindowTimeGapExtractor, \
    EventTimeSessionWindows
from pyflink.common import Time


def python_data_stream_example():
    env = StreamExecutionEnvironment.get_execution_environment()
    # Set the parallelism to be one to make sure that all data including fired timer and normal data
    # are processed by the same worker and the collected result would be in order which is good for
    # assertion.
    env.set_parallelism(1)
    env.set_stream_time_characteristic(TimeCharacteristic.EventTime)

    env.enable_checkpointing(5000)
    # exactly_once - семантика означает, что сообщение будет доставлено ровно 1 раз
    # кажется, такое значение выставляется по умолчанию, но я решила прописать это явно
    env.get_checkpoint_config().set_checkpointing_mode(CheckpointingMode.EXACTLY_ONCE)

    CHECKPOINT_PATH = 'file:///opt/pyflink/tmp/checkpoints/logs'
    env.get_checkpoint_config().set_checkpoint_storage(CheckpointStorage(CHECKPOINT_PATH))

    type_info: RowTypeInfo = Types.ROW_NAMED(['device_id', 'temperature', 'execution_time'],
                                             [Types.LONG(), Types.DOUBLE(), Types.INT()])

    json_row_schema = JsonRowDeserializationSchema.builder().type_info(type_info).build()

    source = KafkaSource.builder() \
        .set_bootstrap_servers('kafka:9092') \
        .set_topics('itmo2023') \
        .set_group_id('pyflink-e2e-source') \
        .set_starting_offsets(KafkaOffsetsInitializer.earliest()) \
        .set_value_only_deserializer(json_row_schema) \
        .build()

    sink = KafkaSink.builder() \
        .set_bootstrap_servers('kafka:9092') \
        .set_record_serializer(KafkaRecordSerializationSchema.builder()
                               .set_topic('itmo2023processed')
                               .set_value_serialization_schema(SimpleStringSchema())
                               .build()
                               ) \
        .set_delivery_guarantee(DeliveryGuarantee.AT_LEAST_ONCE) \
        .build()

    ds = env.from_source(source, WatermarkStrategy.no_watermarks(), "Kafka Source")

    # окно закрывается, когда в него не поступают элементы в течение определенного периода времени
    ds.window_all(EventTimeSessionWindows.with_gap(Time.seconds(30)))\
        .reduce(MaxTemperatureFunctionReducer()) \
        .map(TemperatureFunction(), Types.STRING()) \
        .sink_to(sink)
    # максимальная температура в каждом окне
    env.execute_async("Devices preprocessing")


class TemperatureFunction(MapFunction):

    def map(self, value):
        device_id, temperature, execution_time = value
        return str({"device_id": device_id, "temperature": temperature - 273, "execution_time": execution_time})

class MaxTemperatureFunctionReducer(ReduceFunction):

    def reduce(self, v1, v2):
        if v1.temperature > v2.temperature:
            return v1
        else:
            return v2



if __name__ == '__main__':
    python_data_stream_example()
