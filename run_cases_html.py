import  unittest
import os
from common.HTMLTestRunner import HTMLTestRunner

curDir = os.path.dirname(os.path.realpath(__file__))

casePath = os.path.join(curDir,"cases")




discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern='test*.py')
print(discover)
reportPath = os.path.join(curDir,"report","report.html")
fp=open(reportPath,'wb')

runner = HTMLTestRunner(stream=fp,
                        title='测试报告',
                        description='描述内容，这是XX项目的报告'
)
runner.run(discover)