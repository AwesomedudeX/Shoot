import time
import numpy as np
import streamlit as st
from playsound import playsound as ps
from pydub import AudioSegment as aseg
from pydub.playback import play

st.title("Shoot")
st.write("(Note: Guns and statistical differences may vary from their real-world counterparts due to weapon balancing.)")

st.write("Add realistic damage for shotguns (separate chance for each pellet to hit)")

realism = st.sidebar.checkbox("Statistical Realism (may not be fully accurate)")

if realism:

    smg = {
        "MP5": [30, 95, 20, 420, 3, "9 x 19mm Parabellum", "Heckler & Koch", "mp5"],
        "P90": [50, 70, 10, 800, 5, "5.7 x 28mm FN", "FN Herstal", "p90"],
        "AR-57": [50, 90, 15, 300, 4, "5.7 x 28mm FN", "AR57 LLC", "ar-57"],
        "UMP45": [25, 85, 25, 370, 3, ".45 ACP", "Heckler & Koch", "ump45"],
        "UMP9": [30, 85, 20, 400, 3, "9 x 19mm Parabellum", "Heckler & Koch", "ump9"],
        "AK-74u": [30, 80, 25, 250, 3, "5.45 x 39mm Soviet", "Mikhail Kalashnikov", "ak-74u"]
    }
    ar = {
        "M4": [30, 90, 35, 400, 4, "5.56 x 45mm NATO", "Colt Firearms", "m4"],
        "AR-15": [10, 85, 80, 50, 5, ".458 SOCOM", "ArmaLite Colt's Manufacturing Company", "ar-15"],
        "AKM": [30, 80, 40, 200, 3, "7.62 x 39mm Soviet", "Mikhail Kalashnikov", "akm"],
        "AK-105": [30, 85, 30, 230, 3, "5.45 x 39mm Soviet", "Mikhail Kalashnikov", "ak-105"],
        "AS VAL": [20, 95, 45, 300, 3, "9 x 39mm Subsonic", "TsNIITochMash Pyotr Serdyukov and Vladimir Krasnikov", "as-val"]
    }
    lmg = {
        "DP-28": [47, 85, 52, 350, 7, "7.62 x 54mmR", "Vasiliy Alekseevich Degtyarev,", "dp-28"],
        "PKM": [100, 85, 50, 250, 10, "7.62 x 54mmR", "Mikhail Kalashnikov", "pkm"],
        "M249 SAW": [75, 85, 35, 350, 9, "5.56 x 45mm NATO", "FN Manufacturing LLC", "m249"]
    }
    sg = {
        "Remington 870": [7, 50, 150, 60, 7, "12 Guage Buckshot", "Remington Arms", "m870"],
        "MP220": [2, 80, 250, 120, 3, "12 Guage Buckshot", "Baikal", "mp220"],
        "Saiga-12": [10, 30, 120, 150, 3, "12 Guage Buckshot", "Kalashnikov Concern", "saiga-12"],
        "AA-12": [12, 35, 110, 200, 4, "12 Guage Buckshot", "Maxwell Atchisson", "aa-12"]
    }
    pistol = {
        "Glock 19": [17, 70, 15, 240, 2, "9 x 19mm Parabellum", "Glock Ges.m.b.H", "g19"],
        "Sig Sauer M17": [13, 70, 18, 250, 2, "9 x 19mm Parabellum", "Sig Sauer", "m17"],
        "Colt M1911": [8, 65, 30, 300, 2, ".45 ACP", "Colt Firearms", "m1911"],
        "Desert Eagle": [7, 60, 50, 120, 3, ".50 AE", "Magnum Research Inc.", "desert-eagle"]
    }

