
from pyscript import document


grade_7 = {"Ducut, Inigo", "Manaloto, Beatrice", "Mallari, Cassey", "Narciso, Lexi"}
grade_8 = {"Jo, Kevin", "Aguas, Carlos", "Gonzales, Lucas", "Silvestre, Jared", "Viray, Andrei"}
grade_9 = {"Narciso, Madeline", "Manuntag, Wil Denie", "Chan, Sashia", "Frigillana, Mica", "Mcdonald, Emily"}
grade_10 = {"Chu Tan, Pauline", "Maglaqui, Kortneigh", "Sunga, Khloe"}

def add_member(e):

    first_name = document.querySelector("#fname").value
    last_name = document.querySelector("#lname").value
    
    full_name = f"{last_name}, {first_name}"
    new_member = {full_name}
    
    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_member
    
    formatted_members = "<br>".join(sorted(master_set))
    
    total_members = len(master_set)
    
    output_div = document.querySelector("#output")
    output_div.classList.remove("d-none")
    output_div.innerHTML = f"""
        All members:<br>
        {formatted_members}<br>
        Total members: {total_members}
    """