import numpy as np

def calculate_kpis(hours, energy, disruption):
    """
    Derives actionable KPIs and clarity scores from the simulated state profile.
    """
    idx_2pm = 16  # 2:00 PM corresponds to t=8 hours from 6:00 AM start
    clarity_2pm = float(energy[idx_2pm])
    baseline_2pm = 78.0  # Ideal reference score
    clarity_delta = round(((clarity_2pm - baseline_2pm) / baseline_2pm) * 100, 1)
    
    peak_idx = int(np.argmax(energy))
    peak_energy_hour = (int(hours[peak_idx]) + 6) % 24
    recovery_score = max(10, int(100 - disruption))
    
    return {
        "clarity_2pm": round(clarity_2pm, 1),
        "clarity_delta": clarity_delta,
        "disruption": round(disruption, 1),
        "peak_energy_hour": peak_energy_hour,
        "recovery_score": recovery_score
    }

def get_recommendation(caffeine_time, caffeine_mg, sleep_hours, disruption):
    """
    Generates dynamic advice based on behavioral risks.
    """
    if caffeine_time >= 16 and caffeine_mg > 0:
        return (
            "warning",
            f"⚠️ **Late Caffeine Risk Detected:** Consuming {caffeine_mg}mg of caffeine at {caffeine_time:02d}:00 "
            f"suppresses melatonin release. Shifting intake prior to **14:00** projected to improve tomorrow's "
            f"afternoon focus score by up to **{disruption * 0.8:.1f}%**."
        )
    elif sleep_hours < 7.0:
        return (
            "info",
            "💡 **Sleep Debt Warning:** Baseline sleep duration is below target. "
            "Increasing sleep to 7.5 hours will restore afternoon clarity baseline above **75/100**."
        )
    else:
        return (
            "success",
            "✅ **Optimal Schedule:** Inputs match an ideal circadian window without predicted severe afternoon crashes."
        )