def display(name, grade, **marks):
        print("Name: ", name)
        print ("Grade: ", grade)
        for k, v in marks.items():
            print("Marks in " + k + ": " , v)

display("MJ", "10th", Math=95, Science=78, English=70)