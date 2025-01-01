# PhoneNumber-Geolocation

## 📜 Description
This project allows you to locate the **service provider's region** of any phone number and visualize it on an interactive map using Python. The program extracts the carrier and location information, geocodes the location to get GPS coordinates, and generates an HTML file with a map pinpointing the region.

## 🚀 Features
- Extracts the region of a phone number.
- Retrieves the service provider's name.
- Converts region names into GPS coordinates using OpenCage Geocoder API.
- Displays an interactive map with the detected region.

## 🛠️ Technologies Used
- **Python**
- Libraries: `phonenumbers`, `folium`, `opencage`
- OpenCage Geocoder API

## 📂 Project Structure
```
PhoneNumber-Geolocation/
├── myphone.py            # File to store the phone number (e.g., number = "+1234567890")
├── main.py               # Main script for geolocation and map creation
├── mylocation.html       # Generated map file
└── README.md             # Project documentation
```

## ⚙️ Setup and Usage

### Prerequisites
- Python 3.7+
- An OpenCage Geocoder API key ([Get your key here](https://opencagedata.com/)).

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/PhoneNumber-Geolocation.git
   cd PhoneNumber-Geolocation
   ```
2. Install the required libraries:
   ```bash
   pip install opencage
   pip install phonenumbers
   pip install folium
   ```

### Configuration
1. Create a `myphone.py` file in the project directory and add your phone number:
   ```python
   number = "+1234567890"  # Replace with your phone number
   ```
2. Replace `YOUR_API_KEY` in `main.py` with your OpenCage Geocoder API key:
   ```python
   key = 'YOUR_API_KEY'
   ```

### Run the Program
Execute the main script:
```bash
python main.py
```

### Output
- The service provider's region and carrier name will be displayed in the terminal.
- An interactive map (`mylocation.html`) will be generated in the project directory.

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.
