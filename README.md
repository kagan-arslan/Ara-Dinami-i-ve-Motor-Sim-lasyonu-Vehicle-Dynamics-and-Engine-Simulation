# Arac Dinamigi ve Motor Simulasyonu | Vehicle Dynamics and Engine Simulation

Bu proje, bir aracın dinamiklerini simüle etmek amacıyla geliştirilmiştir. Motor, şanzıman ve araç dinamiklerini modelleyen sınıflar kullanarak, aracın hız, ivme, pozisyon, yakıt tüketimi gibi önemli parametrelerini hesaplar. Ayrıca, yol yüzeyi ve eğimi gibi çevresel faktörlerin simülasyonu da yapılmaktadır. Bu projede, araç dinamiklerini ve motor verimliliğini optimize etmeye yönelik bazı sürüş modları (`eco` ve `performance`) da eklenmiştir.

This project is developed to simulate the dynamics of a vehicle. It calculates important parameters such as speed, acceleration, position, and fuel consumption using classes that model the engine, transmission, and vehicle dynamics. Additionally, environmental factors such as road surface and slope are simulated. The project also includes driving modes (`eco` and `performance`) to optimize vehicle dynamics and engine efficiency.

## Özellikler | Features

- **Motor Modeli**: Motor torku ve gücü, motor devri (RPM) ve verimlilik parametrelerine bağlı olarak hesaplanır.
  - **Engine Model**: Engine torque and power are calculated based on engine RPM and efficiency parameters.
- **Şanzıman Sistemi**: Farklı vites oranlarına sahip şanzıman modeli, motor devrine göre vites değiştirir.
  - **Transmission System**: The transmission system, with various gear ratios, changes gears based on engine RPM.
- **Araç Dinamiği**: Aracın hızı, ivmesi ve pozisyonu, motor gücü, yol yüzeyi, yol eğimi ve yük gibi faktörlere göre hesaplanır.
  - **Vehicle Dynamics**: Vehicle speed, acceleration, and position are calculated based on factors such as engine power, road surface, slope, and load.
- **Sürüş Modları**: `eco` (ekonomik) ve `performance` (performans) sürüş modları ile güç değişikliği yapılabilir.
  - **Driving Modes**: The `eco` (economical) and `performance` driving modes change the power output.
- **Çevresel Faktörler**: Yol yüzeyi (kuru, ıslak, toprak) ve eğim gibi faktörler aracın performansını etkiler.
  - **Environmental Factors**: Factors like road surface (dry, wet, gravel) and slope affect the vehicle's performance.
- **Frenleme ve Regenerasyon**: Frenleme sırasında regeneratif enerji geri kazanımı simüle edilir.
  - **Braking and Regeneration**: Regenerative energy recovery is simulated during braking.

## Kullanım | Usage

### Gereksinimler | Requirements

Proje Python 3.7+ ile uyumludur ve aşağıdaki kütüphanelere ihtiyaç duyar:

The project is compatible with Python 3.7+ and requires the following libraries:

- `numpy`
- `matplotlib`

Bu kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

You can install the required libraries using the following command:

```bash
pip install numpy matplotlib
Başlangıç | Getting Started
Simülasyonu çalıştırmak için aşağıdaki adımları takip edebilirsiniz:
Follow these steps to run the simulation:
	1.	Proje dosyasını indirin veya klonlayın. Download or clone the project files. 
	2.	Ana Python dosyasını çalıştırarak simülasyonu başlatın. Run the main Python file to start the simulation. 
	3.	Simülasyon, aracın hız, pozisyon, ivme, yakıt tüketimi gibi verileri hesaplar ve grafikte görüntüler. The simulation calculates and displays data such as vehicle speed, position, acceleration, and fuel consumption in a graph. 
Çıktılar | Outputs
Simülasyon çalıştırıldığında, aşağıdaki grafikler görüntülenir:
When the simulation runs, the following graphs will be displayed:
	•	Hız (m/s): Zamanla değişen aracın hızı.
	◦	Speed (m/s): The vehicle's speed over time.
	•	Pozisyon (m): Zamanla değişen aracın pozisyonu.
	◦	Position (m): The vehicle's position over time.
	•	İvme (m/s²): Zamanla değişen aracın ivmesi.
	◦	Acceleration (m/s²): The vehicle's acceleration over time.
	•	Yakıt Tüketimi (kWh): Zamanla değişen yakıt tüketimi.
	◦	Fuel Consumption (kWh): Fuel consumption over time.
Kod Yapısı | Code Structure
	•	EngineModel: Motor torku, gücü ve verimliliğini hesaplayan sınıf.
	◦	EngineModel: Class that calculates engine torque, power, and efficiency.
	•	TransmissionSystem: Şanzıman vites oranını ve verimliliğini hesaplayan sınıf.
	◦	TransmissionSystem: Class that calculates the gear ratio and efficiency of the transmission.
	•	VehicleDynamics: Aracın dinamiklerini hesaplayan ana sınıf.
	◦	VehicleDynamics: Main class that calculates the vehicle dynamics.
	•	update(): Aracın hızını, ivmesini, pozisyonunu ve yakıt tüketimini her adımda güncelleyen fonksiyon.
	◦	update(): Function that updates the vehicle's speed, acceleration, position, and fuel consumption at each time step.
Katkı Sağlama | Contributing
Katkıda bulunmak isterseniz, aşağıdaki adımları izleyebilirsiniz:
If you want to contribute, follow these steps:
	1.	Bu depo üzerinde bir fork oluşturun. Create a fork of this repository. 
	2.	Kendi değişikliklerinizi yapın ve commit edin. Make your changes and commit them. 
	3.	Pull request oluşturun. Create a pull request. 
Lisans | License
Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için LICENSE dosyasına bakabilirsiniz.
This project is licensed under the MIT License. See the LICENSE file for details.

