# Simple Wave Packets

## Introduction
A wave packet in physics is a short "burst" or "envelope" of localized wave action that travels as a unit. A good physical example would be a localized disturbance that travels through a medium, like a short burst of sound in air or a localized ripple on a water surface. In mathematical terms, wave packets can be analysed as a superposition of wave functions (e.g., sine and cosine functions) through Fourier analysis.

## Basic Concepts

### Wave Superposition
- Waves can be added together to form a new wave. This is known as superposition.
- The resultant wave function is the sum of the individual wave functions.

### Fourier Analysis
- Fourier analysis is a method to express a function as the sum of periodic components.
- For wave packets, it allows the decomposition of a complex wave into simpler sine and cosine waves.

## Mathematical Representation
A simple wave packet can be represented as a combination of sinusoidal waves of different frequencies. The mathematical form is often given by:

$$\Psi(x, t) = \int_{-\infty}^{\infty} A(k) e^{i(kx - \omega(k)t)} dk$$

where:
- $\Psi(x, t)$ is the wave function.
- $A(k)$ is the amplitude as a function of wave number $k$.
- $\omega(k)$ is the angular frequency as a function of wave number.
- $e^{i(kx - \omega(k)t)}$ represents the sinusoidal components.

## Physical Interpretation
- The wave packet moves through space with a group velocity.
- The spread of the wave packet in space can represent uncertainty in position.
- In quantum mechanics, wave packets are used to describe the probabilistic nature of particles.

## Example: Gaussian Wave Packet
A common example is the Gaussian wave packet, which has a Gaussian shape in both real and Fourier space. Its mathematical expression is:

$$\Psi(x, 0) = A e^{-a(x - x_0)^2} e^{ik_0x}$$

where:
- $A$ is the amplitude.
- $a$ determines the width of the packet.
- $x_0$ is the initial position.
- $k_0$ is the central wave number.

## Applications
Wave packets are crucial in various fields, such as:
- Quantum mechanics: Describing the probabilistic behaviour of particles.
- Optics: Analysing pulse propagation in fibers.
- Acoustics: Understanding sound wave propagation.

## Test Questions
1. Define a wave packet and explain the principle of superposition.
2. How does Fourier analysis apply to wave packets?
3. What is a Gaussian wave packet, and how is it mathematically expressed?

---

By understanding simple wave packets, we grasp the fundamentals of wave behaviour in different physical contexts, from sound waves to quantum particles. The wave packet model bridges the gap between classical and quantum physics, providing a versatile framework for studying wave-like phenomena.