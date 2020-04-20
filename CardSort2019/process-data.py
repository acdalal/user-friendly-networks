import csv
import sys

def connectivity():
    arr = []
    with open('connectivity.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            arr.append(row[0].lower());
    return arr

def bandwidth():
    arr = []
    with open('bandwith.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            arr.append(row[0].lower());
    arr.append('bandwidth')
    return arr

#correct list of elements
def masterList():
    dict = {'bandwidth': [], 'connectivity': []}
    with open('correct.csv') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            if row['category'].lower() == 'bandwidth':
                dict['bandwidth'].append(row['card label'])
            else:
                dict['connectivity'].append(row['card label'])
    return dict


def fixData():
    arr = []
    with open('card_sort_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['category label'].lower() == "network connectivity":
                arr.append([int(row['participant']), row['card label'], 'connectivity'])
            elif row['category label'].lower() == "network capacity/bandwidth":
                arr.append([int(row['participant']), row['card label'], 'bandwidth'])
            else:
                arr.append([int(row['participant']), row['card label'], 'unknown'])
    return arr

def gradeParticipants(arr):
    participants = {}
    correct = masterList()
    for row in arr:
        if (row[1] in correct['bandwidth'] and row[2] == 'bandwidth') or (row[1] in correct['connectivity'] and row[2] == 'connectivity'):
            if row[0] not in participants.keys():
                participants[row[0]] = [1]
            else:
                participants[row[0]][0] = participants[row[0]][0] + 1
    for key in participants.keys():
        participants[key].append('%.2f' % (float(participants[key][0])/28*100))
    return participants

if __name__ == "__main__":
    print(gradeParticipants(fixData()))