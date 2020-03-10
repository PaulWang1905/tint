
def read_data(read_input_note_data):
    # read the input data, and return a list. 
    f = open(read_input_note_data)
    note_list=[]
    for line in f:
        note = line.split(',')[0]
        note = str(int(note)%12)
        duration = line.strip().split(',')[1]
        note_list.append((note,duration))
    return note_dict 

a = read_data('input.txt')
print(a)
