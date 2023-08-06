# The following module allows for the transformation of files for use and analysis in vasp and other codes such as molcas
# The module will include the transfor from .cif file to poscar file and then poscar to .xyz file 
"""
A module for the transformation of file type for use in vasp and other codes such as molcas
"""
# Imports
import numpy as np
import os
from gemmi import cif

# Functions
def convert_cif(cif_file):
    """
    Converts a .cif file to a POSCAR file for use in vasp.
    KNOWN BUGS
    ----------
    - The program doesnt work for .cif files containig "(number)" in the positions of the atoms and the lattice vectors
    - View the .cif file in a text editor to see if this is the case

    Parameters
    ----------
    cif_file : str 

    Returns
    -------
    POSCAR 
    """

    cif_doc =  cif.read_file(cif_file)
    cif_block = cif_doc.sole_block()
    name = cif_file.strip(".cif")
    # Get the lattice vectors
    a = cif_block.find_value("_cell_length_a")
    b = cif_block.find_value("_cell_length_b")
    c = cif_block.find_value("_cell_length_c")
    a, b, c = float(a), float(b), float(c)
    alpha = cif_block.find_value("_cell_angle_alpha")
    beta = cif_block.find_value("_cell_angle_beta")
    gamma = cif_block.find_value("_cell_angle_gamma")
    alpha, beta, gamma = float(alpha), float(beta), float(gamma)
    alpha, beta, gamma = np.radians(alpha), np.radians(beta), np.radians(gamma)
    # Get the atom positions
    xpos, ypos, zpos = list(cif_block.find_loop("_atom_site_fract_x")), list(cif_block.find_loop("_atom_site_fract_y")), list(cif_block.find_loop("_atom_site_fract_z"))
    # Get the atom labels
    atom_labels = list(cif_block.find_loop("_atom_site_label"))
    # Get the atom types
    atom_types = list(cif_block.find_loop("_atom_site_type_symbol"))
    
    # Transform the lattice vectors and angles into a matix
    a_vector = np.array([a, 0, 0])
    b_vector = np.array([b*np.cos(gamma), b*np.sin(gamma), 0])
    c_vector = np.array([np.cos(beta), c*((np.cos(alpha) - np.cos(beta)*np.cos(gamma))/np.sin(gamma)), c*np.sqrt(1 - np.cos(beta)**2 - ((np.cos(alpha) - np.cos(beta)*np.cos(gamma))/np.sin(gamma))**2)])

    # Create the atom position matirx
    position_matrix = [] 
    for i in range(len(xpos)):
        position = np.array([float(xpos[i]), float(ypos[i]), float(zpos[i])])
        position_matrix.append(position)
    position_matrix = np.array(position_matrix)
    
    # Create a list of tuples containing the atom and the number of that atom (atom, number)
    atom_list = []
    for i in atom_types:
        if i not in atom_list:
            atom_list.append(i)
    atom_number_list = []
    for i in atom_list:
        atom_number_list.append(atom_types.count(i))
    atom_number_list = tuple(atom_number_list)
    atom_list = tuple(atom_list)
    atom_list = list(zip(atom_list, atom_number_list))

    atom_list_string = ""
    for i in atom_list:
        atom_list_string += i[0] + " "
    atom_number_list_string = ""
    for i in atom_list:
        atom_number_list_string += str(i[1]) + " "

    # Generate the POSCAR file
    with open('POSCAR', 'w') as f:
        f.write(f'''{name}
1.0
        {a_vector[0]} {a_vector[1]} {a_vector[2]}
        {b_vector[0]} {b_vector[1]} {b_vector[2]}
        {c_vector[0]} {c_vector[1]} {c_vector[2]}
{atom_list_string}
  {atom_number_list_string}
Direct
''')
        for i in position_matrix:
            f.write(f"    {i[0]}     {i[1]}      {i[2]}\n")


def convert_xyz():
    """
    Converts a POSCAR file to a .xyz file for use in molcas

    Parameters
    ----------
    None

    Returns
    -------
    .xyz file
    """
    with open('POSCAR','r') as f:
            poscar = []
            for lines in f:
                stripped_lines = lines.strip()
                split_lines = stripped_lines.split()
                poscar.append(split_lines)
    lattice_matrix = np.float_(poscar[2:5])
    frac_coord = np.float_(poscar[8:])
    name = ''.join(poscar[0])
    cart_coord = []
    for i in range(len(frac_coord)):
        cart_coord.append(np.matmul(frac_coord[i],lattice_matrix))
    element = poscar[5]
    element_num = poscar[6]
    element_num = [int(x) for x in element_num]
    cumsum_element = list(np.cumsum(element_num))
    element_list =[]
    for i in range(len(element)):
        element_list.append(f'{element[i]} '*int(element_num[i]))
    for i in range(len(element_list)):
        element_list[i] = ' '.join(element_list[i].split())
    element_list = ' '.join(element_list)
    element_list = element_list.split()

    with open('POSCAR.xyz','w') as f:
        f.write(f'''{len(cart_coord)}
{name}
''')
        for i in range(len(cart_coord)):
            f.write(f'''{element_list[i]}    {float(cart_coord[i][0])}    {float(cart_coord[i][1])}    {float(cart_coord[i][2])}   
''')  

def get_poscar():
    poscar = []
    with open('POSCAR', 'r') as f:
        for lines in f:
            strippedlines = lines.strip()
            splitlines = strippedlines.split()
            poscar.append(splitlines)
    return poscar

