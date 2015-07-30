#
# script generated by cfview version 0.3.1
#                      
import cf, cfplot as cfp

cfp.gopen(columns=2, rows=2)
cfp.gpos(pos=1)
#Read data
sfield=cf.read('/home/andy/ggap.nc')[10]

#Apply operators
sfield=sfield.collapse('mean',axes='longitude')

#Make contour plot
cfp.con(sfield,title='/home/andy/ggap.nc mean:longitude  time:0.0 ')


#Move to next plot position
cfp.gpos(pos=2)

#Read data
sfield=cf.read('/home/andy/ggap.nc')[7]

#Apply operators
sfield=sfield.collapse('mean',axes='longitude')

#Make contour plot
cfp.con(sfield,title='/home/andy/ggap.nc mean:longitude  time:0.0 ')


#Move to next plot position
cfp.gpos(pos=3)

#Read data
sfield=cf.read('/home/andy/ggap.nc')[2]

#Subspace the data
sfield=sfield.subspace(pressure=1000.0)

#Make contour plot
cfp.con(sfield,title='/home/andy/ggap.nc  time:0.0  pressure:1000.0 ')


#Move to next plot position
cfp.gpos(pos=4)

#Read data
sfield=cf.read('/home/andy/ggap.nc')[8]

#Subspace the data
sfield=sfield.subspace(pressure=500.0)


#Set mapping
cfp.mapset(proj='npstere')

#Make contour plot
cfp.con(sfield,title='/home/andy/ggap.nc  time:0.0  pressure:500.0 ')

cfp.gclose()