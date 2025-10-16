import obspy
import matplotlib.pyplot as plt
from obspy import read, Stream
####

st=read('220910_234700_AK.DHY..BHZ.sac')
st1=read('220910_234700_AK.DIV..BHZ.sac')
st2=read('220910_234700_AK.A22K..BHZ.sac')

st2.filter('bandpass', freqmin=0.1, freqmax=.25)
# st.plot(color='ivory',bgcolor='black', orientation="horizontal", linewidth=.5)
st2.plot(color='lightpink',bgcolor='grey', orientation="horizontal", linewidth=.85)
