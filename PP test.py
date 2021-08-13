# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 10:48:52 2021

@author: juarez
"""
import pandapower as pp

net =pp.create_empty_network(name="empty")

#create buses
b1=pp.create_bus(net,vn_kv=20., name="bus 1")
b2=pp.create_bus(net,vn_kv=.4, name="bus 2")
b3=pp.create_bus(net,vn_kv=.4, name="bus 3")

#external grid
pp.create_ext_grid(net,b1,vm_pu=1.02, name="external grid") #nv_kv=20.*1.02

#create transformer
#print(pp.available_std_types(net,"trafo"))
pp.create_transformer(net,b1,b2,std_type="0.4 MVA 20/0.4 kV")



#create line
#print(pp.available_std_types(net,"line"))
pp.create_line(net,b2,b3, std_type="NAYY 4x50 SE", length_km=0.1, name="line")

#create load
pp.create_load(net,b3,p_mw=0.1, q_mvar=0.05)
pp.create_sgen(net,b3,p_mw=0.1)

pp.runpp(net)
print(net.res_bus)

