# Pokémon Card Collection Scanner

A local web application that allows users to scan Pokémon cards using their mobile device and view a catalog of scanned cards on a desktop dashboard. The app uses a camera-enabled mobile interface for scanning and a sleek desktop dashboard for managing the collection.

## Features

- **Mobile Interface**:
  - Access the camera to scan Pokémon cards.
  - Upload scanned images to the backend for processing.
  - Overlay indicator for card alignment.

- **Desktop Dashboard**:
  - View a table of scanned cards with details like name, series, market price, and scan date.
  - Refresh the table dynamically to see the latest updates.
  - Scan a QR code to connect your mobile device to the scanner.

- **Backend**:
  - Process uploaded images and extract card details.
  - Store card information in a local SQLite database.
  - Generate QR codes for easy mobile access.

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite
- **Image Processing**: Placeholder for future integration with OpenCV or ML models
- **QR Code Generation**: `qrcode` Python library

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)
- [ngrok](https://ngrok.com/) (optional, for exposing the server over HTTPS)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/collection-scanner.git
   cd collection-scanner
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install flask qrcode
   ```

4. Initialize the database:
   ```bash
   python app/database.py
   ```

### Running the Application

1. Start the Flask server:
   ```bash
   python app/server.py
   ```

2. (Optional) Expose the server using `ngrok`:
   ```bash
   ngrok http 5000
   ```
   Copy the HTTPS URL provided by `ngrok` and update the QR code URL in `server.py`:
   ```python
   server_url = "https://<your-ngrok-subdomain>.ngrok.io/mobile"
   ```

3. Access the application:
   - **Desktop Dashboard**: Open `http://127.0.0.1:5000/` in your browser.
   - **Mobile Scanner**: Scan the QR code displayed on the dashboard or visit the mobile URL directly.

## Usage

1. Open the desktop dashboard and scan the QR code with your mobile device.
2. On your mobile device, align the Pokémon card within the overlay and click "Capture."
3. The scanned card will be uploaded and processed.
4. View the scanned card details on the desktop dashboard.

## Folder Structure

```
collection-scanner/
├── app/
│   ├── server.py          # Flask server
│   ├── database.py        # Database initialization
├── templates/
│   ├── dashboard.html     # Desktop dashboard
│   ├── mobile.html        # Mobile scanner interface
├── data/
│   ├── cards.db           # SQLite database (auto-generated)
│   ├── uploads/           # Uploaded images (auto-generated)
└── README.md              # Project documentation
```

## Future Enhancements

- **Image Recognition**:
  - Integrate OpenCV or TensorFlow for card recognition and detail extraction.
- **Market Price Integration**:
  - Fetch real-time market prices from external APIs.
- **User Authentication**:
  - Add user accounts to manage private collections.
- **Cloud Integration**:
  - Migrate to a cloud-based service for remote access and backups.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [qrcode Library](https://pypi.org/project/qrcode/)
- [ngrok](https://ngrok.com/)