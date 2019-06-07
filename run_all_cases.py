import  unittest
import os

curPATH = os.path.realpath(__file__)
print(curPATH)
curDir = os.path.dirname(curPATH)
print(curDir)
casePath = os.path.join(curDir,"cases","model1")
print(casePath)


# casepath = 'D:\\APItest\\cases'
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern='test*.py')
print(discover)


runner = unittest.TextTestRunner()
runner.run(discover)