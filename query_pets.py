import sqlite3
def query_person_pets():
    conn = sqlite3.connect("pets.db")
    cursor = conn.cursor()
    while True:
        try:
            person_id = int(input("\nEnter a person ID (-1 to exit): "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue
        if person_id == -1:
            print("👋 Exiting program.")
            break
        cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?;", (person_id,))
        person = cursor.fetchone()
        if not person:
            print("❌ Person not found.")
            continue
        first_name, last_name, age = person
        print(f"\n{first_name} {last_name}, {age} years old.")
        cursor.execute("""
            SELECT pet.name, pet.breed, pet.age, pet.dead
            FROM pet
            JOIN person_pet ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?;
        """, (person_id,))
        pets = cursor.fetchall()
        if pets:
            for name, breed, pet_age, dead in pets:
                status = "was" if dead else "is"
                print(f"  - {first_name} {last_name} owned {name}, a {breed}, that {status} {pet_age} years old.")
        else:
            print("  (No pets found.)")
    conn.close()
if __name__ == "__main__":
    query_person_pets()