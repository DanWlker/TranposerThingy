keys_dict = {
        'C': 0, 
        'C#': 1,
        'Db' : 1,
        'D': 2, 
        'D#': 3,
        'Eb': 3,
        'E': 4, 
        'F': 5, 
        'F#': 6,
        'Gb': 6,
        'G': 7, 
        'G#': 8,
        'Ab': 8,
        'A': 9, 
        'A#': 10,
        'Bb':10,
        'B': 11}

keys_arr = ['C', 
        'C#', 
        'D', 
        'D#', 
        'E', 
        'F', 
        'F#', 
        'G', 
        'G#', 
        'A', 
        'A#', 
        'B']

print("What is the original key of the song?")
original_key = input()
ori_value = keys_dict[original_key]

print("What are the chords used for this song? (separate them by space)")
ori_chords = input()
ori_chords_arr = ori_chords.split()

for i in range(len(ori_chords_arr)):
    ori_chords_arr[i] = ori_chords_arr[i] + ' ' #enables easier checking

print("What key would you like to transpose it to?")
transposed_key = input()
transposed_value = keys_dict[transposed_key]

if transposed_value < ori_value: #used to prevent negative
    transposed_value += 12

steps = transposed_value - ori_value #see how much to transpose

trans_chords_arr = []

for i in range(len(ori_chords_arr)):
    if(ori_chords_arr[i][1] != '#' or ori_chords_arr[i][1] != 'b'):
        trans_chords_arr.append(keys_arr[ (keys_dict[ori_chords_arr[i][0].upper()] + steps) % 12] + ori_chords_arr[i][1:])
    else:
        trans_chords_arr.append(keys_arr[(keys_dict[ori_chords_arr[i][0:1].upper()] + steps) % 12] + ori_chords_arr[i][2:])

print("The original chords are: ")
print(''.join(ori_chords_arr))

print("The transposed chords are: ")
print(''.join(trans_chords_arr))


