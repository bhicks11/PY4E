def CalculateAverageConfidence(sourceFile, lineSortString):
    fname = sourceFile
    fh = open(fname)

    totalConfidence = 0
    confidenceCount = 0

    for line in fh:
        if not line.startswith(lineSortString): continue
        confidenceIndex = line.find(' ')
        confidence = float(line[confidenceIndex:])
        totalConfidence += confidence
        confidenceCount += 1

    return FindAverage(totalConfidence, confidenceCount)


def FindAverage(sumOfItems, itemCount):
    return float(sumOfItems/itemCount)

print(CalculateAverageConfidence('mbox.txt', 'X-DSPAM-Confidence:'))
