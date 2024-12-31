import numpy as np
import matplotlib.pyplot as plt

class EngineModel:
    """
    Motor modelini tanımlayan sınıf.
    Tork ve güç eğrisini motor devrine (RPM) göre hesaplar.
    """
    def __init__(self, max_torque, max_power, max_rpm, efficiency=0.85):
        self.max_torque = max_torque  # Nm
        self.max_power = max_power  # kW
        self.max_rpm = max_rpm  # RPM
        self.efficiency = efficiency  # Motor verimliliği

    def torque(self, rpm):
        if rpm <= 0 or rpm > self.max_rpm:
            return 0
        peak_rpm = self.max_rpm * 0.5
        if rpm <= peak_rpm:
            return self.max_torque * (rpm / peak_rpm)  # Zirveye kadar artış
        else:
            return self.max_torque * (1 - (rpm - peak_rpm) / (self.max_rpm - peak_rpm))  # Zirve sonrası düşüş

    def power(self, rpm):
        torque = self.torque(rpm)
        return (torque * rpm) / 9548.8  # kW cinsinden güç

    def efficiency_factor(self, rpm):
        # Motor verimliliği, RPM arttıkça azalır
        efficiency = self.efficiency - 0.001 * (rpm / self.max_rpm)
        return max(efficiency, 0.6)

class TransmissionSystem:
    """
    Şanzıman sistemini tanımlayan sınıf.
    """
    def __init__(self, gears, efficiency=0.95):
        self.gears = gears
        self.efficiency = efficiency
        self.current_gear = 0  # Başlangıçta 1. viteste

    def change_gear(self, rpm, max_rpm):
        if rpm > max_rpm * 0.85 and self.current_gear < len(self.gears) - 1:
            self.current_gear += 1  # Yüksek vitese geç
        elif rpm < max_rpm * 0.3 and self.current_gear > 0:
            self.current_gear -= 1  # Düşük vitese geç
        return self.gears[self.current_gear]

    def get_gear_ratio(self):
        return self.gears[self.current_gear]

class VehicleDynamics:
    """
    Araç dinamiklerini tanımlayan sınıf.
    """
    def __init__(self, weight, drag_coefficient, frontal_area, engine, transmission, tire_grip=0.9, cargo_weight=0, ambient_temperature=25):
        self.weight = weight  # kg
        self.cargo_weight = cargo_weight  # kg, araç yükü
        self.drag_coefficient = drag_coefficient
        self.frontal_area = frontal_area  # m^2
        self.air_density = 1.225  # kg/m^3 (hava yoğunluğu)
        self.engine = engine
        self.transmission = transmission
        self.tire_grip = tire_grip  # Lastik tutuş katsayısı
        self.velocity = 0.1  # Başlangıç hızı (m/s)
        self.position = 0  # Başlangıç pozisyonu (m)
        self.time_step = 0.01  # Simülasyon adım zamanı (s)
        self.acceleration = 0  # Başlangıç ivmesi (m/s²)
        self.velocity_limit = 350 / 1  # Maksimum hız (m/s)
        self.is_braking = False  # Frenleme durumu
        self.slope_angle = 0  # Yol eğimi (derece)
        self.ambient_temperature = ambient_temperature  # Çevresel sıcaklık (°C)

    def update(self, rpm, slope=0, driving_style='eco', road_surface=0.9):
        """
        Her adımda hız, pozisyon ve ivmeyi günceller.
        """
        self.slope_angle = slope  # Yol eğimini güncelle
        self.driving_style = driving_style  # Sürüş stilini güncelle
        
        # Hava yoğunluğunun çevresel sıcaklıkla değişimi (sıcaklık arttıkça hava yoğunluğu azalır)
        self.air_density = 1.225 * (1 - 0.0002 * (self.ambient_temperature - 25))

        # Motorun sağladığı güç ve şanzıman oranı
        gear_ratio = self.transmission.change_gear(rpm, self.engine.max_rpm)
        power = self.engine.power(rpm) * self.engine.efficiency_factor(rpm)

        # Sürüş stiline bağlı ivme değişikliği
        if self.driving_style == 'performance':
            power *= 1.2  # Performans modunda daha fazla güç
        elif self.driving_style == 'eco':
            power *= 0.8  # Ekonomik sürüş modunda daha az güç

        # Kuvvet hesapları
        force = (power * 1000 * gear_ratio * self.transmission.efficiency) / max(self.velocity, 0.1)  # 0'a bölmeyi engelle
        drag_force = 0.5 * self.drag_coefficient * self.air_density * self.frontal_area * self.velocity**2
        gravity_force = self.weight * 9.81 * np.sin(np.radians(self.slope_angle))
        net_force = force - drag_force - gravity_force
        
        # Lastik tutuş kaybını kontrol et
        if np.abs(net_force) > road_surface * (self.weight + self.cargo_weight) * 9.81:
            net_force *= road_surface

        self.acceleration = net_force / (self.weight + self.cargo_weight)

        # Frenleme durumunda negatif ivme uygula
        if self.is_braking:
            self.acceleration -= 5

        # Hız ve pozisyon güncelleme
        self.velocity = max(0, min(self.velocity + self.acceleration * self.time_step, self.velocity_limit))
        self.position += self.velocity * self.time_step

        # Yakıt tüketimi hesapla (kWh, çok basitleştirilmiş)
        fuel_consumption = power / 20000 * 0.5  # Yakıt tüketimi: Güç ile orantılı
        regen_energy = 0  # Rejeneratif enerji, frenleme varsa geri kazanılacak

        # Rejeneratif frenleme simülasyonu
        if self.is_braking:
            regen_energy = min(fuel_consumption * 0.5, 10)  # Fren yaparken geri kazanılan enerji

        return self.velocity, self.position, self.acceleration, fuel_consumption, regen_energy

# Parametreler
motor = EngineModel(max_torque=800, max_power=800, max_rpm=16000)
transmission = TransmissionSystem(gears=[4, 2.5, 1.5, 1])
vehicle = VehicleDynamics(weight=1500, drag_coefficient=0.32, frontal_area=2.2, engine=motor, transmission=transmission, cargo_weight=200)

# Simülasyon
time_duration = 2000
rpm_range = np.linspace(1000, 6000, time_duration)
velocities = []
positions = []
accelerations = []
fuel_consumptions = []
regen_energies = []
slopes = np.zeros(time_duration)
road_surfaces = np.zeros(time_duration)

# Yol eğimi ve yüzeyi örneği
for i in range(time_duration):
    if 50 <= i <= 100:  
        slopes[i] = 5  # %5 eğim
        road_surfaces[i] = 0.6  # Islak yol, tutuş katsayısı
    elif 150 <= i <= 180:  
        slopes[i] = -5  # %5 iniş
        road_surfaces[i] = 0.5  # Toprak yol, tutuş katsayısı

    velocity, position, acceleration, fuel_consumption, regen_energy = vehicle.update(rpm_range[i], slope=slopes[i], road_surface=road_surfaces[i])
    velocities.append(velocity)
    positions.append(position)
    accelerations.append(acceleration)
    fuel_consumptions.append(fuel_consumption)
    regen_energies.append(regen_energy)

# Grafikler
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.plot(velocities)
plt.title('Hız (m/s)')
plt.subplot(2, 2, 2)
plt.plot(positions)
plt.title('Pozisyon (m)')
plt.subplot(2, 2, 3)
plt.plot(accelerations)
plt.title('İvme (m/s²)')
plt.subplot(2, 2, 4)
plt.plot(fuel_consumptions)
plt.title('Yakıt Tüketimi (kWh)')

plt.tight_layout()
plt.show()
