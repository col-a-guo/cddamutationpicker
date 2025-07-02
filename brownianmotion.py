import numpy as np
import matplotlib.pyplot as plt

def simulate_adaptive_log_brownian_motion(
    steps=1000, 
    duration=1.0, 
    start_value=1.0, 
    volatility=1.0, 
    base_drift=0.05, 
    reversion_strength=0.05,  # <<< new parameter to control how strongly it pulls toward 1
    seed=None
):
    """
    Simulate Brownian motion in log space with adjustable mean reversion toward 1.

    Parameters:
    - steps: number of time steps
    - duration: total time
    - start_value: initial value (should be 1)
    - volatility: standard deviation of log returns
    - base_drift: steady directional drift (like +5% per year)
    - reversion_strength: how strongly the motion pulls toward 1 (log-space)
    - seed: random seed

    Returns:
    - time_points: np.array of time values
    - values: np.array of simulated values
    """
    if seed is not None:
        np.random.seed(seed)

    dt = duration / steps
    time_points = np.linspace(0, duration, steps + 1)
    values = np.zeros(steps + 1)
    values[0] = start_value

    for i in range(1, steps + 1):
        current = values[i-1]
        log_current = np.log(current)
        
        # Weakened mean reversion toward log(1) = 0
        effective_drift = base_drift - reversion_strength * log_current

        dW = np.random.normal(loc=0.0, scale=np.sqrt(dt))
        log_next = log_current + effective_drift * dt + volatility * dW
        values[i] = np.exp(log_next)

    return time_points, values

# Example usage
if __name__ == "__main__":
    t, x = simulate_adaptive_log_brownian_motion(
        steps=1000,
        duration=5,
        volatility=10,
        base_drift=0,
        reversion_strength=0.2,  # Try 0.01 for *very* weak reversion
        seed=42
    )
    plt.plot(t, x)
    plt.axhline(1, color='gray', linestyle='--', label='Baseline = 1')
    plt.yscale('log')
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title("Log Brownian Motion with Weak Mean Reversion")
    plt.grid(True, which='both', linestyle='--')
    plt.legend()
    plt.show()
