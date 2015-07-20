from com.android.monkeyrunner import MonkeyRunner as mr  
from com.android.monkeyrunner import MonkeyDevice as md  
  
# Connects to the current device, returning a MonkeyDevice object  
device = mr.waitForConnection()  
device.installPackage('./MainActivity.apk') 
# sets a variable with the package's internal name  
package = 'com.example.testandroid'  
  
# sets a variable with the name of an Activity in the package  
activity = '.MainActivity'  
  
# sets the name of the component to start  
runComponent = package + '/' + activity  
  
# Runs the component  
device.startActivity(component=runComponent)  
  
# Presses the Menu button  
device.press('KEYCODE_MENU','DOWN_AND_UP')  
  
# Takes a screenshot  
result = device.takeSnapshot()  
  
# default folder name to save snapshot  
snapshot = 'E:\\tmp\\'    
  
# Writes the screenshot to a file  
result.writeToFile(snapshot + 'shot1.png','png')  