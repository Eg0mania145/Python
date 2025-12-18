name = input("Vad heter du? : ")
age = int(input("Hur gammal är du? : "))
skola = input("Vilken skola går du på? : ")
progSpråk = input("Vad tycker du är bästa programmeringsspråket? : ").lower().strip()
myndig = "myndig" if age >= 18 else "inte myndig"
progSpråk2 = "kan det bästa programeringsspråket" if progSpråk == "python" else "behöver lära dig python"
print(f" * {name} *** \n * \tÅlder : {age} \n * \tSkola : {skola} \n * \tSammanfattning : Du är {myndig} och {progSpråk2} ")