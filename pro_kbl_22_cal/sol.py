import collections
import math

HOUR_CNT = 24
MINUTE_CNT = 60
MAX_TIME = ((HOUR_CNT * MINUTE_CNT) - 1)

def solution(fees: list, records: list)  -> list:
    answerList = [];
    inDict = collections.defaultdict(list);
    outDict = collections.defaultdict(list);
    timeDict = collections.defaultdict(int);
    (baseTime, baseRate, unitTime, unitRate) = fees;

    for curRecord in records:
        (hourMinute, car , history) = curRecord.split(" ");
        (hour, minute) = hourMinute.split(":");
        time = int(hour) * MINUTE_CNT + int(minute);

        print(hour, minute, time ,car, history);

        timeDict[car] = 0;

        if(history == "IN"):
            inDict[car].append(time);
        elif (history == "OUT"):
            outDict[car].append(time);
    for curCar in timeDict.keys():
        for historyIdx in range(len(outDict[curCar])):
            timeDict[curCar] += (outDict[curCar][historyIdx] - inDict[curCar][historyIdx]);
        if(len(inDict[curCar]) != len(outDict[curCar])):
            timeDict[curCar] += (MAX_TIME - inDict[curCar][-1]);

    for curCar in sorted(timeDict.keys()):
        if(timeDict[curCar] > baseTime):
            answerList.append(baseRate + (math.ceil((timeDict[curCar] - baseTime) / unitTime) * unitRate));
        else:
            answerList.append(baseRate);
    return answerList;
