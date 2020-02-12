from http.server import BaseHTTPRequestHandler
import pandas as pd

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        df = pd.read_csv('../data/csv/Day-ahead Prices_201901010000-202001010000.csv',skiprows=1,names=['mtu','price_mwh'])
        df['price_kwh'] = df['price_mwh'] / 1000
        df = df.drop(['price_mwh'], axis=1)
        new = df['mtu'].str.split(' - ',n=1,expand=True)
        df['mtu_start'] = pd.to_datetime(new[0])
        #df['mtu_stop'] = pd.to_datetime(new[1])
        df = df.drop(['mtu'], axis=1)
        #df = df.drop(['mtu_stop'], axis=1)
        df = df.sort_index(axis=1)
        df = df.set_index('mtu_start')
        mean_hour = df.groupby(df.index.hour).mean()
        message = print(df)
        self.wfile.write(message.encode())
        return
