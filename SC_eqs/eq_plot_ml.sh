#! /bin/bash

#ogr2ogr -f "GMT" aus5wgd_l.gmt  aus5wgd_l.shp -t_srs WGS84
PS=map_SC.ps
#set Rmap=-Rg
#set Rmap=-R-135/40/-90/90
Rmap="-R-83.4/-78.289/31.94/35.35" #SC
#set J=-JM8/22
J="-JM12/11" #sa
#set J=-Jx0.023i/0.029i

#set topogrd = /Users/shubham/Research/etopo/etopo_sa_15s.grd

# set oleron = ~/Documents/ScientificColourMaps5/oleron/oleron.cpt
#set afrikakarte = ~/Documents/cpt-city/wkp/lilleskut/afrikakarte

eq_all4minus="eq_sc_all_4minus.txt"
eq_all4plus="eq_sc_all_4plus.txt"

#ßset eq_NA = ~/Dropbox/NA_temp/relocated_eqs/round_1/relocated_eq_na_aust.txt


#sort -k4 -n -r relocated_eq_na_mlv_FINAL.txt > relocated_FINAL_mlsorted.txt

gmt gmtset MAP_FRAME_TYPE plain MAP_FRAME_WIDTH 3p FONT_ANNOT_PRIMARY 9.5p MAP_TICK_LENGTH_PRIMARY 3p MAP_FRAME_PEN 2.2p


gmt psbasemap -BneWS -Bxa1f.25 -Bya1f.25 $J $Rmap -K > $PS

#gmt6 grdimage $topogrd $J $Rmap -CETOPO1.cpt -K -O -P  >> $PS
#gmt6 pscoast  $Rmap $J -B -Na/.005p -Ia -A1000 -P -Sazure -Glightgrey -Di -O -W.01p -K >> $PS
#pscoast -Rg -J -B15g15 -Dc -A10000 -Glightgrey -P -O -W.01p -K >> map.ps
#gmt6 xyz2grd $Rmap $J -I.017 $topoxyz -Gtopo.grd -V
# gmt6 makecpt -Fgray -Cetopo1 -V > etopocolor.cpt # etopo1, -A

#gmt6 makecpt -C$oleron -T-700/700/50 > oleron1.cpt
#gmt6 makecpt -C$tpushuf -T0/900/50 > tpushuf.cpt

#gmt makecpt -C$afrikakarte -T-1320/720/10 > afrikakarte.cpt

# gmt6 grdimage $topogrd $J $Rmap -Bx -By -FRgray -Cafrikakarte.cpt -I+nt.85 -K -O >> $PS # original color
#gmt grdimage $topogrd $J $Rmap -Bx -By -Cfes.cpt -I+nt.85 -K -O >> $PS # gray scale
#gmt pscoast $Rmap $J -Bx -By -Na/.05p -A10 -P -K -Di -O -W.1p >> $PS #-A10+l -Ia

gmt pscoast $Rmap $J -Bx -By -Na/.65p,darkolivegreen -A1 -P -Slightsteelblue@50 -Ia/.3p,navy -Gwhitesmoke@30 -K -Df -O -W.1p >> $PS #-GSeashell FloralWhite Ivory

#geological features
# gmt6 psxy ~/Research/Lake_eyre_data/geological_ft/CrustalBoundaries.txt $Rmap $J -W1.05p,gray -O -K -V >> $PS ### crustal boundary
#awk '{print $1,$2+.18,$3}' ~/Research/Lake_eyre_data/station/old_mix_stuff/per_st.txt | gmt6 pstext $Rmap $J -: -F+f3.5p,Helvetica-Bold -Gwhite -O -P -K >> $PS

#cat
# awk '{print $1,$2,$3,$4*.14}' $eq_NA_ml | gmt6 psxy $Rmap $J -: -Sc -W.15,black -Cdark_reds.cpt -t20 -B -O -P -K >> $PS # eq

#echo $char_eq
head -n1 $eq_all4plus | gmt psxy $Rmap $J -: -Sc2.5 -W.15,black -Gindianred -t60 -B -O -P -K >> $PS # eq
#
awk '{print $1,$2,$3*.08}' $eq_all4plus | gmt psxy $Rmap $J -: -Sc -W.15,black -Gindianred -t40 -B -O -P -K >> $PS # eq

awk '{print $1,$2,$3*.1}' $eq_all4minus | gmt psxy $Rmap $J -: -Sc.09 -W.3,black -Gwhite@95 -B -O -P -K >> $PS # eq


#
#Stations
awk '{print $3,$4}' scsn.txt | gmt psxy -: -W.5,beige -St.35 -Gdimgray@10 $J $Rmap -O -K >> $PS
# awk '{print $3-.06,$4,$2}' scsn.txt | gmt pstext $Rmap $J -: -F+f3p,Helvetica-Bold -Gwhite@10 -O -P -K >> $PS

#echo eqs

#
echo -79.28 33 Historic 1886 | gmt pstext $Rmap $J -F+f6.5p,Helvetica,darkred -Gwhite@10 -O -P -K  >> $PS
echo -79.2 32.91 Charleston earthquake | gmt pstext $Rmap $J -F+f6.5p,Helvetica,darkred -Gwhite@10 -O -P -K  >> $PS

