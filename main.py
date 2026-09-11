import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

df_l = pd.read_excel("CARGAS_GENERAL.xlsx")
secciones = ["P01", "P02"]


stories = df_l["Story"].unique()
piers = df_l["Pier"].unique()
locs = df_l["Loc"].unique()

d_nuevo = {"pier": [], "stat": [], "combo": [], "P": [], "M2": [], "M3": []}

for story in stories:
    for pier in piers:
        for loc in locs:
            df_1 = df_l[df_l["Story"] == story]
            df_2 = df_1[df_1["Pier"] == pier]
            df_3 = df_2[df_2["Loc"] == loc].sort_values(by="Load", ascending=True).reset_index(drop=True)
            
            # Cargas
            P = {"D": df_3.iloc[0,4], "L": df_3.iloc[1,4], "SX": df_3.iloc[2,4], "SY": df_3.iloc[4,4]}
            M2 = {"D": df_3.iloc[0,8], "L": df_3.iloc[1,8], "SX": df_3.iloc[2,8], "SY": df_3.iloc[4,8]}
            M3 = {"D": df_3.iloc[0,9], "L": df_3.iloc[1,9], "SX": df_3.iloc[2,9], "SY": df_3.iloc[4,9]}
            # Combo 1
            d_nuevo["pier"].append(pier)
            d_nuevo["stat"].append(story+"-"+loc)
            d_nuevo["combo"].append("C1")
            d_nuevo["P"].append(1.4*P["D"] + 1.7*P["L"])
            d_nuevo["M2"].append(1.4*M2["D"] + 1.7*M2["L"])
            d_nuevo["M3"].append(1.4*M3["D"] + 1.7*M3["L"])
            # Combo 2A
            d_nuevo["pier"].append(pier)
            d_nuevo["stat"].append(story+"-"+loc)
            d_nuevo["combo"].append("C2A")
            d_nuevo["P"].append(1.25*P["D"] + 1.25*P["L"] + P["SX"])
            d_nuevo["M2"].append(1.25*M2["D"] + 1.25*M2["L"] + M2["SX"])
            d_nuevo["M3"].append(1.25*M3["D"] + 1.25*M3["L"] + M3["SX"])
            # Combo 2B
            d_nuevo["pier"].append(pier)
            d_nuevo["stat"].append(story+"-"+loc)
            d_nuevo["combo"].append("C2B")
            d_nuevo["P"].append(1.25*P["D"] + 1.25*P["L"] - P["SX"])
            d_nuevo["M2"].append(1.25*M2["D"] + 1.25*M2["L"] - M2["SX"])
            d_nuevo["M3"].append(1.25*M3["D"] + 1.25*M3["L"] - M3["SX"])
            # Combo 3A
            d_nuevo["pier"].append(pier)
            d_nuevo["stat"].append(story+"-"+loc)
            d_nuevo["combo"].append("C3A")
            d_nuevo["P"].append(1.25*P["D"] + 1.25*P["L"] + P["SY"])
            d_nuevo["M2"].append(1.25*M2["D"] + 1.25*M2["L"] + M2["SY"])
            d_nuevo["M3"].append(1.25*M3["D"] + 1.25*M3["L"] + M3["SY"])
            # Combo 3B
            d_nuevo["pier"].append(pier)
            d_nuevo["stat"].append(story+"-"+loc)
            d_nuevo["combo"].append("C3B")
            d_nuevo["P"].append(1.25*P["D"] + 1.25*P["L"] - P["SY"])
            d_nuevo["M2"].append(1.25*M2["D"] + 1.25*M2["L"] - M2["SY"])
            d_nuevo["M3"].append(1.25*M3["D"] + 1.25*M3["L"] - M3["SY"])
            # Combo 4A
            d_nuevo["pier"].append(pier)
            d_nuevo["stat"].append(story+"-"+loc)
            d_nuevo["combo"].append("C4A")
            d_nuevo["P"].append(0.9*P["D"] + P["SX"])
            d_nuevo["M2"].append(0.9*M2["D"] + M2["SX"])
            d_nuevo["M3"].append(0.9*M3["D"] + M3["SX"])
            # Combo 4B
            d_nuevo["pier"].append(pier)
            d_nuevo["stat"].append(story+"-"+loc)
            d_nuevo["combo"].append("C4B")
            d_nuevo["P"].append(0.9*P["D"] - P["SX"])
            d_nuevo["M2"].append(0.9*M2["D"] - M2["SX"])
            d_nuevo["M3"].append(0.9*M3["D"] - M3["SX"])
            # Combo 5A
            d_nuevo["pier"].append(pier)
            d_nuevo["stat"].append(story+"-"+loc)
            d_nuevo["combo"].append("C5A")
            d_nuevo["P"].append(0.9*P["D"] + P["SY"])
            d_nuevo["M2"].append(0.9*M2["D"] + M2["SY"])
            d_nuevo["M3"].append(0.9*M3["D"] + M3["SY"])
            # Combo 5B
            d_nuevo["pier"].append(pier)
            d_nuevo["stat"].append(story+"-"+loc)
            d_nuevo["combo"].append("C5B")
            d_nuevo["P"].append(0.9*P["D"] - P["SY"])
            d_nuevo["M2"].append(0.9*M2["D"] - M2["SY"])
            d_nuevo["M3"].append(0.9*M3["D"] - M3["SY"])

