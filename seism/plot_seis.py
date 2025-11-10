import obspy
import matplotlib.pyplot as plt
from obspy import read, Stream
####

st=read('220910_234700_AK.DHY..BHZ.sac')
st1=read('220910_234700_AK.DIV..BHZ.sac')
st2=read('220910_234700_AK.A22K..BHZ.sac')

st_all=read('220910_*..BHZ.sac')

st_all.filter('bandpass', freqmin=0.05, freqmax=.3)
# st.plot(color='ivory',bgcolor='black', orientation="horizontal", linewidth=.5)
st_all.plot(color='slateblue',bgcolor='linen', orientation="horizontal", linewidth=2)