else:

    smg = {
        "MP5": [30, 90, 15, 420, 3, "9 x 19mm Parabellum", "Heckler & Koch", "mp5"],
        "P90": [50, 75, 10, 800, 5, "5.7 x 28mm FN", "FN Herstal", "p90"],
        "AR-57": [50, 85, 7, 300, 4, "5.7 x 28mm FN", "AR57 LLC", "ar-57"],
        "UMP45": [25, 80, 25, 370, 3, ".45 ACP", "Heckler & Koch", "ump45"],
        "UMP9": [30, 85, 20, 400, 3, "9 x 19mm Parabellum", "Heckler & Koch", "ump9"],
        "AK-74u": [30, 65, 25, 250, 3, "5.45 x 39mm Soviet", "Mikhail Kalashnikov", "ak-74u"]
    }
    ar = {
        "M4": [30, 90, 20, 400, 4, "5.56 x 45mm NATO", "Colt Firearms", "m4"],
        "AR-15": [10, 80, 60, 50, 5, ".458 SOCOM", "ArmaLite Colt's Manufacturing Company", "ar-15"],
        "AKM": [30, 75, 30, 200, 3, "7.62 x 39mm Soviet", "Mikhail Kalashnikov", "akm"],
        "AK-105": [30, 85, 25, 230, 3, "5.45 x 39mm Soviet", "Mikhail Kalashnikov", "ak-105"],
        "AS VAL": [20, 90, 35, 300, 3, "9 x 39mm Subsonic", "TsNIITochMash Pyotr Serdyukov and Vladimir Krasnikov", "as-val"]
    }
    lmg = {
        "DP-28": [47, 85, 20, 350, 7, "7.62 x 54mmR", "Vasiliy Alekseevich Degtyarev,", "dp-28"],
        "PKM": [100, 55, 15, 250, 10, "7.62 x 54mmR", "Mikhail Kalashnikov", "pkm"],
        "M249 SAW": [75, 30, 35, 350, 9, "5.56 x 45mm NATO", "FN Manufacturing LLC", "m249"]
    }
    sg = {
        "Remington 870": [7, 50, 150, 60, 7, "12 Guage Buckshot", "Remington Arms", "m870"],
        "MP220": [2, 80, 250, 120, 3, "12 Guage Buckshot", "Baikal", "mp220"],
        "Saiga-12": [10, 30, 120, 150, 3, "12 Guage Buckshot", "Kalashnikov Concern", "saiga-12"],
        "AA-12": [12, 35, 110, 200, 4, "12 Guage Buckshot", "Maxwell Atchisson", "aa-12"]
    }
    pistol = {
        "Glock 19": [17, 70, 15, 240, 2, "9 x 19mm Parabellum", "Glock Ges.m.b.H", "g19"],
        "Sig Sauer M17": [13, 70, 18, 250, 2, "9 x 19mm Parabellum", "Sig Sauer", "m17"],
        "Colt M1911": [8, 65, 35, 300, 2, ".45 ACP", "Colt Firearms", "m1911"],
        "Desert Eagle": [7, 55, 50, 120, 3, ".50 AE", "Magnum Research Inc.", "desert-eagle"]
    }


c1, c2 = st.columns(2)

gunclass = c1.selectbox("What gun class do you want to use?", ["Submachine Guns (SMGs)", "Assault Rifles/Battle Rifles", "Light Machine Guns (LMGs)", "Shotguns", "Pistols"])

if gunclass == "Submachine Guns (SMGs)":
    gunlist = smg
    sound = "SMG"
elif gunclass == "Assault Rifles/Battle Rifles":
    gunlist = ar
    sound = "AR"
elif gunclass == "Light Machine Guns (LMGs)":
    gunlist = lmg
    sound = "LMG"
elif gunclass == "Shotguns":
    gunlist = sg
    sound = "SG"
elif gunclass == "Pistols":
    gunlist = pistol
    sound = "Pistol"

gun = c2.selectbox("What gun do you want to use?", gunlist)

if "ammo" not in st.session_state or "dmg" not in st.session_state or "hits" not in st.session_state or "misses" not in st.session_state or "hit" not in st.session_state:
    st.session_state.ammo = gunlist[gun][0]
    st.session_state.dmg = 0
    st.session_state.hits = 0
    st.session_state.misses = 0
    st.session_state.hit = False

st.write("---")

