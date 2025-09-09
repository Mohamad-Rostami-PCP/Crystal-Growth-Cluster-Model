
# ❄️ Crystal Growth Cluster Model (Rock Candy Model)

This project simulates **cluster growth and crystallization** using a diffusion-limited aggregation (DLA) approach, often referred to as the "Rock Candy Model."

---

## 📂 Code Structure
- **main.py** → particle initialization, diffusion, sticking, and cluster growth visualization.

---

## 🔑 Important Variables
- `N` → total number of particles released  
- `C` → container size (grid dimension)  
- `Stick()` → defines sticking probability  
- `Crystallize()` → function that handles aggregation into clusters  

---

## ⚙️ How to Interact
1. Open **main.py**  
2. Adjust `N` to simulate larger or smaller clusters.  
3. Modify parameters in `Stick()` to change aggregation dynamics.  
4. Run:
   ```bash
   python main.py


---

## 🧠 Physical/Statistical Intuition

* Particles diffuse randomly until they stick to the existing cluster.
* Over time, large-scale structures resembling crystalline "rock candy" emerge.
* Demonstrates the mechanism of **Diffusion-Limited Aggregation (DLA)** and stochastic crystal growth.

---

## 🧮 Numerical Models

* **Stochastic particle diffusion**
* **Diffusion-limited aggregation (DLA)**
* **Monte Carlo cluster growth simulation**


