sukupuoli = input("Anna sukupuol (M/F): ")
hemoglobin = int(input("Anna hemoglobiini (g/l): "))
if sukupuoli == "M" and hemoglobin <= 134:
    print("Hemoglobiini on alhainen.")
elif sukupuoli == "M" and hemoglobin >= 134 and hemoglobin <= 195:
    print("Hemoglobiini ok.")
elif sukupuoli == "M" and hemoglobin >= 195:
    print("Hemoglobiini on korkea.")
elif sukupuoli == "F" and hemoglobin <= 117:
    print("Hemoglobiini on alhainen.")
elif sukupuoli == "F" and hemoglobin >= 117 and hemoglobin <= 175:
    print("Hemoglobiini ok.")
elif sukupuoli == "F" and hemoglobin >= 175:
    print("Hemoglobiini on korkea.")