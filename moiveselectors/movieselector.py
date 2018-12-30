import pprint

# movie_index store the random index list
movie_index=[25, 142, 122, 7, 126, 110, 35, 176, 187, 250, 21, 221, 195, 229, 237, 170, 69, 188, 36, 27, 97, 40, 166, 6, 230, 222, 44, 158, 103, 104, 205, 197, 144, 244, 242, 172, 119, 162, 100, 177, 134, 145, 10, 79, 219, 128, 84, 1, 117, 157, 174, 55, 225, 228, 30, 182, 124, 148, 98, 140, 38, 239, 208, 178, 23, 209, 67, 111, 199, 76, 60, 214, 224, 233, 150, 118, 108, 112, 87, 154, 121, 68, 217, 200, 181, 183, 105, 155, 51, 204, 179, 73, 37, 86, 8, 149, 50, 63, 143, 186, 85, 18, 95, 249, 193, 11, 167, 152, 127, 83, 64, 123, 39, 90, 207, 136, 99, 218, 206, 113, 180, 72, 82, 137, 211, 78, 231, 24, 102, 248, 41, 65, 138, 212, 88, 32, 234, 34, 75, 223, 216, 92, 151, 175, 109, 33, 66, 26, 49, 70, 94, 202, 58, 213, 20, 9, 159, 147, 243, 241, 74, 130, 227, 12, 161, 80, 215, 56, 141, 163, 89, 132, 189, 235, 203, 201, 2, 59, 46, 171, 29, 120, 139, 61, 226, 194, 4, 43, 101, 236, 191, 47, 77, 22, 133, 45, 192, 131, 71, 196, 135, 28, 125, 190, 116, 156, 220, 81, 160, 153, 93, 62, 53, 52, 107, 247, 146, 96, 13, 245, 19, 168, 91, 169, 173, 48, 31, 3, 246, 42, 198, 57, 210, 184, 238, 17, 54, 164, 232, 165, 129, 5, 185, 106, 115, 16, 14, 114, 15, 240]

