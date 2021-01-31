import re
from aip import AipOcr
client = AipOcr('9913119','TmaBuMvfWHmTtq7Ta7swkYKw','iViuP8iDvVzXRyokLyi2mt15Gnyb02eA')
i = open(r'C:\Users\Queker\Desktop\pywork\20210112223521.png','rb')
img = i.read()
message = client.basicGeneral(img)
for i in message.get('words_result'):
    print(i.get('words'))