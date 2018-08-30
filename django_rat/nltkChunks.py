# text = 'Steve Jobs was CEO of Apple Corp. headquarter in London by Mercedes on Indian railway '


def nltkChunks(text):
    # if text.strip() == '' or text.strip() == 'undefined':
    #     text = 'Ratnesh Kushwaha is CEO of SarasAnalytics headquarter in Ujjain owned Ford use Indian railway '
    t = __import__('nltk').pos_tag(text.split())
    k = __import__('nltk').ne_chunk(t)

    a = []

    for v in k:
        if type(v) == tuple:
            # print('B', v)
            a.append('B-' + v[0])
        else:
            # print(str(v), v[0][0])
            a.append(str(v)[1:2] + "-" + v[0][0])
        # print(v,type(v))
    return ",".join(a)
# print("P-Ratnesh,O-Kushwaha,B-is,B-CEO,B-of,O-SarasAnalytics,B-headquarter,B-in,G-Ujjain,B-owned,O-Ford,B-use,G-Indian,B-railway")
# print(nltkChunks(text))