if st.sidebar.checkbox("Show Selected Gun Statistics"):

    st.header(gunclass)

    st.write(f"\n{'-'*len(gun)}\n{gun}\n{'-'*len(gun)}\n\n")
    st.image(f"Images/{gunlist[gun][7]}.jpg")
    st.write(f"**Magazine Capacity:** {gunlist[gun][0]} Rounds")
    st.write(f"**Accuracy:** {gunlist[gun][1]}%")
    st.write(f"**Damage:** {gunlist[gun][2]}")
    st.write(f"**Firerate:** {gunlist[gun][3]} RPM")
    st.write(f"**Reload Time:** {gunlist[gun][4]} Seconds")
    st.write(f"**Ammo Type:** {gunlist[gun][5]}")
    st.write(f"**Manufacturer/Designer:** *{gunlist[gun][6]}*")
    st.write("---")

st.sidebar.header("Controls")

c3, c4, c5 = st.sidebar.columns(3)

if c3.button("Shoot"):
        
    if st.session_state.ammo != 0:

        try:
            sound = aseg.from_wav(f"Shoot.mp3")
            play(sound)

        except:
            st.write("You're pulling the trigger too fast!")

        st.session_state.ammo -= 1
        st.session_state.hit = np.random.randint(1, 101)

        if st.session_state.hit < gunlist[gun][1]:
            st.session_state.dmg += gunlist[gun][2]
            st.session_state.hits += 1
            st.write(f"Hit! Total Damage Dealt: {st.session_state.dmg}")

        else:
            st.session_state.misses += 1
            st.write(f"Miss! Total Damage Dealt: {st.session_state.dmg}")

    else:

        try:
            ps("Click.mp3")
            st.write(f"\*click!\*")
        except:
            st.write(f"\*click!\*")


if c4.button("Mag Dump"):
    
    ps("MagDump.mp3")
    
    while st.session_state.ammo > 0:

        st.session_state.ammo -= 1
        st.session_state.hit = np.random.randint(1, 101)

        if st.session_state.hit < gunlist[gun][1]:
            st.session_state.dmg += gunlist[gun][2]
            st.session_state.hits += 1

        else:
            st.session_state.misses += 1
        
        time.sleep(60/gunlist[gun][3])

        try:
            ps("Click.mp3")
            st.write(f"\*click!\*")
        except:
            st.write(f"\*click!\*")

if c3.button("Reload"):
    
    if gun != "M870":

        if gun in ["MP5", "UMP45", "UMP9"]:
            
            try:
                ps("H&KReload.mp3")
                st.sidebar.write("Reloading!")
            except:
                st.sidebar.write("Already Reloading!")

        time.sleep(gunlist[gun][4])
        st.session_state.ammo = gunlist[gun][0]
        st.session_state.dmg = 0
        st.session_state.hits = 0
        st.session_state.misses = 0
        st.sidebar.write(f"Reload Complete. **Remaining Ammo: {st.session_state.ammo}**")
    else:
        while st.session_state.ammo < gunlist[gun][0]:
            time.sleep(1)
            st.session_state.ammo += 1

if st.session_state.hits == 0 and st.session_state.misses == 0:
    st.session_state.ammo = gunlist[gun][0]

if st.session_state.ammo > 0:
    magcheck = c4.button("Check Mag")
else:
    magcheck = False

if magcheck:

    if st.session_state.ammo == 1:
        st.sidebar.write(f"{st.session_state.ammo} Round Remaining.")
    else:
        st.sidebar.write(f"{st.session_state.ammo} Rounds Remaining.")

if st.session_state.ammo < gunlist[gun][0]:

    st.sidebar.subheader("")
    
    if st.sidebar.button("Finish Session"):

        if st.session_state.hits == 1:
            hits = f"{st.session_state.hits} hit"
        else:
            hits = f"{st.session_state.hits} hits"
        
        if st.session_state.misses == 1:
            misses = f"{st.session_state.misses} miss"
        else:
            misses = f"{st.session_state.misses} misses"

        st.write(f"You dealt a total of {st.session_state.dmg} damage with {hits} and {misses}!")
        st.session_state.hits, st.session_state.misses, st.session_state.dmg = (0, 0, 0)
