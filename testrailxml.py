from xml.etree import ElementTree
from pageobjects.common import Testrail_Binding
tree = ElementTree.parse("reports/junit/TESTS-smoke_tests.smoke_e2e.xml")
root = tree.getroot()

testcases = root.findall("testcase")

for testcase in testcases:
   status=testcase.attrib['status']
   flow_name=testcase.attrib['name']
   if(status=="passed"):
      outputs = testcase.findall("system-out")
      for output in outputs:
         terminal_output=output.text
      Testrail_Binding.testrail_success(flow_name,terminal_output)
   else:
      outputs = testcase.findall("system-out")
      errors=testcase.findall("error")
      for error in errors:
         assert "captured error"
      for output in outputs:
         assert "captured output"
      terminal_output = error.text+output.text
      Testrail_Binding.testrail_fail(flow_name,terminal_output)