def atom_number(poscar):
    atom_number = np.int_(poscar[6])
    return atom_number

def atom_list(poscar):
    atom_list = poscar[5]
    atom_number = list(np.int_(poscar[6]))
    atoms = []
    for atom, number in zip(atom_list, atom_number):
        for i in range(number):
            atoms.append(atom)
    return atoms

def construct_matrix(poscar):
    matrix = np.float_(poscar[8:])
    return matrix

def expansion_list(a,b,c):
    a_list = list(range(a+1))
    del a_list[0]
    a_list.append(0)
    b_list = list(range(b+1))
    del b_list[0]
    b_list.append(0)
    c_list = list(range(c+1))
    del c_list[0]
    c_list.append(0)
    return a_list,b_list, c_list       

def expansion(matrix, a_list, b_list, c_list, atoms):
    mat = []
    for item, atom in zip(matrix, atoms):
        item = np.append(item,[atom])
        mat.append(item)
    mat = np.array(mat)
    a_matrix = []
    b_matrix = []
    c_matrix = []
    for i in a_list[:-1]:
        for j in mat:
                a_matrix.append([((float(i)*1)+float(j[0])), float(j[1]),float(j[2]), j[3]])
    a_matrix = np.array(a_matrix)
    a_matrix = np.unique(a_matrix,axis=0)
    a_matrix = list(a_matrix)
    for i in b_list[:-1]:
        for j in a_matrix:
            b_matrix.append([float(j[0]), ((float(i)*1)+float(j[1])), float(j[2]),j[3]])
    b_matrix = np.array(b_matrix)
    b_matrix = np.unique(b_matrix,axis=0)
    b_matrix = list(b_matrix)
    for i in c_list[:-1]:
        for j in b_matrix:
            c_matrix.append([float(j[0]), float(j[1]), ((float(i)*1)+float(j[2])),j[3]])
    matrix = np.array(c_matrix)
    matrix = np.unique(matrix, axis=0)
    matrix = matrix[matrix[:,3].argsort()]
    return matrix

def fractional_matrix(matrix, a, b,c):
    for i in range(len(matrix)):
        matrix[i][0] = float(matrix[i][0])/a[-2]
        matrix[i][1] = float(matrix[i][1])/b[-2]
        matrix[i][2] = float(matrix[i][2])/c[-2]
    return matrix

def new_atoms(matrix):
    atoms = []
    for i in matrix:
        atoms.append(i[3])
    #append the number of each atom to a new list
    atom_number = []
    for i in atoms:
        atom_number.append(atoms.count(i))
    #remove the duplicate atoms
    atom_list_sc = []
    for i in atoms:
        if i not in atom_list_sc:
            atom_list_sc.append(i)
    #remove duplicate atom numbers
    atom_number_sc = []
    # calcualte the number of times that each atom in atom_liat_sc appears in atoms and append it to atom_number_sc
    for i in atom_list_sc:
        atom_number_sc.append(atoms.count(i))
    return atom_list_sc, atom_number_sc

def multiplied_lattice_matrix(a, b, c, poscar):
    lattice_matrix = poscar[2:5]
    lattice_matrix = np.float_(lattice_matrix)
    for i in range(len(lattice_matrix[0])):
        lattice_matrix[0][i] = lattice_matrix[0][i]*a[-2]
    for i in range(len(lattice_matrix[1])):
        lattice_matrix[1][i] = lattice_matrix[1][i]*b[-2]
    for i in range(len(lattice_matrix[2])):
        lattice_matrix[2][i] = lattice_matrix[2][i]*c[-2]
    return lattice_matrix

def write_poscar(matrix, lattice_matrix, atom_list, atom_number,name):
    with open('POSCAR', 'w') as f:
        f.write(f'''{name}
1.0
                {lattice_matrix[0][0]} {lattice_matrix[0][1]} {lattice_matrix[0][2]}
                {lattice_matrix[1][0]} {lattice_matrix[1][1]} {lattice_matrix[1][2]}
                {lattice_matrix[2][0]} {lattice_matrix[2][1]} {lattice_matrix[2][2]}
''')
        atom_list = ' '.join(atom_list)
        f.write(f'''  {atom_list}
''')
        atom_number = ' '.join(map(str, atom_number))
        f.write(f'''  {atom_number}
''')
        f.write('''Dierct
''')
        for i in matrix:
            f.write(f''' {i[0]} {i[1]} {i[2]}
''')

def supercell_expansion(a,b,c):
    '''
    A program to perform supercell expansions on a POSCAR file.
    where a, b and c are the expansion factors in the a, b and c directons respectively.

    Parameters
    ----------
    a : int 
    b : int 
    c : int 

    Returns
    -------
    POSCAR 

    '''
    poscar = get_poscar()
    name = poscar[0]
    matrix = construct_matrix(poscar)
    a,b,c = expansion_list(a,b,c)
    supercell_lattice_matrix = multiplied_lattice_matrix(a,b,c, poscar)
    atoms = atom_list(poscar)
    new_matrix = expansion(matrix,a,b,c,atoms)
    new_matrix = fractional_matrix(new_matrix, a,b,c)
    atom_list_sc, atom_number_sc = new_atoms(new_matrix)
    write_poscar(new_matrix, supercell_lattice_matrix, atom_list_sc, atom_number_sc, name)


