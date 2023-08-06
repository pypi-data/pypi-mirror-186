from watsoncrdp import rdp as wrdp

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:00:00 2019
@author: omu
Correction of raw sensordata in CALYPSO
"""

import json
import os
import sys
import time

import numpy as np
import pandas as pd
import psycopg2
import psycopg2.extras

CONNECTION = None
schema = "sensor"


def get_insert_statement(decoded, table, update=None):
    columns = list(decoded)
    column_string = ",".join(columns)
    strings = []
    for col in columns:
        if pd.api.types.is_numeric_dtype(decoded[col]):
            strings.append("%s")
        else:
            strings.append("'%s'")

    strings = "({})".format(",".join(strings))
    insert_qry = f"INSERT INTO {table} ({column_string}) VALUES "
    insert_values = ",".join(strings % tup for tup in decoded.itertuples(index=False))
    insert_values = insert_values.replace("'None'", "Null")
    insert_values = insert_values.replace("nan", "Null")
    insert_values = insert_values.replace("'Null'", "Null")
    if update:
        update_cols = ", ".join([f"{name} = EXCLUDED.{name}" for name in columns])
        extra = f" ON CONFLICT ({update}) DO UPDATE SET {update_cols};"
    else:
        extra = ";"
    return insert_qry + insert_values + extra

def get_connection():
    global CONNECTION
    if not CONNECTION:
        CONNECTION = psycopg2.connect(
            dbname="watsonc",
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            host=os.environ["DB_HOST"],
            options=f"-c search_path={schema}",
        )
    return CONNECTION


def get_all_data(ts_id):
    conn = get_connection()

    statement = f"""SELECT timeofmeas, measurement FROM sensordata_corrected
        WHERE ts_id = {ts_id}"""

    data = pd.read_sql(statement, con=conn)

    statement = f"DELETE FROM sensordata_reduced where ts_id = {ts_id}"
    with conn.cursor() as curr:
        curr.execute(statement)
        conn.commit()

    data["timeofmeas"] = pd.to_datetime(data["timeofmeas"], utc=True).dt.tz_convert(
        "Europe/Copenhagen"
    )

    data = data.drop_duplicates(subset=["timeofmeas"])
    data = data.dropna()

    data = data.set_index("timeofmeas")
    data = data.sort_index(ascending=True)
    return data


start = time.time()
data_orig = get_all_data(1411)
data = data_orig.copy()
timeofmeas = data.index.astype(np.int64).tolist()
measurements = data.measurement.tolist()
points = list(zip(timeofmeas, measurements))
epsilon = 0.001
minimum = 2

rd2, order, dis = wrdp(points, epsilon=epsilon, min_points=minimum)
end = time.time()
print(f"before: {len(measurements)} after: {len(rd2)} time: {end-start}")
print(dis)


data["dist"] = dis
data["ts_id"] = 1411
data = data.reset_index()

od = list(zip(dis, order))
od.sort(reverse=True)

start = time.time()
data_reduced = pd.DataFrame(rd2, columns=["timeofmeas", "measurement"])
data_reduced["timeofmeas"] = pd.to_datetime(
    data_reduced["timeofmeas"], utc=True
).dt.tz_convert("Europe/Copenhagen")
data_reduced = data_reduced.set_index("timeofmeas")


data_important = pd.DataFrame(
    [p for i, p in enumerate(points) if dis[i] > 0.0002],
    columns=["timeofmeas", "measurement"],
)
data_important["timeofmeas"] = pd.to_datetime(
    data_important["timeofmeas"], utc=True
).dt.tz_convert("Europe/Copenhagen")

data_important = data_important.set_index("timeofmeas")
data_important = data_important.sort_index(ascending=True)

data_reduced.plot(backend="plotly", title="Reduced data")
data_important.plot(backend="plotly", title="Important data")

# if len(rd2) > 100000:
#     # data = data.rolling(window=5, center=True).mean().dropna()
#     data = data.resample("1H").mean()
#     timeofmeas = data.index.astype(np.int64).tolist()
#     measurements = data.measurement.tolist()
#     rd2 = wrdp(list(zip(timeofmeas, measurements)), epsilon=epsilon, min_points=minimum)

#     data_reduced = pd.DataFrame(rd2, columns=["timeofmeas", "measurement"])
#     data_reduced["timeofmeas"] = pd.to_datetime(
#         data_reduced["timeofmeas"], utc=True
#     ).dt.tz_convert("Europe/Copenhagen")
#     data_reduced = data_reduced.set_index("timeofmeas")

# print(f"before: {len(measurements)} after: {len(rd2)} time: {end-start}")

# freq = 24

# my_range = pd.date_range(
#     start=data_reduced.index.date.min(),
#     end=data_reduced.index.date.max(),
#     freq=f"{freq}H",
# ).tz_localize("Europe/Copenhagen", nonexistent="shift_forward")


# # diff = my_range.difference(data_reduced.index.date).tz_localize("Europe/Copenhagen")

# diff = pd.merge_asof(
#     pd.DataFrame(my_range + pd.Timedelta(hours=freq // 2), columns=["time"]),
#     data_reduced.reset_index(),
#     left_on="time",
#     right_on="timeofmeas",
#     direction="nearest",
#     tolerance=pd.Timedelta(hours=freq // 2),
# )

# diff = diff[diff.timeofmeas.isnull()].time

# merged = pd.merge_asof(
#     pd.DataFrame(diff, columns=["time"]),
#     data.reset_index(),
#     left_on="time",
#     right_on="timeofmeas",
#     direction="nearest",
#     tolerance=pd.Timedelta(hours=freq // 2),
# ).dropna()
# merged = merged.set_index("timeofmeas").drop(columns=["time"])

# out = pd.concat((merged, data_reduced)).sort_index()
# end = time.time()
# print(f"before: {len(rd2)} after: {len(out)} time: {end-start}")

# data.plot(x="timeofmeas", y="measurement")
# plt.show()
