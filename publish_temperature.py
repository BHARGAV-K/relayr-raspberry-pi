    while True:
        client.loop()
        # read sensor
        device_id = '28-0000075dbdd5'
        sensor_value = read_temperature(device_id)
        # publish temerature data
        message = {
            'meaning': 'temperature',
            'value': sensor_value
        }
        client.publish(credentials['topic'] + 'data', json.dumps(message))
        time.sleep(publishing_period / 1000.)