df_nuevo = pd.DataFrame(d_nuevo)
fig, ax = plt.subplots(1,2, figsize=(16,8), dpi=200)

asdasd = 1

for seccion in secciones:

    df = pd.read_excel("DIAGRAMAS_PANASOLES.xlsx", sheet_name=seccion, skiprows=1)

    a = df.iloc[:,1:3]
    a.columns = ["P", "M3"]
    b = df.iloc[:,37:39]
    b.columns = ["P", "M3"]
    diag_0 = pd.concat([a,b], ignore_index=True)

    c = df.iloc[:,19:22:2]
    c.columns = ["P", "M2"]
    d = df.iloc[:,55:58:2]
    d.columns = ["P", "M2"]
    diag_90 = pd.concat([c,d], ignore_index=True)

    if seccion in ["P01", "P02", "P03"]:
        ax[0].plot(diag_0["M3"], diag_0["P"], "--", color="r" if seccion == "P01" else "gray", label=seccion, lw=2)
        ax[1].plot(diag_90["M2"], diag_90["P"], "--", color="r" if seccion == "P01" else "gray", label=seccion, lw=2)
    else:
        ax[0].plot(diag_0["M3"], diag_0["P"], "--", label=seccion)
        ax[1].plot(diag_90["M2"], diag_90["P"], "--", label=seccion)

ax[0].plot([-100,100],[0,0], color='k', lw=3)
ax[0].plot([0,0],[-100,100], color='k', lw=3)
ax[1].plot([-20,20],[0,0], color='k', lw=3)
ax[1].plot([0,0],[-100,100], color='k', lw=3)

ax[0].set_title("Diagrama a 0°")
ax[1].set_title("Diagrama a 90°")

for i in range(2):
    ax[i].set_xlabel("M (ton-m)")
    ax[i].set_ylabel("P (ton)")
    ax[i].invert_yaxis()
    ax[i].grid()
    ax[i].legend()

with st.sidebar:
    filtro = st.pills("PIERS", options=df_nuevo["pier"].unique(), selection_mode="multi")
    filtro

#df_filtrado = df_nuevo[df_nuevo["pier"].isin(filtro)]

for p in filtro:
    df_filtrado = df_nuevo[df_nuevo["pier"] == p]
    ax[0].plot(df_filtrado["M3"], df_filtrado["P"], marker="o", lw=0, ms=4, label=p)
    ax[1].plot(df_filtrado["M2"], df_filtrado["P"], marker="o", lw=0, ms=4, label=p)

for i in range(2):
    ax[i].legend()

st.pyplot(fig)