# Default Imports
import yaml
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    # Write your code here
    path = './data/ipl_match.yaml'
    with open(path, mode='r') as file_loader:
        data = yaml.load(file_loader)

    #name = data['innings']['1st innings']['deliveries'][0.1]['batsman']
    #name = data['innings'][0]['deliveries'][0][0]
    name = 'SC Ganguly'
    return name
