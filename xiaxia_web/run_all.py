import  unittest
from common import HTMLTestRunner_cn


def creatsuite1():
    testunit = unittest.TestSuite()

    #用例路径
    casePath = "E:\\testunitcase\\case"
    rule="Test*.py"

    #读取用例文件的路径目录
    discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)

    print(discover)

    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)

    return  testunit

alltestnames = creatsuite1()

#报告生成的路径
reportPath = "E:\\testunitcase\\report\\"+"result.html"
fp=open(reportPath,"wb")

runner  = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="测试报告",description="用例执行情况：")
runner.run(alltestnames)

fp.close()