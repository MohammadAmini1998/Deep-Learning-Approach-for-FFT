import numpy as np
import pandas as pd
from scipy.fft import ifft

# Parameters
num_samples = 100000
num_carriers = 1  # Number of subcarriers in the OFDM system

# Generate random time-domain symbols
time_symbols = np.random.rand(num_samples, num_carriers)

# Perform FFT to get frequency-domain symbols
frequency_symbols = np.fft.fft(time_symbols, axis=1)

# Reshape data for modeling
X = frequency_symbols.reshape(num_samples, num_carriers, 1)  # Input data (frequency-domain symbols)
y = time_symbols.reshape(num_samples, num_carriers)          # Output data (time-domain symbols)

# Create pandas DataFrame
X_df = pd.DataFrame(X.reshape(num_samples, -1), columns=[f'Frequency_Symbol_{i}' for i in range(1, num_carriers+1)])
y_df = pd.DataFrame(y.reshape(num_samples, -1), columns=['Time_Symbol'])

# Combine input and output DataFrames
df = pd.concat([y_df, X_df], axis=1)

# Save DataFrame to CSV file
df.to_csv('ofdm_dataset.csv', index=False)

# Print a message
print("DataFrame saved to 'ofdm_dataset.csv'")