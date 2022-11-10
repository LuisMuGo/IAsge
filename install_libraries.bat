title Libraries Intallation
cls
@ECHO OFF
echo "========================================"
echo "         Instalador de librerias        "
echo "========================================"
echo Installing MechanicalSoup...
pip install MechanicalSoup
python -m pip show MechanicalSoup
echo Installing scikit-learn...
pip install -U scikit-learn
python -m pip show scikit-learn
echo Installing pandas
pip install pandas
python -m pip show pandas
echo Finish

echo "Pulse cualquier tecla para salir"
pause > nul