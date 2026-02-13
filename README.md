# Efficient and Error-Free Missile Telemetric Data Compression Using LZMA2 🚀

This project presents a **lossless missile telemetry data compression framework** using the **LZMA2 algorithm** to minimize bandwidth usage and improve reliable telemetry transmission during **plasma-induced blackout regions**.

Missile telemetry systems continuously generate large volumes of sensor data. However, during high-speed atmospheric flight, a plasma sheath forms around the missile causing electromagnetic interference and communication blackout intervals. This results in limited transmission windows and possible loss of critical mission data. To overcome this challenge, this project compresses telemetry packets efficiently while maintaining **100% data integrity**.

---

## 📌 Problem Statement
During missile flight, telemetry communication is severely affected due to the formation of a plasma sheath, leading to **blackout regions** and unreliable transmission. Since telemetry data contains mission-critical parameters, reducing the size of transmitted information becomes essential to maximize data delivery within limited bandwidth and link availability.

---

## 🎯 Objectives
- Implement a lossless compression approach for missile telemetry data
- Reduce telemetry packet size while preserving complete accuracy
- Improve transmission efficiency during blackout-prone phases
- Generate a synthetic telemetry dataset for testing and evaluation
- Compare LZMA2 performance with traditional GZIP compression

---

## 🧠 Methodology
The workflow includes:
1. Collection of telemetry sensor parameters
2. Sampling, digitization, and framing of telemetry stream
3. Block/chunk segmentation of telemetry frames
4. Compression using **LZMA2** (dictionary matching + range encoding)
5. Performance evaluation against GZIP

LZMA2 was selected due to its high compression efficiency and suitability for structured telemetry data streams.

---

## 📂 Dataset
Since real missile telemetry data is confidential, a **synthetic telemetric dataset** was created using essential parameters such as:
- Acceleration
- Temperature
- Pressure
- Voltage
- Velocity components

Dataset properties:
- 90,000 minor frames
- 9,000 major frames (each major frame contains 10 minor frames)
- Sampling interval: 10 milliseconds
- Total dataset size: ~10 MB

---

## 📊 Results and Comparison (LZMA2 vs GZIP)

| Algorithm | Compression Factor |
|----------|---------------------|
| GZIP     | 1.41                |
| LZMA2    | 5.58                |

✅ LZMA2 achieved significantly higher compression efficiency than GZIP while maintaining lossless recovery of telemetry data.

