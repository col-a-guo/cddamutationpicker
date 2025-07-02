import numpy as np
import matplotlib.pyplot as plt

def simulate_adaptive_log_brownian_motion_with_integrals(
    steps=1000, 
    duration=5.0, 
    start_value=1.0, 
    volatility=6.0,
    base_drift=0.0, 
    reversion_strength=0.8, 
    seed=9,
    baseline_tolerance=0.05  # log-space tolerance (~±10% around value 1)
):
    if seed is not None:
        np.random.seed(seed)

    dt = duration / steps
    time_points = np.linspace(0, duration, steps + 1)
    values = np.zeros(steps + 1)
    values[0] = start_value

    in_excursion = False
    excursion_start_idx = 0
    excursion_integral = 0.0
    excursion_direction = None
    excursions = []

    for i in range(1, steps + 1):
        current = values[i-1]
        log_current = np.log(current)
        effective_drift = base_drift - reversion_strength * log_current
        dW = np.random.normal(loc=0.0, scale=np.sqrt(dt))
        log_next = log_current + effective_drift * dt + volatility * dW
        next_value = np.exp(log_next)
        values[i] = next_value

        # Deviation measure: 10^|log(value)|, signed
        if log_current > 0:
            delta = current * dt  # Above baseline
        elif log_current < 0:
            delta = (1 / current) * dt  # Below baseline
        else:
            delta = 0

        # Check proximity to baseline
        is_baseline = abs(log_current) < baseline_tolerance

        if not in_excursion and not is_baseline:
            # Start new excursion
            in_excursion = True
            excursion_start_idx = i - 1
            excursion_integral = 0.0
            excursion_direction = "above" if log_current > 0 else "below"

        if in_excursion:
            excursion_integral += delta
            if is_baseline:
                # End of excursion
                start_t = time_points[excursion_start_idx]
                end_t = time_points[i]
                excursions.append(
                    f"{int(round(excursion_integral))} {excursion_direction} baseline from t={start_t:.3f} to t={end_t:.3f}"
                )
                in_excursion = False

    return time_points, values, excursions

# Example usage
if __name__ == "__main__":
    t, x, excursions = simulate_adaptive_log_brownian_motion_with_integrals()

    # Plot the path
    plt.plot(t, x)
    plt.axhline(1, color='gray', linestyle='--', label='Baseline = 1')
    plt.yscale('log')
    plt.ylim(1e-10, 1e10)
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title("Log Brownian Motion with Corrected Excursion Tracking")
    plt.grid(True, which='both', linestyle='--')
    plt.legend()
    plt.show()

    # Print excursion reports
    print("\nExcursions:")
    for e in excursions:
        print(e)
