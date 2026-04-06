#Quiz in Python
questions = ("Was ist die vollständige Form der Abkürzung „IHK“?: ",
             "Wer berät einen Auszubildenden (Azubi) bei der Suche nach einem Ausbildungsplatz?: ",
             "Welche der folgenden Optionen ist keine Software?: ",
             "Wie wird ein geschlossener Stromkreis im Binärsystem dargestellt?: ",
             "Was ist die vollständige Form der Abkürzung „GUI“?: ",
             "Was ist die nächste Phase nach der Projektdurchführung im Projektmanagement?: ",
             "Welches der folgenden ist ein klassisches Projektmanagementmodell?: ",
             "Was ist die vollständige Form der Abkürzung „WLAN“?: ",
             "Was ist die Definition von „Datensicherheit“?: ",
             "Was ist die vollständige Form der Abkürzung „MFA“?: ")

options = (("A.Internationale Handelskammer ","B.Industrie- und Handelskammer ","C. Institut für Handel und Kommunikation ","D.Internationale Hauptkommission "),
           ("A. Die Industrie- und Handelskammer (IHK) ","B.Die Berufsschule ","C.Die Agentur für Arbeit ","D.Das Einwohnermeldeamt "),
           ("A.Betriebssystem ","B.Textverarbeitungsprogramm ","C.Prozessor ","D.Webbrowser "),
           ("A. 0, da kein Signal vorhanden ist ","B.1, da der Strom fließt ","C.0 und 1 gleichzeitig, abhängig von der Spannung ","D.Wird im Binärsystem nicht dargestellt "),
           ("A. General User Integratio ","B. Graphical User Interface","C.Global Utility Interaction ","D. Graphical Unified Internet "),
           ("A.Projektplanung ","B. Projektabschluss ","C.Live-Gang ","D.Projektanalyse "),
           ("A.Wasserfallmodell ","B. Scrum ","C.Kanban ","D.Design Thinking "),
           ("A. Wireless Local Area Network ","B. Wide Local Access Network","C.  Wireless LAN Access Node","D.Wired Local Area Network "),
           ("A. Schutz von Daten vor unbefugtem Zugriff und Verlust ","B.Speicherung von Daten auf einem Computer ","C.Übertragung von Daten über das Internet ","D.Bearbeitung von Daten in Programmen "),
           ("A. Multi-Factor Authentication ","B.Modern File Access ","C.  Managed Firewall Application","D.Multi-Function Algorithm "))

answers = ("B" ,"C" ,"C" ,"B" ,"B" ,"C" ,"A" ,"A" ,"A" ,"A")
guesses = []    
score = 0
ques_num = 0

for question in questions:
    print("-----------------------")
    print(question)
    for option  in options[ques_num]:
        print(option)

    guess = input(" Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[ques_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT") 
        print(f"{answers[ques_num]} is the correct answer")
    ques_num += 1    



print("-----------------------")
print("        RESULTS        ")
print("-----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end= " ")
print()


print("guesses: ", end="")
for guess in guesses:
    print(guess, end= " ")
print()

score = int(score/ len(questions) * 100 )
print(f"Your score is: {score}%")

