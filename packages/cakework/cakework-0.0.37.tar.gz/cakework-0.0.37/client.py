from cakework import Client
import time 

client = Client("fly-machines-4", "fcbaadd4b7786f3eb000f3ff5932ef53dc5e65a32e9ed26b7f989044feca638b", local=True)

request_id = client.say_hello("jessie")
print(request_id)
status = client.get_status(request_id)
while status == 'PENDING' or status == 'IN_PROGRESS':
    time.sleep(1)
    status = client.get_status(request_id)
if status == 'SUCCEEDED':
    result = client.get_result(request_id)
    print(result)
else:
    print("Failed")
