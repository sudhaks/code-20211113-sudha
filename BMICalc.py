import sys
import json
 
# input JSON file
try:
    inf = open ('in.json', 'r', encoding='utf-8')
except FileNotFoundError as error_message:
    print(error_message)
    sys.exit()

# Reading from input file
data = json.loads(inf.read())
inf.close()

# to write to output file
with open("out.json", 'w') as outf: 
    outf.write('[')
    out = {}

    #Col names
    gender = "Gender"
    height = "HeightCm"
    weight = "WeightKg"
    bmi = "BMI"
    bmiCategoty = "BMICategory"
    bmiRange = "BMIRange"
    healthRisk = "HealthRisk"

    BMI = 0.0
    h = 0.0
    w = 0.0
    BMICategory = ""
    BMIRange = 0.0
    HealthRisk = ""

    # Iterating through the inputjson
    for i in data:
        w = i[weight] * 1.0
        h = i[height]/100.0
        if(h>0):
            BMI = w / (h * h)
        else:
            BMI = 0    

        if(BMI>0):
            if(BMI<18.5):
                BMICategory = "Underweight"
                BMIRange = "18.4 and below"
                HealthRisk = "Malnutrition risk"
            elif(BMI<25.0):
                BMICategory = "Normal weight"
                BMIRange = "18.5 - 24.9"
                HealthRisk = "Low risk"
            elif(BMI<30.0):
                BMICategory = "Overweight"
                BMIRange = "25 - 29.9"
                HealthRisk = "Enhanced risk"
            elif(BMI<35.0): 
                BMICategory = "Moderately obese"
                BMIRange = "30 - 34.9"
                HealthRisk = "Medium risk"
            elif(BMI<40.0):
                BMICategory = "Severely obese"
                BMIRange = "35 - 39.9"
                HealthRisk = "High risk"
            elif(BMI>=40.0):
                BMICategory = "Very severely obese"
                BMIRange = "40 and above"
                HealthRisk = "Very high risk"
        else:
            BMICategory = "Invalid details"
            BMIRange = "0 or below"
            HealthRisk = "Error in data"

        # arrange BMI columns to write to outfile
        out = { gender : i[gender],
        height : i[height],
        weight : i[weight],
        bmi : BMI,
        bmiCategoty : BMICategory,
        bmiRange : BMIRange,
        healthRisk : HealthRisk }

        # write to outfile
        json.dump(out,outf,ensure_ascii=False,indent=2)
        if(i!=data[-1]):         
            outf.write(',')

    outf.write(']')
    # close outfile
    outf.close()

sys.exit()