#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import datetime
import pandas as pd


def gateway_simulator(user_id: int, sensor_id: int, verbose=False):
    def timestamp_parser(epoch):
        return pd.to_datetime(epoch, unit='ms')

    base_filename = str(user_id) + '_sensor_' + str(sensor_id) + '_db.csv'

    # Abrir banco de dados completo
    input_filename = 'data/db/' + base_filename
    df_in = pd.read_csv(
        input_filename,
        date_parser=timestamp_parser,
        index_col='timestamp',
    )
    if verbose:
        print('in:', len(df_in))

    # Abrir o banco de dados da api
    output_filename = 'data/' + base_filename
    df_out = pd.read_csv(
        output_filename,
        date_parser=timestamp_parser,
        index_col='timestamp',
    )
    if verbose:
        print('out:', len(df_out))

    # buscar o último horário
    time_last_out = pd.Timestamp(df_out.tail(1).index.to_numpy()[0]).to_pydatetime()
    time_now = datetime.now().replace(microsecond=0, second=0, minute=0)
    if verbose:
        print('last:', time_last_out)
        print('now:', time_now)

    if time_last_out != time_now:

        # Selecionar linhas baseado no tempo atual
        df_sel = df_in.loc[time_last_out:time_now]
        if verbose:
            print('sel:', len(df_sel))

        # Enviar linhas para o banco de dados do sensor
        df_out = df_out.append(df_sel)
        if verbose:
            print('out:', len(df_out))

        # Convert to epoch in ms
        df_out.index = (df_out.index - pd.Timestamp("1970-01-01")) // pd.Timedelta('1ms')

        # salva
        df_out.to_csv(output_filename, float_format='%.4f')


if __name__ == '__main__':
    starttime = time.time()
    PERIOD = 10.0
    USER_ID = 0

    while True:
        for sensor_id in [0, 1]:
            gateway_simulator(USER_ID, sensor_id)
            time.sleep(PERIOD - ((time.time() - starttime) % PERIOD))
