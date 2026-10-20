import numpy as np

def simulate_circadian_twin(
    sleep_h, q_fact, caf_time, caf_mg, screen_mins, chronotype_shift=0.0
):
    """
    Simulates a 24-hour cognitive energy trajectory based on physiological inputs.
    
    Parameters:
    - sleep_h (float): Hours of sleep.
    - q_fact (float): Quality factor derived from sleep quality.
    - caf_time (int): Hour of caffeine consumption (24-hour clock).
    - caf_mg (int): Milligrams of caffeine.
    - screen_mins (int): Minutes of late-night screen exposure.
    
    Returns:
    - hours (np.ndarray): 24-hour time array (0.5h steps).
    - energy_profile (np.ndarray): Calculated cognitive energy levels.
    - total_night_disruption (float): Deep sleep inhibition score (0-100%).
    """
    hours = np.arange(0, 24, 0.5)  # 24-hour cycle starting from 6:00 AM (t=0)

    # 1. Base circadian alertness model (sine curve)
    shifted_hours = hours - chronotype_shift
    base_circadian = 50 + 35 * np.sin((shifted_hours - 2) * np.pi / 8) - 10 * np.cos((shifted_hours - 2) * np.pi / 4)
    
    # 2. Sleep debt penalty
    sleep_debt = max(0, 8.0 - (sleep_h * q_fact))
    debt_penalty = sleep_debt * 6.5
    
    # 3. Caffeine concentration decay model (peak at 1.5h, half-life decay)
    caffeine_effect = np.zeros_like(hours)
    caf_hour_idx = caf_time - 6  # Align with 6:00 AM start time
    
    if 0 <= caf_hour_idx < 24:
        for i, h in enumerate(hours):
            if h >= caf_hour_idx:
                dt = h - caf_hour_idx
                caffeine_effect[i] = (caf_mg / 2) * (dt / 1.5) * np.exp(1 - dt / 1.5)
    
    # 4. Night disruption calculation (adenosine block + blue light penalty)
    adenosine_block_penalty = max(0, (caf_time - 14)) * (caf_mg / 100) * 2.2 if caf_time > 14 else 0
    screen_penalty = (screen_mins / 30) * 3.5
    total_night_disruption = adenosine_block_penalty + screen_penalty
    
    # 5. Composite energy calculation
    energy_profile = base_circadian - debt_penalty + caffeine_effect - (total_night_disruption * 0.3)
    energy_profile = np.clip(energy_profile, 10, 100)

    return hours, energy_profile, total_night_disruption
