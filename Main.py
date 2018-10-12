"""
Test B:
    Write a software library that accepts 2 version string as input
    and returns whether one is greater than, equal, or less than the other.
    As an example: “1.2” is greater than “1.1”.
    Please provide all test cases you could think of.
"""

import sys

def get_version(version_str):
    vers = version_str.split(" ")
    return vers[0].split(".")

def version_compare(version1, version2):
    ver1 = get_version(version1)
    ver2 = get_version(version2)
    print(ver1)
    print(ver2)

    last_version = 0
    loop_counter = 0
    while (loop_counter<len(ver1)):
        #print (loop_counter)
        #print(ver1[loop_counter], ' - ', ver2[loop_counter])

        if (loop_counter>=len(ver2)):
            last_version = -1
            break
        elif ver1[loop_counter]>ver2[loop_counter]:
            last_version = -1
            break
        elif ver1[loop_counter]<ver2[loop_counter]:
            last_version = 1
            break

        loop_counter += 1

    if last_version==0 and len(ver1)<len(ver2):
        last_version=1

    if last_version<0:
        return (version1 + " is greater than " + version2)
    elif last_version>0:
        return (version2 + " is greater than " + version1)
    else:
        return ("both version are the same.")


if __name__ == '__main__':
    false_version1 = "3.7.1 - October 1, 2008."
    false_version2 = "3.7.2 - October 1, 2008."

    print(version_compare(sys.version, false_version2))
