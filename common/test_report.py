import time
from common.HTML_test_runner import HTMLTestRunner


class CreateReport(object):

    def create_report(self, suite, filename):
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        fp = "../test_report/Aurora_Result_" + filename+"_" + now + ".html"
        with open(fp, "wb") as f:
            runner = HTMLTestRunner(stream=f, title="Aurora_Results", description=u"result", verbosity=2)
            runner.run(suite)
