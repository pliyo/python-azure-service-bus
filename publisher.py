from azure.servicebus import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME

namespaceName = 'yournamespace' # Your service bus name, ex: 'whatever' (without single quotes. forget about .servicebus.windows.net )
accessName = 'RootManageSharedAccessKey'  # Your name, ex: 'owner' or 'RootManageSharedAccessKey'
accessKey = 'G6Iaa12aaB1aaHcZ4ghTzJKxLp1nFxf2hs1ZqYCSB5Y=' # Your key: ex: G6Iaa12aaB1aaHcZ4ghTzJKxLp1nFxf2hs1ZqYCSB5Y=

bus_service = ServiceBusService(
    service_namespace=namespaceName,
    shared_access_key_name=accessName,
    shared_access_key_value=accessKey)

topicName = 'test';
subscriptionName = 'readers'

topic_options = Topic()
topic_options.max_size_in_megabytes = '5120'
topic_options.default_message_time_to_live = 'PT1M'

bus_service.create_topic(topicName, topic_options)

bus_service.create_subscription(topicName, subscriptionName)

for i in range(5):
    msg = Message('Msg {0}'.format(i).encode('utf-8'), custom_properties={'messagenumber':i})
    bus_service.send_topic_message(topicName, msg)

for i in range(5):
    msg = bus_service.receive_subscription_message(topicName, subscriptionName, peek_lock=False)
    print(msg.body)

print 'job done';
