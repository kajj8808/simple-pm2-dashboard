import pandas as pd
import streamlit as st
import subprocess
import json


def get_pm2_status():
    result = subprocess.run(["pm2", "jlist"], stdout=subprocess.PIPE)
    pm2_items = json.loads(result.stdout)

    return [
        {
            "pm_id": item["pm_id"],
            "pid": item["pid"],
            "name": item["name"],
            "cpu": item["monit"]["cpu"],
            "memory": item["monit"]["memory"],
            "status": item["pm2_env"]["status"],
        } for item in pm2_items
    ]


def restart_process(pm_id):
    result = subprocess.run(
        ["pm2", "restart", str(pm_id)],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        st.code(f""" `{pm_id}` Process Restart Succeful⭐""")


st.set_page_config(
    page_title="PM2 Kajj8808",
    page_icon="🔮"
)


st.title("Pm2 Dashboard")


pm2_status = get_pm2_status()

df = pd.DataFrame(pm2_status)
st.dataframe(df)

with st.container():
    for status in pm2_status:
        col1, col2 = st.columns(2)
        col1.write(f"`{status['pm_id']}` {status['name']}")
        if col2.button("restart", key=f"restart-{status['name']}"):
            restart_process(status['pm_id'])