# movie_dict is the ditionary of movies
movie_dict={1: '1.The Shawshank Redemption',
 2: '2.The Godfather',
 3: '3.The Godfather: Part II',
 4: '4.The Dark Knight',
 5: '5.12 Angry Men',
 6: "6.Schindler's List",
 7: '7.Pulp Fiction',
 8: '8.The Good, the Bad and the Ugly',
 9: '9.The Lord of the Rings: The Return of the King',
 10: '10.Fight Club',
 11: '11.The Lord of the Rings: The Fellowship of the Ring',
 12: '12.Star Wars: Episode V - The Empire Strikes Back',
 13: '13.Forrest Gump',
 14: '14.Inception',
 15: "15.One Flew Over the Cuckoo's Nest",
 16: '16.The Lord of the Rings: The Two Towers',
 17: '17.Goodfellas',
 18: '18.The Matrix',
 19: '19.Star Wars',
 20: '20.Seven Samurai',
 21: '21.City of God',
 22: '22.Se7en',
 23: '23.The Silence of the Lambs',
 24: '24.The Usual Suspects',
 25: "25.It's a Wonderful Life",
 26: '26.Life Is Beautiful',
 27: '27.Léon: The Professional',
 28: '28.Once Upon a Time in the West',
 29: '29.Interstellar',
 30: '30.Saving Private Ryan',
 31: '31.American History X',
 32: '32.Spirited Away',
 33: '33.Casablanca',
 34: '34.Raiders of the Lost Ark',
 35: '35.Psycho',
 36: '36.City Lights',
 37: '37.Rear Window',
 38: '38.The Intouchables',
 39: '39.Modern Times',
 40: '40.Terminator 2: Judgment Day',
 41: '41.Whiplash',
 42: '42.The Green Mile',
 43: '43.The Pianist',
 44: '44.Memento',
 45: '45.The Departed',
 46: '46.Gladiator',
 47: '47.Apocalypse Now',
 48: '48.Back to the Future',
 49: '49.Sunset Blvd.',
 50: '50.Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb',
 51: '51.The Prestige',
 52: '52.Alien',
 53: '53.The Lion King',
 54: '54.The Lives of Others',
 55: '55.The Great Dictator',
 56: '56.Inside Out',
 57: '57.Cinema Paradiso',
 58: '58.The Shining',
 59: '59.Paths of Glory',
 60: '60.Django Unchained',
 61: '61.The Dark Knight Rises',
 62: '62.WALL·E',
 63: '63.American Beauty',
 64: '64.Grave of the Fireflies',
 65: '65.Aliens',
 66: '66.Citizen Kane',
 67: '67.North by Northwest',
 68: '68.Princess Mononoke',
 69: '69.Vertigo',
 70: '70.Oldeuboi',
 71: '71.Das Boot',
 72: '72.M',
 73: '73.Star Wars: Episode VI - Return of the Jedi',
 74: '74.Once Upon a Time in America',
 75: '75.Amélie',
 76: '76.Witness for the Prosecution',
 77: '77.Reservoir Dogs',
 78: '78.Braveheart',
 79: '79.Toy Story 3',
 80: '80.A Clockwork Orange',
 81: '81.Double Indemnity',
 82: '82.Taxi Driver',
 83: '83.Requiem for a Dream',
 84: '84.To Kill a Mockingbird',
 85: '85.Lawrence of Arabia',
 86: '86.Eternal Sunshine of the Spotless Mind',
 87: '87.Full Metal Jacket',
 88: '88.The Sting',
 89: '89.Amadeus',
 90: '90.Bicycle Thieves',
 91: "91.Singin' in the Rain",
 92: '92.Monty Python and the Holy Grail',
 93: '93.Snatch.',
 94: '94.2001: A Space Odyssey',
 95: '95.The Kid',
 96: '96.L.A. Confidential',
 97: '97.Rash?mon',
 98: '98.For a Few Dollars More',
 99: '99.Toy Story',
 100: '100.The Apartment',
 101: '101.Inglourious Basterds',
 102: '102.All About Eve',
 103: '103.The Treasure of the Sierra Madre',
 104: '104.Jodaeiye Nader az Simin',
 105: '105.Indiana Jones and the Last Crusade',
 106: '106.Metropolis',
 107: '107.Yojimbo',
 108: '108.The Third Man',
 109: '109.Batman Begins',
 110: '110.Scarface',
 111: '111.Some Like It Hot',
 112: '112.Unforgiven',
 113: '113.3 Idiots',
 114: '114.Up',
 115: '115.Raging Bull',
 116: '116.Downfall',
 117: '117.Mad Max: Fury Road',
 118: '118.Jagten',
 119: '119.Chinatown',
 120: '120.The Great Escape',
 121: '121.Die Hard',
 122: '122.Good Will Hunting',
 123: '123.Heat',
 124: '124.On the Waterfront',
 125: "125.Pan's Labyrinth",
 126: '126.Mr. Smith Goes to Washington',
 127: '127.The Bridge on the River Kwai',
 128: '128.My Neighbor Totoro',
 129: '129.Ran',
 130: '130.The Gold Rush',
 131: '131.Ikiru',
 132: '132.The Seventh Seal',
 133: '133.Blade Runner',
 134: '134.The Secret in Their Eyes',
 135: '135.Wild Strawberries',
 136: '136.The General',
 137: '137.Lock, Stock and Two Smoking Barrels',
 138: '138.The Elephant Man',
 139: '139.Casino',
 140: '140.The Wolf of Wall Street',
 141: "141.Howl's Moving Castle",
 142: '142.Warrior',
 143: '143.Gran Torino',
 144: '144.V for Vendetta',
 145: '145.The Big Lebowski',
 146: '146.Rebecca',
 147: '147.Judgment at Nuremberg',
 148: '148.A Beautiful Mind',
 149: '149.Cool Hand Luke',
 150: '150.The Deer Hunter',
 151: '151.How to Train Your Dragon',
 152: '152.Gone with the Wind',
 153: '153.Fargo',
 154: '154.Trainspotting',
 155: '155.It Happened One Night',
 156: '156.Dial M for Murder',
 157: '157.Into the Wild',
 158: '158.Gone Girl',
 159: '159.The Sixth Sense',
 160: '160.Rush',
 161: '161.Finding Nemo',
 162: '162.The Maltese Falcon',
 163: '163.Mary and Max',
 164: '164.No Country for Old Men',
 165: '165.The Thing',
 166: '166.Incendies',
 167: '167.Hotel Rwanda',
 168: '168.Kill Bill: Vol. 1',
 169: '169.Life of Brian',
 170: '170.Platoon',
 171: '171.The Wages of Fear',
 172: '172.Butch Cassidy and the Sundance Kid',
 173: '173.There Will Be Blood',
 174: '174.Network',
 175: '175.Touch of Evil',
 176: '176.The 400 Blows',
 177: '177.Stand by Me',
 178: '178.12 Years a Slave',
 179: '179.The Princess Bride',
 180: '180.Annie Hall',
 181: '181.Persona',
 182: '182.The Grand Budapest Hotel',
 183: '183.Amores Perros',
 184: '184.In the Name of the Father',
 185: '185.Million Dollar Baby',
 186: '186.Ben-Hur',
 187: '187.The Grapes of Wrath',
 188: "188.Hachi: A Dog's Tale",
 189: '189.Nausica? of the Valley of the Wind',
 190: '190.Shutter Island',
 191: '191.Diabolique',
 192: '192.Sin City',
 193: '193.The Wizard of Oz',
 194: '194.Gandhi',
 195: '195.Stalker',
 196: '196.The Bourne Ultimatum',
 197: '197.The Best Years of Our Lives',
 198: '198.Donnie Darko',
 199: '199.Relatos salvajes',
 200: '200.8?',
 201: '201.Strangers on a Train',
 202: '202.Jurassic Park',
 203: '203.The Avengers',
 204: '204.Before Sunrise',
 205: '205.Twelve Monkeys',
 206: '206.The Terminator',
 207: '207.Infernal Affairs',
 208: '208.Jaws',
 209: '209.The Battle of Algiers',
 210: '210.Groundhog Day',
 211: '211.Memories of Murder',
 212: '212.Guardians of the Galaxy',
 213: '213.Monsters, Inc.',
 214: '214.Harry Potter and the Deathly Hallows: Part 2',
 215: '215.Throne of Blood',
 216: '216.The Truman Show',
 217: '217.Fanny and Alexander',
 218: '218.Barry Lyndon',
 219: '219.Rocky',
 220: '220.Dog Day Afternoon',
 221: '221.The Imitation Game',
 222: '222.Yip Man',
 223: "223.The King's Speech",
 224: '224.High Noon',
 225: '225.La Haine',
 226: '226.A Fistful of Dollars',
 227: '227.Pirates of the Caribbean: The Curse of the Black Pearl',
 228: '228.Notorious',
 229: '229.Castle in the Sky',
 230: '230.Prisoners',
 231: '231.The Help',
 232: "232.Who's Afraid of Virginia Woolf?",
 233: '233.Roman Holiday',
 234: '234.Spring, Summer, Fall, Winter... and Spring',
 235: '235.The Night of the Hunter',
 236: '236.Beauty and the Beast',
 237: '237.La Strada',
 238: '238.Papillon',
 239: '239.X-Men: Days of Future Past',
 240: '240.Before Sunset',
 241: '241.Anatomy of a Murder',
 242: '242.The Hustler',
 243: '243.The Graduate',
 244: '244.The Big Sleep',
 245: '245.Underground',
 246: '246.Elite Squad: The Enemy Within',
 247: '247.Gangs of Wasseypur',
 248: '248.Lagaan: Once Upon a Time in India',
 249: '249.Paris, Texas',
 250: '250.Akira'}





    # change the watched_files according to runtimes
