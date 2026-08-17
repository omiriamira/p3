from rich import console
questions = [("question1",["1)a","2)b","3)c","4)d"],"2",1),
    ("question2",["1)aA","2)bB","3)cC","4)dD"],"2",1),
    ("question3",["1)aa","2)bb","3)cc","4)dd"],"2",1),
    ("question4",["1)a","2)b","3)c","4)d"],"2",1),
    ("where is japan's capital",["1)tahran","2)aftab 50","3)washington","4)tokyo"],"4",1)
]
total_score=0
correct_count=0
playing = True
while playing:
    answer_menu = input("1.play game \n2.exit game").strip().lower()
    if answer_menu == "1":

for question,options,correct_answer, score in questions:
    console.print(f"\n{question}")
    for opt in options:
        print(opt)

    answer:str =input("your answer").strip().upper()
    if answer==correct_answer:
        console.print("[green]Correct[/green]")
        total_score +=score
        correct_count +=1
    else:
        console.print("[red]incorrect[/red]")
        total_score -=3
    console.print(f"\n[bold]Your total score:{total_score}[bold]")
elif answer_menu == "2":
console.print(f"[bold]Correct answers:{correct_count}[bold]")
console.print("goodbye",style="red on black")
