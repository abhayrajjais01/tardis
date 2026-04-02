import numpy as np
import pandas as pd

def solve_task_1(atom_data=None):
    """
    Task #1: Identifying Iron Group Elements (IGE)
    Goal: Filter and mark 'Iron Group Elements' in an atomic dataset.
    """
    if atom_data is None:
        # Create a mock atom_data for demonstration if not provided
        # IGEs are elements with atomic masses between 51 and 60
        data = {
            'atomic_number': [1, 2, 24, 25, 26, 27, 28, 29],
            'symbol': ['H', 'He', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu'],
            'mass': [1.008, 4.0026, 51.996, 54.938, 55.845, 58.933, 58.693, 63.546]
        }
        atom_data = pd.DataFrame(data)

    print("--- Task 1: Identifying Iron Group Elements (IGE) ---")
    # Identify elements with atomic masses between 51 and 60
    ige_mask = (atom_data['mass'] >= 51) & (atom_data['mass'] <= 60)
    
    # Create dedicated DataFrame for IGEs
    ige_df = atom_data[ige_mask].copy()
    
    # Add IGE column to the main atom_data DataFrame
    atom_data['IGE'] = ige_mask.astype(int) 
    
    print("Iron Group Elements (IGE) DataFrame:")
    print(ige_df)
    print("\nUpdated Main DataFrame (First 8 rows):")
    print(atom_data.head(8))
    print("-" * 50 + "\n")
    return atom_data, ige_df

def Ni56toCo56(Ni56_count):
    """
    Task #2: Nickel-56 Decay Energy Calculation
    Calculate energy released (photons/neutrinos) during Ni56 -> Co56 decay.
    Output: Scientific notation with 4 significant figures.
    """
    # Precision constants
    MeV_to_J = 1.602176634e-13
    
    # Energy per atom (given in MeV)
    e_photon_per_atom = 1.75 * MeV_to_J
    e_neutrino_per_atom = 0.41 * MeV_to_J
    
    # Total energy released
    total_e_photon_j = Ni56_count * e_photon_per_atom
    total_e_neutrino_j = Ni56_count * e_neutrino_per_atom
    
    return total_e_photon_j, total_e_neutrino_j

def solve_task_2_3():
    """
    Task #3: Total Energy in a Supernova
    Determine total energy released by 1.2 solar masses of Nickel-56.
    """
    print("--- Tasks 2 & 3: Nickel-56 Decay Energy ---")
    
    # Precision constants
    M_sun_kg = 1.98847e30
    u_kg = 1.66053906660e-27
    m_ni56_u = 55.94213 
    
    # 1. Calculate total atoms in 1.2 solar masses of Ni-56
    mass_ni56_total_kg = 1.2 * M_sun_kg
    m_ni56_atom_kg = m_ni56_u * u_kg 
    
    num_atoms_ni56 = mass_ni56_total_kg / m_ni56_atom_kg
    
    # 2. Use function from Task 2 to calculate energy
    e_photon, e_neutrino = Ni56toCo56(num_atoms_ni56)
    
    # Task #2 Requirement: Scientific notation with 4 significant figures
    print(f"Number of Atoms in 1.2 Solar Masses of Ni-56: {num_atoms_ni56:.4e}")
    print(f"Energy released as Photons: {e_photon:.4e} J")
    print(f"Energy released as Neutrinos: {e_neutrino:.4e} J")
    print("-" * 50)

if __name__ == "__main__":
    solve_task_1()
    solve_task_2_3()
