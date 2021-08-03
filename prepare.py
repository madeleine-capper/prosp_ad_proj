import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
def prepare_logs():
    data_arr = []
    with open('webservertrafficlog/access.log') as log:
        for line in log.readlines():
            match = re.match(r'(.+) - - \[(\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}) \+\d{4}\] \"(\w+) .+', line)
            if match:
                data_arr.append([match.group(1), match.group(2), match.group(3)])

    data = pd.DataFrame(data_arr, columns=['ip_address', 'datetime', 'request_type'])

    data['datetime'] = data.datetime.apply(lambda x: x.replace('Jan', '01'))
    data['datetime'] = pd.to_datetime(data.datetime, format='%d/%m/%Y:%H:%M:%S')

    #add datetime columns to group by

    data['day'] = data['datetime'].apply(lambda x: x.day)
    data['hour'] = data['datetime'].apply(lambda x: x.hour)
    data['minute'] = data['datetime'].apply(lambda x: x.minute)

    #aggregate by minute and by hour
    return data
    

    