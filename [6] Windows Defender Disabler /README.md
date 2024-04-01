# Windows Defender Disabler

This project provides a Python script to disable Windows Defender on a Windows machine. The script checks for admin privileges before attempting to modify the registry. If the user is not an administrator, the script prints a message asking them to run the script as an administrator.

## Installation

1. Install Python 3.x (if not already installed)
2. Install the `winreg` package using pip:
```bash
pip install winreg
```
3. Download the script and save it as `KillingTheSlayer.py`

## Usage

1. Open a command prompt (CMD) as an administrator
2. Navigate to the directory where the script is saved
3. Run the script:
```bash
python KillingTheSlayer.py
```
The script will print a message informing you that Windows Defender has been disabled and that you should restart your computer for the changes to take effect.

To Enable the Defender, run the script named `AwakenTheSlayer.py`
```bash
python AwakenTheSlayer.py
```

## Contributing

Contributions are welcome! Please create a pull request or issue on the project's repository if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the License file for details.
