
The Print label service is a daemon that listens to 
messages on mqtt and prints a QR code and name, telephone and email on that label.

## Prepare installation

```sudo pip3 install qrcode brother_ql paho-mqtt```

## Running
```./print_label_service.py```

## Testing
mosquitto_pub -h mqtt.bitraf.no  -t "public/p2k16-dev/label/" -m '{"username": "test", "id": 1, "name": "Test Test", "phone": "01234567", "email": "test@example.com"}'