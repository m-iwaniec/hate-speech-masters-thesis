import collections

file = open('/home/martyna/masters-thesis/data/founta_dataset.csv', encoding="utf8")
a = file.read()

stopwords = set(line.strip() for line in open('/home/martyna/masters-thesis/data/stopwords.txt'))
stopwords = stopwords.union(set(['mr','mrs','one','two','said']))

# instantiate a dictionary, and for every word in the file,
# add to the dictionary if it doesn't exist
# if it exists, increase the count
wordcount = {}

# to eliminate duplicates, split by punctuation, and use case demiliters
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace(";","")
    word = word.replace("\"","")
    word = word.replace("[","")
    word = word.replace("<","")
    word = word.replace(">","")
    word = word.replace("-", "")
    word = word.replace("&","")
    word = word.replace("|","")
    word = word.replace("/","")
    word = word.replace("$","")
    word = word.replace("@","")
    word = word.replace("*","")
    word = word.replace("0", "")
    word = word.replace("1", "")
    word = word.replace("2", "")
    word = word.replace("3", "")
    word = word.replace("4", "")
    word = word.replace("5", "")
    word = word.replace("6", "")
    word = word.replace("7", "")
    word = word.replace("8", "")
    word = word.replace("9", "")
    word = word.replace("rt", "")
    word = word.replace("#", "")
    word = word.replace("normal", "")
    word = word.replace("abusive", "")
    word = word.replace("hateful", "")
    word = word.replace("spam", "")

    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
            # Print most common word

n_print = int(input("How many most common words do you want to print: "))
print("\nOK. The {} most common words are:\n".format(n_print))

word_counter = collections.Counter(wordcount)
x = 0
for word, count in word_counter.most_common(n_print):
    print(str(x), ": ", word, ": ", count)
    x += 1

file.close()



# Top 100:
# 1 :  fucking :  14629
# 2 :  amp :  5302
# 3 :  i'm :  5185
# 4 :  fucked :  4399
# 5 :  don't :  4396
# 6 :  it's :  3787
# 7 :  people :  3517
# 8 :  ass :  2756
# 9 :  time :  2461
# 10 :  day :  2278
# 11 :  you're :  2146
# 12 :  love :  2128
# 13 :  via :  2120
# 14 :  hate :  2077
# 15 :  bitch :  2022
# 16 :  bad :  1981
# 17 :  can't :  1956
# 18 :  fuck :  1951
# 19 :  video :  1857
# 20 :  am :  1653
# 21 :  trump :  1564
# 22 :  life :  1463
# 23 :  look :  1437
# 24 :  free :  1436
# 25 :  shit :  1364
# 26 :  youtube :  1349
# 27 :  im :  1321
# 28 :  stop :  1233
# 29 :  that's :  1222
# 30 :  watch :  1222
# 31 :  stupid :  1207
# 32 :  please :  1176
# 33 :  damn :  1156
# 34 :  ! :  1149
# 35 :  feel :  1149
# 36 :  win :  1118
# 37 :  idiot :  1106
# 38 :  wanna :  1103
# 39 :  thanks :  1073
# 40 :  check :  1068
# 41 :  god :  1061
# 42 :  ugly :  1059
# 43 :  % :  1045
# 44 :  girl :  1041
# 45 :  news :  1039
# 46 :  getting :  1028
# 47 :  world :  1028
# 48 :  april :  1020
# 49 :  ) :  1011
# 50 :  person :  1008
# 51 :  i've :  998
# 52 :  hell :  955
# 53 :  nigga :  927
# 54 :  help :  922
# 55 :  mad :  920
# 56 :  … :  902
# 57 :  happy :  889
# 58 :  didn't :  882
# 59 :  thank :  882
# 60 :  game :  875
# 61 :  bitches :  864
# 62 :  oh :  861
# 63 :  found :  856
# 64 :  tell :  854
# 65 :  gonna :  854
# 66 :  niggas :  826
# 67 :  live :  820
# 68 :  hope :  813
# 69 :  yo :  800
# 70 :  home :  789
# 71 :  looking :  788
# 72 :  y'all :  783
# 73 :  sick :  765
# 74 :  crazy :  765
# 75 :  play :  759
# 76 :  black :  739
# 77 :  he's :  739
# 78 :  trying :  737
# 79 :  pay :  731
# 80 :  music :  728
# 81 :  doing :  724
# 82 :  real :  722
# 83 :  sorry :  718
# 84 :  night :  714
# 85 :  twitter :  711
# 86 :  th :  709
# 87 :  call :  705
# 88 :  money :  698
# 89 :  week :  695
# 90 :  ur :  695
# 91 :  phone :  691
# 92 :  job :  688
# 93 :  team :  686
# 94 :  doesn't :  682
# 95 :  realdonaldtrump :  681
# 96 :  follow :  670
# 97 :  days :  667
# 98 :  pm :  656
# 99 :  i'll :  656
# 100 :  read :  655