echo -81.0348 34.0 | gmt psxy $Rmap $J -Ss.35 -W.35,white -Gdarkslateblue -t0 -B -O -P -K >> $PS # cola
echo -82.3940 34.8526 | gmt psxy $Rmap $J -Ss.25 -W.35,white -Gdarkslateblue -t0 -B -O -P -K >> $PS # cola
echo -78.8802 33.6954 | gmt psxy $Rmap $J -Ss.25 -W.35,white -Gdarkslateblue -t0 -B -O -P -K >> $PS # cola
echo -82.0105 33.4735 | gmt psxy $Rmap $J -Ss.25 -W.35,white -Gdarkslateblue -t0 -B -O -P -K >> $PS # cola
echo -79.9 32.776566 | gmt psxy $Rmap $J -Ss.25 -W.35,white -Gdarkslateblue -t0 -B -O -P -K >> $PS # Charleston
echo -79.196 33.3485 | gmt psxy $Rmap $J -Ss.25 -W.35,white -Gdarkslateblue -t0 -B -O -P -K >> $PS # bmfl




echo -80.68 34.0 Columbia  | gmt pstext $Rmap $J -F+f7.5p,Helvetica -O -P -K  >> $PS
echo -82.3940 34.7526 Greenville | gmt pstext $Rmap $J -F+f6.5p,Helvetica -O -P -K  >> $PS
echo -78.8102 33.5954 Myrtle Beach | gmt pstext $Rmap $J -F+f6.5p,Helvetica -O -P -K  >> $PS
echo -82.2705 33.4735 Augusta | gmt pstext $Rmap $J -F+f6.5p,Helvetica -O -P -K  >> $PS
echo -79.55 32.776 Charleston | gmt pstext $Rmap $J -F+f6.5p,Helvetica -O -P -K  >> $PS
echo -79 33.3485 BMFL | gmt pstext $Rmap $J -F+f5.5p,Helvetica -O -P -K  >> $PS

echo -80.72 34.16 | gmt psxy $Rmap $J -Sa.45 -W.35,darkgoldenrod -Ggold -t0 -B -O -P -K >> $PS # bmfl
echo -80.3 34.3 Elgin Swarm | gmt pstext $Rmap $J -F+f7.5p,Helvetica,darkgoldenrod -O -P -K  >> $PS


###
echo -79.23 35.25 Earthquakes of  | gmt pstext $Rmap $J -F+f12.5p,Courier  -Gwhite@5 -O -P -K  >> $PS
echo -79.23 35.09 South Carolina  | gmt pstext $Rmap $J -F+f12.5p,Courier  -Gwhite@5 -O -P -K  >> $PS

gmt gmtset FONT_ANNOT_PRIMARY 7p MAP_FRAME_PEN .8p FONT_LABEL 7.5p

#gmt psbasemap -B -V $J $Rmap -Lx1.7c/.6c+c32+w100k+l+f -Tdg-78.55/34.8+w.3i+f -O -P -K >> $PS

gmt psbasemap -B -V $J $Rmap -Tdg-78.55/34.8+w.3i+f -O -P -K >> $PS

# gmt6 psscale -Dx11.2c/1.4c+w2.6c/.24c+e -O -K -G-100/700 -Cafrikakarte.cpt -Bx200 -By+l"m"  >> $PS #-G-100/1000

#gmt6 psscale -Dx11.2c/2.2c+w4c/.24c+e -O -K -Cdark_reds.cpt -Bx3 -Bx+l"Depth (km)" >> $PS
#gmt6 pslegend -Dx1.2c/4c+w2.4c/1.6c+o-1c/-.5c -F+gwhite+p.1 -O -K $J $Rmap << EOF >> $PS
gmt pslegend -Dx1.31c/.8c+w3.5c/1.2c+o-1c/-.5c -F+gwhite+p.1 -O $J $Rmap << EOF >> $PS
# gmt pslegend -Dx1.31c/.8c+w1.5c/.5c+o-1c/-.5c -F+gwhite+p.1 -O $J $Rmap << EOF >> $PS

# S 0.2c t 0.35c dimgray - 0.2i SCSN
S 0.2c t 0.35c dimgray - 0.2i Our seismometers
S 0.2c c 0.12c white@40 .5p,black 0.2i low danger earthquakes
S 0.2c c 0.3c darkred@40 - 0.2i damaging earthquakes
#S 0.2c x 0.2c - .95p,firebrick 0.2i Eq (R_19 < 200)
EOF

####LEGEND
# gmt6 pslegend -DJLT+w2.15c/.27c+o-2.15c/-.27c -F+gwhite@10+p.05 -O -K $J $Rmap << EOF >> $PS
# #S 0.2c s 0.3c DarkOrange - 0.2i 1Ds-1Dp
# EOF

# echo Oct'20 - May'22 | gmt6 pstext $J $Rmap -F+cTL+f7.5p -O -P -V >> $PS
# echo GA catalog 1900 - | gmt6 pstext $J $Rmap -F+cTL+f9p,darkpurple -O -P -V >> $PS


gmt ps2raster -A -Tj -E720 -P -Z -Vq $PS
open map_SC.jpg
# cp map.pdf ~/Dropbox/map_na_aust_ml1.pdf
###
