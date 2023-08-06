def traceback_print(file, line, module, lineread, bs, Error, Errorread, other):
    print("Traceback (most recent call last):")
    print('  File "{0}", line {1}, in {2}'.format(file,line,module))
    print("    {0}".format(lineread))
    print("    {0}^".format(bs*" "))
    print("{0}: {1}".format(Error,Errorread))
    if (other == ''):
        pass
    else:
        print(other)