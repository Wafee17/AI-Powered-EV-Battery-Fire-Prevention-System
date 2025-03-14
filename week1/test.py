import pybamm
import matplotlib.pyplot as plt
# Load a lithium-ion battery model
model = pybamm.lithium_ion.DFN()
# Create a simulation
sim = pybamm.Simulation(model)
# Solve for 1 hour (3600 seconds)
solution = sim.solve([0, 3600])
# Extract available SOC-related variable
soc_variable = "Discharge capacity [A.h]"
if soc_variable in solution.all_models[0].variables.keys():
    soc = solution[soc_variable].entries  # Get SOC data
    time = solution["Time [s]"].entries   # Get time data
    
    # Plot SOC over time
    plt.plot(time, soc, label="SOC (Discharge Capacity)", color='blue')
    plt.xlabel("Time (s)")
    plt.ylabel("Discharge Capacity [A.h]")
    plt.title("Battery SOC Simulation")
    plt.legend()
    plt.grid()
    plt.show()
    
    print("SOC simulation completed successfully!")
else:
    print(f"Variable '{soc_variable}' not found in the solution!")
