from Day_0 import day_data

# TODO: change the operating system to make a list of lists rep the hierarchy


def decode(txt=day_data(16)):
    return ''.join(f'{int(x, 16):04b}' for x in txt.strip())

def parse(d_txt, cur=0):
    # print(d_txt[cur:])
    version, cur = int(d_txt[cur:cur+3], 2), cur+3
    type_id, cur = int(d_txt[cur:cur+3], 2), cur+3
    
    if type_id == 4: # literal
        literal_value = ''
        while True:
            cont, cur = d_txt[cur], cur+1
            literal_value, cur = literal_value+d_txt[cur:cur+4], cur+4
            if cont != '1':
                break
        return (version, type_id, literal_value), cur
    
    else: # operator
        length_type_id, cur = d_txt[cur], cur+1
        
        if length_type_id == '0':
            sub_packets = []
            length_of_sub_packets, cur = int(d_txt[cur:cur+15], 2), cur+15
            stop_cur = cur+length_of_sub_packets
            while True:
                if cur >= stop_cur:
                    break
                elif cur+11 > stop_cur:
                    cur = stop_cur
                    break
                packet, cur = parse(d_txt, cur)
                sub_packets.append(packet)
            return (version, type_id, sub_packets), cur
        
        if length_type_id == '1':
            sub_packets = []
            length_of_sub_packets, cur = int(d_txt[cur:cur+11], 2), cur+11
            for _ in range(length_of_sub_packets):
                packet, cur = parse(d_txt, cur)
                sub_packets.append(packet)
            return (version, type_id, sub_packets), cur

def summit(tuple_):
    total_sum = tuple_[0]
    if tuple_[1]==4:
        return total_sum
    else:
        for tuple_2 in tuple_[2]:
            total_sum += summit(tuple_2)
        return total_sum


# print(decode('38006F45291200'))
# print(parse('00111000000000000110111101000101001010000001001000000000'))
# print(parse(decode('38006F45291200')))

# print(decode('8A004A801A8002F478'))
# print(summit(parse(decode('8A004A801A8002F478'))[0])) # test 1
# print(summit(parse(decode('620080001611562C8802118E34'))[0])) # test 2
# print(summit(parse(decode('C0015000016115A2E0802F182340'))[0])) # test 2
# print(summit(parse(decode('A0016C880162017C3686B18A3D4780'))[0])) # test 3

print(summit(parse(decode())[0]))

'''
00111000000000000110111101000101001010000001001000000000
001 110 0 000000000011011 110 100 0 1010 010 100 1 0001 0 0100 0000000
VVV TTT I LLLLLLLLLLLLLLL AAA AAA A AAAA BBB BBB B BBBB B BBBB 
'''

'''test 1
100 010 1 00000000001
    001 010 1 00000000001
        101 010 0 000000000001011
            110 100 0 1111
000
'''


'''
110 000 0 000000001010100
    000 000 0 000000000010110
        000 100 0 1010
        110 100 0 1011
    100 000 1 00000000010
        111 100 0 1100
        000 100 0 1101
000000
'''