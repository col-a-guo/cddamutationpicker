import numpy as np
import matplotlib.pyplot as plt

def simulate_log_brownian_motion(
    steps=1000, 
    duration=1.0, 
    start_value=1.0, 
    volatility=1.0, 
    seed=None
):
    """
    Simulate exponential Brownian motion centered at 1.

    Parameters:
    - steps: number of time steps
    - duration: total time
    - start_value: initial value (should be 1 to match your description)
    - volatility: standard deviation of log returns (controls spread)
    - seed: random seed for reproducibility

    Returns:
    - time_points: np.array of time values
    - values: np.array of simulated values
    """
    if seed is not None:
        np.random.seed(seed)

    dt = duration / steps
    time_points = np.linspace(0, duration, steps + 1)

    # Generate standard Brownian increments in log space
    dW = np.random.normal(loc=0.0, scale=np.sqrt(dt), size=steps)
    log_returns = np.concatenate([[0], np.cumsum(dW * volatility)])

    # Exponentiate and shift to start at start_value
    values = start_value * np.exp(log_returns)

    return time_points, values

# Example usage:
if __name__ == "__main__":
    t, x = simulate_log_brownian_motion(steps=1000, duration=1, volatility=0.3, seed=42)
    plt.plot(t, x)
    plt.axhline(1, color='gray', linestyle='--', label='center = 1')
    plt.yscale('log')  # Optional: log scale shows symmetry nicely
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title("Exponential Brownian Motion Centered at 1")
    plt.legend()
    plt.grid(True, which='both', linestyle='--')
    plt.show()