def watched(run_times,movie_dict,movie_index):
    if run_times==0:
        watched_files=open('watched.txt','w')
        watched_files.truncate()
        watched_files.close()
    elif run_times>0:
        watched_files=open('watched.txt','w')
        watched_files.truncate()
        watched_files.close()
        watched_files=open('watched.txt','a')
        for i in range(1,run_times+1):
            watched_files.write(movie_dict[movie_index[i-1]]+'\n')
        watched_files.close()





# run_times is the times the that the program has been run
run_file=open('runtimes.txt')
run_str=run_file.read()
# eval change the string to code
run_times=eval(run_str)
if run_times==0:
    print('You have not watched any movies.')
    print('The movie you are watching currently is : None')
else:
    print('You have watched {} movies.'.format(run_times-1))
    current_movie=movie_dict[movie_index[run_times-1]]
    print('The moive you are watching currently is {}.'.format(current_movie))



# flag to determine the next action
print('Choose a movie----> Press a')
print('Check the watched list----> Press b')
print('Reset the selection times----> Press c')
flag=input()
if flag=='a':
    watched(run_times,movie_dict,movie_index)
    next_movie=movie_dict[movie_index[run_times]]
    print('The next moive is {}.'.format(next_movie))
    run_times+=1
    run_file=open('runtimes.txt','w')
    run_file.write(str(run_times))
    run_file.close()
    input('please press enter to exit')
elif flag=='b':
    if run_times>1:
        watched_files1=open('watched.txt')
        watched_list=watched_files1.readlines()
        for i in range (1,len(watched_list)+1):
            print('{}--->'.format(i)+watched_list[i-1])
    else:
        print('The list is empty.')
    input('please press enter to exit')
elif flag=='c':
    print('Please input the selection times:')
    run_times=int(input())
    run_file=open('runtimes.txt','w')
    run_file.write(str(run_times))
    run_file.close()
    if run_times==0:
        watched(run_times,movie_dict,movie_index)
    else:
         watched(run_times-1,movie_dict,movie_index)

   

    




