import numpy as np
import matplotlib.pyplot as plt

print("✅ Python ทำงานได้!")
print(f"NumPy version: {np.__version__}")

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Test Plot - ถ้าเห็นกราฟนี้ แสดงว่าพร้อมแล้ว!")
plt.savefig("test_plot.png")  # บันทึกเป็นไฟล์แทน
print("✅ บันทึกกราฟเป็น test_plot.png แล้ว!")