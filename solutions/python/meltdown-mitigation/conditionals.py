def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000: return True
    else: return False    
        
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    group = (generated_power/theoretical_max_power)*100
    if group >= 80: return "green"
    elif group >= 60: return "orange"
    elif group >= 30: return "red"
    else: return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if (temperature * neutrons_produced_per_second) < (threshold - (threshold/10)): return "LOW"
    elif (temperature * neutrons_produced_per_second) <= (threshold + (threshold/10)): return "NORMAL"
    else: return "DANGER"
