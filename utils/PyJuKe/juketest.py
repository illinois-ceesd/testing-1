def readtestresults(filename):

    from os import path

    testresults = {}

    if filename != "":
        if path.exists(filename):
            myfile = open(filename, "r")
            for line in myfile:
                testname, testresult = line.split()
                testresults[testname] = testresult
            myfile.close()

    return testresults


def writetestresults(testresults, filename=""):

    import sys as mysys

    resultfile = mysys.stdout

    if filename != "":
        resultfile = open(filename, "w")

    for testname in testresults:
        print(testname, testresults[testname], file=resultfile)

    if filename != "":
        resultfile.close()


def updatetestresults(testresults, filename=""):

    allresults = readtestresults(filename)

    for testname in testresults:
        allresults[testname] = testresults[testname]

    writetestresults(allresults, filename)


def checkresult(testresults, testname):

    if testname in testresults:
        testresult = testresults[testname]
        if (
            testresult.lower() == "pass"
            or testresult.lower() == "passed"
            or testresult.lower() == "yes"
            or testresult.lower() == "true"
            or testresult.lower() == ".true."
            or testresult.lower() == "1"
        ):
            return 0
        else:
            return 1
    return -1
