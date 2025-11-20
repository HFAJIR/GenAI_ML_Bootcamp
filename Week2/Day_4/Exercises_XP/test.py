
with open("C:/Users/pc/Desktop/GenAI_ML_Bootcamp/Week2/Day_4/Exercises_XP/words.txt", "r") as f:

    print(f.tell())  # 0 au début
    f.read(5)
    print(f.tell())  # 5 après avoir lu 5 caractères