# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 12:15:44 2021

@author: Penghua Ying (hityingph@163.com)
"""
import numpy as np
import random as rd

lx = 50
ly = 50
lz = 3.35
bond_length = 1.42
defect_dens = 0.03 #For pristine graphene without defect, one should set this as zero.

uc_lx = np.sqrt(3) * bond_length
uc_ly = 3 * bond_length
uc_lz = 20
rp_x = int(lx/uc_lx) + 1
rp_y = int(ly/uc_ly) + 1

atom_num = int(4*rp_x*rp_y)
defect_num = int(atom_num*defect_dens)
defect_id = []
for i in range(defect_num):
    defect_id.append(rd.randint(1, atom_num))
    
atom1 = [0.25, 1/6, 0.5]
atom2 = [0.75, 1/3, 0.5]
atom3 = [0.75, 2/3, 0.5]
atom4 = [0.25, 5/6, 0.5]
atoms = [atom1, atom2, atom3, atom4]

atom_id = 0
new_atom_id = 0
atom_type = 0
atom_mass = 12.011

coord_type = []
coord_x = []
coord_y = []
coord_z = []
coord_mass = []
coord_id = []
for i in range(rp_x):
    for j in range(rp_y):
        for k in range(4):
            atom_id += 1
            position_x = atoms[k][0]*uc_lx + i*uc_lx
            position_y = atoms[k][1]*uc_ly + j*uc_ly
            position_z = atoms[k][2]*uc_lz
            if atom_id not in defect_id:
                coord_type.append(atom_type)
                coord_x.append(position_x)
                coord_y.append(position_y)
                coord_z.append(position_z)
                coord_mass.append(atom_mass)
                coord_id.append(new_atom_id)
                new_atom_id +=1
                # print(atom_id, atom_type, position_x, position_y, position_z)

### line 0
N = new_atom_id     #number of atoms
M = 3               #maximum number of neighbors
cutoff = 2.1        #initial cutoff distance used for building the neighbor list
box_shape = 0       #0:orthogonal; 1:triclinic
has_velocity = 0    #0:has initial velocity; 1:not has initial velocity 
number_of_grouping_methods = 1 #we use one grouping method here

### line 1
pbc_x = 1 #1:periodic; 0:free
pbc_y = 1 #1:periodic; 0:free
pbc_z = 0 #1:periodic; 0:free
L_x = uc_lx*rp_x
L_y = uc_ly*rp_y
L_z = lz


f = open("xyz.in", "w")
line0 = ' '.join(str(val) for val in [N, M, cutoff, box_shape, has_velocity, number_of_grouping_methods]) 
f.write(line0)
f.write("\n")
line1 = ' '.join(str(val) for val in [pbc_x, pbc_y, pbc_z, L_x, L_y, L_z]) 
f.write(line1)
f.write("\n")
# line m+2                 
for i in range(new_atom_id):
    line_coord = ' '.join(str(val) for val in [coord_type[i], coord_x[i], coord_y[i], coord_z[i], coord_mass[i], coord_id[i]])
    f.write(line_coord)                                           
    f.write(str("\n"))
f.close()

        

