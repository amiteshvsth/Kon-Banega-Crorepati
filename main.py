# colors
Red = "\033[0;31m"
Blue = "\033[0;34m"
magenta = "\033[0;95m"
grey_back = "\033[0;40m"
bold = "\033[1m"

questions = [
    [
        "1. Spirituality refers to?", "the religion that one adopts as their own.",
        "the search for significance, through the sacred, within the context of a shared belief system.",
        "a god",
        "that unsatisfiable, deepest desire within everyone, and the ways individuals deal with that desire",
        4
    ],
    [
        "2. The capacity to recognize situations and circumstances which have implications for the welfare or well "
        "being of another is referred to as",
        "relational dimension", "spirituality.", "multicultural dimension.",
        "ethical sensitivity.", 4
    ],
    [
        "3. Which of the following is NOT a suggested consideration in ethical analysis and resolution?",
        "Determine the key participants involved, based on the cultural values of the client.",
        "Use relational methods to reach an agreement on potential courses of action.",
        "Determine the culturally significant theoretical perspective",
        "Collect relevant cultural information.", 3
    ],
    [
        "4. Which of the following is NOT a spiritual or religious competency involving the client?",
        "Assess the truthfulness of the client’s spiritual claims.",
        "Acquire knowledge to better understand client’s spiritual worldview",
        "Seek consultation and or further education when indicated",
        "Refer to minister, chaplain, rabbi, or other spiritual leader when indicated.",
        1
    ],
    [
        "5. The relational dimension involves",
        "the relationship between the counselor and his or her advisor.",
        "the study of the client’s family and family dynamics.",
        "how well the counselor can relate to the client.",
        "the capacity for trust, mutuality, ethical sensitivity, and acceptance of uniqueness.",
        1
    ],
    [
        "6. Which of the following is not mandatory to maintain spiritual health?",
        "Peace", "Religion", "Hope", "Purpose", 2
    ],
    [
        "7. What happens when we die (in general)?",
        "Everything is finished; we do not exist after Death. We live only once.",
        "We go to heaven(Swarga-vasa).", "We get moksha(Liberation).",
        "We take birth again in a different body according to our Karma (Reincarnation).",
        4
    ],
    [
        "8. What is the specialty of humans over animals?",
        "Intelligence to enquire about one's relationship with God and cause of suffering in this world.",
        "Eating in Hotels and sleeping on costly beds.", "To work hard in life",
        "Maintaining  family and social relations", 1
    ],
    [
        "9. What are the VEDAS?",
        "Ancient textbooks given by some ancient people though not much relevant in modern day and age.",
        "Mythological stories carried down by tradition.",
        "Manuals given by God which tells us how to live in harmony with God's teachings.",
        "Some books to maintain morality in society  ", 3
    ],
    [
        "10. What is the purpose of YOGA?", "To maintain bodily fitness",
        "To connect with God through an authentic process.",
        "To get free from stress and anxiety.", "None of the above.",
        "All of these", 2
    ],
    [
        "11. What are the real problems of life?",
        "Traffic Jams, Neighbors' issues, high prices.",
        "Birth, old age, disease and Death.", "Unemployment, poverty, corruption.",
        "Relationship issues.", 2
    ],
    [
        "12. Who is Lord Krishna?", "An Avatar of Lord Vishnu", "A demon king",
        "A sage", "A human king", 1
    ],
    [
        "13. What is the Bhagavad Gita?", "A Hindu festival", "A holy river",
        "A sacred text", "A pilgrimage site", 3
    ],
    [
        "14. What is the goal of life according to Lord Krishna?",
        "To accumulate wealth", "To find a perfect partner",
        "To achieve fame and power", "To attain liberation", 4
    ],
    [
        "15. What is Karma Yoga?", "The path of devotion", "The path of knowledge",
        "The path of action", "The path of renunciation", 3
    ],
    [
        "16. Who is Arjuna in the Bhagavad Gita?", "A warrior prince",
        "A powerful sage", "A demon king", "A devotee of Lord Krishna", 1
    ],
    [
        "17. Krishna is a God of compassion, tenderness and?", "Harmony", "Love",
        "Peace", "War", 1
    ],
]

levels = [
    1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000,
    1250000, 2500000, 5000000, 7500000, 10000000, 75000000
]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\n {Red} Question for Rs. {levels[i]}\n")
    print(f"{Blue}{question[0]}")
    print(f"{magenta}a. {question[1]}\nb. {question[2]}\nc. {question[3]}\nd. {question[4]}")
    reply = int(
        input(f"{bold}{grey_back}Enter your answer (1-4) or 0 to quit: \n"))

    if reply == 0:
        if i == 0:
            print("You Cannot take any money")
            exit(0)
        else:
            money = levels[i - 1]
        break
    elif reply == question[-1]:
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 15:
            money = 10000000
        elif i == 16:
            money = 75000000
        print(f"Correct answer, you have won Rs. {levels[i]}")
    else:
        print("Wrong answer!")
        break

print(f"You can take {money} to your home")
